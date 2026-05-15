import pytest

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def login_and_open_products(page, base_url, standard_user, password) -> ProductsPage:
    login_page = LoginPage(page, base_url)
    products_page = ProductsPage(page, base_url)

    login_page.open()
    login_page.login(standard_user, password)
    products_page.is_loaded()

    return products_page


@pytest.mark.scenario_3
@pytest.mark.tc01
def test_s3_tc01_add_product_to_cart(page, base_url, standard_user, password):
    """
    Scenariusz 3: Weryfikacja zarządzania koszykiem
    Przypadek testowy ID 01: Dodanie produktu do koszyka
    """
    products_page = login_and_open_products(page, base_url, standard_user, password)

    products_page.add_product_to_cart("Sauce Labs Backpack")

    assert products_page.get_cart_badge_count() == 1


@pytest.mark.scenario_3
@pytest.mark.tc02
def test_s3_tc02_remove_product_from_cart_from_products_list(page, base_url, standard_user, password):
    """
    Scenariusz 3: Weryfikacja zarządzania koszykiem
    Przypadek testowy ID 02: Usunięcie produktu z koszyka z poziomu listy produktów
    """
    products_page = login_and_open_products(page, base_url, standard_user, password)

    product_name = "Sauce Labs Backpack"
    products_page.add_product_to_cart(product_name)
    assert products_page.get_cart_badge_count() == 1

    products_page.remove_product_from_cart(product_name)

    assert products_page.get_cart_badge_count() == 0


@pytest.mark.scenario_3
@pytest.mark.tc03
def test_s3_tc03_verify_cart_contents(page, base_url, standard_user, password):
    """
    Scenariusz 3: Weryfikacja zarządzania koszykiem
    Przypadek testowy ID 03: Weryfikacja zawartości koszyka
    """
    products_page = login_and_open_products(page, base_url, standard_user, password)
    cart_page = CartPage(page, base_url)

    first_product = "Sauce Labs Backpack"
    second_product = "Sauce Labs Bike Light"

    products_page.add_product_to_cart(first_product)
    products_page.add_product_to_cart(second_product)
    products_page.go_to_cart()
    cart_page.is_loaded()

    cart_items = cart_page.get_cart_items_names()

    assert first_product in cart_items
    assert second_product in cart_items
    assert len(cart_items) == 2
