from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(le=3)
    title: str
    # name: str = Field(alias='_name')

    # @validator('title')
    # def title_must_contain_post(cls, title):
    #     if 'post' not in title.lower():
    #         raise ValueError('Title must contain post')
    #     return title
    #
    # @validator('id')
    # def check_that_id_is_less_than_two(cls, id):
    #     if id > 2:
    #         raise ValueError('Id is not less than 2')
    #     return id


##  {'id':1, 'title': 'Post 1', '_name': 'Kirill'}
