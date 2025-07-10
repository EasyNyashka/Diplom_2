import pytest
import requests
from data import Url
from generators import generate_user


@pytest.fixture(scope='function')
def create_and_delete_user():
    user_data = generate_user()
    response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER}',json=user_data)
    token = response.json().get('accessToken')
    yield {
        'response': response,
        'user_data': user_data,
        'token': token
    }
    requests.delete(f'{Url.BASE_URL}{Url.DELETE_USER}',headers={'Authorization': f'Bearer {token}'})
