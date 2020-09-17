import os
import random
import sys
from time import sleep

sys.path.append(os.getcwd())
import pytest
import allure

from selenium import webdriver
from page.sales_system_page import Sales_SystemPage
from base.base_webaction import BaseAction
from base.base_yml import yml_data_with_file


def data_with_key(key):
    return yml_data_with_file("sales_system_data", key)


class Testsales_system:

    def setup(self):
        self.driver = webdriver.Chrome()
        url = "http://xinnet.com/"
        self.driver.get(url)
        self.driver.maximize_window()
        self.sales_system_page = Sales_SystemPage(self.driver)
        self.base_webaction = BaseAction(self.driver)
        self.driver.implicitly_wait(20)
        # self.login_page.click_btncloseadv()

    # # @pytest.mark.run(order=8)
    # # @pytest.mark.skipif(True, reason="done")
    # @allure.step(title="箭头云新购")
    # @pytest.mark.parametrize("args", data_with_key("test_Buy_Cloud_Computing"))
    # def test_Buy_Cloud_Computing(self, args):
    #     title = args["title"]
    #     screen = args["screen"]
    #     hover = args["hover"]
    #     username = args["username"]
    #     password = args["password"]
    #     label = args["label"]
    #     description = args["description"]
    #     element = args["element"]
    #     label2 = args["label2"]
    #     description2 = args["description2"]
    #     element2 = args["element2"]
    #     label3 = args["label3"]
    #     description3 = args["description3"]
    #     element3 = args["element3"]
    #     exist = args["exist"]
    #
    #     allure.attach("", "标题：" + title)
    #     allure.attach("", "用例编号：" + screen)
    #     allure.attach("", "点击登录按钮")
    #     self.sales_system_page.click_sign()
    #     allure.attach("", "输入：" + username)
    #     self.sales_system_page.input_username(username)
    #     allure.attach("", "输入：" + password)
    #     self.sales_system_page.input_password(password)
    #     allure.attach("", "点击HY登陆页立即登录按钮")
    #     self.sales_system_page.click_login_btn()
    #     allure.attach("", "点击账号连接")
    #     self.sales_system_page.click_after_login()
    #     allure.attach("", "点击控制台页【箭头云】按钮")
    #     self.sales_system_page.click_element(self.sales_system_page.kzt_arrow_cloud)
    #     # 点击箭头云侧边栏【云服务器ECS】按钮
    #     sleep(2)
    #     allure.attach("", "点击" + description)
    #     self.sales_system_page.click_css_xapth(label, element)
    #     # 点击箭头云【新建】按钮
    #     allure.attach("", "点击" + description2)
    #     self.sales_system_page.click_css_xapth(label2, element2)
    #     # 点击【前往结算】按钮
    #     allure.attach("", "点击" + description3)
    #     self.sales_system_page.click_css_xapth(label3, element3)
    #     allure.attach("", "点击确认订单页【协议】勾选框")
    #     sleep(1)
    #     self.sales_system_page.click_element(self.sales_system_page.confirm_order)
    #     allure.attach("", "点击确认订单页【去结算】按钮")
    #     self.sales_system_page.click_element(self.sales_system_page.confirm_settlement)
    #
    #     try:
    #         allure.attach("", "校验页面元素是否包含：" + exist)
    #         assert self.base_webaction.is_toast_exist(exist)
    #         # self.base_webaction.screenshot(screen)
    #         # self.base_webaction.allure_attachment_type(screen, "结果截图")
    #         self.driver.quit()
    #
    #     except Exception as msg:
    #         self.base_webaction.screenshot(screen)
    #         self.base_webaction.allure_attachment_type(screen, "结果截图")
    #         print('测试Fail,异常原因:', msg)
    #         self.driver.quit()
    #         assert False

    # # @pytest.mark.run(order=9)
    # # @pytest.mark.skipif(True, reason="done")
    # # @pytest.mark.repeat(5)
    # @allure.step(title="云计算mysql新购")
    # @pytest.mark.parametrize("args", data_with_key("test_Buy_Cloud_Mysql"))
    # def test_Buy_Cloud_Mysql(self, args):
    #     title = args["title"]
    #     screen = args["screen"]
    #     hover = args["hover"]
    #     username = args["username"]
    #     password = args["password"]
    #     label = args["label"]
    #     description = args["description"]
    #     element = args["element"]
    #     label2 = args["label2"]
    #     description2 = args["description2"]
    #     element2 = args["element2"]
    #     label3 = args["label3"]
    #     description3 = args["description3"]
    #     element3 = args["element3"]
    #     label4 = args["label4"]
    #     description4 = args["description4"]
    #     element4 = args["element4"]
    #     exist = args["exist"]
    #     years = [".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[1]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[2]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[3]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[4]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[5]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[6]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[7]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[8]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[9]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[10]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[11]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[12]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[13]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[14]",
    #              ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[15]",
    #              ]
    #     ret = random.choice(years)
    #
    #     allure.attach("", "标题：" + title)
    #     allure.attach("", "用例编号：" + screen)
    #     allure.attach("", "点击登录按钮")
    #     self.sales_system_page.click_sign()
    #     allure.attach("", "输入：" + username)
    #     self.sales_system_page.input_username(username)
    #     allure.attach("", "输入：" + password)
    #     self.sales_system_page.input_password(password)
    #     allure.attach("", "点击HY登陆页立即登录按钮")
    #     self.sales_system_page.click_login_btn()
    #     allure.attach("", "点击账号连接")
    #     self.sales_system_page.click_after_login()
    #     allure.attach("", "点击控制台页【箭头云】按钮")
    #     self.sales_system_page.click_element(self.sales_system_page.kzt_arrow_cloud)
    #     # 点击箭头云侧边栏【云数据库】按钮
    #     sleep(1)
    #     allure.attach("", "点击" + description)
    #     self.sales_system_page.click_css_xapth(label, element)
    #     # 点击箭头云侧边栏【云数据库RDS MySQL版】按钮
    #     allure.attach("", "点击" + description2)
    #     self.sales_system_page.click_css_xapth(label2, element2)
    #     # 点击【新建】按钮
    #     self.driver.refresh()
    #     allure.attach("", "点击" + description3)
    #     self.sales_system_page.click_css_xapth(label3, element3)
    #     # 向下滑动
    #     sleep(1)
    #     self.base_webaction.slide_up_down(0, 950)
    #     # 随机选择年限
    #     print(ret)
    #     sleep(1)
    #     self.driver.find_element_by_xpath(ret).click()
    #     # 点击【前往结算】按钮
    #     # self.driver.refresh()
    #     # print("刷新")
    #     sleep(1)
    #     allure.attach("", "点击" + description4)
    #     self.sales_system_page.click_css_xapth(label4, element4)
    #     allure.attach("", "点击确认订单页【协议】勾选框")
    #     sleep(1)
    #     self.sales_system_page.click_element(self.sales_system_page.confirm_order)
    #     allure.attach("", "点击确认订单页【去结算】按钮")
    #     self.sales_system_page.click_element(self.sales_system_page.confirm_settlement)
    #
    #     try:
    #         allure.attach("", "校验页面元素是否包含：" + exist)
    #         assert self.base_webaction.is_toast_exist(exist)
    #         # self.base_webaction.screenshot(screen)
    #         # self.base_webaction.allure_attachment_type(screen, "结果截图")
    #         self.driver.quit()
    #
    #     except Exception as msg:
    #         self.base_webaction.screenshot(screen)
    #         self.base_webaction.allure_attachment_type(screen, "结果截图")
    #         print('测试Fail,异常原因:', msg)
    #         self.driver.quit()
    #         assert False
