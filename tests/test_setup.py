
def test_home_page_opens(page):
    page.goto("https://the-internet.herokuapp.com/")

    assert page.title() == "The Internet"
