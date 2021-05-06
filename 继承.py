class Animal:
    def eat(self):
        '''
        吃
        :return:
        '''
        print('吃饭了')
        pass
    def drink(self):
        '''
        喝
        :return:
        '''
        pass
    pass

class Dog(Animal):  # 继承了Animal父类 此时dog就是子类
    def wwj(self):
        print('小狗汪汪叫')
    pass
class Cat(Animal):
    def mmj(self):
        print('小猫喵喵叫')
    pass

d1=Dog()
d1.eat()  # 具备了吃的行为
d1.wwj()

c1=Cat()
c1.eat()
c1.mmj()
