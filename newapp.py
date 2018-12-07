from flask import Flask
from flask import render_template
from flask import request, redirect

import sqlite3
app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/')
def hello_world():
    # Connecting to DB
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM users")
    users = list(c.fetchall())

    # Close connection
    conn.close()
    # Return resulting HTML
    return render_template('page1.html', users=users)

@app.route('/user/<login>/')
def user_page(login):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM users WHERE login='%s'" % login)
    user_data = c.fetchone()

    # Close connection
    conn.close()
    return render_template("user_page.html", user=user_data)


@app.route('/search')
def search_for_person():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    q = request.args.get('query')
    c.execute("SELECT * FROM users where name LIKE '{q}'".format(q=q))
    users = list(c.fetchall())
    return render_template('search_results.html', q=q, users=users)




@app.route('/add_user', methods=['GET', 'POST'])
def add_user():

    user_created = False
    error_message = ""

    if request.method == 'POST':
        # add new user data
        user = {}
        user['login'] = request.form.get('login')
        user['full_name'] = request.form.get('full_name')
        user['email'] = request.form.get('email')
        user['f_genres'] = request.form.get('f_genres')
        user['f_authors'] = request.form.get('f_authors')
        user['photo'] = request.form.get('photo')

        # save to database
        conn = sqlite3.connect('app.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users where email='%s'" % user['email'])
        if c.fetchone():
            error_message = "user_exists"
        else:
            c.execute("INSERT INTO users "
                      "(login, full_name, email, f_genres, f_authors, photo) "
                      "VALUES "
                      "('{login}','{full_name}', '{email}', '{f_genres}','{f_authors}','{photo}')"
                      "".format(**user))
            conn.commit()
            user_created = True
        conn.close()
        # redirect to user page
        #return redirect('/user/%s/' % user['email'])


    return render_template(
        "add_user.html",
        user_created=user_created,
        error_message=error_message
    )



app.run()


