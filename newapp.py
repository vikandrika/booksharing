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

    c.execute("SELECT * FROM books")
    books = list(c.fetchall())

    # Close connection
    conn.close()
    # Return resulting HTML
    return render_template('page1.html', users=users, books=books)


@app.route('/user/<email>/')
def user_page(email):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM users WHERE email='%s'" % email)
    user_data = c.fetchone()

    #c.execute("SELECT * FROM exchange WHERE user2='%s'" % user2)
    #user_data = c.fetchone()

    # Close connection
    conn.close()
    return render_template("user_page.html", user=user_data)


@app.route('/userid/<userid>/')
def user_page_new(userid):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM users WHERE userID='%s'" % userid)
    user_data = c.fetchone()

    #c.execute("SELECT * FROM exchange WHERE user2='%s'" % user2)
    #user_data = c.fetchone()

    # Close connection
    conn.close()
    return render_template("user_page_new.html", user=user_data)


@app.route('/search')
def search_for_person():
    q = request.args.get('query')

    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE full_name LIKE '%{q}%' OR email LIKE '%{q}%'"
              "".format(q=q))
    users = list(c.fetchall())
    c.execute("SELECT DISTINCT * FROM books WHERE book_author LIKE '%{q}%' " \
                                              "OR book_title LIKE '%{q}%' " \
                                              "OR book_genres LIKE '%{q}%'" \
              "".format(q=q))
    books = list(c.fetchall())

    conn.close()
    return render_template('search_results.html', q=q, users=users, books=books)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():

    user_created = False
    error_message = ""

    if request.method == 'POST':
        # add new user data
        user = {}
        user['full_name'] = request.form.get('full_name')
        user['email'] = request.form.get('email')
        user['password'] = request.form.get('password')
        user['f_genres'] = request.form.get('f_genres')
        user['f_authors'] = request.form.get('f_authors')

        # save to database
        conn = sqlite3.connect('app.db')

        c = conn.cursor()

        c.execute("SELECT * FROM users where email='%s'" % user['email'])
        if c.fetchone():
            error_message = "user_exists"
        else:
            c.execute("INSERT INTO users "
                      "(full_name, email, password, f_genres, f_authors) "
                      "VALUES "
                      "('{full_name}', '{email}', '{password}', '{f_genres}','{f_authors}')"
                      "".format(**user))
            conn.commit()
            user_created = True
        conn.close()
        return redirect('/user/%s/' % user['email'])

    return render_template(
        "add_user.html",
        user_created=user_created,
        error_message=error_message

    )


@app.route('/singin')
def singin():
    return render_template('sing_in.html')


@app.route('/sing_in', methods=['GET', 'POST'])
def sing_in():

    if request.method == 'POST':
        # add new user data
        user = {}
        user['email'] = request.form.get('email')
        user['password'] = request.form.get('password')

        # save to database
        conn = sqlite3.connect('app.db')

        c = conn.cursor()

        c.execute("SELECT * FROM users where email='%s'" % user['email'])
        if c.fetchone():
            error_message = "user_exists"

        else:

            conn.close()
        return redirect('/user/%s/' % user['email'])

    return render_template(
        "page1.html"

    )


@app.route('/add_book', methods=['GET', 'POST'])
def add_book():

    book_created = False
    error_message = ""

    if request.method == 'POST':
        # add new user data
        book = {}
        book['book_title'] = request.form.get('book_title')
        book['book_author'] = request.form.get('book_author')
        book['book_genres'] = request.form.get('book_genres')
        book['book_status'] = request.form.get('book_status')
        book['email'] = request.form.get('email')

        # save to database
        conn = sqlite3.connect('app.db')
        c = conn.cursor()

        c.execute("SELECT * FROM users where email='%s'" % book['email'])
        if c.fetchone():
            c.execute("INSERT INTO books "
                      "(email,book_title, book_author, book_genres, book_status) "
                      "VALUES "
                      "('{email}','{book_title}', '{book_author}', '{book_genres}','{book_status}')"
                      "".format(**book))

            conn.commit()
        conn.close()
        return redirect('/book/%s/' % book['email'])

    return render_template(
        "add_book.html",
        book_created=book_created,
        error_message=error_message

    )


@app.route('/book/<email>/')
def book_page(email):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM books WHERE email='%s'" % email)
    book_data = c.fetchone()


    # Close connection
    conn.close()
    return render_template("book_page.html", book=book_data)


@app.route('/bookid/<bookid>/')
def book_page_new(bookid):
    conn = sqlite3.connect('app.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

    # Handler logic here
    c.execute("SELECT * FROM books WHERE bookID='{id}'".format(id=bookid))
    book_data = c.fetchone()


    # Close connection
    conn.close()
    return render_template("book_page_new.html", book=book_data)


if __name__ == '__main__':
    app.run(debug=True)
