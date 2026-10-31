from playwright.sync_api import Page

from pages.infinite_scroll_page import InfiniteScrollPage


def test_infinite_scroll_loads_at_least_10_paragraphs(page: Page, ) -> None:
    URL = "https://the-internet.herokuapp.com/infinite_scroll"
    page.goto(URL)

    scroll_page = InfiniteScrollPage(page)

    expected_count = 10
    scroll_page.scroll_until_paragraphs_count(expected_count)

    actual_count = scroll_page.get_paragraphs_count()

    assert actual_count >= expected_count, (
        f"Paragraph count mismatch. "
        f"Expected: at least {expected_count}, Actual: {actual_count}"
    )
