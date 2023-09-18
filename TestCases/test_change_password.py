from ui.PageObjects.change_password_step import ChangePw
import pytest,os,allure

@allure.feature("直播间")
class TestPassword():
    @allure.story("获取标题")
    def test_pw(self,login_web):
        ChangePw(login_web).change()




