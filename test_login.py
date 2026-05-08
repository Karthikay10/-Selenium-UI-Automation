import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


class TestLogin:
    """UI test cases for Login functionality on SauceDemo."""

    def test_valid_login(self, driver):
        """TC001 - Valid credentials redirects to inventory page."""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        assert "inventory" in driver.current_url, "Login failed — inventory page not loaded"

    def test_page_title_after_login(self, driver):
        """TC002 - Page title after login shows 'Products'."""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "secret_sauce")
        inventory = InventoryPage(driver)
        assert inventory.get_page_title() == "Products"

    def test_invalid_password(self, driver):
        """TC003 - Wrong password shows error message."""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "wrongpassword")
        assert login.is_error_displayed(), "Error message not shown for invalid password"

    def test_invalid_username(self, driver):
        """TC004 - Wrong username shows error message."""
        login = LoginPage(driver)
        login.open()
        login.login("unknown_user", "secret_sauce")
        assert login.is_error_displayed()

    def test_empty_username(self, driver):
        """TC005 - Empty username shows error."""
        login = LoginPage(driver)
        login.open()
        login.login("", "secret_sauce")
        assert login.is_error_displayed()
        assert "Username is required" in login.get_error_message()

    def test_empty_password(self, driver):
        """TC006 - Empty password shows error."""
        login = LoginPage(driver)
        login.open()
        login.login("standard_user", "")
        assert login.is_error_displayed()
        assert "Password is required" in login.get_error_message()

    def test_locked_out_user(self, driver):
        """TC007 - Locked out user shows specific error."""
        login = LoginPage(driver)
        login.open()
        login.login("locked_out_user", "secret_sauce")
        error = login.get_error_message()
        assert "locked out" in error.lower()

    def test_login_page_title(self, driver):
        """TC008 - Login page browser title is correct."""
        login = LoginPage(driver)
        login.open()
        assert "Swag Labs" in driver.title

    def test_login_page_url(self, driver):
        """TC009 - Login page URL is correct."""
        login = LoginPage(driver)
        login.open()
        assert "saucedemo.com" in driver.current_url

    @pytest.mark.parametrize("username, password", [
        ("standard_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ])
    def test_multiple_valid_users(self, driver, username, password):
        """TC010-TC011 - Multiple valid users can log in."""
        login = LoginPage(driver)
        login.open()
        login.login(username, password)
        assert "inventory" in driver.current_url
