# 元组的创建 不能进行修改
tupleA=() # 空元组
tupleA=('abcd',89,9.12,'peter',[11,22,33])
# print(tupleA)
# print(type(tupleA))
# 元组的查询
# for item in tupleA:
#     print(item,end=' ')
# print(tupleA[2:4])
# print(tupleA[::-1])
# print(tupleA[::-2]) # 表示反转字符串， 每隔两个取一次
# print(tupleA[::-3]) # 表示反转字符串， 每隔三个取一次
# print(tupleA[-2:-1:]) # 倒着取下标为-2到-1区间的
#
# print(tupleA[-4:-2:]) # 倒着取下标为-4到-3区间的
# tupleA[4][0]=243435  # 可以对元组中的列表对象进行修改
# print(tupleA)

tupleB=(1,) # 当元组中只有一个数据项的时候，必须要在数据项后面加上逗号
print(tupleB)
print(type(tupleB))
tupleC=tuple(range(10))
tupleC=(1,2,3,4,3,4,4,1)
print(tupleC.count(4))  # 可以统计元素出现的次数