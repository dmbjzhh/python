# -*- coding:utf-8 -*-
# 比版本1的改进在于层级化，以日期作为目录，以时间作为zip文件的名字

import os
import time

# 注意，如果目录名字里有空格，必须要使用双引号
source = ['"C:\\My Documents"', 'C:\\Code']

target_dir = 'E:\\Backup'

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created diretory', today

target = today + os.sep + now + '.zip'

zip_command = 'zip -qr {0} {1}'.format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup Failed'