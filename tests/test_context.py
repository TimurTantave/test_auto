
from playwright.sync_api import Page

from pages.context_menu_page import ContextMenuPage


def test_context_menu(page: Page) -> None:
    URL = "https://the-internet.herokuapp.com/context_menu"
    page.goto(URL)

    context_menu_page = ContextMenuPage(page)

    actual_message = context_menu_page.actions.run_and_accept_alert(
        context_menu_page.right_click_hot_spot
    )

    expected_message = "You selected a context menu"

    assert actual_message == expected_message, (
        f"Context menu message mismatch. "
        f"Expected: '{expected_message}', "
        f"Actual: '{actual_message}'"
    )