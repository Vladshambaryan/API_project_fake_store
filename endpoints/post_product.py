import requests
import allure

from endpoints.base_endpoint import Base_Endpoint

url = 'https://fakestoreapi.com'

class Post(Base_Endpoint):

    @allure.step('Отправка  POST-запроса на добавление продукта')
    def add_a_post_product(self, title, price, description, image, category, expected_title):
        headers = {'Content-Type': 'application/json'}
        self.response = requests.post(f"{self.url}/products",
                                      json={'title': title, 'price': price, 'description': description,
                                            'image': image, 'category': category,
                                            'expected_title': expected_title}, headers=headers)
        print(self.response.status_code)

    @allure.step('Проверка типа содержимого')
    def check_post_content_type(self, text):
        assert self.response.headers['Content-Type'] == text

    @allure.step('Проверка структуры данных в теле ответа')
    def check_post_response_body(self, text):
        data = self.response.json()
        assert 'id' in data
        assert 'title' in data
        assert 'price' in data
        assert 'description' in data
        assert 'category' in data
        assert 'image' in data
        assert all(key in self.response.json() for key in text)
