from ui.PageLocators.huanchang_page_locator import HuangchangPageLocator as  HC
from ui.Common.basepage import BasePage
class BoFang(BasePage):
    def bofang(self):
        # self.hover(HC.play,doc="悬浮播放按钮上")
        #
        # self.click(HC.zhibojian,doc="进入直播间")
        #
        # self.wait_elevisible(HC.title,doc="获取标题元素")
        #
        # text_title=self.get_element_text(HC.title,doc="获取到标题")
        #
        # return text_title
        if self.get_element_isDisplay(HC.corn):
            self.hover(HC.play,doc="悬浮播放按钮上")

            self.click(HC.zhibojian,doc="进入直播间")

            self.wait_elevisible(HC.title,doc="获取标题元素")

            text_title=self.get_element_text(HC.title,doc="获取到标题")

            return text_title

        else:
            print("没有直播")
            






