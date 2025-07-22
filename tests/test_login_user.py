import pytest
import allure
import requests

from data import Url, User


class TestLoginUser:

    @allure.title('Авторизация пользователя, который уже зарегистрирован')
    def test_login_user(self, create_and_delete_user):
        data = create_and_delete_user['user_data']

        with allure.step("Отправка запроса на авторизацию с валидными данными"):
            response = requests.post(f'{Url.BASE_URL}{Url.LOGIN}', json=data)

        with allure.step("Проверка успешной авторизации"):
            assert response.status_code == 200
            assert response.json()['success'] == True


    allure.title('Авторизация пользователя с неверных данных авторизации')
    @pytest.mark.parametrize("test_case", [
        {"use_invalid_email": True, "use_invalid_password": False},
        {"use_invalid_email": False, "use_invalid_password": True}
    ])
    def test_login_invalid_combinations(self, create_and_delete_user, test_case):
        valid_data = create_and_delete_user['user_data']
        invalid_data = User.data_invalid

        with allure.step("Подготовка тестовых данных"):
            test_data = {
                "email": invalid_data["email"] if test_case["use_invalid_email"] else valid_data["email"],
                "password": invalid_data["password"] if test_case["use_invalid_password"] else valid_data["password"]
            }

        with allure.step("Отправка запроса на авторизацию с неверными данными"):
            response = requests.post(f'{Url.BASE_URL}{Url.LOGIN}', json=test_data)

        with allure.step("Проверка ошибки авторизации"):
            assert response.status_code == 401
            assert response.json() == {
            'success': False,
            'message': 'email or password are incorrect'
            }
