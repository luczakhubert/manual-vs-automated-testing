from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.title_label: Locator = page.locator('[data-test="title"]')
        self.first_name_input: Locator = page.locator('[data-test="firstName"]')
        self.last_name_input: Locator = page.locator('[data-test="lastName"]')
        self.postal_code_input: Locator = page.locator('[data-test="postalCode"]')
        self.continue_button: Locator = page.locator('[data-test="continue"]')
        self.finish_button: Locator = page.locator('[data-test="finish"]')
        self.error_message: Locator = page.locator('[data-test="error"]')
        self.complete_header: Locator = page.locator('[data-test="complete-header"]')

    def is_checkout_information_loaded(self) -> bool:
        expect(self.title_label).to_have_text("Checkout: Your Information")
        return True

    def fill_checkout_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def continue_checkout(self) -> None:
        self.continue_button.click()

    def is_checkout_overview_loaded(self) -> bool:
        expect(self.title_label).to_have_text("Checkout: Overview")
        return True

    def finish_checkout(self) -> None:
        self.finish_button.click()

    def get_error_message(self) -> str:
        expect(self.error_message).to_be_visible()
        return self.error_message.text_content() or ""

    def get_complete_header(self) -> str:
        expect(self.complete_header).to_be_visible()
        return self.complete_header.text_content() or ""