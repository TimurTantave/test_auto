from urllib import request

import requests

from services.general.base_service import BaseService
from services.university.helpers.grades_helper import GradesHelper
from services.university.models.grades_stats_response import GradesStatsResponse
from utils.session_utils import ApiUtils


class GradesService(BaseService):

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.grades_helper = GradesHelper(self.api_utils)

    def get_grades_stats(
        self,
        student_id: int | None = None,
        teacher_id: int | None = None,
        group_id: int | None = None,
    ) -> GradesStatsResponse:

        params = {
            "student_id": student_id,
            "teacher_id": teacher_id,
            "group_id": group_id,
        }

        response = self.grades_helper.get_grades_stats(
            params={key: value for key, value in params.items() if value is not None}
        )

        return GradesStatsResponse(**response.json())

    def create_grade(
            self,
            teacher_id: int,
            student_id: int,
            grade: int,
    ) -> requests.Response:
        data = {
            "teacher_id": teacher_id,
            "student_id": student_id,
            "grade": grade,
        }

        return self.grades_helper.post_grade(data=data)
