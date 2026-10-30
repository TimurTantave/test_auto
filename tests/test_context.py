
from pages.context_menu_page import ContextMenuPage


def test_context_menu(page):
    URL = "https://the-internet.herokuapp.com/context_menu"
    page.goto(URL)

    context_menu_page = ContextMenuPage(page)
    context_menu_page.right_click_hot_spot()

    expected_message = "You selected a context menu"
    actual_message = page.locator("body").inner_text()

    assert expected_message in actual_message, (
        f"Context menu message mismatch. "
        f"Expected to contain: '{expected_message}', "
        f"Actual: '{actual_message}'"
    )