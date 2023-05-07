# Unit 4 project: Recipe sharing social network 

![](https://github.com/KaiFig/Unit_4/blob/main/Project/Pictures/Project%204%20picture.jpeg)
**Fig 1** This is the title picture for my repository

# Criteria A: Planning

## Problem definition
When I brainstormed with my client (myself) about problems I face and a SNS that would solve that, I realized that in school, we are not able to share recipes that we make, which is a shame as we come from such a diverse background and have lots of new and interesting recipes to share. There are no applications where we are able to get large numbers of people together, in one platform to share their ideas, each having an equal voice. At school, unless we are close to someone, we usually do not get the opportunity to cook with them or learn their recipes. Even if I share recipes to someone usually I tend to forget what I wrote since I don't have a visible record of my sharing of recipes with all their information. Also, even if I search online, it is hard to get help on a recipe as I don't know them, and there are usually no ways of contacting them. Therefore, an SNS would enable messaging for help. Additionally, whenever I go to the supermarket, since I go there without a shopping list for recipes, I end up buying more than I need. This contributes to increased spending, and also, since I am not able to use everything, it makes me waste food. I have tried writing my own shopping list by looking at the recipe before and writing stuff down, however I have forgotten a nmber of things before so it's not the most effective. Additionally, when I have lots of one ingredint I tend to not use all of it as I do not konw how to use that ingredient since I am not able to scan lots of recipes for a specific ingredient. This contributes to even more food waste. As proof of this, the notest taken from the brainstorming session are listed in the appendix. 
　
## Proposed solution
To solve my client’s issue I will be creating a website using HTML CSS and Python. This site will have a login and signup system so that multiple users are able to use it. This site will allow the end user to share their own recipes and other users to share theirs as well. Within the website, there will be a shopping list so that people can put the ingredients they need and a search bar to search for recipes based on the ingredients 


## Rationale for proposed solution
I will be making an social media website as it is the most convenient way for the client to be able to view other people's recipes and to comment on them. An SNS involves quick sharing of these recipes making it the most effective. Additionally, it will also enable the user to search through the recipes very effectively through ingredients and name. 

As for the software, first of all, I will be using HTML to create the website. This is because HTML enables the creation of the structure of the webpage, and for the developer it is quite easy to learn. [^1] Additionally, for the user, it enables them to see a website that is structured, making it easier to navigate. One final thing is that HTML allows for python code to be enbedded in it, enabling more functions for the end user [^2]

Another language I will be using is CSS. This will enable me to structure the HTML webpage exactly how I want by creating a set of rules for it. This is important as for the end user, it enables them to have a clean website that they can use and navigate through easily. It makes the user experience a lot better and easier for them to use. [^3]

Lastly for the last language I will be using is Python. Python enables me to create the functionality for the website. I used python as it can be placed in HTML as well, creating an integrated website. Additionaly, it has a large library that enables me, the developer to rely on other libraries to make the website. Also, it has a very large community of developers, enabling the quick use of research in support of my project. [^4]

[^1]: “HTML vs JavaScript: Which Should You Learn?” Hackr.io, https://hackr.io/blog/html-vs-javascript. 
[^2]: “HTML vs JavaScript: Top 8 Most Amazing Comparison You Need to Know.” EDUCBA, 3 Mar. 2023, https://www.educba.com/html-vs-javascript/. 
[^3]: User, Devmountain. “What Is CSS and Why Should You Use It?” Devmountain, 22 Apr. 2019, https://devmountain.com/blog/what-is-css-and-why-use-it/#:~:text=CSS%20makes%20the%20front%2Dend,for%20font%20color%20and%20more. 
[^4]: Korsun, Julia. “The 16 Most Important Pros and Cons of Using Python for Web Development.” Software Development Blog &amp; IT Tech Insights | Django Stars, 10 Feb. 2023, https://djangostars.com/blog/python-web-development/. 

**Design statement:**
I will design and make a web based social media site for a client who is a high school student that is interested in cooking. The SNS will be about sharing and viewing other peoples recipes and is constructed using the software CSS, HTML and Python. It will take 4 weeks to make and will be evaluated according to the criteria A, B, C, D, and E. 


## Success criteria
| No. | Success critieria	         | Issue tackled       |
|----------------------------|---------------------------------|----------------|
| 1 | The user can upload their own recipes as a social media post. The post includes the title, content and ingredients  | "in school, we are not able to share recipes that we make"  | 
| 2 | There is a login and registration page for each user | "There are no applications where we are able to get large numbers of people together, in one platform to share their ideas"  | 
| 3 | The user can view other social media post  | "At school, unless we are close to someone, we usually do not get the opportunity to cook with them or learn their recipes"  | 
| 4 | Users are able to create their own shopping list in the app  | "I go there without a shopping list for recipes, I end up buying more than I need. This contributes to increased spending, and also, since I am not able to use everything, it makes me waste food" | 
| 5 | Users can search recipes based on ingredients  | "I have lots of one ingredint I tend to not use all of it as I do not konw how to use that ingredient since I am not able to scan lots of recipes for a specific ingredient"  | 
| 6 | User can have their own profile page that displays their email and posts. | "Even if I share recipes to someone usually I tend to forget what I wrote since I don't have a visible record of my sharing of recipes with all their information" | 


# Criteria B: Design

## System diagram
![](https://github.com/KaiFig/Unit_4/blob/main/Project/Pictures/Project_4_system_diagram.jpg)

**Fig 2** This shows the system diagram for my project. All the files that I had in pycharm and the database "social_net.db" that I used to store all of the data. This was all done with flask and was displayed in safari on my macbookair 

## ER diagram
![](https://github.com/KaiFig/Unit_4/blob/main/Project/Pictures/Project_4_ER_diagram.jpg)

**Fig 3** This shows the ER diagram for my project showing how each table in the database is structured and what is in it 

| id | Email          | Password      |
|----------------------------|---------------------------------|----------------|
|1	|kai@icloud.com |$5$rounds=30000$GeacpgiixTRHUfj6$edv.zYRWn4ZxkcaaS0CKGA1ZunLzBNjwtKM2czahj9B | 

| id | Title	| Content	| Ingredients	| User_id | 
|--------|----------------|--------------------|---------------|-------| 
|1	| Banana bread | Easy banana bread  | Bananas 2, Eggs 1, Sugar 100g, Salt 5g, Baking powder 10g | 1 | 

|id | Ingredient | User_id | 
|--------|-----------|-------------| 
|16 | milk | 2| 

## Wireframe diagram 
![](https://github.com/KaiFig/Unit_4/blob/main/Project/Pictures/Project_4_wireframe.jpg)

**Fig  4** This shows the wireframe for my project. Before starting the code, I tried to visualize how my website would look as then I would be able to design it much easier and I was able to show this to the client for feedback 

## Flowcharts 
![](https://github.com/KaiFig/Unit_4/blob/main/Project/Pictures/Project_4_flowchart_1.jpg)

**Fig 5** The first flowchart shows my login page

![](https://github.com/KaiFig/Unit_4/blob/main/Project/Pictures/Project_4_flowchart_2.jpg)

**Fig 6** The second flowchart shows my home page

![](https://github.com/KaiFig/Unit_4/blob/main/Project/Pictures/Project_4_flowchart_3.jpg)

**Fig 7** The third flowchart shows my shopping list function 

## UML diagram 
![](https://github.com/KaiFig/Unit_4/blob/main/Project/Pictures/Project_4_UML.jpg)

**Fig 8** The UML diagram shows the class that I used called database worker to connect to the database 

## Record of Tasks

| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Planning: Meeting my client                         | To identify what my client wants for a database  | 15min         | Apr 8th               | A         |
| 2       | Planning: Write the Problem defition                        | Expand our problem context and identify a customer and their specific problem so that we know what we need to acheive with our project  |  20min         | Apr 8th          | A         |
|3       | Planning: Write the proposed solution and rationale for propsed solution  | My client is able to see what I am creating as a solution and input feedback so that he gets what he wants |50 min | Apr 8th    | A     | 
|4       | Planning: Write the design statement | Able to proceed with a clear plan and goal now that the design statement is written    | 10 min  | Apr 8th  | A |
|5       | Planning: Write each success criteria  | Have a clear outline of what is needed to be acheived for my client so I am able to fulfill the clients needs   | 20 min | Apr 8th | A  |
|6       | Design: Create the system diagram  | Can showcase what the whole SNS will look like and what files and programs it will run  | 30 min  | Apr 9th | B  | 
|7       | Design: Create the wireframe diagram  | We can showcase what the SNS will look like, and i have a plan for how to style it using HTML and CSS | 45 min  | Apr 14th | B   | 
|8      | Development: Create the database   | I have a database so that each user is able to have their own account and they are able to have a record of posts   | 20 min | Apr 15th | C | 
|9      | Development: Create the login page  | I create the functionality for the login page, enabling each user to have their own account, and their posts to be linked back to them   | 30 min  | Apr 16th | C | 
|10     | Development: Create the signup page | This enables users to signup to the application, making sure that their passwords are long and strong enough   | 30 min | Apr 16th  | C | 
|11     | Development: Create the home page  | This will be the first screen that the user encounters when they login to the application   | 30 min  | Apr 16th | C | 
|12     | Development: Create the new posts page   | This enables each user to add a post to the Social media site, with their recipe and other important information. Additionally, it will be linked back to the user  | 30 min  | Apr 16th | C | 
|13     | Development: Create the css for the signup page  | It makes everything look much better and the user is able to have a better user experience | 30 min   | Apr 16th  | C   | 
|14     | Development: Create the css for the login and new posts page   | Better user experience  | 30 min  | Apr 16th  | C | 
|15     | Development: Create the css for home page  | Better user experience  | 30 min  | Apr 16th  | C | 
|16     | Development: Create the search bar   | It enables the user to search the database for a recipe with a specific ingredient so that they can base their recipes on what they have | 45 min   | Apr 17th  | C | 
|17     | Design: Create the flow diagrams for an interesting function  | I am able to showcase to everyone how my code works so that they are able to further develop on it  | 45 min  | Apr 17th | B | 
|18     | Development: Create the profile page in the website   | The user is able to have their own profile page where they are able to see all their posts   | 45 min  | Apr 17th  | C | 
|19     | Development: Create the shopping list page in the database | This saves the users ingredients that they click on   | 20 min  | Apr 18th  | C | 
|20     | Development: Create the shopping list page in the website  | The user is able to see each ingredient that they saved   | 1 hr 30 min  | Apr 19th  | C  | 
|21     | Design: Update the record of tasks    | I have already done a few unit tests so this enables me to give a record of them  | 20 min | Apr 19th  | C | 
|22     | Evaluation: Test the login and signup pages   | I make sure that the user is able to login and signup into the website and that all the error messages work | 20 min | Apr 20th | C |
|23     | Development: Fix the search and sql queries | The user can search the database with a specific recipe and it returns everything. Also the search bar works more than once  | 1 hr  | Apr 21st | C  | 
|24     | Design: Complete the UML diagram | I show the relations between all the classes in the website so that other people viewing the code understand it | 20 min   | Apr 21st | B  | 
|25     | Development: Better the CSS for each page  | The UI is much more improved and users are able to enjoy a website that looks nice    | 45 min    | Apr 21st  | C   |







## Test plan

| Instruction                        | Category     | Input example / code                               | Description                                                                                                        | Expected output                                                         | Success criteria |
|------------------------------------|--------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|------------------|
|Test the login   | Unit testing  | Email, password | The user is able to login to the application and the home screen is displayed when they enter. An error message appears if the password or the username is not correct  | The user logs in if the username and password is correct and the home screen is displayed with a cookie being created as well   |2, 3 | 
|Test the login if wrong username or password | Unit testing  | Email, Password | The user inputs the wrong password, username or both when trying to login | An error message appears letting the user know that there is an error with their attempted login | 2  | 
|Test the registration | Unit testing | Email, password, check password  | The user inputs their email and passwords and try to sign up | The user is able to sign up and their email and password (which is hashed) is saved in the database 
|Test the registration with wrong inputs | Unit testing | Email, password, check password | The user doesn't input the correct values for email or the passwords aren't matching | An error message is displayed on the user interface 	| 2  | 
|Test the profile page | Unit testing | n/a  | The user is clicks on teh button in the home page to access their profile page 	| The user is able to see their personal details and the posts that they have posted in the past 	| 6  | 
|Test the login, registeration, home screen, new posts and profile page  | Integration testing   | Email, Password, Check password, title, content, ingredients  | The user is able to signup and then login, letting them go to the home screen where they are able to view everyone's posts and then they are able upload new posts | They are able to signup and login and create a new post that is displayed in the home screen and profile page  | 1, 2, 3, 6 |
|Test the shopping list function	|Unit testing 	| n/a	| This enables the user to add their ingredients into their shopping list from the post so that they do not miss any ingredients  | The ingredients from the post are in the shopping list 	| 4  | 
| Test the posting and shopping functions 	| Usability testing	|Title, content, ingredients	|  The user is able to use these functions with no issue and they are able to see if it is easy to naviage and use 	| User is able to use these functions with ease 	| 1,4 | 
| Test the search function  | Unit testing  | Word searched in search bar   | The user inputs a search word in the search bar which searches the database   | The posts with the key word is outputted in the home page |  5 |  
| Test the new posts, home page, shopping list 	| Integration testing 	| Title, content, ingredient	| The user inputs a recipe, then adds them into the shopping list 	| The shopping list displays the ingredients and the home page displays the post  | 1,3, 4  | 


# Criteria C: Development
## Existing Tools

| Software/Development Tools | Coding Structure Tools          | Libraries      |
|----------------------------|---------------------------------|----------------|
| PyCharm                    |Encryption                       | Flas           |
| Relational databases       | Objects, attributes and methods | sqlite3        |
| SQLite                     | If statements                   | passlib        |
| Python                     |                                 |                |
| Chat GPT                   |                                 |                | 

## List of techniques used
1. Flask library/routes
2. For loops
3. If statements
4. Password hashing
5. Interacting with databases
6. Lists
7. Cookies


## Success criteria 1 

The first success criteria was that the user would be able to post on the website. To do this, I had to work through several things. I split this into 3 sections, getting the information from the UI, then validating it, and then I uploaded it into the database. Althoguh it seemed simple, I wasn't sure how everything would work so the biggest challenge was taking all the skills and putting them together. 

```.py
@app.route('/new_post', methods=['GET','POST']) # For the user to upload posts
def new_post():
    msg = ""
    if request.cookies.get('user_id'): #Validate the user 
        user_id = request.cookies.get('user_id') #Get the user_id of the user
        db = database_worker("social_net.db")
        if request.method == 'POST': #Check if the form is being submittted 
            title = request.form['title']
            content = request.form['content']
            ingredients = request.form['ingredients']
            if len(title) > 0 and len(content) > 0 and len(ingredients)>0:
                new_post = f"INSERT into posts (title, content, ingredients, user_id) values('{title}','{content}','{ingredients}',{user_id})"
                db.run_save(query=new_post)
                posts = db.search("Select * FROM posts")
                return redirect(url_for('home', posts = posts ))
            else:
                msg = "Please enter title, content and ingredients"
                return render_template("new_posts.html", message=msg) # Can display an error message 
        return render_template("new_posts.html", message=msg)
    else:
        return redirect('login')
```
With the above code, I created an algorithim for the user so that they are able to upload new posts to the social media site. I made sure to have a step by step solution for the user so that they are able to upload their posts. First, I make sure to validate the user as like in all the other pages needs to be logged in to be able to access it preventing unauthorized access. Then I check which method it is, and if the form is being posted, then I get the information from the UI and validate it. After it is validated, I connet to the database using the database_worker function, then insert it into the post page. As I wanted the user to get redirected to the home page again, I had to search the database again by using the database_worker function, searching, then using the return redirect(url_for  ) tool to redirect them to the home page that would display alll the posts including the new one. 

Using the database worker function enables me to simplify my code as it is something that is repeated lots of timees throughout the application (showing patter recognition) as I need to use a database many times. Therefore, makign it into a function makes it much easier to edit is something is worng. 

## Success criteria 2
For this success criteria I had to create a login page and a signup page for the user. The signup roughly followed the same format as the new_posts page, however I had to call a library to hash the function. For the login, I had to do the same as the new_posts page as well, however, I had to make sure to validate to check if it was right, then redirect them to the home screen. 

```.py

@app.route('/', methods=["GET","POST"])
@app.route('/login', methods=["GET","POST"])
def login():
    msg = ""
    if request.method == "POST":
        email = request.form['email']
        passwd=request.form['passwd']
        db = database_worker("social_net.db")
        user = db.search(f"Select * from users where email = '{email}'")
        if user:
            user = user[0] #because search function returns a list
            id, email_db, hashed = user
            if check_password(hashed_password=hashed, user_password=passwd):
                db = database_worker("social_net.db")
                posts = db.search("Select * FROM posts")
                response = make_response(redirect('home'))
                response.set_cookie('user_id', f"{id}")#cookie is a string
                return response
            else: msg = "Please enter the correct password"
        else:
            msg = "user does not exist"
    return render_template("login.html", message=msg)
```


```.py
@app.route('/signup', methods=["GET","POST"])
def signup():
    msg = ""
    if request.method == "POST":
        email = request.form['email']
        passwd=request.form['passwd']
        passwdconfirm=request.form['confirmpasswd']
        if passwd==passwdconfirm:
            hash = encrpyt_password(passwd)
            db = database_worker("social_net.db")
            new_post = f"INSERT into users (email,password) values('{email}','{hash}')"
            db.run_save(query=new_post)
            return redirect(url_for('login'))
        else:
            msg = "Passwords do not match"
    return render_template("signup.html", message=msg)
    
```
For the signup page, I follow the same process as the new_posts page. However, on this page, I do not find the cookie for the user as they are still not logged in because its the signup page. Then I check if the method is posts to make sure that the user is trying to signup. Then I get the information from the UI, then i check if the passwords are corrrect. As for the email, in the HTML, I specified the input as an email so it will automatically send an error code if its not a valid email address. If the passwords do not match, it displays an error code and the user has to reinput it. If it does then I first hash the password to make it more secure, to do this I call on a function that I imported from my library called encrypt password. Then I used the database_worker class to insert the information into the users page in the social_net database and redirect them to my login page. 

For the login page, it is slightly more complicated. The first two steps, checking the mthod and getting the information is the same. However, to check that the users email is correct I use the database_worker function to see if the user does exist. If it does, I get the information from that row and then use the check_password function imported from my library to check if the passwords are correct. If everything is good, I first set the cookie for the user so that I am able to use that later. Then I redirect it to the home page by getting all the posts from the post page in the database, then redirecting to the home page. 


## Success Criteria number 3 and 5
For these 2 success criteria, there were two main issues. First was getting all of the posts from the database, then displaying them in the homepage for the user to see. Then the other problem was that I had to search the database for a specific ingredient and then display only the posts that applied to the statement. The first one was not as challenging, however the second was quite a challenge. 

```.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% if title %}
    <title>{{ title }}</title>
    {% else %}
    <title>Welcome to the most popular SNS</title>
    {% endif %}
    <link rel="stylesheet" href="/static/home.css">
</head>
<body>
<div>
    <a href = "{{ url_for("shopping_list2", user_id = user_id) }}"> Shopping List </a>
    <a href = "{{ url_for("new_post") }}">Create a new post</a>
    <a href = "{{ url_for ("logout") }}"> Logout</a>
    <a href="{{ url_for('profile', user_id=user_id) }}" class="btn btn-primary">Profile</a>
    <form action="/home" method="post">
        <input type="text" name="query" placeholder="Search...">
        <button type="submit">Search</button>
    </form>

</div>

<table>
    <tr>
        <th>id (Click to add ingredients to shopping list)</th>
        <th>Title</th>
        <th>Content</th>
        <th>Ingredients</th>
    </tr>
        {# template language jinja2 #}
    {% for p in posts %}
    <tr>
        <td><a href = "{{ url_for('shopping_list', user_id=p[4], post_id=p[0]) }}">{{ p[0] }}</a></td>
        <td>{{ p[1].title() }}</td>
        <td>{{ p[2] }}</td>
        <td>{{ p[3] }}</td>
    </tr>
    {% endfor %}
</table>

</body>
</html>
```
This first piece of code is for my HTML. For the HTML, I made sure to create a table that would display everything from the posts page. This enables the user to see other users posts. Additionally I made sure to have at the top of the page a menu bar that would take the users to different pages in the application and there is also a search bar so that the user can search for recipes based on ingredients. Lastly, for each post in the table, the ID is made into a link for the shopping list. Therefore, clicking this will enable the user to create their own shopping list in the application. 

```.py
@app.route('/home', methods=['GET','POST'])
def home():
    if request.cookies.get('user_id'):
        user_id = request.cookies.get('user_id')
        db = database_worker("social_net.db")
        posts = db.search("Select * FROM posts")
        if request.method=='POST':
            search_query = request.form['query']
            posts2 = db.search(f"SELECT * FROM posts WHERE ingredients like '%{search_query}%' ")
            return render_template("home.html", posts=posts2, user_id = user_id)

        return render_template("home.html", posts=posts, user_id = user_id)

    else:
        return redirect('login')
    return render_template("home.html", posts=posts, user_id = user_id)

```
The above code is showcasing the home page python code. First I make sure that the user is logged in as this page is restricted to people who have an accout. Then I just use the database_worker function to get all the posts. However, if the user sends a search request, then I don't get all the posts, instead I use the % signs to get posts that are like the search query and then show those on the page. 


## Success criteria number 4
For this success criteria, I had to figure out how to let the user have their own shopping list. This was challenging as I had to first for each recipe that the user wanted to have, I needed to add those ingredients into the database. Then I had to show those ingredients into another table. 
```.py
@app.route('/shopping_list/<int:user_id>/<int:post_id>', methods=['GET'])
def shopping_list(user_id, post_id):
    if request.cookies.get('user_id'):
        db = database_worker("social_net.db")
        post = db.search(f"SELECT * FROM posts WHERE id = {post_id}")[0]
        ingredients = post[3].split(",")
        for ingredient in ingredients:
            new_ingredients = f"INSERT INTO ingredients (user_id, ingredients) VALUES ({user_id}, '{ingredient}')"
            db.run_save(new_ingredients)
        return redirect(url_for('shopping_list2',user_id=user_id))
    else:
        return redirect('login')

@app.route('/shopping_list2/<int:user_id>')
def shopping_list2(user_id):
    if request.cookies.get('user_id'):
        db = database_worker("social_net.db")
        ingredients = db.search(f"SELECT * FROM ingredients WHERE user_id = {user_id}")
        db.close()
        return render_template("shoppiing_list.html", ingredients=ingredients)
    else:
        return redirect('login')
        
```
For this code, I continue on from the home page. If the user clicks on the links in the home page table, then I take the user_id but also the post_id. Having the post_id enables me to search for the post that the user wants to add to their shopping list, then get the ingredients from that post. After I get the ingredients I redirect the user to a seperate route. This is because the original shopping list has the post_id which is great for when I need to add the post's ingredients to the database, however, when I'm showing the shopping_list, I don't want it to just be of one post's ingredients but of all of them that the user has inputted. Thereofre the shopping_list2 route only takes the user_id so that I only select the ingredients that are from that user using the database_worker function then I use the render_template to showcase the shopping list. For both pages, I made sure to validate that the user does exist to prevent unauthorized access. 

The above code shows how I used the computation thinking skills pattern generalization and abstraction and also decomposition in the code for the shopping list. I split the shopping list into two parts, making sure to only take the information that is only necessary for each one. For the first I made sure to get the post id and the user id for the shopping list url as I needed to add data to the database. Having the post id made it easy for me to do that. However, if I had the post id, it would be hard to show all of the ingredients as it would be post sensitive. Therefore, I made a second method without the post_id that showed all of the ingredients. Therefore, this shows how I only used the variables that were only needed and how I disregarded the ones that weren't important.


## Success criteria number 6
```.py
@app.route('/profile/<user_id>', methods=['GET','POST'])
def profile(user_id:int):
    if request.cookies.get('user_id'):
        db = database_worker("social_net.db")
        user,posts = None, None
        user= db.search(f"SELECT * from users where id={user_id}")
        if user:
            posts = db.search(f"select * from posts where user_id={user_id}")
            user = user[0] #remeber db.search returns a list
        return render_template("profile.html", user=user, posts=posts)
    else:
        return redirect('login')
	
```
The above code shows the function for the profile page. This enables the user to view information about themselves, which includes their prior posts. To do this I used databases to save their posts and if statmenets to validate if they were users. This would enable me to showcase their posts for which I used the same format as the home method and called it from the database then displayed it. 

```.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="/static/home.css">
</head>
<body>
<div>
    <a href = "{{ url_for("home") }}"> Homepage</a>
</div>

{% if user %}
    <h1>Welcome, {{ user[1] }}</h1>
    {% if posts|length > 0 %}
    <p>Your posts are:</p>
    <table>
    <tr>
        <th>id</th>
        <th>Title</th>
        <th>Content</th>
    </tr>
        {# template language jinja2 #}
    {% for p in posts %}
    <tr>
        <td>{{ p[0] }}</td>
        <td>{{ p[1].title() }}</td>
        <td>{{ p[2] }}</td>
    </tr>
    {% endfor %}
    </table>
    {% else %}
        <p>You don't have posts yet</p>
    {% endif %}
    {% else %}
    <h1> User does not exist</h1>
{%  endif %}
</body>
</html>

```
The above code shows my HTML for my profile page. This enables the user to view their own profile, and I coded python in the HTML page so that I could adjust what message appears in the final HTML rendering. This makes the code much simpler as it's not going through the python file and it's in the HTML. 
 
## Pattern recognition

```.py
from my_lib import database_worker, encrpyt_password, check_password
```
I made this to simplify my code. Creating this function means that every time i have to save something to a database, I am able to just call the function instead of writing it all out every single time. Additionally, if I need to change something I only have one point to change. This is an example of the computational thinking skill pattern recognition as I was able to see that this is something that is repeated throughout. Additionally, it also shows algorithm design as I used an algorithm that enabled me to do the exact same things many times. 



## Base.html
```.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% if title %}
    <title>{{ title }}</title>
    {% else %}
    <title>Welcome to the most popular SNS</title>
    {% endif %}
    <link rel="stylesheet" href="/static/my_style.css">
</head>
<body>
<div>
    <a href = "{{ url_for("home") }}"> Homepage</a>
    <a href = "{{ url_for("new_post") }}">Create a new post</a>
    <a href = "{{ url_for ("logout") }}"> Logout</a>
    <form action="/home" method="post">
        <input type="text" name="query" placeholder="Search...">
        <button type="submit">Search</button>
    </form>

</div>
{% block content %}{% endblock %}
</body>
</html>
```

I made this file as it enabled me to have a common html throughout my website. This enabled me to add a menu bar which I used in a few of my pages. Again, this was to prevent redundant code in my files. I could just have one file that organized the menu bar of a few of my screens instead of writing it in each single one. 

## Signup 

```.py
@app.route('/signup', methods=["GET","POST"])
def signup():
    msg = ""
    if request.method == "POST":
        email = request.form['email']
        passwd=request.form['passwd']
        passwdconfirm=request.form['confirmpasswd']
        if passwd==passwdconfirm:
            hash = encrpyt_password(passwd)
            db = database_worker("social_net.db")
            new_post = f"INSERT into users (email,password) values('{email}','{hash}')"
            db.run_save(query=new_post)
            return redirect(url_for('login'))
        else:
            msg = "Passwords do not match"
    return render_template("signup.html", message=msg)
    
```
    
   In this route I used the database worker function to save the users details to the database. I first checked if the method was a post method and then from there I started the process of saving it to the database. I first got the user inputs from the webpage and then from there I made sure to validate them. The email is automatically validated but I made sure that the password was correct by having a confirmation. If it didn’t go through the page would display a message saying that and if it did the user would be redirected to the login. 
   
## User validation

```.py
if request.cookies.get('user_id'):
```
For each web route, I made sure to request the cookies from the user. This made sure that the user was already logged in and has a cookie. This means that even if someone knows the url of the website and they input the url into their search bar,they are not able to access it. This increases the security of the whole website as people need to have had accounts made and have to login as normal.

## Home.css

```.css
body {
  background-color: #FCEADE;
  background-image: url("/static/Cooking-Home-Collection.jpeg");
  background-size: cover;
  height: 100%;
  font-family: Arial, sans-serif;
  font-size: 16px;
  line-height: 1.5;
  background-color: rgba(252, 234, 222, 1);
}
div {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #ffffff;
  border-bottom: 1px solid #cccccc;
}

div a {
  color: #333333;
  text-decoration: none;
  margin-right: 10px;
}

div form {
  display: flex;
  align-items: center;
}

div form input[type="text"] {
  padding: 5px;
  border: 1px solid #cccccc;
  border-radius: 5px;
  margin-right: 5px;
}

div form button[type="submit"] {
  padding: 5px;
  border: 1px solid #cccccc;
  border-radius: 5px;
  background-color: #ffffff;
  color: #333333;
  cursor: pointer;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px auto;
  background-color: rgba(255, 255, 255, 0.9);
}

table th {
  text-align: left;
  background-color: #333333;
  color: #ffffff;
  padding: 10px;
}

table td {
  border: 1px solid #cccccc;
  padding: 10px;
}

table td a {
  color: #333333;
  text-decoration: none;
}

table td a:hover {
  text-decoration: underline;
}
table td:first-child {
  color: red;
}

```
This is the CSS file for my home page. For each file, I made sure to use the same background image and the same style as this one. However, as different pages were made to do different things, I made seperate CSS files for each one, ending up with 3. One for the login and all the other form pages, one for the home page, and one for the shopping list page. This made the CSS as simple as possible without compromising on each pages needs. 

## Delete shopping list items 

```.py
@app.route('/delete_ingredient/<int:ingredient_id>', methods=['POST'])
def delete_ingredient(ingredient_id):
    if request.cookies.get('user_id'):
        user_id = request.cookies.get('user_id')
        db = database_worker("social_net.db")
        db.run_save(f"DELETE FROM ingredients WHERE id = {ingredient_id}")
        db.close()
        return redirect(url_for('shopping_list2',user_id=user_id))
    else:
        return redirect('login')
```
At first, I was not sure how to delete the items from the shopping list. This is because I needed a way to access each indvidual ingredient in the shopping list database and select their id. Therefore, to do this, I used the same technique we did in the users page in class, and in my home page. For each ingredient that I showed in the table, I managed to get their ids. Then I would be able to get the id whenver I wanted and then connect to the database to delete the item from it. 

## Shopping_list.html 

```.html
<!DOCTYPE html>
<html>
<head>
	<title>Shopping list</title>
    <link rel="stylesheet" href="/static/shopping_list.css">
</head>
<body>
<div>
    <a href = "{{ url_for("home") }}"> Homepage</a>
</div>

	<table>
		<thead>
			<tr>
				<th>ID</th>
				<th>Ingredients</th>
				<th>Check</th>
			</tr>
		</thead>
		<tbody>
			{% for ingredient in ingredients %}
			<tr>
				<td>{{ ingredient[2] }}</td>
				<td>{{ ingredient[1] }}</td>
				<td>
                    <form action="{{ url_for('delete_ingredient', ingredient_id=ingredient[0]) }}" method="post">
                        <input type="hidden" name="_method" value="DELETE">
                        <button type="submit">Delete</button>
                    </form>
                </td>
			</tr>
			{% endfor %}
		</tbody>
	</table>
</body>
</html>

```
The above piece of code is my shopping list page. I followed the same format as my home page, creating a table by looping throuh each ingredient in the shopping list database. Then I made sure to include the delete function which enabled users to delete their items once they bought it which was very important as without it, it would be very impractical. 



# Critieria E: Evaluation

## Evaluation table

### Client (Record of this is in the appendix) 
| Critieria | Met or not?        | Feedback       |
|----------------------------|---------------------------------|----------------|
|1. The user can upload their own recipes as a social media post. The post includes the title, content and ingredients  |Met      |Met, no suggestions	|
|2. There is a secure login and registration page for each user  | 	Met	| Met, no suggestions		| 
|3. The user can view other social media posts   | Met		| Nice posts, however, could it be possible to have images on each posts to see the recipe  | 
|4. Users are able to create their own shopping list in the app  | Met		| Make the adding function more intuitive and make the shopping list look a little better| 
|5. Users can search recipes based on ingredients  | Met		|Specify that it is search by ingredient 			| 
|6. User can have their own profile page that displays their email and posts.   | Met			| Add a button to the shopping list		| 

### Other user (Record of this is in the appendix) 
| Critieria | Met or not?        | Feedback       |
|----------------------------|---------------------------------|----------------|
|1. The user can upload their own recipes as a social media post. The post includes the title, content and ingredients  |Met      |Good		|
|2. There is a secure login and registration page for each user  | 	Met	| Good		| 
|3. The user can view other social media posts   | Met		| Add the names of the people who posted the recipe		| 
|4. Users are able to create their own shopping list in the app  | Met		| Make how to add more clear since it is quite confusing 			| 
|5. Users can search recipes based on ingredients  | Met		|Specify that it is search by ingredient 			| 
|6. User can have their own profile page that displays their email and posts.   | Met			| Make the username a bit more visible			| 

This was after I showed this to an anonymous student here at my school to get their feedback on the project.

## Suggestions for future development
For future development the first suggestion was including the names of the people posting the ingredients. This would be in the homepage so that people would be able toee who posted them. Right now, even though the project does enable users to share recipes, wich was the initial aim, it would be better for the end user if they could talk to the person for feedback and questions. For example, if they don't understand some instructions, then they can ask for clarification, making the site much more useful

The second suggestion was to let the user post images of their recipes to their posts. This would enable the users of the social media site to see much more clearly how to make their recipe. Right now, all the users have are written steps which are a bit confusing to follow at times if the instructions are complicated. Therefore, having images would make it much more easier to understand making the site more useful to the end user. 


# Appendix

## Client interview (planning and design) 
![](https://github.com/KaiFig/Unit_4/blob/main/Project/Pictures/Client_notes_project_4.jpg)

## Client interview (Feedback) 
![](https://github.com/KaiFig/Unit_4/blob/main/Project/Pictures/Client_feedback_project_4.jpg)
