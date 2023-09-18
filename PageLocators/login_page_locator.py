from selenium.webdriver.common.by import By


class Login:

    login=(By.XPATH,'//*[@id="app"]/div/div/div[1]/header/div/div[2]/div[2]/div/form/div/div/button[1]/span')


    username=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/form/div[1]/div/div/div/input')
    username_value='ontest'

    password=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/form/div[2]/div/div/div/input')
    password_value='qaz159357'

    confim_button=(By.XPATH,'//*[@id="app"]/div/div[1]/div[2]/div[1]/form/div[4]/div/button')

    name=(By.XPATH,'//*[@id="app"]/div/div/div[1]/header/div/div[2]/div[2]/div[1]/div/span/div/img')



