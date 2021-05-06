# 递归满足的条件
# 自己调用自己
# 必须有一个明确的结束条件
# 优点：逻辑简单、定义简单
# 缺点：容易导致栈溢出，内存资源紧张，甚至内存泄漏
# 求阶乘
# 循环的方式去实现
# def jiecheng(n):
#     result=1
#     for item in range(1,n+1):
#         result*=item
#         pass
#     return result
#
# print('5的阶乘{}'.format(jiecheng(5)))
# 递归方式去实现
# def diguiJc(n):
#     '''
#     递归实现
#     :param n:阶乘参数
#     :return:
#     '''
#     if n==1:
#         return 1
#     else:
#         return n*diguiJc(n-1)
#     pass
# # 递归调用
# print('5的阶乘{}'.format(diguiJc(5)))

# 递归案例：模拟实现 树形结构的遍历
import os # 引入文件操作模块
def findFile(file_Path):
    listRs=os.listdir(file_Path) # 得到该路径下所有文件夹
    for fileItem in listRs:
        full_path=os.path.join(file_Path,fileItem) # 获取完整地文件路径
        if os.path.isdir(full_path):  # 判断是否是文件夹
            findFile(full_path) # 如果是文件夹，再次去递归
        else:
            print(fileItem)
            pass
        pass
    else:
        return
    pass

# 调用搜索文件夹函数
findFile('D:\\马冬梅\\3.培训文档')