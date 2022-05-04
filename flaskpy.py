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


@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        print("////////////////////////////////////////")
        name = request.form.get('name')
        email = request.form.get('email')
        text = request.form.get('review')
        print(name, email, text)
        new_review = Reviews(name=name, email=email, text=text, time=datetime.now())
        
        db.session.add(new_review)
        db.session.commit()
    return render_template("about.html", reviews=Reviews.query.all())


@app.route('/catalog')
def catalog():
    return render_template("catalog.html", items=Items.query.all())


@app.route('/ice/<item_id>')
def ice(item_id):
    item_id = escape(item_id)

    return render_template("ice.html", item=Items.query.filter_by(id=item_id).one())


if __name__ == '__main__':
    app.run(debug=True)


