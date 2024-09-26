import pytest
import requests
import allure

from endpoints.base_endpoint import Base_Endpoint

url = 'https://fakestoreapi.com'

class Patch(Base_Endpoint):

    @allure.step('Отправка  PATCH-запроса на добавление продукта')
    def patch_a_post_success(self, new_post_id):
        headers = {'Content-Type': 'application/json'}
        self.response = requests.patch(f"{self.url}/products/{new_post_id['id']}",
                                       json={'title': 'Partially Updated Post'},
                                       headers=headers)

    def check_patch_response(self, text):
        assert self.response.json()['title'] == text

