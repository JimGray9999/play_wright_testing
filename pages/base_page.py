from playwright.sync_api import Page, expect
from config.settings import settings


class BasePage:
    """Base class for all page objects."""
    
    def __init__(self, page: Page):
        self.page = page
        self.timeout = settings.timeout
    
    def navigate(self, path: str = "") -> None:
        """Navigate to a path relative to base URL."""
        url = f"{settings.base_url}/{path}".rstrip("/")
        self.page.goto(url)
    
    def get_title(self) -> str:
        """Return the page title."""
        return self.page.title()
    
    def get_url(self) -> str:
        """Return the current URL."""
        return self.page.url
    
    def wait_for_page_load(self) -> None:
        """Wait for page to reach load state."""
        self.page.wait_for_load_state("networkidle")
    
    def take_screenshot(self, name: str) -> None:
        """Capture screenshot with given name."""
        self.page.screenshot(path=f"screenshots/{name}.png")
    
    def click(self, locator: str) -> None:
        """Click an element."""
        self.page.locator(locator).click()
    
    def fill(self, locator: str, text: str) -> None:
        """Fill a text input."""
        self.page.locator(locator).fill(text)
    
    def get_text(self, locator: str) -> str:
        """Get text content of an element."""
        return self.page.locator(locator).text_content() or ""
    
    def is_visible(self, locator: str) -> bool:
        """Check if element is visible."""
        return self.page.locator(locator).is_visible()
    
    def wait_for_element(self, locator: str, state: str = "visible") -> None:
        """Wait for element to reach specified state."""
        self.page.locator(locator).wait_for(state=state, timeout=self.timeout)
    
    def expect_visible(self, locator: str) -> None:
        """Assert element is visible using Playwright's expect."""
        expect(self.page.locator(locator)).to_be_visible()
    
    def expect_text(self, locator: str, text: str) -> None:
        """Assert element contains expected text."""
        expect(self.page.locator(locator)).to_have_text(text)
    
    def expect_url_contains(self, text: str) -> None:
        """Assert URL contains expected text."""
        expect(self.page).to_have_url(f".*{text}.*")