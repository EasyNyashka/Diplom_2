import pytest
import allure
import requests

from data import Url, User


class TestLoginUser:

    @allure.title('Авторизация пользователя, который уже зарегистрирован')
    def test_login_user(self, create_and_delete_user):
        data = create_and_delete_user['user_data']
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN}', json=data)
        assert response.status_code == 200 and response.json().get('success') == True

    @allure.title('Авторизация пользователя с неверным логином и паролем')
    def test_login_invalid_login_or_password(self):
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN}', json=User.data_invalid)
        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': 'email or password are incorrect'}

