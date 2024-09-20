# Property Hub
This repo contains the code for Property Hub

## Branches
* There are majorly three branches `main`, `release` and `production` public facing
* Production branch points to live environment, release to testing environment, main to development environment
* New branches will be used by developers to work on a new feature or bug fixes by taking a fresh branch from `main`

### Workflow
* Developers should create a feature branch from `main` branch
* Once the work is complete, create a PR with `main`
* To make the new feature live, PR of uat is  needed to merge in production
* Mention Jira ticket number in PR title, and commit message.

## Contributing

#### Technology Stack
* Python 3.10.5 - [Official Download Link](https://www.python.org/downloads/)
* Django 4.0.6 - [Official Link](https://www.djangoproject.com/)
* PostgreSQL - [Official Download Link](https://www.postgresql.org/download/)

#### Development Setup
##### Git & Clone Code
Write this command in the directory where you want to place the project
```shell
git clone https://github.com/malikshahzad28/django-getting-started.git
```

##### Virtual Environment
Create and activate virtual environment and then install the requirements.
```shell
python -m venv .venv                      # First time
#windows
./.venv/Scripts/activate                # In every new terminal window
pip install -r requirements.txt     # First time, and if new package is added
```

##### Database
**Step 1:** Download PostGreSQL

[Download Link](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
Download according to your operating system 32bit/64bit Install PostGreSQL with default settings.

**Step 2:** Download PgAdmin4

Now for the GUI interface of our database we install pgadmin4
[Download Link](https://www.postgresql.org/ftp/pgadmin/pgadmin4/v6.11/windows/)
download according to your operating system 32bit/64bit

**Step 3:** Creating Database
* Open PgAdmin4
* Goto `Servers > PostgreSQL`
* Right click on Databases and click Create
* Select Database name and user by default its postgres, Now click create

**Step 5:** Setup the database environment variables, according to OS.

Guide Link: [https://www.schrodinger.com/kb/1842](https://www.schrodinger.com/kb/1842)


##### Database Migrations
For development environment setup,
```shell
python manage.py migrate
```

##### Run Application
```shell
python manage.py runserver
```
Access local environment at: [localhost:8000](localhost:8000)

## Deployment
Deployment guides will be here.
