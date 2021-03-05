# 函数返回值
# 概念：函数执行完以后会返回一个对象，如果在函数的内部有return就可以返回实际的值，否则返回none
# 类型：可以返回任意类型，返回值类型应该取决于return后面的类型
# 用途：给调用方返回数据
# 在一个函数体内可以出现多个return值：但是肯定只能返回一个return
# 如果在一个函数体内执行了return，意味着函数就执行完成退出了，return后面的代码语句将不会执行
def Sum(a,b):
    sum=a+b
    return sum  # 将计算结果返回
    pass

# rs=Sum(10,40) # 将返回值赋给其他的变量
# print(rs) # 函数的返回值返回到调用的地方
def calComputer(num):
    list=[]
    result=0
    i=1
    while i<=num:
        result+=i
        i+=1
        pass
    list.append(result)
    return list
    pass

# 调用函数
# value=calComputer(10)
# print(type(value)) # value 类型
# print(value)
def returnTuple():
    '''
    返回元组类型的数据
    :return:
    '''
    # return 1,2,3
    return {"name":"测试"}
    pass

A=returnTuple()
print(type(A))