import pytest
import allure
import requests

from data import Url
from generators import generate_user_no_email, generate_user_no_password, generate_user_no_name


class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_user(self, create_and_delete_user):
        data = create_and_delete_user
        response = data['response']
        response_body = response.json()
        assert response.status_code == 200
        assert 'success' in response_body
        assert response_body['success'] is True

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_duplicate_user(self, create_and_delete_user):
        data = create_and_delete_user
        user_data = data['user_data']
        duplicate_response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER}',json=user_data)
        assert duplicate_response.status_code == 403
        assert duplicate_response.json() == {"success": False, "message": "User already exists"}

    @pytest.mark.parametrize('user_incomplete_data', [generate_user_no_email, generate_user_no_password, generate_user_no_name])
    @allure.title('Создание пользователя при не заполненном одним из обязательных полей')
    def test_create_user_data_invalid(self, user_incomplete_data):
        incomplete_data = user_incomplete_data()
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER}', json=incomplete_data)
        assert response.status_code == 403
        assert response.json() == {"success": False,"message": "Email, password and name are required fields"}