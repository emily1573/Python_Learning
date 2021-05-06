class Person(object):
    def __init__(self):
        self.__age = 18  # 定义一个私有化属性，属性名字前加两个下划线
    # def get_age(self): # 访问私有实例属性
    #     return self.__age
    # def set_age(self,age): # 修改私有实例属性
    #     if age < 0:
    #         print('年龄不能小于0')
    #     else:
    #         self.__age = age
    #         pass
    #     pass
    # # 定义一个类属性 实现通过直接访问属性的形式去访问私有属性
    # age=property(get_age,set_age)

    # 实现方式2 通过装饰器的方式去声明
    @property # 用装饰器修饰 添加属性标志 提供一个getter方法
    def age(self):
        return self.__age
    @age.setter # 提供一个setter方法
    def age(self,parms):
        if parms < 0:
            print('年龄不能小于0')
        else:
            self.__age = parms
            pass
        pass
    pass
p1=Person()
print(p1.age)
p1.age=30
print(p1.age)
