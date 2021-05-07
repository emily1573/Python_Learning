import types # 添加方法的库

def dymicMethod(self):
    print('{}的体重是：{}kg 在 {} 读大学'.format(self.name,self.weight,Student.shcool))
    pass
@classmethod
def classTest(cls):
    print('这是一个类方法')
    pass
@staticmethod
def staticMethodTest():
    print('这是一个静态方法')
    pass

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        pass
    def __str__(self):
        return '{}今年{}岁了'.format(self.name,self.age)
    pass

print('绑定类方法')
Student.TestMethod=classTest
Student.TestMethod()

Student.staticMethodTest=staticMethodTest
Student.staticMethodTest()

print('---------绑定类方法执行结束--------')

zyh=Student('张艳华',20)
zyh.weight=50 # 动态添加的，归张艳华所有
zyh.printInfo=types.MethodType(dymicMethod,zyh)
zyh.TestMethod()

print('---------另实例对象调用 动态绑定方法--------')
# print(zyh)
# print(zyh.weight)

print('---------另外一个实例对象 张明--------')
zm=Student('张明',18)
zm.weight=80
zm.printInfo=types.MethodType(dymicMethod,zm)
print(zm)
# print(zm.weight)

print('---------g给类对象添加属性--------')
Student.shcool='北京邮电大学' # 动态添加类属性
print(zm.shcool)

print('---------执行动态的调用实例方法--------')
zyh.printInfo()
zm.printInfo()
