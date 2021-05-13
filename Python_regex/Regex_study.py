# 通过python中re模块去学习并使用正则表达式的基本知识点
# group(num) 可以获取匹配的数据 如果有多个匹配结果的话 那么会以元组的形式存放到group对象中
import re
data = 'Python is the best language in the world'
result=re.match('(.*) is (.*?) .*',data,re.I|re.M) # 精确匹配 match只尝试匹配以什么为开头的
# print(type(result))  # 返回<class 're.Match'> 对象
# print(result.group())
if result:
    print('匹配成功')
    print(result)
    print(result.groups())
    print(result.group(1))
    print(result.group(2))
else:
    print(result.group())  # 如果匹配失败是没有group函数的，因为是个空对象NONE
    print(result)
    print('匹配失败')