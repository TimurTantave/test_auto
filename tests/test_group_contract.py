import requests
from faker import Faker

from services.university.helpers.group_helper import GroupHelper

fake = Faker()


class TestGroupContract:
    def test_create_group_anonym(self, university_api_utils_anonym):
        group_helper = GroupHelper(api_utils=university_api_utils_anonym)
        response = group_helper.post_group({"name": fake.name()})
        expected_status = requests.status_codes.codes.unauthorized

        assert response.status_code == expected_status, (
            f"Wrong status code: {response.status_code}, "
            f"but expected: {expected_status}"
        )