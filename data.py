class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER = '/api/auth/register'
    LOGIN = '/api/auth/login'
    CHANGE_USER_DATA = '/api/auth/user'
    DELETE_USER = '/api/auth/user'
    MAKE_ORDER = '/api/orders'
    GET_ORDERS = '/api/orders'
    headers = {'Content-Type': 'application/json'}

class User:

    data_invalid = {
        "email": 'Elena23@yandex.ru',
        "password": "777777"}