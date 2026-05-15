from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url

    def open(self, path: str = "") -> None:
        self.page.goto(f"{self.base_url}{path}")

    def get_title(self) -> str:
        return self.page.title()

    def get_current_url(self) -> str:
        return self.page.url

    def wait_for_url_contains(self, value: str) -> None:
        expect(self.page).to_have_url(lambda url: value in url)
