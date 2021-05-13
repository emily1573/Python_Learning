import os
import shutil
# os.rename('test.txt','Test_重命名.txt')
# os.remove('File_del.py') # 删除文件 前提是文件存在
# os.mkdir('Test_CJ') # 创建文件夹
# os.rmdir('Test_CJ') # 删除文件夹 文件夹必须存在
# os.mkdir('d:/Python编程/sub核心') # 不允许创建多级，只能创建一级目录
# os.makedirs('d:/Python编程/sub核心/三级') # 创建多级目录
# os.rmdir('d:/Python编程') # 只能删除空目录
# 如果要删除非空目录 就需要调用shutil模块
# shutil.rmtree('d:/Python编程') # 多级删除非空目录

# 获取当前目录
# print(os.getcwd())
# 路径的拼接
# print(os.path)
# print(os.path.join(os.getcwd(),'venv'))
# 获取python中的目录列表
# listRs=os.listdir('d:/') # 老版本的用法
# for dirname in listRs:
#     print(dirname)

# 使用现代版的写法
# scandir 和with一起来使用 这样的话 上下文管理器会在迭代器遍历完成后自动释放资源
# with os.scandir('d:/') as entries: # with是上下文管理器
#     for entry in entries:
#         print(entry.name)

# basePath='d:/'
# for entry in os.listdir(basePath):
#     if os.path.isdir(os.path.join(basePath,entry)):
#         print(os.path.join(basePath,entry))
#         pass

def findFile(file_Path):
    listRs=os.listdir(file_Path) # 得到该路径下所有文件夹
    for fileItem in listRs:
        full_path=os.path.join(file_Path,fileItem) # 获取完整地文件路径
        if os.path.isdir(full_path): # 判断是否是文件夹
            findFile(full_path) # 如果是文件夹 再次去递归
        else:
            print(os.path.join(full_path,fileItem))
            pass
        pass
    else:
        return
    pass

findFile('D:\\tortoise svn\\Languages')