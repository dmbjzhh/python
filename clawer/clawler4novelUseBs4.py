# -*- coding:utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup
import re


txtFile = open("./龙图案卷集续.txt", "w") # 小说文件

baseUrl = r"https://www.yn388.com/book/4201/r3YuBskcyBBYH.html" # 小说基础链接，和?page=x形成当前章节完整链接
# 存储待访问的章节地址
chapUrls = [baseUrl]

# 伪造浏览器
headers = {
    "User-Agent": r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}

count = 1 # 章节计数器

# 如果下一章不为空就一直获取下一章内容
while len(chapUrls) != 0:
    url = chapUrls.pop(0)
    # page不是固定的从1到6，因此需要根据章标题确认有多少页
    tempUrl = url
    req = request.Request(url=tempUrl, headers=headers)
    res = request.urlopen(req)
    pageHtml = res.read().decode("utf-8")
    soup = BeautifulSoup(pageHtml, "lxml")
    title = soup.find("h1").string
    title = title.strip()
    strTemp = re.findall(r".*\(1/(.*)\).*", title)
    if len(strTemp) != 0:
        pageNum = int(strTemp[0])
    else:
        break

    # 每一章都分为page1到pageNum
    for i in range(1, pageNum+1):
        tempUrl = url
        tempUrl += "?page=" + str(i)
        req = request.Request(url=tempUrl, headers=headers)
        res = request.urlopen(req)
        pageHtml = res.read().decode("utf-8")
        soup = BeautifulSoup(pageHtml, "lxml")
        # 对于page1，删除第一个无用广告段，获取章标题
        if 1 == i:
            # 找当前章标题
            title = soup.find("h1").string
            title = re.findall('[\u4e00-\u9fa5]', title)
            title = ''.join(title)
            chapName = "第%d章  "%(count)
            chapName += title
            txtFile.write(chapName+'\n')
            # 找正文div标签
            contentDiv = soup.find(attrs={'id': 'txt'})
            contents = contentDiv.select('p')
            # 删除第一个无用广告段
            for j in range(2, len(contents)):
                content = contents[j].text
                if content != "":
                    txtFile.write(content.strip())
                else:
                    txtFile.write('\n')
        # 对于page6，获取指向下一章都链接
        elif i == pageNum:
            # 找出指向下一章的a标签
            nextATag = soup.find(attrs={'id': 'pt_next'})
            # 下一章的完整链接
            nextChap = nextATag.attrs["href"]
            # 放入待访问链接列表中
            chapUrls.append(nextChap)
            # 获取正文内容
            contentDiv = soup.find(attrs={'id': 'txt'})
            # 获取第一段不在p标签中的内容
            firstPara = contentDiv.contents[0].strip()
            txtFile.write(firstPara)
            # 获取其他正文
            contents = contentDiv.select('p')
            # 删除第一个无用广告段
            for j in range(0, len(contents)):
                content = contents[j].text
                if content != "":
                    txtFile.write(content.strip())
                else:
                    txtFile.write('\n')
        # 对于其他页面，正常获取段落内容
        else:
            # 获取正文内容
            contentDiv = soup.find(attrs={'id': 'txt'})
            # 获取第一段不在p标签中的内容
            firstPara = contentDiv.contents[0].strip()
            txtFile.write(firstPara)
            # 获取其他正文
            contents = contentDiv.select('p')
            # 删除第一个无用广告段
            for j in range(0, len(contents)):
                content = contents[j].text
                if content != "":
                    txtFile.write(content.strip())
                else:
                    txtFile.write('\n')
    print("第%d章获取完成哦^ v ^,下一章链接是%s"%(count, chapUrls[0]))
    count += 1
    # 所有待查看待章节都看完了
    if len(chapUrls) != 0:
        if "laomaoxs" in chapUrls[0]:
            break

txtFile.close()