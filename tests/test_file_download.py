
from pathlib import Path

from playwright.sync_api import Page

from pages.file_download_page import FileDownloadPage


def test_download_third_file(page: Page, tmp_path: Path) -> None:
    download_page = FileDownloadPage(page)
    download_page.open(download_page.URL)

    expected_file_name = download_page.get_file_name(2)

    downloaded_file = download_page.download_file(2, tmp_path)

    assert downloaded_file.exists(), (
        f"Downloaded file was not saved: {downloaded_file}"
    )
    assert downloaded_file.name == expected_file_name, (
        f"Expected file '{expected_file_name}', "
        f"but downloaded '{downloaded_file.name}'"
    )
