import random
from time import sleep

from selenium import webdriver
import xlwt

import time, datetime
from page.login_page import LoginPage
from base.base_webaction import BaseAction
from page.sales_system_page import Sales_SystemPage

# def write_excel(list, sheet, save_path):
#     filter = ['--', '入门型', '1核1G', '1核2G', 'mysql5.7双机']
#     workbook = xlwt.Workbook(encoding='utf-8')
#     # 创建一个worksheet
#     worksheet = workbook.add_sheet(sheet)
#     worksheet.col(0).width = 9200
#     worksheet.col(1).width = 4500
#     worksheet.col(2).width = 2000
#     worksheet.col(3).width = 2000
#     worksheet.col(4).width = 2800
#     worksheet.col(5).width = 3000
#     # i = 0
#     # for x in new:
#     #     if i == 0:
#     #         m = 1
#     #     m = i // 7 + 1
#     #     f = i % 7
#     #     worksheet.write(m, f, label=x)
#     #     i += 1
#     i = 0
#     m = 1
#     for x in list:
#         if x not in filter:
#             worksheet.write(m, i, label=x)
#             i += 1
#             if len(x) == 10 and x.count("2020"):
#                 # if len(x) == 10 and x.count("2020") > 0:
#                 m += 1
#                 i = 0
#     t = datetime.date.today()
#     workbook.save(save_path % t)
#
#
# driver = webdriver.Chrome()
# url = "http://xinnet.com/"
# driver.get(url)
# driver.maximize_window()
# driver.implicitly_wait(20)
#
# login_page = LoginPage(driver)
# sales_system_page = Sales_SystemPage(driver)
# base_webaction = BaseAction(driver)
#
# '''账户资料-联系人管理中判断显示删除-确定按钮'''
# login_page.click_sign()
#
# login_page.input_username("17600807331")
# login_page.input_password("tianmo231")
# base_webaction.click_element(login_page.login_btn)
# base_webaction.click_element(login_page.after_login)
# base_webaction.move_to_element(login_page.kzt_cost)
# sleep(2)
# base_webaction.click_element(login_page.kzt_order)
# ret = driver.find_element_by_css_selector("#fndo-orderList").text
# new = ret.split()
# driver.quit()
#
# # new = ['A80QVLHZOJGTPQBR0EMVFING1D', 'HB3-负载均衡', '入门型', '1月', '--', '续费', '143.00', '2020-08-11',
# #        'A04JU2WN3X4TE0F2Z93HYFQYSB', '弹性IP-华北1', '1月', '--', '续费', '86.00', '2020-08-11', 'A0SY0SO8CZQSAE5ZDYH3D9988H',
# #        'HB3-云数据库', '1核1G', 'mysql5.7双机', '1月', '--', '续费', '138.00', '2020-08-11', 'A3GN4LIV0QJTWJERYIX7Z5F57I',
# #        '弹性IP-华北1', '1年', '--', '新开', '928.80', '2020-08-11', 'A5WC25KB2G0S0S4ZEEKZI14914', 'HB3-负载均衡', '入门型', '2年',
# #        '--', '新开', '2471.04', '2020-08-11', 'A8RBK5562RWRJP75U9BUX8GVZH', 'HB3-云数据库', '1核1G', 'mysql5.7双机', '1年', '--',
# #        '新开', '1703.07', '2020-08-11', 'A89C42H5HLFRYX9S4CJY1CV7US', 'HB3-云数据库', '1核1G', 'mysql5.7双机', '1年', '--', '新开',
# #        '1703.07', '2020-08-11', 'A8N7CWRYSPHSOVESX599BIGQLW', 'HB3-云数据库', '1核1G', 'mysql5.7双机', '1年', '--', '新开',
# #        '1703.07', '2020-08-11', 'A0HCGKPXWLHTWGDANYQLLX5SU3', 'NAT网关-通用型', '1月', '--', '新开', '331.40', '2020-08-04',
# #        'A276786461391192517', 'HB3-箭头云SSD', '1核2G', '1月', '--', '退费', '156.40', '2020-07-29']
# #
# write_excel(new, "退费表", 'D:\工作\新网数码\退费申请%s.xls')
# write_excel(new, "费用", 'D:\工作\新网数码\退费申请%s.xls' % t)

# # 点击账户资料按钮

# login_page.click_kzt_kzt_data()
# sleep(2)
# ret1 = base_webaction.is_displayed(login_page.account_del_determine)
# print(ret1)
# sleep(2)
# # 点击删除按钮
# base_webaction.click_element(login_page.account_delete)
# sleep(2)
# ret2 = base_webaction.is_displayed(login_page.account_del_determine)
# print(ret2)
# driver.quit()

'''云计算选购页'''
# # 点击登录按钮"
# sales_system_page.click_sign()
# # 输入用户名
# sales_system_page.input_username()
# # 输入密码
# sales_system_page.input_password()
# # 点击HY登陆页立即登录按钮
# sales_system_page.click_login_btn()
# # 登陆后点击账号连接
# sales_system_page.click_after_login()
# # 点击控制台页【箭头云】按钮
# sales_system_page.click_element(sales_system_page.kzt_arrow_cloud)
# # 点击箭头云侧边栏【云数据库】按钮
# sleep(1)
# sales_system_page.click_element(sales_system_page.cloud_database)
# # 点击箭头云侧边栏【云数据库RDS MySQL版】按钮
# sales_system_page.click_element(sales_system_page.cloud_database_mysql)
# # 点击【新建】按钮
# sales_system_page.click_element(sales_system_page.new_arrow_cloud)
# sleep(3)
# # 获取购买年限
# years = [".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[1]",
#          ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[2]",
#          ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[3]",
#          ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[4]",
#          ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[5]",
#          ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[6]",
#          ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[7]",
#          ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[8]",
#          ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[9]",
#          ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[10]",
#          ".//*[@id='main']/div/div[1]/div/div[2]/div/div[8]/div[2]/div/button[11]"
#          ]
#
# element = random.choice(years)
# print(element)
# base_webaction.slide_up_down(0, 900)
# sleep(1)
# sales_system_page.click_element(element)
# sleep(1)
# # 点击【前往结算】按钮
# # sales_system_page.click_element(sales_system_page.settlement)
# # driver.quit()

# a = [1, 3, 6, 8, 12, 555, 666, 77]
# b = [1, 2, 4, 6, 7, 5, 8, 5, 12, 66, 44, 333, 88, 444]
# c = [x for x in a if x in b]
# d = [y for y in (a + b) if y not in c]
# print(c)
# print(d)