
from pages.basic_auth_page import BasicAuthPage


def test_basic_auth_success(auth_page):
    basic_auth_page = BasicAuthPage(auth_page)

    basic_auth_page.open_with_credentials()

    assert (
        basic_auth_page.get_success_message()
        == BasicAuthPage.SUCCESS_MESSAGE
    )
