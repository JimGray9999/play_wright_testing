from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page object for SauceDemo inventory/products page."""
    
    # Locators
    TITLE = ".title"
    INVENTORY_LIST = ".inventory_list"
    INVENTORY_ITEM = ".inventory_item"
    SHOPPING_CART_BADGE = ".shopping_cart_badge"
    SHOPPING_CART_LINK = ".shopping_cart_link"
    SORT_DROPDOWN = ".product_sort_container"
    
    # Individual product locators (using data-test attributes)
    ADD_TO_CART_BACKPACK = "[data-test='add-to-cart-sauce-labs-backpack']"
    REMOVE_BACKPACK = "[data-test='remove-sauce-labs-backpack']"
    
    def goto(self) -> None:
        """Navigate directly to inventory page."""
        self.navigate("inventory.html")
    
    def is_loaded(self) -> bool:
        """Check if inventory page is loaded."""
        return self.is_visible(self.INVENTORY_LIST)
    
    def get_page_title(self) -> str:
        """Return the page title text."""
        return self.get_text(self.TITLE)
    
    def get_item_count(self) -> int:
        """Return number of inventory items displayed."""
        return self.page.locator(self.INVENTORY_ITEM).count()
    
    def add_backpack_to_cart(self) -> None:
        """Add Sauce Labs Backpack to cart."""
        self.click(self.ADD_TO_CART_BACKPACK)
    
    def get_cart_count(self) -> str:
        """Return the cart badge count."""
        if self.is_visible(self.SHOPPING_CART_BADGE):
            return self.get_text(self.SHOPPING_CART_BADGE)
        return "0"
    
    def go_to_cart(self) -> None:
        """Click shopping cart link."""
        self.click(self.SHOPPING_CART_LINK)
    
    def expect_page_loaded(self) -> None:
        """Assert inventory page is loaded."""
        self.expect_visible(self.INVENTORY_LIST)
        self.expect_text(self.TITLE, "Products")