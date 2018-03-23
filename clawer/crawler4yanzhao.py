# -*- coding=utf8 -*-

'''
一个研招网调剂系统的爬虫
'''


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time

import smtplib
from email.mime.text import MIMEText
_user = '' # 填写qq邮箱
_pwd  = '' # 填写qq邮箱授权码
_to   = '' # 填写目标邮箱

msg = MIMEText("快去填志愿")
msg["Subject"] = "档案学上线啦"
msg["From"]    = _user
msg["To"]      = _to


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


while True:
    driver = webdriver.Chrome()

    # 登录模块
    username_input = go_forward(driver, r'https://account.chsi.com.cn/passport/login?entrytype=yzgr&service=https%3A%2F%2Fyz.chsi.com.cn%2Fsytj%2Fj_spring_cas_security_check', '#username')
    username_input.send_keys('')  # 替换成用户名

    password_input = driver.find_element_by_css_selector('#password')
    password_input.send_keys('')  # 替换成密码

    login_button = driver.find_element_by_css_selector('#fm1 > div.yz-pc-loginbtn > input.btn_login.yz_btn_login')
    login_button.click()

    time.sleep(10)

    # 点击缺额查询
    tj_menu = driver.find_element_by_css_selector('[data-nav="qecx"]>a')
    # tj_menu = driver.find_element_by_xpath("//a/u[contains(text(),'缺额查询')]")
    # print tj_menu.get_attribute('href')
    tj_menu.click()

    time.sleep(10)

    # 填入招生单位
    search_school = driver.find_element_by_css_selector('#dwxx')
    search_school.send_keys(u'湖北大学')

    # 填入专业
    search_major = driver.find_element_by_css_selector('#zyxx')
    search_major.send_keys(u'档案学')

    # 点击查询
    search_button = driver.find_element_by_css_selector('#tj_seach_form > table > tbody > tr > td > a.tj-btn-middle.tj-seach-btn')
    search_button.click()

    time.sleep(10)
    # 在返回结果中搜索档案学
    result_table = driver.find_element_by_css_selector('#content-qecxList>.tj-table > tbody > tr > td')
    print result_table.text
    if result_table.text == u'该条件下没有查询到缺额信息':
        print u'emmm，还是没有'
    else:
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(_user, _pwd)
            s.sendmail(_user, _to, msg.as_string())
            s.quit()
            print("Success!")
            driver.close()
            break
        except smtplib.SMTPException,e: 
            print ("Falied,%s" %e) 
    # https://blog.csdn.net/huayuhuan/article/details/76559465
    # https://github.com/anjingcuc/yzwb/blob/master/yzwb.py

    driver.close()
    time.sleep(1800)