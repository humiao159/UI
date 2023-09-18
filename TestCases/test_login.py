from ui.PageObjects.login_step import LoginStep
import os, pytest, allure


class TestLogin():
    pytest.mark.smoke
    def test_login(self,access_web):
        result=LoginStep(access_web).login()
        assert result==True




if __name__ == '__main__':
    pytest.main(
        ["-s", "-v", "-m", "sj", "--html=Outputs/pytest_report/pytest.html", "--alluredir=Outputs/allure_report", '-n',
         '2'])






