import pytest, time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def access_web():
    desired_capabilities = DesiredCapabilities.CHROME
    # 注释这两行会导致最后输出结果的延迟，即等待页面加载完成再输出
    desired_capabilities["pageLoadStrategy"] = "none"
    # 实例化对象
    driver = webdriver.Chrome()
    # 访问网址
    driver.get("https://www.kty296.com/pc2/#/home/index")
    # 窗口最大化
    driver.maximize_window()
    # 等待
    time.sleep(10)
    #处理弹框
    driver.find_element(By.XPATH,'//*[@id="app"]/div/div/section/div/div[1]/div/div/div[2]/div/div/button[1]').click()
    # 返回对象
    yield driver
    time.sleep(5)
    # 后置：关闭浏览器
    driver.quit()

@pytest.fixture
def refresh(access_web):
    yield access_web
    # 刷新页面
    access_web.refresh()
    # 操作1
    # access_web.find_element(*LP.s).click()
    # 操作2
    # access_web.find_element(*LP.che).click()
    time.sleep(1)


def pytest_configure(config):
    config.addinivalue_line("markers", 'smoke')
    config.addinivalue_line("markers", 'P0')
    config.addinivalue_line("markers", 'P1')
