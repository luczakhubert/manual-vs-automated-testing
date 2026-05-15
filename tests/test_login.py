import pytest

from pages.login_page import LoginPage


@pytest.mark.scenario_1
@pytest.mark.tc01
def test_s1_tc01_valid_login(page, base_url, standard_user, password):
    """
    Scenariusz 1: Weryfikacja procesu logowania użytkownika
    Przypadek testowy ID 01: Logowanie z poprawnymi danymi użytkownika
    """
    login_page = LoginPage(page, base_url)

    login_page.open()
    login_page.login(standard_user, password)

    assert "inventory" in page.url


@pytest.mark.scenario_1
@pytest.mark.tc02
def test_s1_tc02_invalid_password(page, base_url, standard_user):
    """
    Scenariusz 1: Weryfikacja procesu logowania użytkownika
    Przypadek testowy ID 02: Logowanie z błędnym hasłem użytkownika
    """
    login_page = LoginPage(page, base_url)

    login_page.open()
    login_page.login(standard_user, "fakepassword")

    error_message = login_page.get_error_message()
    assert "Username and password do not match" in error_message


@pytest.mark.scenario_1
@pytest.mark.tc03
def test_s1_tc03_login_without_username(page, base_url, password):
    """
    Scenariusz 1: Weryfikacja procesu logowania użytkownika
    Przypadek testowy ID 03: Logowanie bez podania loginu
    """
    login_page = LoginPage(page, base_url)

    login_page.open()
    login_page.login_without_username(password)

    error_message = login_page.get_error_message()
    assert "Username is required" in error_message


@pytest.mark.scenario_1
@pytest.mark.tc04
def test_s1_tc04_login_without_password(page, base_url, standard_user):
    """
    Scenariusz 1: Weryfikacja procesu logowania użytkownika
    Przypadek testowy ID 04: Logowanie bez podania hasła
    """
    login_page = LoginPage(page, base_url)

    login_page.open()
    login_page.login_without_password(standard_user)

    error_message = login_page.get_error_message()
    assert "Password is required" in error_message


@pytest.mark.scenario_1
@pytest.mark.tc05
def test_s1_tc05_locked_out_user(page, base_url, locked_out_user, password):
    """
    Scenariusz 1: Weryfikacja procesu logowania użytkownika
    Przypadek testowy ID 05: Logowanie zablokowanego użytkownika
    """
    login_page = LoginPage(page, base_url)

    login_page.open()
    login_page.login(locked_out_user, password)

    error_message = login_page.get_error_message()
    assert "Sorry, this user has been locked out." in error_message