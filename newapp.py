from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('page1.html')


@app.route('/<username>')
def user_page(username):
    user_data=db.get_user(username)
    return render_template('page1.html', user=user_data)


@app.route('/new_book')
def register_new_book(book_id):
    return render_template('page1.html', book=book_id)


app.run()

