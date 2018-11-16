from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('page1.html')

app.run()

@app.route('/<username>')
def user_page(username):
    return render_template('page1.html', user = username)

