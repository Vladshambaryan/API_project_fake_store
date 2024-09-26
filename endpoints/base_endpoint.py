import allure

class Base_Endpoint:

    url = 'https://fakestoreapi.com'
    response = None
    json = None
    errors = []

    @allure.step('Проверьте код состояния')
    def check_status_code_is_correct(self, status_code):
        assert self.response.status_code == status_code

    @allure.step('Проверьте код состояния')
    def check_status_code(self, status_code):
        assert self.response.status_code == status_code
