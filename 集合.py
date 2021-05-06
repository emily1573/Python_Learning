# set 不支持索引和切片，是一个无序且不重复的容器
# 类似于字典 但是只有key 没有value
# 创建集合
set1={1,2,3}
set2={2,3,4}
dic1={1:3}
# print(type(set1))
# print(type(dic1))
# 添加操作
set1.add('python')
# print(set1)
# # 清空操作
# set1.clear()
# print(set1)
# 差集操作
# rs=set1.difference(set2)
# print(rs)
# print(set1-set2)
# print(set1)
# 交集操作
# print(set1.intersection(set2))
# print(set2&set1)
# 并集操作
# print(set1.union(set2))
# print(set1 | set2)
# pop就是从集合中拿数据并且同时删除
# print(set1)
# quData=set1.pop()
# print(quData)
# print(set1)
# print(set1.discard(3)) # 指定移除的元素
# print(set1)
# set1.update(set2) # 更新集合
# print(set1)