from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_promo()
        self.should_be_cart_button()
        self.go_to_cart()

    def should_be_promo(self):
        assert "?promo=newYear" in self.url, "promo is not in url"
        assert True

    def should_be_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Cart button is not presented"
        assert True

    def go_to_cart(self):
        cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        cart_button.click()
