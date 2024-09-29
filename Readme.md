# Website Library Online 

This project is a website to complete my take home test as python developer. In this website there are many main feature like : 
- Login 
- Register new user 
- Add new transaction borrow book 
- See list all transaction borrow book 
- Update status transaction 
- Admin page from Django to update database manual 

## Method Used 
- Authentication
- Migration Database 
- Django lifecycle

## Technology 
- Python 
- Django 
- Sqllite 
- Tailwind 

## Getting Started 

These are enviroment used for this project: 
- python version > 3.11.7 
- django version 5.1.1 

### Set Up Python

To download python you can follow instruction from this [link](https://www.python.org/downloads/). You can check your python is installed in your computer by running this command below on terminal
```
python --version
```

### Set Up Django

After you install python, you can install django (framework website from python). You can do that by running this command below on terminal 
```
python -m pip install Django
```
To verify your django is installed, you can check that by running this below code on file python. 
```
>>> import django
>>> print(django.get_version())
5.1
```

After that, you can run this below command on terminal to run this project 
```
python manage.py runserver
```
You can see this project running in http://127.0.0.1:8000/pinjamBuku. You can also open page admin to access database in http://127.0.0.1:8000/admin 

### User for this project 
To try this project you can try this super admin to access any page. 
- email : admin@examople.com 
- password : temp123456
- username : admin

Or you can try this user , but it can't access page admin 
- email : yudis@mailinator.com 
- password : Temp1234
- username : yudisaditya