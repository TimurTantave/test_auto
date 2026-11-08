
from pages.basic_auth_page import BasicAuthPage


def test_basic_auth_success(auth_page):
    URL = "https://the-internet.herokuapp.com/basic_auth"
    auth_page.goto(URL)

    basic_auth_page = BasicAuthPage(auth_page)

    expected_result = "Congratulations! You must have the proper credentials."
    actual_result = basic_auth_page.get_success_message()

    assert actual_result == expected_result, (
        f"Basic Auth success message mismatch. "
        f"Expected: '{expected_result}', Actual: '{actual_result}'"
    )
