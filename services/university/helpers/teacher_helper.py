import requests

from services.general.helpers.base_helper import BaseHelper


class TeacherHelper(BaseHelper):
    TEACHER_PREFIX = "/teachers"
    TEACHER_ENDPOINT = f"{TEACHER_PREFIX}/"

    def post_teacher(self, json: dict) -> requests.Response:
        response = self.api_utils.post(self.TEACHER_ENDPOINT, json=json)
        return response