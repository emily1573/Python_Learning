# class People:
#     def __init__(self): # 魔术方法
#         self.name='小倩' # 实例属性
#         self.sex='女生'
#         self.age=20
#     def eat(self):
#         '''
#         吃的行为
#         :return:
#         '''
#         print('喜欢吃榴莲')
#     pass
# xq=People()
# xq.name='小倩' # 添加实例属性
# xq.sex='女生' # 添加实例属性
# xq.age=20 # 添加实例属性
# xq.eat()
# print(xq.name,xq.sex,xq.age)
#
# xl=People()
# xl.name='小丽'
# xl.sex='女生' # 添加实例属性
# xl.age=28 # 添加实例属性
# print(xl.name,xl.sex,xl.age)
#
# xm=People()  # 在创建新对象的时候是自动执行的
# print(xm.name)
# xm.name='小明'
# print(xm.name)

# 如果有n个对象 被实例化 那么就需要添加很多次这样的属性了 显然是比较麻烦

# init传递参数 改进
class People:
    def __init__(self,name,sex,age): # 魔术方法
        self.name=name # 实例属性
        self.sex=sex
        self.age=age
    def eat(self,food):
        '''
        吃的行为
        :return:
        '''
        print(self.name+'喜欢吃'+food)
    pass
zp=People('张鹏','男生',18)
print(zp.name,zp.age)
zp.eat('香蕉')


lh=People('李辉','男生',18)
lh.eat('橘子')
print(lh.name,lh.age)

# 总结 __init__
# 1.python 自带的内置函数 具有特殊的函数 使用双下划线 包起来的【魔术方法】
# 2.是一个初始化的方法 用来定义实例属性 和初始化数据的，在创建对象的时候自动调用 不用手动调用
# 3.利用传参的机制可以让我们定义功能更加强大并且方便的 类