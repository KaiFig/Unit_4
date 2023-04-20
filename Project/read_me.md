# Unit 4 project: Recipe sharing social network 

![](https://github.com/KaiFig/Unit_4/blob/main/Project/Project%204%20picture.jpeg)
**Fig 1** This is the title picture for my repository

# Criteria A: Planning

## Problem definition
When I brainstormed with my client (myself) about problems I face and a SNS that would solve that, I realized that in school, we are not able to share recipes that we make, which is a shame as we come from such a diverse background and have lots of new and interesting recipes to share. At school, unless we are close to someone, we usually do not get the opportunity to cook with them or learn their recipes. Also, even if I search online, it is hard to get help on a recipe as I don't know them, and there are usually no ways of contacting them. Therefore, an SNS would enable messaging for help. Additionally, whenever I go to the supermarket, since I go there without a shopping list for recipes, I end up buying more than I need. This contributes to increased spending, and also, since I am not able to use everything, it makes me waste food. I have tried writing my own shopping list by looking at the recipe before and writing stuff down, however I have forgotten a nmber of things before so it's not the most effective. As proof of this, the notest taken from the brainstorming session are listed in the appendix. 
　
## Proposed solution
To solve my client’s issue I will be creating a web based social media site using HTML CSS and Python. This site will allow the end user to share their own recipes and other users to share theirs as well. Additionally, they can make a shopping list


## Rationale for proposed solution
I will be making an social media website as it is the most convenient way for the client to be able to view other people's recipes and to comment on them. An SNS involves quick sharing of these recipes making it the most effective. Additionally, it will also enable the user to search through the recipes very effectively through ingredients and name.

As for the software, first of all, I will be using HTML to create the website. This is because HTML enables the creation of the structure of the webpage, and for the developer it is quite easy to learn. Additionally, for the user, it creates a nice website. [^2]

Another language I will be using is CSS. This will enable me to structure the HTML webpage exactly how I want by creating a set of rules for it. This is important as for the end user, it enables them to have a clean website that they can use and navigate through easily. 

Lastly for the last language I will be using is Python. Python enables me to create the functionality for the website. I used python as it can be placed in HTML as well, creating an integrated website. Additionaly, it has a large library that enables me, the developer to rely on other libraries to make the website. Also, it has a very large community of developers, enabling the quick use of research in support of my project. 


**Design statement:**
I will to design and make a web based social media site for a client who is a high school student that is interested in cooking. The SNS will be about sharing and viewing other peoples recipes and is constructed using the software CSS, HTML and Python. It will take 4 weeks to make and will be evaluated according to the criteria A, B, C, D, and E. 


## Success criteria
1. The user can upload their own recipes as a social media post. The post includes the title, content and ingredients 
2. There is a secure login and registration page for each user 
3. The user can view other social media posts
4. Users are able to create their own shopping list in the app
5. Users can search recipes based on ingredients 
6. User can have their own profile page that displays their email and posts. 


# Criteria B: Design

## System diagram

## ER diagram

## UML diagram



## Wireframe diagram 


## Flowcharts 

## Record of Tasks

| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Meeting my client                         | To identify what my client wants for a database  | 15min         | Apr 8th               | A         |
| 2       | Write the Problem defition                        | Expand our problem context and identify a customer and their specific problem so that we know what we need to acheive with our project  |  20min         | Apr 8th          | A         |
|3       | Write the proposed solution and rationale for propsed solution  | My client is able to see what I am creating as a solution and input feedback so that he gets what he wants |50 min | Apr 8th    | A     | 
|4       | Write the design statement | Able to proceed with a clear plan and goal now that the design statement is written    | 10 min  | Apr 8th  | A |
|5       | Write each success criteria  | Have a clear outline of what is needed to be acheived for my client so I am able to fulfill the clients needs   | 20 min | Apr 8th | A  |
|6       | Create the system diagram  | Can showcase what the whole SNS will look like and what files and programs it will run  | 30 min  | Apr 9th | B  | 
|7       | Create the wireframe diagram  | We can showcase what the SNS will look like, and i have a plan for how to style it using HTML and CSS | 45 min  | Apr 14th | B   | 
|8      | Create the database   | I have a database so that each user is able to have their own account and they are able to have a record of posts   | 20 min | Apr 15th | C | 
|9      | Create the login page  | I create the functionality for the login page, enabling each user to have their own account, and their posts to be linked back to them   | 30 min  | Apr 16th | C | 
|10     | Create the signup page | This enables users to signup to the application, making sure that their passwords are long and strong enough   | 30 min | Apr 16th  | C | 
|11     | Create the home page  | This will be the first screen that the user encounters when they login to the application   | 30 min  | Apr 16th | C | 
|12     | Create the new posts page   | This enables each user to add a post to the Social media site, with their recipe and other important information. Additionally, it will be linked back to the user  | 30 min  | Apr 16th | C | 
|13     | Create the css for the signup page  | It makes everything look much better and the user is able to have a better user experience | 30 min   | Apr 16th  | C   | 
|14     | Create the css for the login and new posts page   | Better user experience  | 30 min  | Apr 16th  | C | 
|15     | Create the css for home page  | Better user experience  | 30 min  | Apr 16th  | C | 
|16     | Create the search bar   | It enables the user to search the database for a recipe with a specific ingredient so that they can base their recipes on what they have | 45 min   | Apr 17th  | C | 
|17     | Create the flow diagrams for an interesting function  | I am able to showcase to everyone how my code works so that they are able to further develop on it  | 45 min  | Apr 17th | B | 
|18     | Create the profile page in the website   | The user is able to have their own profile page where they are able to see all their posts   | 45 min  | Apr 17th  | C | 
|19     | Create the shopping list page in the database | This saves the users ingredients that they click on   | 20 min  | Apr 18th  | C | 
|20     | Create the shopping list page in the website  | The user is able to see each ingredient that they saved   | 40 min  | Apr 19th  | C  | 
|21     | Update the record of tasks    | I have already done a few unit tests so this enables me to give a record of them  | Apr 19th  | C   | 



## Test plan

| Instruction                        | Category     | Input example / code                               | Description                                                                                                        | Expected output                                                         | Success criteria |
|------------------------------------|--------------|----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|------------------|
|Test the login   | Unit testing  | Username and password   | The user is able to login to the application and the home screen is displayed when they enter. An error message appears if the password or the username is not correct  | The user logs in if the username and password is correct and the home screen is displayed with a cookie being created as well   |2, 3 | 
|Test the login, registeration, home screen, new posts and profile page  | Integration testing   | Username, password, title, content, ingredients   | The user is able to signup and then login, letting them go to the home screen where they are able to view everyone's posts and then they are able upload new posts | They are able to signup and login and create a new post that is displayed in the home screen and profile page  | 1, 2, 3, 6



# Criteria C: Development

```.py
from my_lib import database_worker, encrpyt_password, check_password
```
I made this to simplify my code. Creating this function means that every time i have to save something to a database, I am able to just call the function instead of writing it all out every single time. Additionally, if I need to change something I only have one point to change. This is an example of the computational thinking skill pattern recognition as I was able to see that this is something that is repeated throughout. Additionally, it also shows algorithm design as I used an algorithm that enabled me to do the exact same things many times. 

```.py
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


