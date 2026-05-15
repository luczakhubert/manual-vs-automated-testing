import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def prepare_user_with_product_in_cart(page, base_url, standard_user, password) -> tuple[CartPage, CheckoutPage]:
    login_page = LoginPage(page, base_url)
    products_page = ProductsPage(page, base_url)
    cart_page = CartPage(page, base_url)
    checkout_page = CheckoutPage(page, base_url)

    login_page.open()
    login_page.login(standard_user, password)
    products_page.is_loaded()

    products_page.add_product_to_cart("Sauce Labs Backpack")
    products_page.go_to_cart()
    cart_page.is_loaded()

    return cart_page, checkout_page


@pytest.mark.scenario_4
@pytest.mark.tc01
def test_s4_tc01_go_to_checkout_form(page, base_url, standard_user, password):
    """
    Scenariusz 4: Weryfikacja procesu realizacji zamówienia
    Przypadek testowy ID 01: Przejście do formularza zamówienia
    """
    cart_page, checkout_page = prepare_user_with_product_in_cart(page, base_url, standard_user, password)

    cart_page.click_checkout()

    assert checkout_page.is_checkout_information_loaded() is True


@pytest.mark.scenario_4
@pytest.mark.tc02
def test_s4_tc02_complete_checkout_with_valid_data(page, base_url, standard_user, password):
    """
    Scenariusz 4: Weryfikacja procesu realizacji zamówienia
    Przypadek testowy ID 02: Finalizacja zamówienia z poprawnymi danymi
    """
    cart_page, checkout_page = prepare_user_with_product_in_cart(page, base_url, standard_user, password)

    cart_page.click_checkout()
    checkout_page.fill_checkout_information("Adam", "Testowy", "50-001")
    checkout_page.continue_checkout()
    checkout_page.is_checkout_overview_loaded()
    checkout_page.finish_checkout()

    assert "checkout-complete" in page.url
    assert checkout_page.get_complete_header() == "Thank you for your order!"


@pytest.mark.scenario_4
@pytest.mark.tc03
def test_s4_tc03_checkout_without_form_data(page, base_url, standard_user, password):
    """
    Scenariusz 4: Weryfikacja procesu realizacji zamówienia
    Przypadek testowy ID 03: Próba realizacji zamówienia bez wypełnienia danych formularza
    """
    cart_page, checkout_page = prepare_user_with_product_in_cart(page, base_url, standard_user, password)

    cart_page.click_checkout()
    checkout_page.continue_checkout()

    error_message = checkout_page.get_error_message()
    assert "First Name is required" in error_message