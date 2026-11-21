from faker import Faker

from services.university.university_service import UniversityService
from services.university.models.group_request import GroupRequest
from services.university.models.group_response import GroupResponse

fake = Faker()


class TestGroup:

    def test_get_groups(self, uni_api_utils_admin):
        # Arrange
        university_service = UniversityService(
            api_utils=uni_api_utils_admin
        )

        group_request = GroupRequest(
            name=fake.name()
        )

        # Act
        created_group = university_service.create_group(
            group_request=group_request
        )

        groups = university_service.get_groups()

        assert all(
            isinstance(group, GroupResponse)
            for group in groups
        ), "Response contains objects that are not GroupResponse"

        assert created_group in groups, (
            f"Created group with id={created_group.id} "
            f"was not found in groups response"
        )
