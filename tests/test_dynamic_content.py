
from playwright.sync_api import Page

from pages.dynamic_content_page import DynamicContentPage


def test_find_duplicate_images(page: Page) -> None:
    content_page = DynamicContentPage(page)
    content_page.open(content_page.URL)

    max_attempts = 20

    for attempt in range(max_attempts):
        if content_page.has_duplicate_images():
            break

        if attempt < max_attempts - 1:
            content_page.refresh_page()
    else:
        raise AssertionError(
            f"No duplicate images found after {max_attempts} attempts"
        )

    assert content_page.has_duplicate_images(), (
        "Expected at least two identical images"
    )
