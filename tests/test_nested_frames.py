
from playwright.sync_api import Page

from pages.nested_frames_page import NestedFramesPage


def test_nested_frames_content(page: Page) -> None:
    URL = "https://the-internet.herokuapp.com/nested_frames"
    page.goto(URL)

    frames_page = NestedFramesPage(page)

    expected_values = {
        "left": "LEFT",
        "right": "RIGHT",
        "middle": "MIDDLE",
        "bottom": "BOTTOM",
    }

    actual_values = {
        "left": frames_page.get_left_text(),
        "right": frames_page.get_right_text(),
        "middle": frames_page.get_middle_text(),
        "bottom": frames_page.get_bottom_text(),
    }

    for frame_name, expected_value in expected_values.items():
        actual_value = actual_values[frame_name]

        assert actual_value == expected_value, (
            f"{frame_name.capitalize()} frame text mismatch. "
            f"Expected: '{expected_value}', Actual: '{actual_value}'"
        )
