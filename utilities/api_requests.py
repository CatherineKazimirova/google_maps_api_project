import utilities.urls
from utilities.http_methods import HttpMethods
from faker import Faker

faker = Faker()


class GoogleMapsApi:

    @staticmethod
    def create_location(address):
        """Создает локацию и возвращает ответ на запрос POST /maps/api/place/add/json. Требует передачи
        какого-либо адреса"""
        post_body = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": address,
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_url = utilities.urls.base_url + utilities.urls.post_url
        response_create = HttpMethods.post(post_url, post_body)
        print(f'Full response: {response_create.json()}')
        return response_create

    @staticmethod
    def get_location(place_id):
        """Получение локации с place_id из ответа на запрос создания локации,
        возвращается ответ на запрос GET /maps/api/place/get/json"""
        get_url = utilities.urls.base_url + utilities.urls.get_url + place_id
        response_get = HttpMethods.get(get_url)
        print(f'GET request URL: {get_url}')
        print(f'Location current details: {response_get.json()}')
        return response_get

    @staticmethod
    def update_location(place_id, address):
        """Обновление локации, возвращается ответ на запрос PUT /maps/api/place/update/json. Требуется передача
        place_id и address, которые надо забрать из ответа на запрос создания локации"""
        put_url = utilities.urls.base_url + utilities.urls.put_url
        put_body = {
            "place_id": place_id,
            "address": address,
            "key": "qaclick123"
        }
        response_put = HttpMethods.put(put_url, put_body)
        print(f'Update body: {put_body}')
        print(f'Location update response: {response_put.json()}')
        return response_put

    @staticmethod
    def delete_location(place_id):
        """Удаление локации с place_id из ответа на запрос создания локации,
        возвращается ответ на запрос DELETE /maps/api/place/delete/json"""
        delete_url = utilities.urls.base_url + utilities.urls.delete_url
        delete_body = {
            "place_id": place_id
        }
        response_delete = HttpMethods.delete(delete_url, delete_body)
        print(f'Delete body: {delete_body}')
        print(f'Location delete response: {response_delete.json()}')
        return response_delete
