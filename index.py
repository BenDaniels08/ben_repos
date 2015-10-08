# -*- coding: utf-8 -*-
from flask import Flask, Response, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
# from pymongo import Connection, MongoClient
from flask.ext.basicauth import BasicAuth
from functools import wraps
import json
import os
# import pandas as pd
# import requests
import datetime
import time

# conn = Connection('127.0.0.1', 27017)

app = Flask(__name__)
app.config.from_object('settings')

# the toolbar is only enabled in debug mode:
app.debug = False



def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    #     return username == app.config['USER'] and password == app.config['PASS']

    return username == app.config['USER'] and password == app.config['PASS']

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated




Auth = []
Auth.append(0)

 # set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = os.urandom(24)

toolbar = DebugToolbarExtension(app)

@app.route ("/")
@requires_auth
def find():
	

	
	
	return render_template('index.html',title='Index')


@app.route ("/contact")

def cont():
	
	return render_template('contact.html', title='contact')

@app.route ("/about")

def about():
	
	return render_template('about.html', title='about')






if __name__ == "__main__":
    app.run()