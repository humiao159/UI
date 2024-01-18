
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
print("开始测试")
driver.get("https://www.baidu.com/")
driver.find_element(By.ID,'kw').send_keys('taobao')
print("测试完成")
driver.maximize_window()
time.sleep(6)

