# 匿名函数
# 语法：
# lambda 参数1、参数2、参数3：表达式
# 特点：
# 1.使用lambda关键字去创建函数
# 2.没有名字的函数
# 3.匿名函数冒号后面的表达式有且只有一个，注意：是表达式，而不是语句
# 4.匿名函数自带return，而这个return的结果就是表达式计算后的结果
# 缺点
# lambda只能是单个表达式，不是一个代码块，lambda的设计就是为了满足简单函数的场景
# 仅仅能封装有限的逻辑，复杂逻辑实现不了，必须使用def来处理
# def computer(x,y):
#     '''
#     计算数据和
#     :param x:
#     :param y:
#     :return:
#     '''
#     return x+y

# print(computer(10,45))
# 对应的匿名函数
# M=lambda x,y:x+y
# 通过变量去调用匿名函数
# print(M(23,10))

# result=lambda a,b,c:a*b*c
# print(result(12,34,2))
# age=15
# print('可以参军' if age>18 else '继续上学') # 可以替换传统双分支的写法

# funcTest=lambda x,y:x if x>y else y
# print(funcTest(2,12))

# rs=(lambda x,y:x if x>y else y)(16,12)# 直接的调用
# print(rs)
varRs=lambda x:(x**2)+890
print(varRs(10))