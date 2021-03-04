# li=[1,2,3,"你好"]
# print(type(li))
# print(len(li)) # len函数可以获取到列表对象中的数据个数
# strA='我喜欢Python'
# print(len(strA))

# 查找
listA=['abcd',785,12.3,'qiuzhi',True]
# print(listA) # 输出完整地列表
# print(listA[0]) # 输出第一个元素
# print(listA[1:3]) # 从第二个开始到第三个元素
# print(listA[2:]) #从第三个元素开始到最后所有的元素
# print(listA[::-1]) # 负数从右向左开始输出
# print(listA*2)  # 输出多次列表中的数据【复制】
# print('---------------增加--------------')
# print('追加之前',listA)
# listA.append(['fff','ddd']) # 追加操作
# listA.append(8888)
# print('追加之后',listA)
# listA.insert(1,'这是我刚插入的数据') # 插入操作
# print(listA)
# rsData=list(range(10))  # 强制转换为list对象
# print(type(rsData))
# listA.extend(rsData) # 扩展 等于批量添加
# print(listA)

# print('------------------修改--------------')
# print('修改之前',listA)
# listA[0]='peter'
# print('修改之后',listA)
listB=list(range(10,50))
print('------------------删除list数据项--------------')
print('删除之前',listB)
# del listB[0] # 删除列表中第一个元素
# del listB[1:3] # 批量删除列表中多项元素
# listB.remove(20) # 移除指定的元素 参数是具体的数据
listB.pop(1) # 可以移除指定的项的索引下标值
print('删除之后',listB)
print(listB.index(25)) # 返回的是索引下标