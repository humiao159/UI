import os, pytest, allure

from ui.PageObjects.bofang_step import BoFang

@allure.feature("直播间")

class TestEnter():
    @allure.story("获取标题")
    def test_bofang(self,access_web):
        result=BoFang(access_web).bofang()
        assert result=='温哈努FC VS 奇文岛FC'

