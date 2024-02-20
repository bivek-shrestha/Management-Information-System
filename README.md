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


# DJANGO BACKEND SERVER FOR MIS

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


