from ui.PageLocators.password_page_locator import  PasswordPage as ps

from ui.Common.basepage import BasePage

from ui.Common.keep_strong import KeepStrong

class ChangePw(BasePage):
    def change(self):
        self.baseurl=KeepStrong().get_url()
        print(self.baseurl)
        self.path=ps.url
        self.url_all=self.baseurl + self.path
        self.open_url(self.url_all)


        self.input_text(ps.old_password,ps.old_password_value)
        self.input_text(ps.new_password,ps.new_password_value)
        self.input_text(ps.confirm_password,ps.confirm_password_value)
        self.click(ps.confirm_button)
    def revert(self):
        self.driver.get()










