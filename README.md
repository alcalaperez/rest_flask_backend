# rest_flask_backend
A flask-driven restful API with swagger interaction
## [Swagger](https://gymnast-api-heroku.herokuapp.com/)
* You can create an user, authorize yourself with the JWT and use the rest endpoints

 ## Technologies used
* **[Python3](https://www.python.org/downloads/)** - A programming language that lets you work more quickly (The universe loves speed!).
* **[Flask](flask.pocoo.org/)** - A microframework for Python based on Werkzeug, Jinja 2 and good intentions
* **[Virtualenv](https://virtualenv.pypa.io/en/stable/)** - A tool to create isolated virtual environments
* **[SQLAlchemy](https://www.sqlalchemy.org/)** – PSQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL.


 ## Installation / Usage
* If you wish to run your own build, first ensure you have python3 globally installed in your computer. If not, you can get python3 [here](https://www.python.org).
* After this, ensure you have installed virtualenv globally as well. If not, run this:
    ```
        $ pip install virtualenv
    ```
* Git clone this repo to your PC
    ```
        $ git clone https://github.com/gitgik/flask-rest-api.git
    ```


 * #### Dependencies
    1. Cd into your the cloned repo as such:
        ```
        $ cd rest_flask_backend
        ```

     2. Create and fire up your virtual environment in python3:
        ```
        $ virtualenv -p python3 venv
        $ pip install autoenv
        ```

 * #### Install your requirements
    ```
    (venv)$ pip install -r requirements.txt
    ```

 * #### Migrations    
    Then, make and apply your Migrations
    ```
    (venv)$ python manage.py db init
     (venv)$ python manage.py db migrate
    ```

     And finally, migrate your migrations to persist on the DB
    ```
    (venv)$ python manage.py db upgrade
    ```

 * #### Running It
    On your terminal, run the server using this one simple command:
    ```
    $ python manage.py run
    ```
    You can now access the app on your local browser by using
    ```
    http://localhost:5000/
    ```
