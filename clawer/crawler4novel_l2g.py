# -*- coding:utf-8 -*-

from selenium import webdriver
import codecs
import time

dr = webdriver.Chrome()
dr.get('http://www.5200xiaoshuo.com/6_6722/4715817.html')

while True:
    # 获取章节名字
    chap_name = dr.find_element_by_css_selector('.content_read > .box_con >.bookname > h1').text

    # 获取章节内容
    contents = dr.find_element_by_css_selector('#content').text

    # 写入文件
    with codecs.open('E:/l2g.txt', 'a+', 'utf-8') as f:
        f.write(chap_name)
        f.write(contents)
    print unicode(chap_name) + ' has finished~'
    
    # 跳转到下一页
    dr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    try:
        bot_tags = dr.find_elements_by_css_selector('.box_con > .bottem2 > a')
        next_chap = bot_tags[3]
        next_chap.click()
    except:
        break
    
dr.quit()