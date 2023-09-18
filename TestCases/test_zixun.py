from ui.PageObjects.article_step import  Zixun

import pytest,allure,os

@allure.feature("直播间")
class Test_zixun():
    def test_zixun(self,access_web):
        a=Zixun(access_web).is_exsit_zixun()
        assert a=='U15东亚杯决赛-中国U15点球大战4-2日本U15夺冠'





