Test='python'
# print(type(Test))
# print('获取第一个字符:%s'%Test[0])

# name='peter'
# print('姓名首字母转换成大写%s'%name.capitalize()) #首字母变大写

a='      hello      '
# b=a.strip() # 去除字符串中的空格
# print(b)
# print(a.lstrip()) # 删除左边的空格
# print(a.rstrip()) # 删除右边的空格
# b=a 复制字符串
# print('a的内存地址%d'%id(a)) #id函数 可以查看一个对象的内存地址
# b=a # 在此只是把a对象的内存地址赋给了b
# print('b的内存地址%d'%id(b))

# dataStr='I love Python'
# print(dataStr.find('o')) # 可以查找目标对象在序列对象中的位置,如果没找到就返回-1
# print(dataStr.index('o')) # 检测字符串中是否包含子字符串，返回的是下标值
# index如果没有找到对象的数据， 便会报异常，而find函数不会，找不到返回-1
# print(dataStr.startswith('p')) #判断开头
# print(dataStr.endswith('n'))  # 判断结尾
#
# print(dataStr.lower())  # 转换成小写
# print(dataStr.upper())  # 转换成大写

strMsg='hello world'
# slice [start:end:step] 左闭右开 start<=value<end
# print(strMsg) # 输出完整地数据
# print(strMsg[2:5]) # 2-5 下标之间的数据
# print(strMsg[2:]) # 第三个字符到最后
# print(strMsg[:3]) # 1-3 strMsg[0:3]=strMsg[:3]
# print(strMsg[::-1]) #倒序输出 负号表示方向 从右往左遍历

# 共有方法 + * in
strA='人生苦短'
strB='我用python'
# list 合并
listA=list(range(10))
listB=list(range(11,20))
print(listA+listB)
print(strA+strB)
# 复制 *
print(strA*3)
print(listA*3)
# in 对象是否存在
print('我' in strA) # boole值
print(9 in listA)
dictA={"name":"peter"}
print("name" in dictA)