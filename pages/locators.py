from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    REGISTRATION_AND_LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, ".login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, ".register_form")
    #url = self.browser.current_url данный элемент был сохранён просто чтобы не потерять его:)
