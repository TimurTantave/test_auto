
from playwright.sync_api import Page

from pages.nested_frames_page import NestedFramesPage


def test_nested_frames_text(page: Page) -> None:
    nested_frames_page = NestedFramesPage(page)
    nested_frames_page.open(nested_frames_page.URL)

    assert nested_frames_page.get_left_text() == "LEFT"
    assert nested_frames_page.get_right_text() == "RIGHT"
    assert nested_frames_page.get_bottom_text() == "BOTTOM"
    assert nested_frames_page.get_middle_text() == "MIDDLE"
