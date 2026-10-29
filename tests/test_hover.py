from playwright.sync_api import Page

from pages.hover_page import HoversPage


def test_hover_all_users(page: Page) -> None:
    hovers_page = HoversPage(page)
    hovers_page.open(hovers_page.URL)

    users_count = hovers_page.get_users_count()

    assert users_count > 0, "No users found on the page"

    for index in range(users_count):
        hovers_page.hover_user(index)

        user_name = hovers_page.get_user_name(index)

        assert hovers_page.is_valid_user_name(user_name), (
            f"Invalid user name at index {index}: {user_name}"
        )