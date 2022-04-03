import requests
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends1.herokuapp.com/'

    def get_api_key(self, email, password):

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


def create_pet_simple(self, auth_key: json, name: str, animal_type: str, age: int) -> json:
    data = MultipartEncoder(
        fields={
            'name': name,
            'animal_type': animal_type,
            'age': age
        })
    headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
    res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(result)
    return status, result


def set_photo(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
    data = MultipartEncoder(
        fields={
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        })
    headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
    res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
    status = res.status_code

    return status


def add_new_pet_2(self, auth_key: json, name: str, anemal_type: str, age: str, country: str, pet_photo: str) -> json:
    data = MultipartEncoder(
        fields={
            'name': name,
            'anemal_type': anemal_type,
            'age': age,
            'country': country,
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        })
    headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
    res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(result)
    return status, result


def add_new_pet_with_str_age(self, auth_key: json, name: str, animal_type: str, age: int, pet_photo: str) -> json:
    data = MultipartEncoder(
        fields={
            'name': name,
            'animal_type': animal_type,
            'age': age,
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        })
    headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
    res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    print(result)
    return status, result


def update_pet_name(self, auth_key: json, pet_id: str, name: str) -> json:
    headers = {'auth_key': auth_key['key']}
    data = {
        'name': name
    }

    res = requests.put(self.base_url + 'api/pets/' + pet_id, headers=headers, data=data)
    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return status, result


def add_new_pet_empty(self, auth_key: json) -> json:
    headers = {'auth_key': auth_key['key']}
    res = requests.post(self.base_url + 'api/pets', headers=headers)
    status = res.status_code

    return status


def delete_pet(self, auth_key: json, pet_id: str) -> json:
    headers = {'auth_key': auth_key['key']}

    res = requests.delete(self.base_url + 'api/pets/' + pet_id, headers=headers)
    status = res.status_code
    result = ""
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return status, result


def set_photo_tif(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
    data = MultipartEncoder(
        fields={
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/tiff')
        })
    headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
    res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
    status = res.status_code

    return status