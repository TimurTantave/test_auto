from playwright.sync_api import Page

from pages.hover_page import HoversPage
from utils.validators import is_valid_user_name

def test_hover_all_users(page: Page) -> None:
    URL = "https://the-internet.herokuapp.com/hovers"
    page.goto(URL)

    hovers_page = HoversPage(page)

    users_count = hovers_page.get_users_count()

    for index in range(users_count):
        hovers_page.hover_user(index)

        actual_name = hovers_page.get_user_name(index)
        is_valid = is_valid_user_name(actual_name)

        expected_format = f"name: user{index + 1}"

        assert is_valid, (
            f"User name format is invalid. "
            f"Expected format: '{expected_format}', Actual: '{actual_name}'"
        )