class Validation:

    @staticmethod
    def get_response(address):
        """Схема для проверки ответа на GET запрос получения локации"""
        get_response = {"type": "object",
                        "required": ["address"],
                        "properties": {"location": {"type": "object",
                                                    "properties": {
                                                        "latitude": {
                                                            "type": "string"},
                                                        "longitude": {
                                                            "type": "string"}}},
                                       "accuracy": {"type": "string"},
                                       "name": {"type": "string"},
                                       "phone_number": {
                                           "type": "string"},
                                       "address": {"type": "string", "enum": [address]},
                                       "types": {"type": "string"},
                                       "website": {"type": "string"},
                                       "language": {
                                           "type": "string"}}}
        return get_response

    @staticmethod
    def post_response():
        """Схема для проверки ответа на POST запрос создания локации"""
        post_response = {"type": "object",
                         "required": ["status", "place_id"],
                         "properties": {"status": {"type": "string", "enum": ["OK"]},
                                        "place_id": {"type": "string"},
                                        "scope": {"type": "string", "enum": ["APP"]},
                                        "reference": {"type": "string"},
                                        "id": {"type": "string"}}}
        return post_response

    @staticmethod
    def standard_response(field_name, expected_message):
        """Схема для проверки однострочных ответов"""
        standard_response = {"type": "object",
                             "required": [field_name],
                             "properties": {field_name: {"type": "string", "enum": [expected_message]}}}
        return standard_response
