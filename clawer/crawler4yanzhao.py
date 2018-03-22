# -*- coding=utf8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


def go_forward(d, url, css_selector):
    while True:
        d.get(url)

        try:
            element = WebDriverWait(d, 1).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
            )

            if url == d.current_url:
                return element

        except TimeoutException:
            continue


driver = webdriver.Chrome()

# 登录模块
username_input = go_forward(driver, 'https://account.chsi.com.cn/passport/login?entrytype=yzgr&service=https%3A%2F%2Fyz.chsi.com.cn%2Fsytj%2Fj_spring_cas_security_check', '#username')
username_input.send_keys('')  # 替换成用户名

password_input = driver.find_element_by_css_selector('#password')
password_input.send_keys('')  # 替换成密码

login_button = driver.find_element_by_css_selector('#fm1 > div.yz-pc-loginbtn > input.btn_login.yz_btn_login')
login_button.click()

# 点击缺额查询
tj_menu = driver.find_element_by_css_selector('[data-nav="qecx"]')
tj_menu.click()

# 填入招生单位
search_school = driver.find_element_by_id('dwxx')
search_school.send_keys('湖北大学')

# 点击查询
search_button = driver.find_element_by_css_selector('#tj_seach_form > table > tbody > tr > td.text-c > a.tj-btn-middle.tj-seach-btn')
search_button.click()

# 在返回结果中搜索档案学
result_table = driver.find_element_by_css_selector('#content-qecxList > table.tj-table > tbody')
# https://blog.csdn.net/huayuhuan/article/details/76559465
# https://github.com/anjingcuc/yzwb/blob/master/yzwb.py