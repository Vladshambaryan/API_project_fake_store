
import requests
import pytest
from endpoints.post_product import Post
from endpoints.patch_product import Patch
from endpoints.put_products import Put
from endpoints.get_one_product import Get
from endpoints.get_all_products import GetAll
from endpoints.delete_product import Delete

url = 'https://fakestoreapi.com'

@pytest.fixture()
def post_endpoint():
    return Post()

@pytest.fixture()
def put_endpoint():
    return Put()

@pytest.fixture()
def patch_endpoint():
    return Patch()


@pytest.fixture()
def get_one_endpoint():
    return Get()


@pytest.fixture()
def get_all_endpoints():
    return GetAll()


@pytest.fixture()
def delete_endpoint():
    return Delete()


@pytest.fixture
def new_post_id():
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f"{url}/products", json={'title': 'New Post', 'price': 10.99,
                                                      'description': 'This is a new post',
                                                      'image': 'https://example.com/image.jpg',
                                                      'category': 'electronics'})
    yield response.json()
    requests.delete(f"{url}/products/{response.json()['id']}", headers=headers)
