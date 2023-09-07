from selenium import webdriver
import time
import random
import pyautogui
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://www.dltkh.top/")
driver.maximize_window()
actions = ActionChains(driver)
time.sleep(2)
a=driver.find_element('xpath','//*[@id="app"]/div[2]/div[2]/div/div[1]/img[1]')

actions.move_to_element(a).perform()
a.click()
time.sleep(3)
driver.find_element("CLASS_NAME","zhibo").click()
time.sleep(2)
 # 定位百度的输入框，输入python
screenshot = pyautogui.screenshot(region=(400, 300, 980, 500))
time.sleep(3)
# 保存截图到文件
screenshot.save('screenshot.png')


import cv2

# 读取两个图像
image1 = cv2.imread('screenshot.png')
image2 = cv2.imread('Snipaste.png')

# 比较两个图像
difference = cv2.subtract(image1, image2)

# 计算差异图像的总和
sum_of_differences = difference.sum()

# 设置阈值，用于判断两个图像是否不同
threshold = 1000  # 根据需要调整阈值

# 如果总差异超过阈值，则认为图像不同（正确），否则认为图像相同（不正确）
if sum_of_differences > threshold:
    print("图像不同（正确）")
else:
    print("图像相同（不正确）")

