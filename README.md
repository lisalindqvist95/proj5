![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Glimpse

## Project Goals:
Glimpse is a content sharing app for makeup-artists and enthusiasts to share content. The users are able to follow each other, like each others content and pin things for later. The goal for the user is to find inspiration, share their work and find other like-minded people. This is the API that tracks and stores users, likes, pins, posts and followers. 

## Data Model
This Project is based around Object-Oriented Programming.
***It is built with Django’s Class-Based Generic Views and Django AllAuth is used as the authentication system.
The project has a Post model wich allows the admin to create blogposts and a Comment model which allows users to comment on posts.***

## Testing

### Validator Testing

#### Python
All Python files passed through Pep8.

#### Manual Testing

## Security Features and Defensive Design

### User Authentication
Django's UserPassesTestMixin is used so that only users who created the comment edit/delete it.

### Form Validation
The form won't submit if it contains empty or invalid data.

### Database Security
An env.py file is used to store the database url and secret key to prevent unwanted connections to the database.
Cross-Site Request Forgery (CSRF) tokens are used on the forms on the site.



## Deployment
This project was depolyed via Heroku from the GitHub repository. See the steps taken below:

### Create Heroku App:
Log in to Heroku
Press the "New" button on the main page and choose "Create New App" from the drop-down menu
Enter the app name and select your region
Then "Create App"

### Create a database with ElephantSQL
Log in to ElephantSQL
Press the button "Create New Instance" i the top right corner
Give your plan a name and select your plan
Press the button "Select Region" and select a data center near you
Then press the "Review" button
Check that all your details are correct and press "Create instance"
Copy the URL database to paste in your GitPod workspace

### Github env.py and settings.py file:
Create an env.py file in the main directory of your GitPod workspace
In the env.py file add the DATABASE_URL value and create a chosen SECRET_KEY
Go into the settings.py file to import the env.py file, add file paths for both the SECRETKEY and DATABASE_URL (comment out the default database)
Save your files and make migrations

### Create files / directories
Create a requirements.txt file in the main directory
Create a "Procfile" in the main directory and add: gunicorn project-name.wsgi

Heroku Config Vars
DATABASE_URL value (copy database from ElephantSQL)
SECRET_KEY value
CLOUDINARY_URL
PORT = 8000
DISABLE_COLLECTSTATIC = 1

### Deployment
Under the deploy tab on Heroku conncet to your GitHub and add your repository
Deploy at the bottom of the page
Click View to view the deployed site.

## Languages
Python
HTML
CSS
Javascript

## Frameworks & Libraries Used
Django: Main framework used for the project
Django-allauth: Authentication library used for the project
PostgreSQL Used as database
Heroku: Used for deployement
Chrome Dev Tools: Used to test responsiveness
Font Awesome: Used for icons
GitHub: Used for version control and agile tool
Google Fonts: Used for fonts
W3C: Used to validate HTML & CSS
PEP8 Online: used to validate Python code
Summernote: Editor to allow users to edit their posts
Crispy Forms: used for Django Forms
Cloudinary: Image hosting service
Bootstrap: CSS Framework for responsiveness and styling
Tables Generator: Used to create markdown table

## Credits
W3Schools
Django Docs
Bootstrap
Stack Overflow
Code Institute - Blog Walkthrough Project
AliOKeeffe - Easy Eater Project
Unsplash
Adobe stock


