# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
_user = 'xxxx@qq.com'
_pwd  = 'xxxx'
_to   = 'xxxx'

msg = MIMEText("快去填志愿")
msg["Subject"] = "档案学上线啦"
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print("Success!")
except smtplib.SMTPException,e: 
    print ("Falied,%s" %e) 