import requests
import allure
from endpoints.base_endpoint import Base_Endpoint

url = 'https://fakestoreapi.com'

class Delete(Base_Endpoint):

    @allure.feature('Delete')
    @allure.step('Отправка  DELETE-запроса на удаление')
    def delete_post(self, new_post_id):
        headers = {'Accept': 'application/json'}
        self.response = requests.delete(f"{self.url}/products/{new_post_id['id']}", headers=headers)
        print(self.response.status_code)

    @allure.step('Проверьте код состояния')
    def check_status_code_negative_test(self, new_post_id, status_code):
        self.response = requests.get(f"{url}/products/{new_post_id}")
        assert self.response.status_code == status_code
        print(self.response.status_code)
