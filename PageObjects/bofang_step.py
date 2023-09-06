from ui.PageLocators.huanchang_page_locator import HuangchangPageLocator as  HC
from ui.Common.basepage import BasePage
class BoFang(BasePage):
    def bofang(self):
        self.stay(HC.play,doc="悬浮播放按钮上")

        self.click(HC.zhibojian,doc="进入直播间")

        text_title=self.get_element_text(HC.title,"获取到标题")

        return text_title



