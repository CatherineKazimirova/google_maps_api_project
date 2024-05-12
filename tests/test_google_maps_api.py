from utilities.api_requests import GoogleMapsApi
from utilities.base_methods import BaseMethods
from utilities.validation_schemes import Validation
from faker import Faker

faker = Faker()


class TestLocation:

    def test_create_and_check_location(self):
        """Создание локации и проверка ответа"""
        print('CREATING LOCATION')
        """Генерация адреса через Faker"""
        address = faker.address()
        """Создание переменной со схемой валидации"""
        post_response_schema = Validation.post_response()
        """Запрос на создание локации, в address передается сгенерированный Faker адрес"""
        response_post = GoogleMapsApi.create_location(address)
        """Сохранение ответа на запрос в переменную"""
        response_post_json = response_post.json()
        """Сохранение place_id в переменную"""
        place_id = response_post_json.get('place_id')
        """Проверка статус-кода и проверка ответа валидатором"""
        BaseMethods.check_status_code('POST', 200, response_post)
        BaseMethods.check_response('POST', response_post_json, post_response_schema)
        print('LOCATION CREATED', '\n')

        print('GETTING CREATED LOCATION')
        """Получение локации и проверка ответа"""
        """Создание переменной со схемой валидации"""
        get_response_schema = Validation.get_response(address)
        """Запрос на получение локации, в place_id передается сохраненный из ответа на запрос POST id"""
        response_get = GoogleMapsApi.get_location(place_id)
        """Проверка статус-кода и проверка ответа валидатором"""
        BaseMethods.check_status_code('GET', 200, response_get)
        BaseMethods.check_response('GET', response_get.json(), get_response_schema)
        print('CREATED LOCATION RECEIVED', '\n')

        print('UPDATING CREATED LOCATION')
        """Обновление локации и проверка ответа"""
        """Генерация нового адреса через Faker"""
        new_address = faker.address()
        """Создание переменных с ожидаемыми названием поля и значением в этом поле"""
        put_response_field_name, put_response_message = "msg", "Address successfully updated"
        """Создание переменной со схемой валидации, в переменную передаются ожидаемое название поля
        и значение в этом поле"""
        put_response_schema = Validation.standard_response(put_response_field_name, put_response_message)
        """Запрос на обновление локации, в place_id передается сохраненный из ответа на запрос POST id,
        в new_address - новый сгенерированный Faker адрес"""
        response_put = GoogleMapsApi.update_location(place_id, new_address)
        """Проверка статус-кода и проверка ответа валидатором"""
        BaseMethods.check_status_code('PUT', 200, response_put)
        BaseMethods.check_response('PUT', response_put.json(), put_response_schema)
        print('LOCATION UPDATED', '\n')

        print('GETTING UPDATED LOCATION')
        """Получение обновленной локации и проверка ответа"""
        """Создание переменной со схемой валидации, в схему передается новый адрес"""
        get_response_schema = Validation.get_response(new_address)
        """Запрос на получение локации, в place_id передается сохраненный из ответа на запрос POST id"""
        response_get = GoogleMapsApi.get_location(place_id)
        """Проверка статус-кода и проверка ответа валидатором"""
        BaseMethods.check_status_code('GET', 200, response_get)
        BaseMethods.check_response('GET', response_get.json(), get_response_schema)
        print('UPDATED LOCATION RECEIVED', '\n')

        print('DELETING LOCATION')
        """Получение созданной и обновленной локации и проверка ответа"""
        """Создание переменных с ожидаемыми названием поля и значением в этом поле"""
        delete_response_field_name, delete_response_message = "status", "OK"
        """Создание переменной со схемой валидации, в переменную передаются ожидаемое название поля
        и значение в этом поле"""
        delete_response_schema = Validation.standard_response(delete_response_field_name, delete_response_message)
        """Запрос на удаление локации, в place_id передается сохраненный из ответа на запрос POST id"""
        response_delete = GoogleMapsApi.delete_location(place_id)
        """Проверка статус-кода и проверка ответа валидатором"""
        BaseMethods.check_status_code('DELETE', 200, response_delete)
        BaseMethods.check_response('DELETE', response_delete.json(), delete_response_schema)
        print('LOCATION DELETED', '\n')

        print('GETTING DELETED LOCATION')
        """Попытка получения удаленной локации и проверка ответа"""
        """Создание переменных с ожидаемыми названием поля и значением в этом поле"""
        get_response_field_name, get_response_message = "msg", ("Get operation failed, looks like place_id  doesn't "
                                                                "exists")
        """Создание переменной со схемой валидации, в переменную передаются ожидаемое название поля
        и значение в этом поле"""
        get_response_schema = Validation.standard_response(get_response_field_name, get_response_message)
        response_get = GoogleMapsApi.get_location(place_id)
        """Проверка статус-кода и проверка ответа валидатором"""
        BaseMethods.check_status_code('GET', 404, response_get)
        BaseMethods.check_response('GET', response_get.json(), get_response_schema)
        print('RESPONSE RECEIVED', '\n')
