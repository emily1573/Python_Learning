class shenxian:
    def fly(self):
        print('神仙都会飞')
    pass
class Monkey:
    def chitao(self):
        print('猴子喜欢吃桃')
    pass
class Sunwukong(shenxian,Monkey): # 既是神仙 同时也是猴子
    pass

swk=Sunwukong()
swk.chitao()
swk.fly()
# 问题是 当多个父类中存在相同方法的时候 应该去调用哪一个
class D(object):
    def eat(self):
        print('D.eat')
        pass
    pass
class C(D):
    def eat(self):
        print('C.eat')
        pass
    pass
class B(D):
    pass
class A(B,C):
    pass
a=A()
a.eat()
print(A.__mro__)
# 在执行eat的方法时 查找方法的顺序应该是
# 首先到A里面去查找 如果A中没有 则继续去B类中查找  如果B中没有 则去C中查找 如果C类中没有 则去D类中查找
# 如果没有找到，则会报错 A-B-C-D