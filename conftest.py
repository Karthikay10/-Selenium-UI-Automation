import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    """
    Sets up Chrome WebDriver in headless mode for each test.
    Quits after each test to ensure isolation.
    """
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    yield driver

    driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """
    Fixture that provides an already logged-in driver session.
    """
    from pages.login_page import LoginPage
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    yield driver
