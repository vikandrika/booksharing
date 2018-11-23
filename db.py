_users = {
    'paul': {
        'name': 'Pavel Okopnyi',
        'fav_categories': 'Ужасы',
        'own_books': 'book184637'
    },

    'igor': {
        'name': 'Igor Novikov',
        'fav_categories': 'Научная фантастика',
        'own_books': 'book407836'
    },

    'boris': {
        'name': 'Boris Ivanov',
        'fav_categories': 'Триллер',
        'own_books': 'book846339'
    },

    'alena': {
        'name': 'Alena Popova',
        'fav_categories': 'Научная литература',
        'own_books': 'book899111',
    },

    'tom': {
        'name': 'Tom Riddle',
        'fav_categories': 'Драма',
        'own_books': 'book189007'
    },

    ' alex': {
        'name': 'Alex Smith',
        'fav_categories': 'Биография',
        'own_books': 'book503255'
    },

    'ivan': {
        'name': 'Ivan Borisov',
        'fav_categories': 'Детектив',
        'own_books': 'book846009'
    },

    'anna': {
        'name': 'Anna Karenina',
        'fav_categories': 'Драма',
        'own_books': 'book9346613'
    },

    'jack': {
        'name': 'Jack Potter',
        'fav_categories': ['Фантастика', 'Поэзия'],
        'own_books': 'book870839'
    },

    'alexander': {
        'name': 'Alexander Petrov',
        'fav_categories': 'Любовный роман',
        'own_books': 'book992303',
    }
}


_user_list = []

for login, user_data in _users.items():
    _new_element = {'login': login}
    _new_element.update(user_data)
    _user_list.append(_new_element)



# Get users filtered by name
def get_users_by_name(q):
    results = []
    # SEARCH
    for user in _user_list:
        if q.lower() in user['name'].lower():
            results.append(user)
    return results


def get_user(username):
    return _users.get(username)




