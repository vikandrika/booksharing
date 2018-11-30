import sqlite3

conn = sqlite3.connect('app.db')

c = conn.cursor()

c.execute ('''
CREATE TABLE users (
           userID INTEGER PRIMARY KEY AUTOINCREMENT,
           password TEXT,
           email TEXT,
           user_info TEXT,
           f_genres TEXT,
           f_authors TEXT,
           wish_books TEXT,
           owned_books TEXT,
           time_from_reg INTEGER,
           number_of_exchanges INTEGER,
           rating REAL
)
''')
conn.commit()

c.execute('''
    ALTER TABLE users
    ADD COLUMN login TEXT
''')
conn.commit()

c.execute ('''
CREATE TABLE books (
           bookID INTEGER PRIMARY KEY AUTOINCREMENT,
           book_status TEXT,
           book_author TEXT,
           book_title TEXT, 
           book_genres TEXT,
           creatorID INTEGER,
           FOREIGN KEY (creatorID) REFERENCES users(userID) 
)
''')
conn.commit()

c.execute ('''
CREATE TABLE exchange (
          exchangeID INTEGER PRIMARY KEY AUTOINCREMENT,
          user1 INTEGER,
          user2 INTEGER,
          bookU1 INTEGER,
          bookU2 INTEGER,
          date INTEGER,
          time INTEGER,
          exchange_type TEXT,
          exchange_period INTEGER, 
          exchange_conformation NULL,
          FOREIGN KEY (user1) REFERENCES users(userID),
          FOREIGN KEY (bookU1) REFERENCES books(bookID),
          FOREIGN KEY (user2) REFERENCES users(userID),
          FOREIGN KEY (bookU2) REFERENCES books(bookID)    
)
''')
conn.commit()

c.execute ('''
CREATE TABLE genres (
          genreID INTEGER PRIMARY KEY AUTOINCREMENT,
          genre_name TEXT    
)
''')
conn.commit()

c.execute ('''
CREATE TABLE users_genres (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          user_ID INTEGER,
          genre_ID INTEGER,
          FOREIGN KEY (user_ID) REFERENCES users(userID),
          FOREIGN KEY (genre_ID) REFERENCES genres(genreID)     
)
''')

conn.commit()

users = {
    'paul': {
        'name': 'Pavel Okopnyi',
        'f_genres': 'Ужасы',
        'owned_books': 'book184637'
    },

    'igor': {
        'name': 'Igor Novikov',
        'f_genres': 'Научная фантастика',
        'owned_books': 'book407836'
    },

    'boris': {
        'name': 'Boris Ivanov',
        'f_genres': 'Триллер',
        'owned_books': 'book846339'
    },

    'alena': {
        'name': 'Alena Popova',
        'f_genres': 'Научная литература',
        'owned_books': 'book899111',
    },

    'tom': {
        'name': 'Tom Riddle',
        'f_genres': 'Драма',
        'owned_books': 'book189007'
    },

    ' alex': {
        'name': 'Alex Smith',
        'f_genres': 'Биография',
        'owned_books': 'book503255'
    },

    'ivan': {
        'name': 'Ivan Borisov',
        'f_genres': 'Детектив',
        'owned_books': 'book846009'
    },

    'anna': {
        'name': 'Anna Karenina',
        'f_genres': 'Драма',
        'owned_books': 'book9346613'
    },

    'jack': {
        'name': 'Jack Potter',
        'f_genres': ['Фантастика', 'Поэзия'],
        'owned_books': 'book870839'
    },

    'alexander': {
        'name': 'Alexander Petrov',
        'f_genres': 'Любовный роман',
        'owned_books': 'book992303',
    }
}

for user in users:
    c.execute("INSERT INTO users "
              "(name, f_genres, owned_books) "
              "VALUES "
              "('{login}','{f_genres}' ,'{owned_books}', 0)".format(**user))

    conn.commit()


conn.close()