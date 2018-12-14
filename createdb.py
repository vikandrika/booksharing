import sqlite3

conn = sqlite3.connect('app.db')

c = conn.cursor()

c.execute('''
CREATE TABLE users (
           userID INTEGER PRIMARY KEY AUTOINCREMENT,
           password TEXT,
           email TEXT,
           full_name TEXT,
           user_info TEXT,
           f_genres TEXT,
           f_authors TEXT,
           wish_books TEXT,
           owned_books TEXT,
           time_from_registration INTEGER,
           number_of_exchanges INTEGER,
           rating REAL
)
''')
conn.commit()



c.execute('''
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

users = [
      {
        'full_name': 'Pavel_Okopnyi',
        'password': 'fdfdfdgdfg',
        'email': 'dfsdgfsfg@gmail.com',
        'f_genres': 'Ужасы',
        'f_authors': 'Ghj',
        'wish_books': 'sdfgdsfgsd',
        'owned_books': 'book184637',
        'time_from_registration': 43456747,
        'number_of_exchanges': 8,
        'rating': 5
    }
]

for user in users:
    c.execute("INSERT INTO users "
              "(full_name, email, f_genres, f_authors, wish_books, owned_books, time_from_registration, number_of_exchanges, rating) "
              "VALUES "
              "('{full_name}', '{email}','{f_genres}','{f_authors}','{wish_books}','{owned_books}','{time_from_registration}','{number_of_exchanges}','{rating}')".format(**user))

    conn.commit()


conn.close()

