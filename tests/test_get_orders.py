import allure
import requests
from data import Url, Ingredients


class TestGetUserOrders:

    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_orders_with_auth_user(self, auth_token):
        token = {**Url.headers, 'Authorization': auth_token}
        data = {'ingredients': [Ingredients.valid_ingredient_one, Ingredients.valid_ingredient_two]}

        with allure.step("Создание заказа"):
            requests.post(f'{Url.BASE_URL}{Url.MAKE_ORDER}', json=data, headers=token)

        with allure.step("Получение заказов пользователя"):
            response = requests.get(f'{Url.BASE_URL}{Url.GET_ORDERS}', headers=token)

        with allure.step("Проверка ответа"):
            assert response.status_code == 200
            assert response.json()['success'] == True


    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_orders_no_auth_user(self, auth_token):
        token = {**Url.headers, 'Authorization': auth_token}
        data = {'ingredients': [Ingredients.valid_ingredient_one, Ingredients.valid_ingredient_two]}

        with allure.step("Создание заказа"):
            requests.post(f'{Url.BASE_URL}{Url.MAKE_ORDER}', json=data, headers=token)

        with allure.step("Попытка получить заказы без авторизации"):
            response = requests.get(f'{Url.BASE_URL}{Url.GET_ORDERS}',headers=Url.headers)

        with allure.step("Проверка ответа"):
            assert response.status_code == 401
            assert response.json() == {'success': False,'message': 'You should be authorised'}