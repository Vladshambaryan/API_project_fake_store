import requests
import allure

from endpoints.base_endpoint import Base_Endpoint

url = 'https://fakestoreapi.com'

class GetAll(Base_Endpoint):

    @allure.step("GET запрос на получение всех товаров")
    def get_all_products(self):
        headers = {'Accept': 'application/json'}
        self.response = requests.get(f"{self.url}/products", headers=headers)
        print(self.response.status_code)

    @allure.step('Проверка структуры данных в теле ответа')
    def check_response_body_all_product(self, text):
        data = self.response.json()
        data = data[0] if isinstance(data, list) else data
        assert isinstance(data, dict)
        assert 'id' in data
        assert 'title' in data
        assert 'price' in data
        assert 'description' in data
        assert 'category' in data
        assert 'image' in data
        assert all(key in data for key in text)
