import re
from typing import List

from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.title_label: Locator = page.locator('[data-test="title"]')
        self.sort_select: Locator = page.locator('[data-test="product-sort-container"]')
        self.cart_link: Locator = page.locator('[data-test="shopping-cart-link"]')
        self.cart_badge: Locator = page.locator('[data-test="shopping-cart-badge"]')
        self.product_prices: Locator = page.locator('[data-test="inventory-item-price"]')

    def is_loaded(self) -> bool:
        expect(self.title_label).to_have_text("Products")
        return True

    def sort_by_low_to_high(self) -> None:
        self.sort_select.select_option("lohi")

    def get_all_prices(self) -> List[float]:
        raw_prices = self.product_prices.all_text_contents()
        return [float(price.replace("$", "").strip()) for price in raw_prices]

    def open_product_details(self, product_name: str) -> None:
        self.page.locator(f'[data-test="inventory-item-name"]:has-text("{product_name}")').click()

    def get_product_details_name(self) -> str:
        locator = self.page.locator('[data-test="inventory-item-name"]')
        expect(locator).to_be_visible()
        return locator.text_content() or ""

    def add_product_to_cart(self, product_name: str) -> None:
        product_id = self._slugify_product_name(product_name)
        self.page.locator(f'[data-test="add-to-cart-{product_id}"]').click()

    def remove_product_from_cart(self, product_name: str) -> None:
        product_id = self._slugify_product_name(product_name)
        self.page.locator(f'[data-test="remove-{product_id}"]').click()

    def get_cart_badge_count(self) -> int:
        if self.cart_badge.count() == 0:
            return 0
        text = self.cart_badge.text_content() or "0"
        return int(text)

    def go_to_cart(self) -> None:
        self.cart_link.click()

    @staticmethod
    def _slugify_product_name(product_name: str) -> str:
        slug = product_name.strip().lower()
        slug = re.sub(r"[^a-z0-9]+", "-", slug)
        return slug.strip("-")