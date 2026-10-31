
from pathlib import Path

from playwright.sync_api import Page

from pages.file_upload_page import FileUploadPage


def test_file_upload(page: Page, tmp_path: Path) -> None:
    URL = "https://the-internet.herokuapp.com/upload"

    file_name = "test_upload.txt"
    file_path = tmp_path / file_name
    file_path.write_text("Test file for upload", encoding="utf-8")

    upload_page = FileUploadPage(page)
    upload_page.open(URL)
    upload_page.upload_file(file_path)

    assert upload_page.get_uploaded_message() == "File Uploaded!"
    assert upload_page.get_uploaded_filename() == file_name
