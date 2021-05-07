# 1.python中如何通过类创建对象，请用代码举例说明
# class Student:
#     def run(self):
#         print('学生每天进行2000米的跑步训练')
#         pass
#     pass
#
# xiaoli=Student() # 创建一个对象
# xiaoli.run()

# 2.如何在类中定义一个方法，请用代码举例说明
# 参考上述demo
# 3.定义一个水果类，然后通过水果类，创建苹果对象、橘子对象、西瓜对象并分别添加上颜色属性
# class SgClass:
#     def __init__(self,name,color):
#         '''
#
#         :param color:
#         '''
#         self.name=name
#         self.color=color
#         pass
#     def __str__(self):
#         return '%s 的颜色是【%s】'%(self.name,self.color)
#     pass
# pg=SgClass('苹果','红色')
# print(pg)
# print('*'*40)
# jz=SgClass('橘子','橙色')
# print(jz)
# print('*'*40)
# xg=SgClass('西瓜','黑皮')
# print(xg)
# # 4.请编写代码，验证self就是实例本身
# class Person:
#     def weight(self):
#         print('self=%s'%(id(self)))
#         pass
# liming=Person()
# liming.weight()
# print(id(liming))
# 5.定义一个Animal类
# （1）使用__init__初始化方法为对象添加初始化属性，例如颜色、名字、年龄
# （2）定义动物方法，如run，eat等方法，如调用eat方法时打印XX在吃东西就可以
# （3）定义一个__str__方法，输出对象的所有属性
# class Animal():
#     def __init__(self,name,color,age):
#         '''
#         初始化实例
#         :param name: 名字
#         :param color: 颜色
#         :param age: 年龄
#         '''
#         self.name=name
#         self.color=color
#         self.age=age
#         pass
#     def run(self):
#         print('%s 在快速奔跑!'%(self.name))
#         pass
#     def eat(self):
#         print('%s 在吃东西!' % (self.name))
#         pass
#     def __str__(self):
#         return '%s 的颜色是：%s，年龄是： %s'%(self.name,self.color,self.age)
#     pass
#
# pig=Animal('猪','黑色',5)
# pig.run()
# pig.eat()
# print(pig)
# sheep=Animal('羊','白色',8)
# sheep.run()
# sheep.eat()
# print(sheep)

# 2021-5-6
# 1.python中new方法的作用是什么？
#     用来创建实例对象的，只有继承了object的话，才能有这个方法
# 2.什么是单例模式？单例模式适用于什么场景？
#     答：要求一个类有且只有一个实例，并且提供了一个全局的访问点
#     日志插入logger的操作，网站计数器，权限验证模块，windows资源管理器，系统回收站，数据库连接池
# 3.私有化方法与私有化属性在子类中能否继承？
#     不能的
# 4.在python中什么是异常？
#     异常就是程序在执行过程中发生的错误
# 5.python中是如何处理异常的
#    分别根据异常的类型去处理
# 6.python中异常处理语句的一般格式，可以使用伪代码的形式描述
#     try：
#         # 正常操作
#     except：
#         # 。。。。
#     else:
#         # .....
#     finally:
#         # .....
# 7.__slots__属性的作用
#     限制属性的随意输入
#     节省内存空间
# 8.私有化属性的作用？
#     保护数据，封装性的体现
# 9.在类外面是否能修改私有属性
#     不可以直接修改 通过方法去实现 还可以借助属性函数property去实现
# 10.如果一个类中，只有指定的属性或者方法能被外部修改，那么该如何限制外部修改
#     对属性进行私有化的设定

# 1.编写一段代码以完成下面的要求
# 定义一个Person类，类中要有初始化方法，方法中要有人的姓名，年龄两个私有属性
# 提供获取用户信息的函数
# 提供获取私有属性的方法
# 提供可以设置私有属性的方法
# 设置年龄的范围在（0-120），如果不在这个范围，不能设置成功
# class Person:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#         pass
#     def __str__(self):
#         return  '{}的年龄是{}'.format(self.__name,self.__age)
#     def getAgeInfo(self):
#         return self.__age
#     def setAge(self,age):
#         if age>0 and age<120:
#             self.__age=age
#             pass
#         else:
#             print('您输入的数据不合法')
#     def getNameInfo(self):
#         return self.__name
#     def setName(self,name):
#         self.__name=name

# 2. 请写一个单例模式
#     省略
# 3.创建一个类，并定义两个私有化属性，提供一个获取属性的方法，和设置属性的方法，利用property属性给调用者提供属性方式的调用
# class Student:
#     def __init__(self):
#         self.__name='张三'
#         self.__score=90
#         pass
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,name):
#         self.__name=name
#         pass
#
#     @property
#     def score(self):
#         return self.__score
#
#     @score.setter
#     def score(self, score):
#         self.__score = score
#         pass
#     def __str__(self):
#         return ''
#     def __call__(self, *args, **kwargs):
#         # print(self.__name+'的得分是：'+(str)self.__score)
#         print('{}的得分是：{}'.format(self.__name,self.__score))
#         pass
#     pass
# xw=Student()
# xw() # 将实例以函数的方式调用
# xw.name='李四'
# xw.score=98
# xw()
# print(xw)

# 4.创建一个Animal类，实例化一个cat对象，请给cat对象动态绑定一个run方法，给类绑定一个类属性colour，给类绑定一个类方法打印字符串'ok'。
import types
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        pass
    def __str__(self):
        return '{}今年{}岁了'.format(self.name,self.age)
    pass

def run(self):
    print('{}今年{}岁了,颜色是：{},正在奔跑。'.format(self.name,self.age,Animal.colour))
    pass
@classmethod
def PrintOK(cls):
    print('ok')
    pass

Animal.info=PrintOK  # 绑定类方法
Animal.info()

Animal.colour='黑白条纹' # 绑定类属性

#绑定实例化方法
cat=Animal('小花猫',3)
cat.run=types.MethodType(run,cat) # 动态绑定
cat.run()
print(cat.colour)
