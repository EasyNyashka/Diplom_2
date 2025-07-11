import pytest
import allure
import requests

from data import Url


class TestChangingUserData:

    @pytest.mark.parametrize('data_user,new_value', [
        ('email', 'new_email@yandex.com'),
        ('password', 'new_password'),
        ('name', 'new_name')
         ])
    @allure.title('Изменение данных пользователя с авторизацией')
    def test_changing_user_data_auth(self, data_user, auth_token,new_value):
        token = {**Url.headers,'Authorization': auth_token}
        data = {data_user: new_value}
        response = requests.patch(f'{Url.BASE_URL}{Url.CHANGE_USER_DATA}',json=data, headers=token)
        assert response.status_code == 200
        assert response.json()['success'] == True
        assert response.json()['user'][data_user] == new_value

    @pytest.mark.parametrize('data_user,new_value', [
        ('email', 'two_new_email@yandex.com'),
        ('password', 'two_new_password'),
        ('name', 'two_new_name')
        ])
    @allure.title('Изменение данных пользователя без авторизации')
    def test_changing_user_data_not_auth(self, data_user, new_value):
        data = {data_user: new_value}
        response = requests.patch(f'{Url.BASE_URL}{Url.CHANGE_USER_DATA}', json=data , headers=Url.headers)
        assert response.status_code == 401
        assert response.json() == {'success': False, 'message': 'You should be authorised'}




