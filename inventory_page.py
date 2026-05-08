from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """
    Page Object for SauceDemo Products / Inventory Page.
    """

    # Locators
    PAGE_TITLE = (By.CLASS_NAME, "title")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "[data-test^='add-to-cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    URL = "https://www.saucedemo.com/inventory.html"

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def add_first_item_to_cart(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        if buttons:
            buttons[0].click()

    def add_item_to_cart(self, index: int = 0):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        buttons[index].click()

    def get_cart_count(self):
        try:
            return int(self.get_text(self.CART_BADGE))
        except Exception:
            return 0

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def get_all_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [e.text for e in elements]

    def get_all_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(e.text.replace("$", "")) for e in elements]

    def logout(self):
        self.click(self.BURGER_MENU)
        self.click(self.LOGOUT_LINK)
