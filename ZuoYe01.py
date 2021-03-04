# 猜年龄小游戏,有3点需求:
# 1.允许用户最多尝试3次
# 2.每尝试3次后, 如果还没猜对,就问用户是否继续,如果回答y或Y,就继续让其猜3次,以此往复,如果回答n或N,就退出程序
# 3.如果猜对了,就直接退出
# 目的:演练while的使用和if的使用

# age=9
# PD='y'
# while PD=='y' or PD=='Y':
#     for i in range(3):
#         age_in = int(input('请猜年龄(3次机会):'))
#         if age==age_in:
#             print('恭喜您猜对了....')
#             PD='n'
#             break
#             pass
#         else:
#             print('猜错了....')
#         pass
#     else:
#         PD=input('是否继续(y/n)?:')
# print('退出游戏......')

# 老师给的答案
# times=0
# count=3
# while times<=3:
#     age=int(input('请输入你猜的年龄....'))
#     if age==25:
#         print('恭喜你猜对了....')
#         break
#         pass
#     elif age>25:
#         print('猜大了,请再试试....')
#         pass
#     else:
#         print('猜小了,请再试试....')
#         pass
#     times+=1
#     if times==3:
#         choose=input('想不想再继续猜呢, Y/N ?')
#         if choose=='Y' or choose=='y':
#             times=0
#             pass
#         elif choose=='N' or choose=='n':
#             times=4
#             pass
#         else:
#             print('请不要乱输....')
#         pass

# 小王身高1.75,体重80.5kg.请根据BMI公式(体重除以身高的平方)帮小王计算他的BMI指数,并根据BMI指数:
# 低于18.5 过轻
# 18.5-25 正常
# 25-28 过重
# 28-32 肥胖
# 高于32 严重肥胖
# 用if-elif判断并打印结果

# height,weight=1.75,80.5
# BMI=weight/(height**2)
# print('BMI指数为:%d'%BMI)
# if BMI<18.5:
#     print('BMI低于18.5,体重过轻')
#     pass
# elif BMI<=25:
#     print('BMI在18.5-25,体重正常')
#     pass
# elif BMI<=28:
#     print('BMI在25-28,体重过重')
#     pass
# elif BMI<=32:
#     print('BMI在28-32,已属于肥胖,请注意控制体重')
#     pass
# else:
#     print('BMI指数已大于32,属于严重肥胖,请注意控制体重')