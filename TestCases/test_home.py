import os, pytest, allure

from ui.PageObjects.bofang_step import BoFang

@allure.feature("直播间")

class TestEnter():
    @allure.story("获取标题")
    def test_bofang(self,access_web):
        result=BoFang(access_web).bofang()
        assert result=='FC岐阜 VS 宫崎棒牛鸟'


