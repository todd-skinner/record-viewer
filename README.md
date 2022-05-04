## Install Flask-AppBuilder

Refer to the [documentation](https://flask-appbuilder.readthedocs.io/en/latest/installation.html) for instructions on installation

## Create admin user

Navigate to the project root directory and run the following command:
```
flask fab create-admin
```
Follow the prompts to create admin user and password

## Run
Execute the command:
```
flask run
```
If the app runs succesfully, the command will return the address it is running on. By default, it is http://127.0.0.1:5000/.

## Create standard user

After running the Flask app, open it on your web browser and login using your admin credentials. In the Security dropdown in the top toolbar, select `List Roles`

![image](https://user-images.githubusercontent.com/13643320/166690934-258ce0b7-a66e-44bd-900e-6b845010b561.png)

Select the Admin role and click `Copy Role` from the `Actions` dropdown.

![image](https://user-images.githubusercontent.com/13643320/166691622-a3558452-3191-4561-8f73-b8879cb6340a.png)

Find the new role, and click the "Edit" button.

![image](https://user-images.githubusercontent.com/13643320/166691910-c202315d-e265-4e15-9b7b-28d7f52d9c5a.png)

In the Edit view, find the permission called `menu access on Security` and click the small "X" to remove it

![image](https://user-images.githubusercontent.com/13643320/166692212-84feb620-dd55-4382-ae6d-51e0270fb3d0.png)

In the Security dropdown in the top toolbar, select `List Users`

![image](https://user-images.githubusercontent.com/13643320/166692492-09dd7e8b-a7e9-4416-91f8-59ac974e3286.png)

In the List Users view, click the blue "+" button to add a new user. Create a user with the role you made earlier and save it.

![image](https://user-images.githubusercontent.com/13643320/166693050-0f572ada-b804-49f2-9c0a-570698661de0.png)


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

