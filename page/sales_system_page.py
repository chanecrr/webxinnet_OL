# coding:utf-8
import os
import random
import sys
from time import sleep

sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page.login_page import LoginPage


class Sales_SystemPage(LoginPage):
    """控制台-箭头云-云服务器ECS"""
    # 箭头云【新建】按钮
    new_arrow_cloud = By.XPATH, ".//*[@id='main']/div/div[1]/div/div[2]/div[1]/div/div[1]/div/a"

    # 箭头云侧边栏【云服务器ECS】按钮
    cloud_server = By.XPATH, ".//*[@id='main']/div/div[1]/nav/ul/li[1]/ul/li[1]/a"

    # 箭头云侧边栏【云数据库】按钮
    cloud_database = By.XPATH, ".//*[@id='main']/div/div[1]/nav/ul/li[2]/a"

    # 箭头云侧边栏【云数据库RDS MySQL版】按钮
    cloud_database_mysql = By.XPATH, ".//*[@id='main']/div/div[1]/nav/ul/li[2]/ul/li[1]/a"

    # 箭头云【前往结算】按钮
    settlement = By.CSS_SELECTOR, ".fwQVGNAtQ7wiXuxJ7K3Zg.btn.btn-primary.ladda-button"

    """确认订单页"""
    # 确认订单页【协议】勾选框
    confirm_order = By.CSS_SELECTOR, "#choose"

    # 确认订单页【去结算】按钮
    confirm_settlement = By.CSS_SELECTOR, "#toSettle"

    """付款页"""
    # 付款页【余额支付】按钮
    balance_payment = By.CSS_SELECTOR, ".btn.btn-primary.pay1"
