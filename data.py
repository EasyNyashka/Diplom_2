class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = '/api/auth/register'
    DELETE_USER = '/api/auth/user'
    LOGIN = '/api/auth/login'
    CHANGE_USER_DATA = '/api/auth/user'
    MAKE_ORDER = '/api/orders'
    GET_ORDERS = '/api/orders'
    headers = {'Content-Type': 'application/json'}

class User:

    data_invalid = {
        "email": 'Elena23@yandex.ru',
        "password": "777777"}

class Ingredients:

    valid_ingredient_one = '61c0c5a71d1f82001bdaaa6d'
    valid_ingredient_two = '61c0c5a71d1f82001bdaaa6f'
    invalid_ingredient = 'invalid_hash_666'