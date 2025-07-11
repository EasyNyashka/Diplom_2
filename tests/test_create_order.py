import allure
import requests
from data import Url, Ingredients


class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_create_order_auth_with_ingredients(self, auth_token):
        token = {**Url.headers, 'Authorization': auth_token}
        data = {'ingredients': [Ingredients.valid_ingredient_one, Ingredients.valid_ingredient_two]}
        response = requests.post(f'{Url.BASE_URL}{Url.MAKE_ORDER}',json=data,headers=token)
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Создание заказа с авторизацией без ингредиентов')
    def test_create_order_auth_no_ingredients(self, auth_token):
        token = {**Url.headers,'Authorization': auth_token}
        data = {'ingredients': []}
        response = requests.post(f'{Url.BASE_URL}{Url.MAKE_ORDER}',json=data,headers=token)
        assert response.status_code == 400
        assert response.json() == {'success': False,'message': 'Ingredient ids must be provided'}

    @allure.title('Создание заказа без авторизации с ингредиентами')
    def test_create_order_no_auth_with_ingredients(self):
        data = {'ingredients': [Ingredients.valid_ingredient_one, Ingredients.valid_ingredient_two]}
        response = requests.post(f'{Url.BASE_URL}{Url.MAKE_ORDER}', json=data, headers=Url.headers)
        assert response.status_code == 200
        assert response.json()['success'] == True

    @allure.title('Создание заказа без авторизации без ингредиентов')
    def test_create_order_auth_no_ingredients(self, auth_token):
        data = {'ingredients': []}
        response = requests.post(f'{Url.BASE_URL}{Url.MAKE_ORDER}', json=data, headers=Url.headers)
        assert response.status_code == 400
        assert response.json() == {'success': False, 'message': 'Ingredient ids must be provided'}

    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_ingredient_hash(self, auth_token):
        token = {**Url.headers, 'Authorization': auth_token}
        data = {'ingredients': [Ingredients.invalid_ingredient]}
        response = requests.post(f'{Url.BASE_URL}{Url.MAKE_ORDER}',json=data, headers=token)
        assert response.status_code == 500
        assert 'Internal Server Error' in response.text