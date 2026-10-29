
from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

from pages.infinite_scroll_page import InfiniteScrollPage


def test_infinite_scroll_loads_at_least_10_paragraphs(
    page: Page,
) -> None:
    scroll_page = InfiniteScrollPage(page)
    scroll_page.open(scroll_page.URL)

    max_attempts = 30

    for _ in range(max_attempts):
        previous_count = scroll_page.get_paragraphs_count()

        if previous_count >= 10:
            break

        scroll_page.scroll_down()

        try:
            page.wait_for_function(
                """previousCount =>
                    document.querySelectorAll(
                        '.jscroll-inner .jscroll-added'
                    ).length > previousCount
                """,
                arg=previous_count,
                timeout=3000,
            )
        except PlaywrightTimeoutError:
            continue

    actual_count = scroll_page.get_paragraphs_count()

    assert actual_count >= 10, (
        f"Expected at least 10 paragraphs, found {actual_count}"
    )
