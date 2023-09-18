
from selenium import webdriver
import time
import random
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.dltkh.top/")
driver.maximize_window()
time.sleep(3)
a=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div[4]')
a.click()
time.sleep(6)

