import pytest

from config.config_reader import ConfigReader
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage, SortType


@pytest.mark.parametrize("name", ["city", "habits"])
@pytest.mark.parametrize(
    "n, sort_order",
    [
        (10, SortType.PRICE_ASC),
        (15, SortType.PRICE_DESC),
    ],
)
def test_search_and_sort(page, name, n, sort_order):
    home_page = HomePage(page)
    config = ConfigReader()
    page.goto(config.get("base_url"))

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

    if sort_order == SortType.PRICE_ASC:
        assert prices == sorted(prices), (
            f"Цены должны идти по возрастанию: {prices}"
        )
    elif sort_order == SortType.PRICE_DESC:
        assert prices == sorted(prices, reverse=True), (
            f"Цены должны идти по убыванию: {prices}"
        )
