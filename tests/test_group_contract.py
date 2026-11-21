from faker import Faker
import requests

from services.university.helpers.group_helper import GroupHelper

fake = Faker()


class TestGroupContract:
    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.post_group({"name": fake.name()})

        assert response.status_code == requests.status_codes.codes.unauthorized, \
            f"Wrong status code: {response.status_code}, but expected: {requests.status_codes.codes.unauthorized}"
