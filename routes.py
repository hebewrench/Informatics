from flask import Flask, session, render_template, redirect, url_for, request, flash
from app import app
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db, forms, login_manager, admin, basic_auth
from app import db

import json
from urllib.request import urlopen







#from app.forms import
#from app.models import

#EXAMPLE FROM OTHER MODULE
@app.route("/")
@app.route("/homepage")
def homepage():
    form=forms.search()
    return render_template('homepage.html', title='Homepage', form=form)

@app.route("/test", methods=['POST'])
def test():
    title = request.form['title']
    title = title.replace(" ", "+")
    title = title.lower()

    author = request.form['author']
    author = author.replace(" ", "+")
    author = author.lower()


    subject = request.form['genre']
    subject = subject.replace(" ", "+")
    subject = subject.lower()

    string=""

    if title != "":
        string = string + "&title=" + title

    if author != "":
        string = string + "&author=" + author

    if subject != "":
        string = string + "&subject=" + subject

    api = "https://openlibrary.org/search.json?" + string
    resp = urlopen(api)
    book_data = json.load(resp)["docs"]
    book_data = book_data[:10]
    return render_template('test.html', number=book_data, api=api, book_data=book_data)
