
from selenium import webdriver
import time

driver = webdriver.Chrome()
print("开始测试")
driver.get("https://www.dltkh.top/")
print("测试完成")
driver.maximize_window()
time.sleep(6)

