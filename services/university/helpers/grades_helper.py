import requests

from services.general.helpers.base_helper import BaseHelper


class GradesHelper(BaseHelper):
    GRADES_PREFIX = "/grades"
    STATS_ENDPOINT = f"{GRADES_PREFIX}/stats/"
    GRADE_ENDPOINT = f"{GRADES_PREFIX}/"

    def get_grades_stats(self, params: dict) -> requests.Response:
        response = self.api_utils.get(self.STATS_ENDPOINT, params=params)
        return response

    def post_grade(self, data: dict) -> requests.Response:
        response = self.api_utils.post("/grades/", data=data)
        return response