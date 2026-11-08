
from pathlib import Path

from playwright.sync_api import Page

from pages.file_download_page import FileDownloadPage


def test_download_third_file(page: Page, tmp_path: Path) -> None:
    URL = "https://the-internet.herokuapp.com/download"
    page.goto(URL)

    download_page = FileDownloadPage(page)

    expected_file_name = download_page.get_file_name(2)
    downloaded_file = download_page.download_file(2, tmp_path)

    expected_file_exists = True
    actual_file_exists = downloaded_file.exists()

    assert actual_file_exists == expected_file_exists, (
        f"Downloaded file existence mismatch. "
        f"Expected: '{expected_file_exists}', Actual: '{actual_file_exists}'"
    )

    expected_file_name = expected_file_name
    actual_file_name = downloaded_file.name

    assert actual_file_name == expected_file_name, (
        f"Downloaded file name mismatch. "
        f"Expected: '{expected_file_name}', Actual: '{actual_file_name}'"
    )

