## Install Flask-AppBuilder

Refer to the [documentation](https://flask-appbuilder.readthedocs.io/en/latest/installation.html) for instructions on installation

## Create admin user

Navigate to the project root directory and run the following command:
```
flask fab create-admin
```
Follow the prompts to create admin user and password

## Add sample data

Execute the command:
```
python sample_data.py
```
This script will clear out the Contacts table and insert dummy data

## Clear database

Execute the command:
```
python cleardb.py
```
This script will drop all tables in the database. This includes users, so you will need to create an admin user again.

## Run
Execute the command:
```
flask run
```
If the app runs succesfully, the command will return the address it is running on. By default, it is http://127.0.0.1:5000/.