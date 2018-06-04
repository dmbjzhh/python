# -*- coding:utf-8 -*-
from wxpy import *
import requests
import json
import time

# 调用图灵机器人api，发送消息并获得回复
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "207f16f893194a938b433ce05c4f327d"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "267047"
    }
    r = requests.post(url, data=json.dumps(payload))    
    result = json.loads(r.content)    
    return result["text"]

bot = Bot(cache_path=True)
friend = bot.friends().search(u"一行")[0]
print friend
friend.send(u"你在干嘛？")

@bot.register(friend)
def reply_my_friend(msg):
    print msg
    return auto_reply(msg.text)

embed()

