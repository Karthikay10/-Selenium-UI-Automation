from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os


class BasePage:
    """
    Base class for all Page Objects.
    Contains reusable helper methods for interacting with web elements.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find(locator).text

    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def take_screenshot(self, name="screenshot"):
        os.makedirs("reports/screenshots", exist_ok=True)
        path = f"reports/screenshots/{name}.png"
        self.driver.save_screenshot(path)
        return path
