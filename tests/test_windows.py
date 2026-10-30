
from playwright.sync_api import Page

from pages.window_page import WindowsPage


def test_open_multiple_windows(page: Page) -> None:
    URL = "https://the-internet.herokuapp.com/windows"
    page.goto(URL)

    windows_page = WindowsPage(page)

    first_window = windows_page.open_new_window()

    expected_heading = "New Window"
    actual_heading = first_window.get_heading_text()

    assert actual_heading == expected_heading, (
        f"First window heading mismatch. "
        f"Expected: '{expected_heading}', Actual: '{actual_heading}'"
    )

    second_window = windows_page.open_new_window()

    expected_heading = "New Window"
    actual_heading = second_window.get_heading_text()

    assert actual_heading == expected_heading, (
        f"Second window heading mismatch. "
        f"Expected: '{expected_heading}', Actual: '{actual_heading}'"
    )

    expected_tabs_count = 3
    actual_tabs_count = len(page.context.pages)

    assert actual_tabs_count == expected_tabs_count, (
        f"Open tabs count mismatch. "
        f"Expected: {expected_tabs_count}, Actual: {actual_tabs_count}"
    )

    first_window.page.close()
    second_window.page.close()

    expected_tabs_count = 1
    actual_tabs_count = len(page.context.pages)

    assert actual_tabs_count == expected_tabs_count, (
        f"Open tabs count after closing windows mismatch. "
        f"Expected: {expected_tabs_count}, Actual: {actual_tabs_count}"
    )