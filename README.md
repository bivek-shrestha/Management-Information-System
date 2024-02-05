# React + Vite

# Frontend for the MIS.

## Setup instructions:

### Prerequistes

node must be installed.

### for the first time only

We only need to install all our dependencies only once.
Move to folder with package.json file and type the following command.

```
npm install
```

### everytime when you need to start development server.

```
npm run dev
```

### this project consist the code for our frontend of MIS system for Department of Electronics and Computer Enginneering.

We have just started out our project so currently it contains only Routine Management system of MIS. Other features would be added by our juniors who will come to 4th year.

### Home Screen

![dashboard](/imgs/dashboard_img1.png)

if you aren't authenticated you will be directed to login page. For authentication mechanism we have used jwt

![loginpage](/imgs/loginpage.png)

if you click on Routine under the class table you can view classRoutine.

![classroutine](/imgs/classroutine.png)

when you click on edit icon you get a model where you can update your model.

![editperiodmodel](/imgs/editperiodpage.png)

whe you click on any field you want to edit that is being , card changes to provide a form for upation within the card itself.

![telecommunicationcard](/imgs/telecommunicationcard.png)

For example if I click on the telecommunication card. I will get a form inside card like this for updation.

![subjectfieldupdate](/imgs/updatesubjectfield.png)

similary for other fields on card as well.



# DJANGO BACKEND SERVER FOR MIS (IOE) CAMPUS
## this is our backend server for the department of computer and electronics engineering pulchowk campus

## set up instruction using pipenv

### navigate to the folder containing Pipfile and Pipfile.lock

#### step 1 : to activate environment 

```
pipenv shell

```

#### step 2 : to install dependencies for our server 
Note: this instruction needs to be run only the first time to install dependencies

```
pipenv install  

```

#### step 1 : to run the server
Navigate to the folder containing manage.py file in this case 

```
cd backend\
```
and then type this

```
pipenv run python manage.py runserver

```

## if error occurs 

#### remove the Pipfile and Pipfile.lock

and then use any python virtual environment management pakage like pipenv or venv or poetry

## example using only pip

pip install -r requirements.txt


