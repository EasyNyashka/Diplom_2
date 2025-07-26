import pytest
import allure
import requests

from data import Url


class TestChangingUserData:

    @pytest.mark.parametrize('field,new_value', [
        ('email', 'new_email@yandex.com'),
        ('password', 'new_password'),
        ('name', 'new_name')
         ])
    @allure.title('Изменение данных пользователя с авторизацией')
    def test_changing_user_data_auth(self, field, auth_token,new_value):
        token = {**Url.headers,'Authorization': auth_token}
        data = {field: new_value}

        with allure.step(f"Отправка PATCH-запроса для изменения поля {field} с авторизацией"):
            response = requests.patch(f'{Url.BASE_URL}{Url.CHANGE_USER_DATA}',json=data, headers=token)

        with allure.step("Проверка кода ответа и данных"):
            assert response.status_code == 200
            assert response.json()['success'] == True
            assert response.json()['user'][field] == new_value

    @pytest.mark.parametrize('field,new_value', [
        ('email', 'two_new_email@yandex.com'),
        ('password', 'two_new_password'),
        ('name', 'two_new_name')
        ])
    @allure.title('Изменение данных пользователя без авторизации')
    def test_changing_user_data_not_auth(self, field, new_value):
        data = {field: new_value}

        with allure.step(f"Отправка PATCH-запроса для изменения поля {field} без авторизации"):
            response = requests.patch(f'{Url.BASE_URL}{Url.CHANGE_USER_DATA}', json=data , headers=Url.headers)

        with allure.step("Проверка кода ответа и сообщения об ошибке"):
            assert response.status_code == 401
            assert response.json() == {'success': False, 'message': 'You should be authorised'}




