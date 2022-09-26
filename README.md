# Flask-app
This is production ready flask application used for reference in future

# Get started
Clone the project using following command

```git clone https://github.com/aditya-deshmukh-tech/flask-app.git```

once cloned the project get inside directory and run the following commands

```cd flask-app```

```virtualenv venv```

For linux users

```source venv/bin/activate```

For Windows users

```venv\Scripts\activate```

```pip install -r requirements.txt```

To start application in developement mode use the following command

```python wsgi.py```

To start application in production mode use th following ``gunicorn`` commande

```gunicorn --bind 0.0.0.0:5000 wsgi:gunicorn_app```

# Flask setup script
flask is a really easy and quickly ready to run application but to use flask for production we cannot use this simple single py file approch.
For production case we need flask app to be more modular and dynamic.
i have seen a lot of structure for flask but what i use for this project found to be best one for me especially for rest app.
But creating this structure from scratch again for new project is kind of hard to remember so thats why i created one ``flask-setup.sh`` script which will automatically create basic flask structure for me

```./flask-setup.sh```
