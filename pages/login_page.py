from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page object for SauceDemo login page."""
    
    # Locators
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    
    def goto(self) -> None:
        """Navigate to login page."""
        self.navigate()
    
    def login(self, username: str, password: str) -> None:
        """Perform login with given credentials."""
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self) -> str:
        """Return the error message text if present."""
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self) -> bool:
        """Check if error message is visible."""
        return self.is_visible(self.ERROR_MESSAGE)
    
    def expect_error_message(self, expected_text: str) -> None:
        """Assert error message contains expected text."""
        self.expect_text(self.ERROR_MESSAGE, expected_text)