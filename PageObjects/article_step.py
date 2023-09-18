from ui.Common.basepage import BasePage

from ui.PageLocators.article_page_locator import ArticlePagelocator as ZX


class Zixun(BasePage):
    def is_exsit_zixun(self):
        # self.hover(ZX.zixun,doc="悬浮播放按钮上")
        self.click(ZX.zixun,doc="进入资讯")
        self.click(ZX.frist_title,doc="进入详情")
        self.switch_window()
        text=self.get_element_text(ZX.xiangqing, doc="获取标题")

        # a=self.get_element_isDisplay(zx.frist_title,"判断是否有文章")

        return text


    def same_title(self):
        text = self.get_element_text(ZX.frist_title, doc="获取标题")
        self.click(ZX.frist_title,doc="进入文章详情")
        lasttext=self.get_element_text(ZX.xiangqing,doc="获取详情标题")
        if text==lasttext:
            return True
        else:
            False





    #判断是否有资讯文章

    #     if self.get_element_isDisplay(zx.frist_title,"判断是否有文章") :
    #
    # #获取资讯标题
    #         text=self.get_element_text(zx.frist_title,doc="获取标题")
    #         return text
    #     else:
    #
    #         return