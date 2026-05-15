from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.username_input: Locator = page.locator('[data-test="username"]')
        self.password_input: Locator = page.locator('[data-test="password"]')
        self.login_button: Locator = page.locator('[data-test="login-button"]')
        self.error_message: Locator = page.locator('[data-test="error"]')

    def open(self) -> None:
        super().open()

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def login_without_username(self, password: str) -> None:
        self.username_input.fill("")
        self.password_input.fill(password)
        self.login_button.click()

    def login_without_password(self, username: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill("")
        self.login_button.click()

    def get_error_message(self) -> str:
        expect(self.error_message).to_be_visible()
        return self.error_message.text_content() or ""