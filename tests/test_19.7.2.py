import os

import pytest
from api import PetFriends
from settings import v_email,v_password, n_email,n_password
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json
pf=PetFriends()

def test_get_api_key_for_not_valid_user(email=n_email,password=n_password):
    status,result=pf.get_api_key(email,password)
    assert status==403
    print("Пользователя с таким email/password не существует")

def test_create_pet_simple_not_valid_user(name='Жак',animal_type='Жако',age='2'):
    """Проверяем что нельзя создать питьмца, с несуществующим профилем"""
    _, auth_key = pf.get_api_key(n_email, n_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_create_pet_simple(name='Жак',animal_type='Жако',age='2'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    status, result = pf.create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_set_photo(pet_photo='img/попугай.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(v_email, v_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status= pf.set_photo(auth_key, pet_id,pet_photo)
    assert status == 200

def test_post_add_new_pet_with_valid_data_2(name='Жорr',anemal_type='Жако',age='2',country='Африка',pet_photo='img/попугай.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(v_email, v_password)
    status, result = pf.add_new_pet_2(auth_key, name, anemal_type, age,country, pet_photo)
    assert status == 400
    print('Синтаксическая ошибка в запросе')

def test_post_add_new_pet_with_str_age(name='Жорж',animal_type='Жако',age='три',pet_photo='img/попугай.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(v_email, v_password)
    status, result = pf.add_new_pet_with_str_age(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    print("Создается питомец с возрастом написанным буквами,на сайте строка возраст воспринимает к воду только цыфрами")

def test_update_pets_name(name='Жан'):
    _, auth_key = pf.get_api_key(v_email, v_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    animal_type=my_pets['pets'][0]['animal_type']
    age=my_pets['pets'][0]['age']

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:

        raise Exception("There is no my pets")

def test_post_add_new_pet_without_data():
        _, auth_key = pf.get_api_key(v_email, v_password)
        status= pf.add_new_pet_empty(auth_key)
        assert status == 400
        print("Нельзя создать питомца с пустыми параметрами")

def test_delete_pet_with_index_one():
    _, auth_key = pf.get_api_key(v_email, v_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) == 0 or len(my_pets['pets']) == 1:
        pf.add_new_pet(auth_key, "Жорж1", "Жако", "2", "img/попугай.jpg")
        pf.add_new_pet(auth_key, "Жорж2", "Жако", "2", "img/попугай.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")


    pet_id = my_pets['pets'][-1]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in my_pets.values()

def test_set_photo_tif(pet_photo='img/попугай.tif'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(v_email, v_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    pet_id = my_pets['pets'][0]['id']
    status= pf.set_photo_tif(auth_key, pet_id,pet_photo)
    assert status == 500
    print('Нельзя добавить фото в формате TIFF')


