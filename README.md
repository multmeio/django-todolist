django-todolist
===============
-----------
A simple "ToDo List", built in Django and used to help and show the awesomeness of the django, 
to the folks in the Python tutorial, at [Evolux](http://evolux.net.br) and [Multmeio](http://www.multmeio.com.br).

How to install e config
===============
-----------
#### Follow the steps:

1. Star this and Follow us;
2. Clone or Download this repo;
3. Install [pip](http://www.pip-installer.org/en/latest/) or [easy_install](http://pythonhosted.org/distribute/easy_install.html);
4. Install [South](http://south.readthedocs.org/en/latest/installation.html);
5. Install the project dependencies;
    - ```pip install -r requirements.txt``` in your root project folder.
6. Setup the ```DATABASES``` confs, inside the [settings](https://github.com/multmeio/django-todolist/blob/master/todolist/settings.py#L20) file.
7. Sync your database with the project models and external apps's models:
    - ```python manage.py syncdb```
        - You don't have to add the ```superuser```, this simple project don't will use him. So, when the Django ask if you want to add the ```superuser```, you answer: **no**.
8. Migrate your database's  schema, use the South's command called **migrate**
    - ```python manage.py migrate```
9. Run the tests.
    - ```python manage.py test core```
10. Run your project:
    - ```python manage.py runserver```
11. See in the localhost; 
    - ```127.0.0.1:8000```

- You can change the *port* what django will run your project: 
    - ```python manage.py runserver 8080``` --> ```127.0.0.1:8080```
