import requests
from jsonschema import validate
from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
from src.schemas.post import POST_SCHEMA


def test_getting_posts():
    response = requests.get(url=SERVICE_URL, )

    received_posts = response.json()
    # 
    # received_posts = [{'id':1, 'title': 'Post 1'},{'id':2, 'title': 'Post 2'},{'id':3, 'title': 'Post 3'}]
    # 
    print(received_posts)

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
    for item in received_posts:
        # assert 'id' in item
        # assert 'title' in item
        validate(item, POST_SCHEMA)

    # print(response.json(url=SERVICE_URL))

## https://my-json-server.typicode.com/typicode/demo/posts
