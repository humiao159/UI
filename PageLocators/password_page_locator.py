from selenium.webdriver.common.by import By


class PasswordPage:

    url= '/pc2/#/personalCenter/amendPassword'

    #原密码
    old_password=(By.XPATH,'//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/section/div/div[2]/div/form/div[1]/div/div[1]/input')
    old_password_value='1qaz2wsx'

    #新密码

    new_password=(By.XPATH,'//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/section/div/div[2]/div/form/div[2]/div/div/input')
    new_password_value='qaz159357'
    #确认密码

    confirm_password=(By.XPATH,'/html/body/div[1]/div/div/section/div/div[2]/div/div[2]/section/div/div[2]/div/form/div[3]/div/div/input')
    confirm_password_value='qaz159357'
    #确认修改

    confirm_button=(By.XPATH,'//*[@id="app"]/div/div/section/div/div[2]/div/div[2]/section/div/div[2]/div/form/div[4]/div/button')






