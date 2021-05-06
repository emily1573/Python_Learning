# 使用私有属性的场景
# 1.把特定的一个属性隐藏起来 不想让类的外部进行直接调用
# 2.我想保护这个属性 不想让属性的值随意的改变
# 3.保护这个属性 不想让派生类【子类】去继承

class Person:
    __hobby='跳舞' # 类属性
    def __init__(self):
        self.__name='李四' # 加两个下划线 将此属性私有化 就不能在外部直接访问了，当然在类内部是可以访问的
        self.age=30
        pass
    def __str__(self):
        return '{}的年龄是{} 爱好是{}'.format(self.__name,self.age,Person.__hobby)
    def changeValue(self):
        Person.__hobby='唱歌'
class Student(Person):
    def printInfo(self):
        # print(self.__name) # 在此访问父类中的私有属性，可以吗
        print(self.age)
    pass

stu=Student()
stu.printInfo()
stu.changeValue()
print(stu)
# print(stu.__hobby) # 实例对象访问类属性
# print(Person.__hobby) # 实例对象访问类属性
# xl=Person()
# # print(xl.__name) # 是通过类对象 在外部访问的 不能访问私有属性
# print(xl)

# 小结
# 1.私有化的【实例】属性 不能在外部直接的访问 可以在类的内部随意使用
# 2.子类不能继承父类的私有化属性【只能继承父类公共的属性和行为】
# 3.在属性名前面直接加'__'就可以变为私有化了