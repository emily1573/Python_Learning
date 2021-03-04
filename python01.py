# if-else 嵌套使用
xuefen=int(input("请输入你的学分:"))
if xuefen>=10:
    grade = int(input("请输入你的成绩:"))
    if grade>=80:
        print('你可以升班了...恭喜你')
        pass
    else:
        print('很遗憾,你的成绩还不达标....')
        pass
else:
    print("您的表现也太差了吧...")