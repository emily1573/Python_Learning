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
class Animal():
    def __init__(self,name,color,age):
        '''
        初始化实例
        :param name: 名字
        :param color: 颜色
        :param age: 年龄
        '''
        self.name=name
        self.color=color
        self.age=age
        pass
    def run(self):
        print('%s 在快速奔跑!'%(self.name))
        pass
    def eat(self):
        print('%s 在吃东西!' % (self.name))
        pass
    def __str__(self):
        return '%s 的颜色是：%s，年龄是： %s'%(self.name,self.color,self.age)
    pass

pig=Animal('猪','黑色',5)
pig.run()
pig.eat()
print(pig)
sheep=Animal('羊','白色',8)
sheep.run()
sheep.eat()
print(sheep)


