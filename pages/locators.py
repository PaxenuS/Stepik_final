from selenium.webdriver.common.by import By
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")

class MainPageLocators():
    pass
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_R = (By.CSS_SELECTOR, "#id_registration-password2")
    BOTTON = (By.CSS_SELECTOR, "#register_form > button:nth-child(7)")

class ProductPageLocator():
    ADD_BASKET = (By.CSS_SELECTOR, "button.btn-lg:nth-child(3)")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6:nth-child(2) > h1:nth-child(1)")
    ADD_PRODUCT_NAME = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)")
    PRICE = (By.CSS_SELECTOR, "p.price_color:nth-child(2)")
    ADD_PRICE = (By.CSS_SELECTOR, "div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) > div:nth-child(2)")
