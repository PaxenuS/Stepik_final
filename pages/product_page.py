from .base_page import BasePage
from .locators import ProductPageLocator
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_basket(self):
        add_basket = self.browser.find_element(*ProductPageLocator.ADD_BASKET)
        add_basket.click()

    def check_add_product(self):
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT_NAME).text
        add_product_name = self.browser.find_element(*ProductPageLocator.ADD_PRODUCT_NAME).text
        assert product_name == add_product_name, "Товар не был добавлен в корзину"

    def check_price(self):
        price = self.browser.find_element(*ProductPageLocator.PRICE).text
        add_price = self.browser.find_element(*ProductPageLocator.ADD_PRICE).text
        assert price == add_price, "Цена товара, не совпадает с ценой в корзине"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocator.SUCCESS_MESSAGE),\
        "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocator.SUCCESS_MESSAGE),\
        "Success message is not disppeared"