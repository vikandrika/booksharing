from flask import Flask
from flask import render_template
from flask import request
import db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('page1.html')

@app.route('/search')
def search_for_person():
    q = request.args.get('query')
    users = db.get_users_by_name(q)
    return render_template('search_results.html', q=q, users=users)

app.run()






