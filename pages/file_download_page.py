
from pathlib import Path

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class FileDownloadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/download"

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.files = MultiWebElement(
            page=self.page,
            locator=self.page.locator("#content a"),
            description="Downloadable files",
        )

    def open(self, url: str) -> None:
        self.page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=30000,
        )

    def get_file_name(self, index: int) -> str:
        return self.files.nth(index).get_inner_text()

    def download_file(self, index: int, download_dir: str | Path) -> Path:
        file_link = self.files.nth(index)

        with self.page.expect_download() as download_info:
            file_link.click()

        download = download_info.value
        file_path = Path(download_dir) / download.suggested_filename
        download.save_as(str(file_path))

        return file_path
