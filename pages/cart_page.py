from typing import List

from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.title_label: Locator = page.locator('[data-test="title"]')
        self.cart_items: Locator = page.locator('[data-test="inventory-item-name"]')
        self.checkout_button: Locator = page.locator('[data-test="checkout"]')

    def is_loaded(self) -> bool:
        expect(self.title_label).to_have_text("Your Cart")
        return True

    def get_cart_items_names(self) -> List[str]:
        return [name.strip() for name in self.cart_items.all_text_contents()]

    def click_checkout(self) -> None:
        self.checkout_button.click()