from typing import Generator

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, Playwright, sync_playwright


@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://www.saucedemo.com/"


@pytest.fixture(scope="session")
def standard_user() -> str:
    return "standard_user"


@pytest.fixture(scope="session")
def locked_out_user() -> str:
    return "locked_out_user"


@pytest.fixture(scope="session")
def password() -> str:
    return "secret_sauce"


@pytest.fixture(scope="session")
def playwright_instance() -> Generator[Playwright, None, None]:
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Generator[Browser, None, None]:
    browser = playwright_instance.chromium.launch(headless=False)
    yield browser
    browser.close()


@pytest.fixture()
def context(browser: Browser) -> Generator[BrowserContext, None, None]:
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    yield context
    context.close()


@pytest.fixture()
def page(context: BrowserContext) -> Generator[Page, None, None]:
    page = context.new_page()
    yield page
    page.close()