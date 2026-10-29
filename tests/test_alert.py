
from pages.alert_page import AlertsPage


def test_js_alert(auth_page):
    alerts_page = AlertsPage(auth_page)
    alerts_page.open_page()

    alerts_page.click_js_alert()

    assert alerts_page.get_result() == "You successfully clicked an alert"


def test_js_confirm(auth_page):
    alerts_page = AlertsPage(auth_page)
    alerts_page.open_page()

    alerts_page.click_js_confirm()

    assert alerts_page.get_result() == "You clicked: Ok"


def test_js_prompt(auth_page):
    alerts_page = AlertsPage(auth_page)
    alerts_page.open_page()

    prompt_text = "Hello Playwright"
    alerts_page.click_js_prompt(prompt_text)

    assert alerts_page.get_result() == f"You entered: {prompt_text}"
