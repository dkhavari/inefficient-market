import os
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.mongoengine import MongoEngine

# ------------------------------
# Setting up the program.
# ------------------------------
app = Flask(__name__)

# Turn on debugging.
app.debug = True

app.config['MONGODB_SETTINGS'] = {
	'db': 'muse',
	'host': 'ds049170.mongolab.com',
	'port': 49170,
	'username': 'primary', # Probably read these in from a non-committed file.
	'password': 'gunda'
}

app.config['SECRET_KEY'] = 'satisfactionize'

db = MongoEngine(app)

# Register the blueprints.
def register_blueprints(app):
    # Prevents circular imports
    from views import posts
    app.register_blueprint(posts)

register_blueprints(app)

import views