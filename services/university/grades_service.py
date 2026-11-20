from services.general.base_service import BaseService
from services.university.helpers.grades_helper import GradesHelper
from services.university.models.grades_stats_request import GradesStatsRequest
from services.university.models.grades_stats_response import GradesStatsResponse
from utils.session_utils import ApiUtils


class GradesService(BaseService):

    def __init__(self, api_utils: ApiUtils):
        super().__init__(api_utils)

        self.grades_helper = GradesHelper(self.api_utils)

    def get_grades_stats(
        self,
        grades_request: GradesStatsRequest
    ) -> GradesStatsResponse:
        response = self.grades_helper.get_grades_stats(
            params=grades_request.model_dump(exclude_none=True)
        )

        return GradesStatsResponse(**response.json())