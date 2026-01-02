import pytest
from config.settings import settings
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:
    """Test suite for login functionality."""
    
    @pytest.mark.smoke
    def test_valid_login(self, login_page: LoginPage, page):
        """Verify standard user can log in successfully."""
        login_page.goto()
        login_page.login(settings.standard_user, settings.default_password)
        
        inventory = InventoryPage(page)
        inventory.expect_page_loaded()
    
    @pytest.mark.smoke
    def test_locked_out_user(self, login_page: LoginPage):
        """Verify locked out user sees appropriate error."""
        login_page.goto()
        login_page.login(settings.locked_out_user, settings.default_password)
        
        login_page.expect_error_message("Epic sadface: Sorry, this user has been locked out.")
    
    @pytest.mark.regression
    def test_invalid_password(self, login_page: LoginPage):
        """Verify invalid password shows error."""
        login_page.goto()
        login_page.login(settings.standard_user, "wrong_password")
        
        login_page.expect_error_message("Epic sadface: Username and password do not match any user in this service")
    
    @pytest.mark.regression
    def test_empty_username(self, login_page: LoginPage):
        """Verify empty username shows error."""
        login_page.goto()
        login_page.login("", settings.default_password)
        
        login_page.expect_error_message("Epic sadface: Username is required")
    
    @pytest.mark.regression
    def test_empty_password(self, login_page: LoginPage):
        """Verify empty password shows error."""
        login_page.goto()
        login_page.login(settings.standard_user, "")
        
        login_page.expect_error_message("Epic sadface: Password is required")