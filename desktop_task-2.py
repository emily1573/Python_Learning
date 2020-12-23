from os import walk, mkdir, remove
import os
import time
from shutil import copy, move

# 桌面的数据整理
# path = 'file_prac' #os.walk 返回文件路径 文件夹 文件
# for filepath, folders, files in walk(path):
#     # 基于文件大小
#     for file in files:
#         size = os.path.getsize(os.path.join(filepath, file)) / 1024 / 1024 #B KB MB
#         if size > 1.0:
#             print(file)
#             remove(os.path.join(filepath, file)) #一旦删除无法恢复
#
#     # 基于创建时间
#     for file in files:
#         # 获取文件创建时间，返回时间戳
#         create_time = os.path.getmtime(os.path.join(filepath, file))
#         # print(create_time)
#         # 时间戳从1970年开始计时 1 2 3 4 5
#         # 时间戳格式化 显示2000-01-01 20：00
#         real_time = time.localtime(create_time)
#         dt = time.strftime("%Y-%m-%d %H:%M", real_time)
#         # print(dt)
#
#         # 格式化转时间戳用于比对
#         target_time = '2020-10-08 10:30' # 用户这里确定时间标准
#         # 转为时间数组
#         time_array = time.strptime(target_time, "%Y-%m-%d %H:%M")
#         my_target_time = float(time.mktime(time_array))
#         # print(my_target_time)
#
#         if my_target_time < create_time: #10点32分之前的，就说小于
#             print(file)
#             print(dt)
#             copy(os.path.join(filepath, file), os.path.join('zipfolder', file))

# 压缩处理

import zipfile
def zipf():
    z = zipfile.ZipFile( 'abc.zip','w')
    for file in os.listdir('zipfolder'):
        z.write(os.path.join('zipfolder', file))
        with open('abc.txt','a',encoding='gbk') as w: #注意编码问题
            w.write(file+'\n')
    z.close()

# zipf()

def unzipf():
    f = zipfile.ZipFile('abc.zip', 'r')
    for file in f.namelist():
        f.extract(file, "MYunzip/")

unzipf()
