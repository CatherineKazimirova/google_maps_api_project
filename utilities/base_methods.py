from jsonschema import validate
from jsonschema.exceptions import ValidationError


class BaseMethods:

    @staticmethod
    def check_status_code(method_name, expected_status, response):
        """Сравнение ожидаемого статус-кода с фактическим. Если неуспешно - отображается ошибка"""
        try:
            assert expected_status == response.status_code
            print(f'Status code of {method_name} request is the same as expected - {response}')
        except AssertionError:
            print(f'Error! Current status code of {method_name} request: {response}')

    @staticmethod
    def check_response(method_name, response, schema):
        """Вызов валидатора и проверка ответа в соответствии со схемой (см validation_schemes.py). Если
        валидация неуспешна - отображается ошибка"""
        try:
            validate(response, schema)
            print(f'Response of {method_name} method is equal to expected')
        except ValidationError as error:
            print(f'Error! Response of {method_name} method is not equal to expected')
            print(error)
