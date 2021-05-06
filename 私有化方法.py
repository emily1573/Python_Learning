class Animal:
    def __eat(self):
        print('吃东西')
        pass
    def run(self):
        self.__eat() # 在此调用私有化的方法
        print('飞快的跑')
        pass

class Bird(Animal):
    pass

b1=Bird()
# b1.__eat()
b1.run()