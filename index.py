# score=int(input('请输入你的成绩....'))
# if score>90:
#     print('您的成绩是A等级%s' %score)
#     pass
# elif score>=80:
#     print('您的成绩是B等级%s' %score)
#     pass
# elif score>=70:
#     print('您的成绩是C等级%s' %score)
#     pass
# elif score>=60:
#     print('您的成绩是D等级%s' %score)
#     pass
# else:
#     print("成绩不合格,请继续努力")

# 多分枝 多条件演练
# 猜拳机小游戏: 0:石头 1:剪刀 2:布
import random #直接导入产生随机数的模块
# 计算机 人
count=1
while count<=10:
    person=int(input('请出拳:[0:石头 1:剪刀 2:布]'))
    computer=random.randint(0,2)
    print("person:%s,computer:%s" %(person,computer))
    if person==0 and computer==1: #多条件
        print('厉害了,你赢了....')
        pass
    elif person==1 and computer==2: #多条件
        print('厉害了,你赢了....')
        pass
    elif person==2 and computer==0: #多条件
        print('厉害了,你赢了....')
        pass
    elif person==computer: #多条件
        print('不错, 居然是平手')
        pass
    else:
        print('哈哈,你输了')
    count+=1