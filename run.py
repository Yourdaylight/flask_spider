# -*- coding: utf-8 -*-
# @Time    :2022/3/2 15:57
# @Author  :lzh
# @File    : run.py
# @Software: PyCharm
import os
if __name__ == '__main__':
    # 启动脚本，启动vue、flask服务
    os.system("python app.py")
    os.system("cd static && npm run serve")
