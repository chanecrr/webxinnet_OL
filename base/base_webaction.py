# coding:utf-8
import os
import sys

from selenium.webdriver import ActionChains

sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    # 找元素
    def wait_element(self, element):
        ele = WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located(element))
        return ele

    # 找多元素
    def wait_elements(self, element):
        ele = WebDriverWait(self.driver, 20, 1).until(EC.presence_of_all_elements_located(element))
        return ele

    # 点击元素
    def click_element(self, element):
        click = self.wait_element(element).click()
        return click

    # 点多击元素
    def click_elements(self, element, sub):
        click = self.wait_elements(element)[sub].click()
        return click

    #  输入内容
    def send_key(self, element, text):
        tex = self.wait_element(element).send_keys(text)
        return tex

    # 清除元素
    def clear_element(self, element):
        clear = self.wait_element(element).clear()
        return clear

    # 查找页面元素是否存在
    def is_toast_exist(self, text, timeout=20, poll_frequency=0.5):
        try:
            ele = By.XPATH, ".//*[text()='%s']" % text
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(ele))
            return True
        except:
            return False

    # 判断元素是否可见
    def is_displayed(self, element):
        ret = self.wait_element(element).is_displayed()
        return ret

    # 警告窗处理
    def swich_to_alert(self, status="agree"):
        alert = self.driver.switch_to.alert
        ret = status
        if ret == "agree":
            alert.accept()
        elif ret == "cancel":
            alert.dismiss()
        else:
            print("请输入同意：agree或取消：cancel")

    # 上下滑动滚动条
    def slide_up_down(self, up=0, down=700):
        scroll = "window.scrollTo(%d, %d)" % (up, down)
        self.driver.execute_script(scroll)

    # 获取当前句柄
    def current_handle(self):
        current = self.driver.current_window_handle
        return current

    # 获取全部句柄,并切换至最新句柄
    def handles_handle(self, window):
        handles = self.driver.window_handles
        for x in handles:
            if x != window:
                self.driver.switch_to.window(x)

    # 截图
    def screenshot(self, file_name):
        self.driver.get_screenshot_as_file("./screen/" + file_name + ".png")

    # 鼠标悬停
    def move_to_element(self, ele):
        ret = self.wait_element(ele)
        ActionChains(self.driver).move_to_element(ret).perform()
