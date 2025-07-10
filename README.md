# Дипломный проект. Задание 2: API-тесты
## Елена Ермоленкова 
## Когорта: 20
## <h1 align="left" style="color:green">Тестирование ручки API для Stellar Burgers</h1>

## <h>Инструкция по запуску:</h>

### <h>1. Установите зависимости:</h>

> pip install -r requirements.txt</h>

### <h>2. Запустить все тесты:</h>

> pytest tests --alluredir=allure_results

### <h>3. Посмотреть отчет по прогону html</h>

> allure serve allure_results


<hr>

<h3 align="left" style="color:green">Project files and description:</h3>

| Название файла         | Содержание файла               |
|------------------------|--------------------------------|
| tests dir              | Директория с тестами           |
| test_create_user.py    | Тесты на создание пользователя |
| ?test_delete_booking.py | Тесты на удаление бронирования |
| conftest.py            | Фикстуры                       |
| ?helpers.py            | Хэлпер для тела запросов       |
| ?data.py               | Файл с URL и body запросов     |
| ? auth_methods.py      | http клиент к auth методам     |
| ?booking_methods.py    | http клиент к booking методам  |
| ?generators.py         | Генератор данных               |
| requirements.txt       | Файл с зависимостями           |
| allure_results.dir     | Папка с отчетами Allure        |


