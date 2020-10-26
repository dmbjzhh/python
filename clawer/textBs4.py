# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

html = '''
<div class="txt" id="txt">
	人是吧？”<p></p><p>　　  小四子点头啊点头。</p><p></p><p>　　  “那应该是吕林了。”展昭给白玉堂喂定心丸，“他也去的话，应该司天监和翰林院的人都去了，估计真是有记载的什么古墓了。”</p><p></p><p>　　  白玉堂点点头，“听着挺有意思。”</p><p></p><p>　　  小四子继续噘嘴，“我也想去呢，但是爹爹不让我去。”</p><p></p><p>　　  展昭想了想，“一会儿我去送猫的那家面馆也在西郊，不如顺道去瞧瞧？”</p><p></p><p>　　  白玉堂点头同意，小四子举手。</p><p></p><p>　　  展昭伸手把他抱起来，“当然带着你一起去啊，但是你可不准乱跑！”</p><p></p><p>　　  小四子点头啊点头，“嗯呢！”</p><p></p><p>　　  </p><p <br="">	</p><h1 id="chaptername" class="chaptername">1、01 西郊古墓                    (6/6)
                    </h1></div>
'''

soup = BeautifulSoup(html, "lxml")
print(soup.body.div.p.text == "")