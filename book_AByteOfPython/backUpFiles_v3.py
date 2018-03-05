# -*- coding:utf-8 -*-
# 比v2的改进在于，用户可以给文件名添加注释，使文件更加好懂

import os
import time

source = ['"C:\\My Documents"', 'C:\\Code']

target_dir = 'E:\\Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment --->')

if len(comment) == 0: # 检查有没有输入注释
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' +\
    comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup Failed'