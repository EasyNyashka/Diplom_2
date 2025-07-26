import pytest
import allure
import requests

from data import Url
from generators import generate_user, generate_user_no_email, generate_user_no_password, generate_user_no_name


class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_user(self):
        data = generate_user()

        with allure.step("Отправка POST-запроса для создания нового пользователя"):
            response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER}',json=data,headers=Url.headers)
            response_body = response.json()

        with allure.step("Проверка успешного создания пользователя"):
            assert response.status_code == 200
            assert 'success' in response_body
            assert response_body['success'] is True


    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_duplicate_user(self):
        data = generate_user()

        with allure.step("Первая регистрация пользователя"):
            first_response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER}',json=data, headers=Url.headers)
            assert first_response.status_code == 200
            assert first_response.json().get('success') is True

        with allure.step("Попытка повторной регистрации того же пользователя"):
            duplicate_response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER}',json=data,headers=Url.headers)

        with allure.step("Проверка ошибки дублирования пользователя"):
            assert duplicate_response.status_code == 403
            assert duplicate_response.json() == {"success": False, "message": "User already exists"}


    @pytest.mark.parametrize('user_incomplete_data', [generate_user_no_email, generate_user_no_password, generate_user_no_name])
    @allure.title('Создание пользователя при не заполненном одним из обязательных полей')
    def test_create_user_data_invalid(self, user_incomplete_data):
        incomplete_data = user_incomplete_data()

        with allure.step("Отправка запроса с неполными данными пользователя"):
            response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER}', json=incomplete_data)

        with allure.step("Проверка ошибки валидации обязательных полей"):
            assert response.status_code == 403
            assert response.json() == {"success": False,"message": "Email, password and name are required fields"}