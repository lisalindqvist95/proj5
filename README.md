# Glimpse

## Project Goals:
Glimpse is a content sharing app for makeup-artists and enthusiasts to share content. The users are able to follow each other, like each others content and pin things for later. The goal for the user is to find inspiration, share their work and find other like-minded people. This is the API that tracks and stores users, likes, pins, posts and followers. 

Frontend repository can be found [here](https://github.com/lisalindqvist95/proj5_frontend).
Live API can be found [here](https://proj5-api.herokuapp.com/).

## Testing

### Validator Testing

#### Python
All Python files passed through Pep8.

#### Manual Testing

Manual testing involved visiting each URL to make sure that the correct results were returned. See results below:

| URL         | Passed Y/N? |
|-------------|-------------|
| root        | Y           |
| /profiles/  | Y           |
| /posts/     | Y           |
| /comments/  | Y           |
| /likes/     | Y           |
| /pins/      | Y           |
| /followers/ | Y           |

## Security Features 

### Database Security
An env.py file is used to store the database url and secret key to prevent unwanted connections to the database.

## Deployment
This project was depolyed via Heroku from the GitHub repository. See the steps taken below:

### Create Heroku App:
- Log in to Heroku
- Press the "New" button on the main page and choose "Create New App" from the drop-down menu
- Enter the app name and select your region
- Then "Create App"

### Create a database with ElephantSQL
 - Log in to ElephantSQL
 - Press the button "Create New Instance" i the top right corner
 - Give your plan a name and select your plan
 - Press the button "Select Region" and select a data center near you
 - Then press the "Review" button
 - Check that all your details are correct and press "Create instance"
 - Copy the URL database to paste in your GitPod workspace

### Github env.py and settings.py file:
 - Create an env.py file in the main directory of your GitPod workspace
 - In the env.py file add the DATABASE_URL value and create a chosen SECRET_KEY
 - Go into the settings.py file to import the env.py file, add file paths for both the SECRETKEY and DATABASE_URL (comment out the default database)
 - Save your files and make migrations

### Create files / directories
Create a requirements.txt file in the main directory
Create a "Procfile" in the main directory and add: gunicorn project-name.wsgi

### Heroku Config Vars
DATABASE_URL - value (copy database from ElephantSQL)
SECRET_KEY - value
CLOUDINARY_URL - value (copy from cloudinary)
DISABLE_COLLECTSTATIC = 1
CLIENT_ORIGIN - URL is the deployed version of your front end app
CLIENT_ORIGIN_DEV - URL is the development URL of your front end app
ALLOWED_HOST - Deployed version of API

### Deployment
Under the deploy tab on Heroku conncet to your GitHub and add your repository
Deploy at the bottom of the page
Click View to view the deployed site.

## Languages
Python
Django
Django REST framework

## Frameworks & Libraries Used
 - [Cloudinary](https://cloudinary.com/): Image hosting service 
 - [Django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/): Authentication library used for the project 
 - [PostgreSQL](https://www.postgresql.org/): Used as database
 - [Heroku](https://id.heroku.com/login): Used for deployement
 - [GitHub](https://github.com/): Used for version control and agile tool 
 - [PEP8 Online](http://ww1.pep8online.com/): used to validate Python code
 

## Credits
 - [Tables Generator](https://www.tablesgenerator.com/markdown_tables): Used to create markdown table
 - [Stack Overflow](https://stackoverflow.com/)
 - [Code Institute - Django REST Framework Walkthrough Project](https://github.com/Code-Institute-Solutions/drf-api/tree/ed54af9450e64d71bc4ecf16af0c35d00829a106)


