from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Корзина не пуста"
    
    def basket_massage_empty(self):
        massage_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY).text
        assert "Ваша корзина пуста" in massage_empty, "Нет текста о том, что корзина пуста"