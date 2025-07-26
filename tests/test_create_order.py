import allure
import requests
from data import Url, Ingredients


class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_create_order_auth_with_ingredients(self, auth_token):
        token = {**Url.headers, 'Authorization': auth_token}
        data = {'ingredients': [Ingredients.valid_ingredient_one, Ingredients.valid_ingredient_two]}

        with allure.step("Отправка POST-запроса для создания заказа с авторизацией и ингредиентами"):
            response = requests.post(f'{Url.BASE_URL}{Url.MAKE_ORDER}',json=data,headers=token)

        with allure.step("Проверка успешного создания заказа"):
            assert response.status_code == 200
            assert response.json()['success'] == True


    @allure.title('Создание заказа с авторизацией без ингредиентов')
    def test_create_order_auth_no_ingredients(self, auth_token):
        token = {**Url.headers,'Authorization': auth_token}
        data = {'ingredients': []}

        with allure.step("Отправка POST-запроса для создания заказа с авторизацией без ингредиентов"):
            response = requests.post(f'{Url.BASE_URL}{Url.MAKE_ORDER}',json=data,headers=token)

        with allure.step("Проверка ошибки при отсутствии ингредиентов"):
            assert response.status_code == 400
            assert response.json() == {'success': False,'message': 'Ingredient ids must be provided'}


    @allure.title('Создание заказа без авторизации с ингредиентами')
    def test_create_order_no_auth_with_ingredients(self):
        data = {'ingredients': [Ingredients.valid_ingredient_one, Ingredients.valid_ingredient_two]}

        with allure.step("Отправка POST-запроса для создания заказа без авторизации с ингредиентами"):
            response = requests.post(f'{Url.BASE_URL}{Url.MAKE_ORDER}', json=data, headers=Url.headers)

        with allure.step("Проверка успешного создания заказа без авторизации"):
            assert response.status_code == 200
            assert response.json()['success'] == True


    @allure.title('Создание заказа без авторизации без ингредиентов')
    def test_create_order_auth_no_ingredients(self, auth_token):
        data = {'ingredients': []}

        with allure.step("Отправка POST-запроса для создания заказа без авторизации и без ингредиентов"):
            response = requests.post(f'{Url.BASE_URL}{Url.MAKE_ORDER}', json=data, headers=Url.headers)

        with allure.step("Проверка ошибки при отсутствии ингредиентов без авторизации"):
            assert response.status_code == 400
            assert response.json() == {'success': False, 'message': 'Ingredient ids must be provided'}


    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_ingredient_hash(self, auth_token):
        token = {**Url.headers, 'Authorization': auth_token}
        data = {'ingredients': [Ingredients.invalid_ingredient]}

        with allure.step("Отправка POST-запроса с неверным хешем ингредиента"):
            response = requests.post(f'{Url.BASE_URL}{Url.MAKE_ORDER}',json=data, headers=token)

        with allure.step("Проверка ошибки сервера при неверном хеше ингредиента"):
            assert response.status_code == 500
            assert 'Internal Server Error' in response.text