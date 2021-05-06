# 案例演示
class Animal:
    '''
    父类【基类】
    '''
    def say_who(self):
        print('我是一个动物。。。。')
        pass
    pass
class Duck(Animal):
    '''
    鸭子类【子类】派生类
    '''
    def say_who(self):
        '''
        在这里重写父类的方法
        :return:
        '''
        print('我是一只漂亮的鸭子。。。。。')
        pass
    pass
class Dog(Animal):
    '''
    小狗类【子类】派生类
    '''
    def say_who(self):
        print('我是一只哈巴狗。。。。')
        pass
    pass
class Cat(Animal):
    '''
    小猫类【子类】派生类
    '''
    def say_who(self):
        print('我是一只小花猫。。。。')
        pass
    pass

class Bird(Animal):
    '''
    小鸟类【子类】派生类
    '''
    def say_who(self):
        print('我是一只小小鸟。。。。')
        pass
    pass

def commonInvoke(obj):
    '''
    统一调用的方法
    :param obj: 对象的实例
    :return:
    '''
    obj.say_who()

# duck1=Duck()
# duck1.say_who()
# dog1=Dog()
# dog1.say_who()
# cat1=Cat()
# cat1.say_who()

listObj=[Duck(),Dog(),Cat(),Bird()]
for item in listObj:
    '''
    循环调用函数
    '''
    commonInvoke(item)