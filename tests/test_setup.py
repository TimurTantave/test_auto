
def test_home_page_opens(page):
    page.goto("https://the-internet.herokuapp.com/")

    expected_title = "The Internet"
    actual_title = page.title()

    assert actual_title == expected_title, (
        f"Home page title mismatch. "
        f"Expected: '{expected_title}', Actual: '{actual_title}'"
    )