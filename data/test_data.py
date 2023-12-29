import datetime
from datetime import date as d


class TestCourier:
    login_only_password = {"password": "qweqwe"}
    login_empty_password = {"login": "tester", "password": ""}
    login_empty_login = {"login": "", "password": "qweqwe!"}

    create_no_login_courier = {"password": "qweqwe", "firstName": 'evgen'}
    create_no_password_courier = {"login": "tester", "firstName": "evgen"}
    create_empty_login = {"login": "", "password": "qweqwe", "firstName": "evgen"}
    create_empty_password = {"login": "tester", "password": "", "firstName": "evgen"}


class TestOrder:
    delivery_date = (d.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    test_order = {"order":
{
    "firstName": "Harry",
    "lastName": "Potter",
    "address": "Privet drive, 4 ",
    "metroStation": 4,
    "phone": "+7 999 888 77 66",
    "rentTime": 5,
    "deliveryDate": "2022-02-22",
    "comment": "test comment",
    "color": ["BLACK"]
 }
    }


class OrdersErrors:
    track_order_no_data = "Недостаточно данных для поиска"
    track_order_no_such_order = "Заказ не найден"

    accept_order_no_order_number = "Недостаточно данных для поиска"
    accept_order_no_such_courier = "Курьера с таким id не существует"
    accept_order_no_data = "Недостаточно данных для поиска"


class CourierErrors:
    create_no_data = "Недостаточно данных для создания учетной записи"
    create_already_exist = "Этот логин уже используется. Попробуйте другой."

    login_no_data = "Недостаточно данных для входа"
    login_no_such_user = "Учетная запись не найдена"
