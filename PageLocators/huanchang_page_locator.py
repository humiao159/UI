from  selenium.webdriver.common.by import By



class HuangchangPageLocator:


    #首页播放按钮
    play=(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/img[1]')

    #播放器内置播放按钮
    bofangqi=(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/div[4]/div[1]/img')

    #进入直播间
    zhibojian=(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[1]/div[3]')

    #侧边栏，可以判断是否有比赛
    corn=(By.XPATH,'//*[@id="app"]/div[2]/div[2]/div/div[2]/ul/li[1]/img')

    #获取直播间标题
    title=(By.XPATH,'//*[@id="app"]/div[2]/div/div[2]/div/div[3]/div[1]/div/div[1]')




