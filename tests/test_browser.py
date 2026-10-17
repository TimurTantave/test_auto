def test_browser_opens(page, config):
    page.goto(config.get("base_url"))

    assert page.url.startswith(config.get("base_url"))