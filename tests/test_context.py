
from pages.context_menu_page import ContextMenuPage


def test_context_menu_right_click(page):
    context_menu_page = ContextMenuPage(page)
    context_menu_page.open_page()

    page.on("dialog", lambda dialog: dialog.accept())

    context_menu_page.right_click_hot_spot()
