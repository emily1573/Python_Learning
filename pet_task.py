from os import walk,mkdir,rename,path
import os

# 以文件夹的名字给宠物图片命名

path = 'pets'
for filepath, folders, files in walk(path):
    # print(filepath, folders, files)
    # 注意我们要以文件夹名字 作为 文件夹下文件的名字， 同时加上一个顺序
    counter = 0
    for file in files:
        print(filepath)
        type_name = filepath.split('\\')[-1] #注意使用这种方式取文件夹的名字 split
        renamed = type_name+str(counter)+'.jpg' #组合新名字
        # 注意这里为全路径 源文件 目标文件
        rename(os.path.join(filepath, file), os.path.join(filepath, renamed))
        counter += 1
