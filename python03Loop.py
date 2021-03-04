# 循环的分类
# while 语法结构
# 语法特点:
# 1.有初始值
# 2.条件表达式
# 3.变量[循环体内计数变量]的自增自减,否则会造成死循环
# 使用条件: 循环的次数不确定,是依靠循环条件来结束
# 目的: 为了将相似或者相同的代码操作变得更加简介,使得代码可以重复利用

# 案例: 输出1-100之间的数据
# index=1 #定义一个变量
# while index<=100:
#     print(index)
#     index+=4
#     pass

# 案例:打印九九乘法表
# row=1
# while row<=9:
#     col=1
#     while col<=row:
#         print("%d*%d=%d"%(col,row,row*col),end=" ")
#         col+=1
#         pass
#     print( )
#     row+=1
#     pass

# 案例 打印直角三角形
# row=7
# while row>=1:
#     j=1
#     while j<=row:
#         print("*",end=' ')
#         j+=1
#         pass
#     print()
#     row-=1
#     pass

# 案例拓展 等腰三角形打印
# row=1
# while row<=5:
#     j=1
#     while j<=5-row: #控制打印空格的数量
#         print(' ',end='')
#         j+=1
#         pass
#     k=1
#     while k<=2*row-1: #控制打印*号
#         print('*',end='')
#         k+=1
#         pass
#     print()
#     row+=1

# for 循环
# 语法特点:遍历操作,依次取集合容器中的每个值
# for 临时变量 in 容器:
#     执行代码块
# tags='我是一个中国人' #字符串类型本身就是一个字符类型的集合
# for item in tags:
#     print(item)
#     pass

# range 此函数可以生成一个数据集合列表
# range(起始:结束:步长) 步长不能为0
# sum=0
# for data in range(1,101): # 左边包含右边不包含
#     sum+=data
#     print(data,end=' ')
#     pass
# print()
# print("sum=%d"%sum)

# break和continue
# break 代表中断结束 满足条件之间结束本层循环
# continue: 结束本次循环, 继续进行下次循环(当continue的条件满足的时候,本次循环剩下的语句将不再执行,后面的循环继续)
# 这两个关键字只能用在循环中

# sum=0
# for item in range(1,51):
#     if sum>100:
#         print("循环执行到%d就退出来了"%item)
#         break
#         pass
#     sum+=item
#     pass
# print("sum=%d"%sum)

# print('continue的使用')
# for item in range(1,100):#求出奇数
#     if item%2==0:
#         continue
#         pass
#     print(item)
#     pass

# for item in 'i love python':
#     # if item=='e':
#     #     break
#     if item=='o':
#         continue
#     print(item)

# 99乘法表用for来实现
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(j,i,i*j),end=' ')
#         pass
#     print()
#     pass

# for-----else
# for item in range(1,11):
#     print(item,end=' ')
#     if item>=5:
#         break
#     pass
# else:
#     print('只要再上面的循环中,出现了break 那么else的代码将不再执行')

# account='mdm'
# pwd='123'
# for i in range(3):
#     zh=input('请输入账号:')
#     pd=input('请输入密码:')
#     if account==zh and pwd==pd:
#         print('恭喜您登录成功....')
#         break
#         pass
#     pass
# else:
#     print('您的账号已经被系统锁定......')

# while----else
# index=1
# while index<=10:
#     print(index)
#     if index==6:
#         break
#     index+=1
#     pass
# else:
#     print('else执行了吗?')