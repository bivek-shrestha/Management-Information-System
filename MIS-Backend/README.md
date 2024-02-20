## Backend Setup Instructions (Django Server):
### Setup with pipenv:
### Navigate to the folder containing the Pipfile and Pipfile.lock.

### Step 1: Activate the virtual environment:

```
pipenv shell

```

#### Step 2: Install server dependencies (only required the first time):


```
pipenv install  

```

#### Run the Server:

a. Navigate to the folder containing manage.py:

```
cd backend\
```
b. Start the Django server:

```
pipenv run python manage.py runserver

```

## Troubleshooting

#### remove the Pipfile and Pipfile.lock

Remove the Pipfile and Pipfile.lock. <br>

Use any Python virtual environment management package like pipenv, venv, or poetry.
```
pip install -r requirements.txt
```

