import pytest
from playwright.sync_api import Page, Browser, BrowserContext
from dotenv import load_dotenv

from config.settings import settings
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# Load environment variables from .env file
load_dotenv()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Override default browser context arguments."""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
    }


@pytest.fixture(scope="function")
def login_page(page: Page) -> LoginPage:
    """Provide a LoginPage instance."""
    return LoginPage(page)


@pytest.fixture(scope="function")
def inventory_page(page: Page) -> InventoryPage:
    """Provide an InventoryPage instance."""
    return InventoryPage(page)


@pytest.fixture(scope="function")
def logged_in_page(page: Page) -> Page:
    """Provide a page that's already logged in as standard user."""
    login = LoginPage(page)
    login.goto()
    login.login(settings.standard_user, settings.default_password)
    
    # Verify login succeeded
    inventory = InventoryPage(page)
    inventory.expect_page_loaded()
    
    return page


@pytest.fixture(scope="function")
def logged_in_inventory(logged_in_page: Page) -> InventoryPage:
    """Provide an InventoryPage instance that's already logged in."""
    return InventoryPage(logged_in_page)