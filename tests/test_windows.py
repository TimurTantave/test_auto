
from playwright.sync_api import Page

from pages.window_page import WindowsPage


def test_open_multiple_windows(page: Page) -> None:
    windows_page = WindowsPage(page)
    windows_page.open(windows_page.URL)

    # Открываем первую новую вкладку
    first_window = windows_page.open_new_window()

    assert first_window.get_heading_text() == "New Window"

    # Возвращаемся к исходной вкладке
    windows_page.return_to_original_tab()

    # Открываем вторую новую вкладку
    second_window = windows_page.open_new_window()

    assert second_window.get_heading_text() == "New Window"

    # Возвращаемся к исходной вкладке
    windows_page.return_to_original_tab()

    # Закрываем обе новые вкладки
    first_window.close()
    second_window.close()

    # Проверяем, что осталась только исходная вкладка
    assert windows_page.get_open_tabs_count() == 1
