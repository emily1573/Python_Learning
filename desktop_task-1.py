from os import walk, mkdir, remove
import os
from shutil import copy, move

# 桌面的数据整理，基于名字
path = 'file_prac' #os.walk 返回文件路径 文件夹 文件
for filepath, folders, files in walk(path):
    for file in files:
        if 'docx' in file:
            if os.path.exists(r'backupfolder\docx'):
                print(os.path.join(filepath, file))
                copy(os.path.join(filepath, file), os.path.join(r'backupfolder\docx', file))

            else:
                print('docx is not existed and create folder')
                os.mkdir(r'backupfolder\docx')

                print(os.path.join(filepath, file)) #r'c:\aa\aa.jpg'  'c:\\aa\\aa.jpg'
                copy(os.path.join(filepath, file), os.path.join(r'backupfolder\docx', file))
            #move
        elif 'ppt' in file:
            if os.path.exists(r'backupfolder\ppt'):
                print(os.path.join(filepath, file))
                copy(os.path.join(filepath, file), os.path.join(r'backupfolder\ppt', file))

            else:
                print('ppt is not existed and create folder')
                os.mkdir(r'backupfolder\ppt')

                print(os.path.join(filepath, file))
                copy(os.path.join(filepath, file), os.path.join(r'backupfolder\ppt', file))
            #move
        elif 'txt' in file:
            if os.path.exists(r'backupfolder\txt'):
                print(os.path.join(filepath, file))
                copy(os.path.join(filepath, file), os.path.join(r'backupfolder\txt', file))

            else:
                print('txt is not existed and create folder')
                os.mkdir(r'backupfolder\txt')

                print(os.path.join(filepath, file))
                copy(os.path.join(filepath, file), os.path.join(r'backupfolder\txt', file))
