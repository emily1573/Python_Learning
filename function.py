# 函数的 定义
# def printInfo():
#     '''
#     这个函数是用来打印个人信息的 是对小张信息显示的组合
#     :return:
#     '''
#     # 函数代码块
#     print('小张的身高是%f' % 1.73)
#     print('小张的体重是%d' % 160)
#     print('小张的爱好是%s' % '唱歌')
#     print('小张的专业是%s' % '计算机信息管理')

# 函数的调用
# printInfo() # 函数的调用
# printInfo() # 函数的调用
#
# print('我是其他的代码块。。。。。')

# 进一步完善需求【输出不同人的信息】 方案：输入参数来解决
# def printInfo(name,height,weight,hobby,pro):
#     # 函数代码块
#     print('%s的身高是%f' % (name,height))
#     print('%s的体重是%d' % (name,weight))
#     print('%s的爱好是%s' % (name,hobby))
#     print('%s的专业是%s' % (name,pro))
#     pass
# 调用函数
# printInfo('小李',189,200,'打游戏','咨询师')
# print('------------带参数的调用--------------------')
# printInfo('peter',175,160,'码代码','计算机应用')

# 参数的分类：
# 必选参数、默认参数【缺省参数】、可选参数、关键字参数
# 参数：其实就是函数为了实现某项特定的功能，进而为了得到实现功能所需要的数据
# 为了得到外部数据
# 1.必选参数
# def sum(a,b): # 形式参数，只是意义上的一中参数，在定义的时候是不占内存地址
#     sum=a+b
#     print(sum)
#     pass
# # 函数的调用 在调用的时候必选参数 是必须要赋值的
# sum(20,15) # 20,15实际参数：实参，实实在在的参数，是实际占用内存地址的
# sum(15) # 不能这样写
# 2.默认参数【缺省参数】始终存在于参数列表中的尾部
# def sum1(a,b=30):
#     print('默认参数使用=%d'%(a+b))
#     pass
# 默认参数的调用
# sum1(10) # 在调用的时候如果未赋值，就会用定义函数时给定的默认值
#可变参数（当参数的个数不确定时使用，比较灵活
# def getComputer(*args): # 可变长的参数,参数关键字是一个元组类型
#     '''
#     计算累加和
#     :param args: 可变长的参数类型
#     :return:
#     '''
#     #print(args)
#     result=0
#     for item in args:
#         result+=item
#         pass
#     print('result=%d'%result)
#     pass
# getComputer(1,2)
# getComputer(1,2,3,4,5,6)

# 关键字可变参数 0-n
# ** 来定义
# 在函数体内 参数关键字是一个字典类型 key是一个字符串
# def keyFunc(**kwargs):
#     print(kwargs)
#     pass
# # 调用
# # keyFunc（1,2,3）不可以传递的
# dictA={"name":'Leo',"age":35}
# # keyFunc(**dictA)
# keyFunc(name='peter',age=26)
# keyFunc()
# 组合的使用
# def complexFunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     pass
# complexFunc(1,2,3,4,name='刘德华')
# complexFunc(age=36)

def TestMup(**kwargs,*args):
    '''
    可选参数必须放到关键字可选参数之前
    可选参数：接受的数据是一个元组类型
    关键字可选参数：接受的数据是一个字典类型
    :param kwargs:
    :param args:
    :return:
    '''
    pass
