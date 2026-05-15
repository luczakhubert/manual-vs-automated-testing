# Analiza efektywności testów manualnych i automatycznych wybranej aplikacji webowej

Projekt kierunkowy przedstawiający analizę efektywności testów manualnych oraz automatycznych na przykładzie aplikacji webowej typu e-commerce z wykorzystaniem frameworka `pytest` oraz narzędzia `Playwright`.

## Cel projektu

Celem projektu było porównanie testów manualnych oraz automatycznych pod względem:

- czasu wykonywania testów,
- powtarzalności,
- skuteczności wykrywania błędów,
- możliwości testowania obszarów UX/UI oraz dostępności cyfrowej.

Badania zostały przeprowadzone na podstawie aplikacji webowej:  
https://www.saucedemo.com/

---

## Wykorzystane technologie

Projekt został zrealizowany z wykorzystaniem:

- Python 3.12
- pytest
- Playwright
- PyCharm
- Google Chrome / Chromium

---

## Zakres testów

Zaimplementowane testy obejmują następujące obszary aplikacji:

- logowanie użytkownika,
- przeglądanie produktów,
- zarządzanie koszykiem,
- proces realizacji zamówienia,
- podstawowe aspekty UX/UI,
- wybrane elementy dostępności cyfrowej.

---

## Struktura projektu

```text
tests/
├── test_login.py
├── test_products.py
├── test_cart.py
└── test_checkout.py

pages/
├── login_page.py
├── products_page.py
├── cart_page.py
└── checkout_page.py

conftest.py
pytest.ini
requirements.txt
