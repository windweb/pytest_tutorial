import requests
# from jsonschema import validate
from configuration import SERVICE_URL
# from src.enums.global_enums import GlobalErrorMessages
from src.baseclasses.response import Response
from src.schemas.post import POST_SCHEMA



def test_getting_posts():
    r = requests.get(url=SERVICE_URL, )
    response = Response(r)
    response.assert_status_code(200).validate(POST_SCHEMA)

    # received_posts = response.json()
    # 
    # received_posts = [{'id':1, 'title': 'Post 1'},{'id':2, 'title': 'Post 2'},{'id':3, 'title': 'Post 3'}]
    # 
    # print(received_posts)
    #
    # # assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    # assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
    # for item in received_posts:
    #     validate(item, POST_SCHEMA)

    # print(response.json(url=SERVICE_URL))

## https://my-json-server.typicode.com/typicode/demo/posts
