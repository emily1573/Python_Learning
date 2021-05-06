# 取绝对值
# print(abs(-34))
# # round（）对浮点数进行近似取值，保留几位小数,四舍五入
# print(round(3.66,1))
# # pow求次方
# print(pow(3,3))
# max 求最大值
# print(max([23,123,4,5,2,1,786]))
# print(sum(range(50),3))
# eval 执行表达式
# a,b,c=1,2,3
# print('动态执行的函数={}'.format(eval('a+b+c')))
def TestFun():
    print('我执行了吗')
    pass
# eval('TestFun()') # 可以调用函数执行

# 类型转换函数
# print(bin(10)) # 转换二进制
# print(hex(23))
# 元组转换为列表
# tup=(1,2,3,4)
# print(type(tup))
# li=list(tup)
# print(type(li))
# li.append('强制转换成功')
# print(li)
# tupList=tuple(li)
# print(tupList)

# 字典操作 dict()
# dic=dict(name='小明',age=18) # 创建一个字典
# print(type(dic))
# print(dic)
# # dict['name']='小明'
# # dict['age']=18  # 不对的
# print(dic)

# bytes转换
print(bytes('我喜欢python',encoding='utf-8'))

