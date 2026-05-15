import pytest

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def login_as_standard_user(page, base_url, standard_user, password) -> ProductsPage:
    login_page = LoginPage(page, base_url)
    products_page = ProductsPage(page, base_url)

    login_page.open()
    login_page.login(standard_user, password)
    products_page.is_loaded()

    return products_page


@pytest.mark.scenario_2
@pytest.mark.tc01
def test_s2_tc01_products_list_visible_after_login(page, base_url, standard_user, password):
    """
    Scenariusz 2: Weryfikacja przeglądania listy produktów
    Przypadek testowy ID 01: Wyświetlenie listy produktów po zalogowaniu
    """
    products_page = login_as_standard_user(page, base_url, standard_user, password)

    assert products_page.is_loaded() is True
    assert "inventory" in page.url


@pytest.mark.scenario_2
@pytest.mark.tc02
def test_s2_tc02_sort_products_by_price_ascending(page, base_url, standard_user, password):
    """
    Scenariusz 2: Weryfikacja przeglądania listy produktów
    Przypadek testowy ID 02: Sortowanie produktów według ceny rosnąco
    """
    products_page = login_as_standard_user(page, base_url, standard_user, password)

    products_page.sort_by_low_to_high()
    prices = products_page.get_all_prices()

    assert prices == sorted(prices)


@pytest.mark.scenario_2
@pytest.mark.tc03
def test_s2_tc03_open_product_details(page, base_url, standard_user, password):
    """
    Scenariusz 2: Weryfikacja przeglądania listy produktów
    Przypadek testowy ID 03: Wyświetlenie szczegółów produktu
    """
    products_page = login_as_standard_user(page, base_url, standard_user, password)

    product_name = "Sauce Labs Backpack"
    products_page.open_product_details(product_name)

    assert products_page.get_product_details_name() == product_name