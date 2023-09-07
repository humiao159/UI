
from selenium import webdriver
import time
import random
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.dltkh.top/liveTwo?Match_Id=4288246")
driver.maximize_window()
time.sleep(3)
a=driver.find_element('xpath','//*[@id="app"]/div[2]/div/div[2]/div/div[3]/div[1]/div/div[1]').text
print(a)

