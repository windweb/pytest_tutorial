from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                # validate(item, schema)  # используя jsonschema
                # используя pydantic v1.x
                # schema.parse_obj(item)
                # используя pydantic v2.x+ https://docs.pydantic.dev/2.6/migration/#continue-using-pydantic-v1-features
                schema.model_validate(item)
        else:
            # validate(self.response_json, schema)  # используя jsonschema
            # используя pydantic v1.x
            # schema.parse_obj(self.response_json)
            # используя pydantic v2.x+
            schema.model_validate(self.response_json)
        return self

        # for item in received_posts:
        #     validate(item, POST_SCHEMA)

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value

        return self


