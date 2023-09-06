from selenium import webdriver
import time
import random
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.dltkh.top/")
driver.maximize_window()
time.sleep(3)

 # 定位百度的输入框，输入python
screenshot = pyautogui.screenshot(region=(400, 300, 980, 500))

# 保存截图到文件
screenshot.save('Snipaste.png')
time.sleep(5)






