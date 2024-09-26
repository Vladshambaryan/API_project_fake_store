import allure
import pytest

from conftest import (new_post_id, post_endpoint, put_endpoint, patch_endpoint, get_one_endpoint,
                      get_all_endpoints, delete_endpoint)

@allure.feature('get')
@pytest.mark.regression
def test_get_one_product_post(new_post_id, get_one_endpoint):
    get_one_endpoint.get_one_product()
    get_one_endpoint.check_response_body_product(['id', 'title', 'price', 'description', 'category', 'image'])
    get_one_endpoint.check_status_code(200)
    get_one_endpoint.check_status_code_is_correct(200)


@allure.feature('get')
@pytest.mark.regression
def test_get_all_product(get_all_endpoints):
    get_all_endpoints.get_all_products()
    get_all_endpoints.check_response_body_all_product(['id', 'title', 'price', 'description', 'category', 'image'])
    get_all_endpoints.check_status_code(200)
    get_all_endpoints.check_status_code_is_correct(200)


@allure.feature('Post')
@pytest.mark.regression
@pytest.mark.parametrize("title, price, description, image, category, expected_title", [
    ("Another New Post", 9.99, "This is another new post", "https://example.com/image.jpg", "electronics",
     "Another New Post")])
def test_post_add_product(post_endpoint, title, price, description, image, category, expected_title):
    post_endpoint.add_a_post_product(title, price, description, image, category, expected_title)
    post_endpoint.check_post_content_type('application/json; charset=utf-8')
    post_endpoint.check_post_response_body(['id', 'title', 'price', 'description', 'category', 'image'])
    post_endpoint.check_status_code(200)
    post_endpoint.check_status_code_is_correct(200)


@allure.feature('Put')
@pytest.mark.parametrize("title, price, description, image, category, expected_title", [
    (" New Post", 777, "This is post", "https://example.com/image.jpg", "electronic",
     "Another Post")])
def test_put_a_post_success(new_post_id, put_endpoint, title, price, description, image, category, expected_title):
    put_endpoint.put_a_post_success(new_post_id, title, price, description, image, category, expected_title)
    put_endpoint.check_put_response_body_product(['id', 'title', 'price', 'description', 'category', 'image'])
    put_endpoint.check_status_code(200)
    put_endpoint.check_status_code_is_correct(200)


@allure.feature('Patch')
@pytest.mark.regression
def test_patch_a_post_success(new_post_id, patch_endpoint):
    patch_endpoint.patch_a_post_success(new_post_id)
    patch_endpoint.check_patch_response('Partially Updated Post')
    patch_endpoint.check_status_code(200)
    patch_endpoint.check_status_code_is_correct(200)


@allure.feature('Delete')
def test_delete_post(delete_endpoint, new_post_id):
    delete_endpoint.delete_post(new_post_id)
    delete_endpoint.check_status_code(200)
    delete_endpoint.check_status_code_negative_test(new_post_id, 404)
