# 函数嵌套
# def fun1():
#     print('-------------fun1 start----------------')
#     print('-------------执行代码省略----------------')
#     print('-------------fun1 end----------------')
#     pass
#
# def fun2():
#     print('-------------fun2 start----------------')
#     # 调用第一个函数
#     fun1()
#     print('-------------fun2 end----------------')
#     pass
#
# fun2() # 调用函数2
# 函数的分类：根据函数的返回值和函数的参数
# 有参数无返回值的
# 有参数有返回值的
# 无参数有返回值的
# 无参数无返回值的

# 作业
# 1.写函数，接收n个数字，求这些参数数字的和
# def Sum(*args):
#     '''
#     处理列表数据
#     :param args:可变长参数 可以接受一个元组
#     :return:计算和
#     '''
#     sum=0
#     for item in args:
#         sum+=item
#         pass
#     return  sum
#
# sum1=Sum(10,20,30,50)
# print(sum1)

# 2.写函数，找出传入的列表或元组的奇数位对应的元素，并返回一个新的列表
# def returnList(list):
#     '''
#     处理列表数据
#     :param list:接受的是一个列表或元组
#     :return:新的列表对象
#     '''
#     result=[]
#     for item in range(len(list)):
#         if (item+1)%2!=0:
#            result.append(list[item])
#            pass
#         pass
#     return result
#
# a=(2,1,4,3,6,5,8,7,9,10,11,12)
# print(type(a))
# print(returnList(a))

# 3.写函数，检查传入字典的每一个value的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。PS：字典中的value值只能是字符串或列表。
# def checkDict(dict): # **kwargs
#     '''
#     处理字典类型的数据
#     :param dict: 字典
#     :return: 处理后的字典内容
#     '''
#     for key,value in dict.items():
#         if len(value)>2:
#             dict[key]=value[0:2]
#         pass
#     return dict
#     pass
# print(checkDict({1:"wreqituiqt",2:"r",3:[1,2,3,4,5]}))

