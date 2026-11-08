
from playwright.sync_api import Page

from pages.dynamic_content_page import DynamicContentPage


def test_dynamic_content_has_duplicate_images(page: Page) -> None:
    URL = "https://the-internet.herokuapp.com/dynamic_content"
    page.goto(URL)

    dynamic_content_page = DynamicContentPage(page)

    max_attempts = 10
    expected_images_count = 3
    actual_sources = []

    for attempt in range(max_attempts):
        actual_sources = dynamic_content_page.get_image_sources()

        assert len(actual_sources) == expected_images_count, (
            f"Images count mismatch. "
            f"Expected: {expected_images_count}, Actual: {len(actual_sources)}"
        )

        if dynamic_content_page.has_duplicate_images():
            break

        if attempt < max_attempts - 1:
            page.reload()

    actual_duplicate_exists = (
        len(actual_sources) != len(set(actual_sources))
    )

    assert actual_duplicate_exists, (
        f"Expected at least 2 matching images out of {expected_images_count} "
        f"after {max_attempts} attempts. Actual image sources: {actual_sources}"
    )