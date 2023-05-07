from flask import Flask, render_template, request, redirect, url_for, make_response
from my_lib import database_worker, encrpyt_password, check_password

#Main python code 

app = Flask(__name__)


def create_database():
    db = database_worker("social_net.db")
    query_user = """ CREATE table if not exists users (
        id INTEGER PRIMARY KEY,
        email TEXT NOT NULL,
        password TEXT
    )
    """
    query_post = """CREATE table if not exists posts (
        id INTEGER PRIMARY KEY,
        title VARCHAR(100),
        content TEXT,
        ingredients TEXT,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade 
    )
    """
    query_ingredients = """Create table if not exists ingredients(
    id INTEGER PRIMARY KEY,
    ingredients TEXT,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade 
    )
    """
    db.run_save(query_user)
    db.run_save(query_post)
    db.run_save(query_ingredients)
    db.close()

@app.route('/', methods=["GET","POST"])
@app.route('/login', methods=["GET","POST"])
def login():
    msg = ""
    if request.method == "POST":
        email = request.form['email']
        passwd=request.form['passwd']
        db = database_worker("social_net.db")
        user = db.search(f"Select * from users where email = '{email}'") #Check the user in the database
        if user:
            user = user[0] #because search function returns a list
            id, email_db, hashed = user
            if check_password(hashed_password=hashed, user_password=passwd): #Call function from my_lib to check password
                db = database_worker("social_net.db")
                posts = db.search("Select * FROM posts")
                response = make_response(redirect('home'))
                response.set_cookie('user_id', f"{id}")#Set cookie for functions later in the website
                return response
            else: msg = "Please enter the correct password"
        else:
            msg = "user does not exist"
    return render_template("login.html", message=msg)

@app.route('/logout')
def logout():
    response = make_response(redirect('login'))
    response.set_cookie("user_id","",expires=0)
    return response

@app.route('/signup', methods=["GET","POST"])
def signup():
    msg = ""
    if request.method == "POST":
        email = request.form['email']
        passwd=request.form['passwd']
        passwdconfirm=request.form['confirmpasswd'] #Get the information from the UI
        if passwd==passwdconfirm:
            hash = encrpyt_password(passwd) #Encrypt the password for better security
            db = database_worker("social_net.db")
            new_post = f"INSERT into users (email,password) values('{email}','{hash}')"  #Save in the database to call back later
            db.run_save(query=new_post)
            return redirect(url_for('login'))
        else:
            msg = "Passwords do not match"
    return render_template("signup.html", message=msg)

@app.route('/profile/<user_id>', methods=['GET','POST'])
def profile(user_id:int): #Get the user_id to know which user it is 
    if request.cookies.get('user_id'): #Check if user is logged in (For security purposes)
        db = database_worker("social_net.db")
        user,posts = None, None
        user= db.search(f"SELECT * from users where id={user_id}") 
        if user:
            posts = db.search(f"select * from posts where user_id={user_id}") 
            user = user[0] #remeber db.search returns a list
        return render_template("profile.html", user=user, posts=posts) #Showcases the user name and posts
    else:
        return redirect('login')
@app.route('/home', methods=['GET','POST'])
def home():
    if request.cookies.get('user_id'): #Check if user is logged in (For security purposes)
        user_id = request.cookies.get('user_id')
        db = database_worker("social_net.db")
        posts = db.search("Select * FROM posts")
        if request.method=='POST':
            search_query = request.form['query']
            posts2 = db.search(f"SELECT * FROM posts WHERE ingredients like '%{search_query}%' ") #Search function, returns posts searched by ingredient
            return render_template("home.html", posts=posts2, user_id = user_id)

        return render_template("home.html", posts=posts, user_id = user_id)

    else:
        return redirect('login')
    return render_template("home.html", posts=posts, user_id = user_id)


@app.route('/new_post', methods=['GET','POST'])
def new_post():
    msg = ""
    if request.cookies.get('user_id'): #Check if user is logged in (For security purposes)
        user_id = request.cookies.get('user_id') #To track whose post this is
        db = database_worker("social_net.db")
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            ingredients = request.form['ingredients']
            if len(title) > 0 and len(content) > 0 and len(ingredients)>0: #Validate that the user is not posting an empty post
                new_post = f"INSERT into posts (title, content, ingredients, user_id) values('{title}','{content}','{ingredients}',{user_id})"
                db.run_save(query=new_post)
                posts = db.search("Select * FROM posts")
                return redirect(url_for('home', posts = posts )) #Redirect to home page 
            else:
                msg = "Please enter title, content and ingredients" #Error the message is displayed in the UI
                return render_template("new_posts.html", message=msg)
        return render_template("new_posts.html", message=msg)
    else:
        return redirect('login')




@app.route('/shopping_list/<int:user_id>/<int:post_id>', methods=['GET'])
def shopping_list(user_id, post_id):
    if request.cookies.get('user_id'): #Check if user is logged in (For security purposes)
        db = database_worker("social_net.db")
        post = db.search(f"SELECT * FROM posts WHERE id = {post_id}")[0]
        ingredients = post[3].split(",") #Ingredients in a comma seperated list 
        print(ingredients)
        for ingredient in ingredients:
            new_ingredients = f"INSERT INTO ingredients (user_id, ingredients) VALUES ({user_id}, '{ingredient}')" #Save in the database
            db.run_save(query=new_ingredients)
        return redirect(url_for('shopping_list2',user_id=user_id)) #Redirect since for the actual shopping list, don't need the post_id just the user_id
    else:
        return redirect('login')

@app.route('/shopping_list2/<int:user_id>')
def shopping_list2(user_id): 
    if request.cookies.get('user_id'): #Check if user is logged in (For security purposes)
        db = database_worker("social_net.db")
        ingredients = db.search(f"SELECT * FROM ingredients WHERE user_id = {user_id}") #Show all the ingredients from the user
        print(ingredients)
        db.close()
        return render_template("shoppiing_list.html", ingredients=ingredients)
    else:
        return redirect('login')
@app.route('/delete_ingredient/<int:ingredient_id>', methods=['POST']) 
def delete_ingredient(ingredient_id): #Check if user is logged in (For security purposes)
    if request.cookies.get('user_id'):
        user_id = request.cookies.get('user_id') #Delete the right persons ingredient
        db = database_worker("social_net.db")
        db.run_save(f"DELETE FROM ingredients WHERE id = {ingredient_id}") 
        db.close()
        return redirect(url_for('shopping_list2',user_id=user_id)) #Keep them on the shopping list page 
    else:
        return redirect('login')

create_database()

if __name__ == '__main__':
    app.run()
