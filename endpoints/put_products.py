import requests
import allure

from endpoints.base_endpoint import Base_Endpoint

url = 'https://fakestoreapi.com'

class Put(Base_Endpoint):

    @allure.step('Отправка  PUT-запроса на добавление продукта')
    def put_a_post_success(self, new_post_id, title, price, description, image, category, expected_title):
        headers = {'Content-Type': 'application/json'}
        self.response = requests.put(f"{self.url}/products/{new_post_id['id']}",
                                     json={'title': title, 'price': price, 'description': description,
                                           'image': image, 'category': category,
                                           'expected_title': expected_title}, headers=headers)

    @allure.step('Проверка структуры данных в теле ответа')
    def check_put_response_body_product(self, text):
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
