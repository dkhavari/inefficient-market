from app import app
from flask import render_template, request, redirect, url_for

# Homepage.
@app.route("/index.html")
@app.route("/")
def index():
	return render_template("index.html")

# Blog post display page.
@app.route("/blog.html")
def blog():
	# TODO:
	# --------------------------------------------------
	# Get the name of the blog post from the args,
	# retrieve from the database, then render the content.
	# --------------------------------------------------
	return render_template("blog.html")