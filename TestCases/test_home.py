import os, pytest, allure

from ui.PageObjects.bofang_step import BoFang

@allure.feature("直播间")
class Enter():
    @allure.story("获取标题")
    def test_bofang(self,refresh):
        result=BoFang(refresh).bofang()
        assert result=='所罗门U23 VS 斐济U23'

