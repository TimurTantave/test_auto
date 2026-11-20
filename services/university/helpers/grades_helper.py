import requests

from services.general.helpers.base_helper import BaseHelper


class GradesHelper(BaseHelper):
    GRADES_PREFIX = "/grades"
    STATS_ENDPOINT = f"{GRADES_PREFIX}/stats/"

    def get_grades_stats(self, params: dict) -> requests.Response:
        response = self.api_utils.get(self.STATS_ENDPOINT, params=params)
        return response