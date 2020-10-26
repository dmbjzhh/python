# -*- coding:utf-8 -*-

import re
h1 = '''18、18 夜袭                    (1/100)
                    '''
pageNum = re.findall(r".*\(1/(.*)\).*", h1)
print(pageNum)