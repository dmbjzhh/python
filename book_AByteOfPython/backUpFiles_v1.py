# -*- coding:utf-8 -*-

import os
import time

# 1. 要备份的文件和目录被指定为一个列表
source = ['/home/sameen/byte', '/home/sameen/bin']
# 如果使用的是Windows，这么写：source = [r'C:\Documents', r'C:\Work']或者其他这样的

# 2. 备份文件的存储目录，可以根据需要改动
target_dir = '/mnt/e/backup/'

# 3. 文件被备份为一个zip文件，zip文件的名字是当前的日期和时间，os.sep使得写的代码可以跨操作系统，不用修改 '/'，'\\'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 4. 如果目标目录不存在的话，创建目标目录
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 5. 在Linux里用zip命令来压缩文件
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

# 运行备份
if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup Failed'