
from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class NestedFramesPage(BasePage):
    URL = "https://the-internet.herokuapp.com/nested_frames"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        top_frame = self.page.frame_locator(
            'frame[name="frame-top"]'
        )

        self.left_frame_text = WebElement(
            locator=top_frame.frame_locator(
                'frame[name="frame-left"]'
            ).locator("body"),
            description="Left frame text",
        )

        self.right_frame_text = WebElement(
            locator=top_frame.frame_locator(
                'frame[name="frame-right"]'
            ).locator("body"),
            description="Right frame text",
        )

        self.middle_frame_text = WebElement(
            locator=top_frame.frame_locator(
                'frame[name="frame-middle"]'
            ).locator("body"),
            description="Middle frame text",
        )

        self.bottom_frame_text = WebElement(
            locator=self.page.frame_locator(
                'frame[name="frame-bottom"]'
            ).locator("body"),
            description="Bottom frame text",
        )

    def get_left_text(self) -> str:
        return self.left_frame_text.get_inner_text()

    def get_right_text(self) -> str:
        return self.right_frame_text.get_inner_text()

    def get_middle_text(self) -> str:
        return self.middle_frame_text.get_inner_text()

    def get_bottom_text(self) -> str:
        return self.bottom_frame_text.get_inner_text()
