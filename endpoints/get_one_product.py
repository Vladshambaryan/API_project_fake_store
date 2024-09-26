import requests
import allure


from endpoints.base_endpoint import Base_Endpoint

url = 'https://fakestoreapi.com'

class Get(Base_Endpoint):

    @allure.step("GET запрос на получение одного товара")
    def get_one_product(self):
        headers = {'Accept': 'application/json'}
        self.response = requests.get(f"{self.url}/products", headers=headers)
        print(self.response.json())
        print(self.response.status_code)

    @allure.step('Проверка структуры данных в теле ответа')
    def check_response_body_product(self, text):
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
