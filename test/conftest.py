import pytest


@pytest.fixture
def post_keys():
    keys = ["userId", "id", "title", "body"]
    return keys


@pytest.fixture
def create_post_data():
    data = {
        'userId': '13',
        'title': 'test_title',
        'body': 'test_body'
    }
    return data
