import requests
import pytest
from random import randint

BASE_URL = "https://jsonplaceholder.typicode.com"
RANDOM_ID_POST = randint(1, 100)
PATH = "/posts"


@pytest.mark.parametrize(
        "header, value",
        [
            ("Content-Type", "application/json; charset=utf-8"),
        ]
)
def test_get_posts(header, value):
    response = requests.get(BASE_URL+PATH)
    assert response.headers[header] == value
    assert response.status_code == 200
    assert len(response.json()) == 100
    assert type(response.json()) == list


@pytest.mark.parametrize(
        "name_str, type_str",
        [
            ("id", int),
            ("userId", int),
            ("title", str),
            ("body", str)
        ]
)
def test_get_post_id(post_keys, name_str, type_str):
    response = requests.get(BASE_URL+PATH+f"/{RANDOM_ID_POST}")

    assert response.status_code == 200
    response_json = response.json()
    set_keys = set(post_keys)
    assert len(response_json) == len(set(post_keys))
    assert response_json.keys() == set_keys
    assert type(response_json[name_str]) == type_str


@pytest.mark.parametrize(
        'key',
        [
            "userId",
            "title",
            "body"
        ]
)
def test_create_post(create_post_data, key):
    response = requests.post(url=BASE_URL+PATH, data=create_post_data)
    assert response.status_code == 201
    new_post = response.json()
    assert new_post[key] == create_post_data[key], (
        f"Incorrectly specified: {key}"
    )


def test_delete_post(create_post_data):
    response_create = requests.post(url=BASE_URL+PATH, data=create_post_data)
    get_post_id = response_create.json()["id"]
    path_create_post = PATH+f"/{get_post_id}/"
    response_delete = requests.delete(url=BASE_URL+path_create_post)

    assert response_delete.status_code == 200
