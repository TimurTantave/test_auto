
import pytest

from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


@pytest.mark.parametrize(
    "name, n, filter_type, sort_order",
    [
        ("city", 10, "Price: low to high", "price_asc"),
        ("city", 15, "Price: high to low", "price_desc"),
        ("habits", 10, "Price: low to high", "price_asc"),
        ("habits", 15, "Price: high to low", "price_desc"),
    ],
)
def test_search_and_sort(page, name, n, filter_type, sort_order):
    home_page = HomePage(page)
    home_page.open_home_page()

    # Поиск по слову city или habits
    home_page.search(name)

    # Проверяем переход на страницу результатов поиска
    page.wait_for_url(f"**/search?q={name}")

    results_page = SearchResultsPage(page)

    # Проверяем, что поиск вернул карточки
    assert results_page.cards.count() > 0, (
        f"По запросу '{name}' ничего не найдено"
    )

    # Сортируем результаты по цене
    results_page.sort_by_price(sort_order)

    # Получаем цены первых n карточек
    prices = results_page.get_cards_price(n)

    assert len(prices) == n, (
        f"Ожидалось {n} цен, получено {len(prices)}"
    )
