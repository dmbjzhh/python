# -*- coding:utf-8 -*-

# from selenium import webdriver
import codecs
# import time

# dr = webdriver.Chrome()
# dr.get('http://www.jjwxc.net/onebook.php?novelid=2109567&chapterid=1')

# while True:
#     # 获取章节名字
#     chap_name = dr.find_element_by_css_selector('.novelbody > .noveltext > div > h2').text

#     # 获取章节内容
#     contents = dr.find_element_by_css_selector('.novelbody > .noveltext').text

#     # 写入文件
#     with codecs.open('E:/sci5.txt', 'a+', 'utf-8') as f:
#         f.write(contents)
#     print unicode(chap_name) + ' has finished~'
    
#     # 跳转到下一页
#     dr.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
#     try:
#         next_chap = dr.find_elements_by_css_selector('.noveltitle > span > a')
#         if len(next_chap) == 1:
#             next_chap[0].click()
#         else:
#             next_chap[1].click()
#     except:
#         break
    
# dr.quit()

# 打开旧文件
f = codecs.open('E:/sci5.txt','r','utf-8')

# 打开新文件
f_new = codecs.open('E:/sci5_new.txt','w','utf-8')

# 循环读取旧文件
for line in f:
    # 进行判断
    if u"插入书签" in line:
        line = line.replace(u'插入书签','')
    if u"[收藏此章节]　[下载]  [免费得晋江币] [举报]" in line:
        line = line.replace(u'[收藏此章节]　[下载]  [免费得晋江币] [举报] ', '')
    # 如果不符合就正常的将文件中的内容读取并且输出到新文件中
    f_new.write(line)

f.close()
f_new.close()