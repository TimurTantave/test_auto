
from pages.alert_page import AlertsPage


def test_js_alert(page):
    URL = "https://the-internet.herokuapp.com/javascript_alerts"
    page.goto(URL)

    alerts_page = AlertsPage(page)
    alerts_page.click_js_alert()

    expected_result = "You successfully clicked an alert"
    actual_result = alerts_page.get_result()

    assert actual_result == expected_result, (
        f"Alert result mismatch. "
        f"Expected: '{expected_result}', Actual: '{actual_result}'"
    )


def test_js_confirm(auth_page):
    auth_page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    alerts_page = AlertsPage(auth_page)

    alerts_page.click_js_confirm()

    expected_result = "You clicked: Ok"
    actual_result = alerts_page.get_result()

    assert actual_result == expected_result, (
        f"JS Confirm result mismatch. "
        f"Expected: '{expected_result}', Actual: '{actual_result}'"
    )


def test_js_prompt(auth_page):
    auth_page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    alerts_page = AlertsPage(auth_page)

    prompt_text = "Hello Playwright"
    alerts_page.click_js_prompt(prompt_text)

    expected_result = f"You entered: {prompt_text}"
    actual_result = alerts_page.get_result()

    assert actual_result == expected_result, (
        f"JS Prompt result mismatch. "
        f"Expected: '{expected_result}', Actual: '{actual_result}'"
    )
