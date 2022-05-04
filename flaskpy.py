import datetime

from flask import request, render_template, escape, session, redirect, url_for
from orm import *
from init import app


def workers_list_func(lst, n=4):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]



@app.route('/')
def main_page():
    return render_template("main.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/catalog')
def catalog():
    return render_template("catalog.html")

if __name__ == '__main__':
    app.run(debug=True)
