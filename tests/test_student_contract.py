
from faker import Faker
import requests

from services.university.helpers.student_helper import StudentHelper
from services.university.helpers.group_helper import GroupHelper

fake = Faker()


class TestStudentContract:

    def test_create_student_success(self, uni_api_utils_admin):
        group_helper = GroupHelper(api_utils=uni_api_utils_admin)
        student_helper = StudentHelper(api_utils=uni_api_utils_admin)

        group_response = group_helper.post_group(
            json={"name": fake.name()}
        )

        assert group_response.status_code == requests.status_codes.codes.created

        student_data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "degree": "Bachelor",
            "phone": fake.numerify("+7##########"),
            "group_id": group_response.json()["id"]
        }

        response = student_helper.post_student(json=student_data)

        assert response.status_code == requests.status_codes.codes.created, (
            f"Wrong status code: {response.status_code}, "
            f"but expected: {requests.status_codes.codes.created}"
        )

        assert response.json()["email"] == student_data["email"]

    def test_create_student_anonym(self, university_api_utils_anonym):
        student_helper = StudentHelper(api_utils=university_api_utils_anonym)

        response = student_helper.post_student(
            json={
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "degree": "Bachelor",
                "phone": fake.numerify("+7##########"),
                "group_id": 1
            }
        )

        assert response.status_code == requests.status_codes.codes.unauthorized, (
            f"Wrong status code: {response.status_code}, "
            f"but expected: {requests.status_codes.codes.unauthorized}"
        )

    def test_create_student_invalid_group(self, uni_api_utils_admin):
        student_helper = StudentHelper(api_utils=uni_api_utils_admin)

        response = student_helper.post_student(
            json={
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "degree": "Bachelor",
                "phone": fake.numerify("+7##########"),
                "group_id": 999999999
            }
        )

        assert response.status_code == requests.status_codes.codes.not_found, (
            f"Wrong status code: {response.status_code}, "
            f"but expected: {requests.status_codes.codes.not_found}"
        )

    def test_create_student_missing_field(self, uni_api_utils_admin):
        student_helper = StudentHelper(api_utils=uni_api_utils_admin)

        response = student_helper.post_student(
            json={
                "last_name": fake.last_name(),
                "email": fake.email(),
                "degree": "Bachelor",
                "phone": fake.numerify("+7##########"),
                "group_id": 1
            }
        )

        assert response.status_code == requests.status_codes.codes.unprocessable_entity, (
            f"Wrong status code: {response.status_code}, "
            f"but expected: {requests.status_codes.codes.unprocessable_entity}"
        )

    def test_create_student_duplicate_email(self, uni_api_utils_admin):
        group_helper = GroupHelper(api_utils=uni_api_utils_admin)
        student_helper = StudentHelper(api_utils=uni_api_utils_admin)

        group_response = group_helper.post_group(
            json={"name": fake.name()}
        )

        assert group_response.status_code == requests.status_codes.codes.created

        student_data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
            "degree": "Bachelor",
            "phone": fake.numerify("+7##########"),
            "group_id": group_response.json()["id"]
        }

        first_response = student_helper.post_student(json=student_data)

        assert first_response.status_code == requests.status_codes.codes.created

        duplicate_data = student_data.copy()
        duplicate_data["phone"] = fake.numerify("+7##########")

        response = student_helper.post_student(json=duplicate_data)

        assert response.status_code == requests.status_codes.codes.conflict, (
            f"Wrong status code: {response.status_code}, "
            f"but expected: {requests.status_codes.codes.conflict}"
        )
