
from pathlib import Path

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class FileUploadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/upload"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.file_input = WebElement(
            locator=self.page.locator("#file-upload"),
            description="File input",
        )

        self.upload_button = WebElement(
            locator=self.page.locator("#file-submit"),
            description="Upload button",
        )

        self.uploaded_message = WebElement(
            locator=self.page.locator("h3"),
            description="Uploaded message",
        )

        self.uploaded_filename = WebElement(
            locator=self.page.locator("#uploaded-files"),
            description="Uploaded filename",
        )

    def upload_file(self, file_path: str | Path) -> None:
        self.file_input.locator.set_input_files(str(file_path))
        self.upload_button.click()

    def get_uploaded_message(self) -> str:
        return self.uploaded_message.get_inner_text()

    def get_uploaded_filename(self) -> str:
        return self.uploaded_filename.get_inner_text()
