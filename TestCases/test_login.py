from ui.PageObjects.login_step import LoginStep
import os, pytest, allure


class TestLogin():
    pytest.mark.smoke
    def test_login(self,access_web):
        result=LoginStep(access_web).login()
        assert result==True








