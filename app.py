import os
from flask import Flask, render_template, request, redirect, url_for
from flask.ext.mongoengine import MongoEngine

# ------------------------------
# Setting up the program.
# ------------------------------
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
	'db': 'muse',
	'host': 'ds049170.mongolab.com',
	'port': 49170,
	'username': 'primary', # Probably read these in from a non-committed file.
	'password': 'gunda'
}
db = MongoEngine(app)

import views