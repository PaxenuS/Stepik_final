from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocator():
    ADD_BASKET = (By.CSS_SELECTOR, "button.btn-lg:nth-child(3)")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    ADD_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)")
    PRICE = (By.CSS_SELECTOR, "p.price_color:nth-child(2)")
    ADD_PRICE = (By.CSS_SELECTOR, "div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)")
