import requests

from services.general.helpers.base_helper import BaseHelper


class StudentHelper(BaseHelper):
    STUDENT_PREFIX = "/students"
    STUDENT_ENDPOINT = f"{STUDENT_PREFIX}/"

    def post_student(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.STUDENT_ENDPOINT, json=json)
        return response