import time

from ui.PageLocators.login_page_locator import Login
from ui.Common.basepage import BasePage


class LoginStep(BasePage):
    def login(self):
        self.click(Login.login)
        self.input_text(Login.username,Login.username_value)
        self.input_text(Login.password,Login.password_value)
        self.click(Login.confim_button)
        time.sleep(8)
        result=self.is_element_exsits(Login.name)
        return result