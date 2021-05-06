# 所谓重写 就是子类中，有一个和父类相同名字的方法，在子类中的方法会覆盖掉父类中同名方法
# 为什么要重写，父类的方法已经不满足子类的需要，那么子类就可以重写父类或者完善父类
class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print('汪汪叫-------')
        pass
    pass
class keji(Dog):
    def __init__(self,name,color): # 属于重写父类的方法
        # 针对这种需求，我们就需要调用父类的函数了
        # Dog.__init__(self,name,color) # 手动调用调用父类的方法了 执行完毕就可以具备 name，color这两个实例属性了
        super().__init__(name,color) # super是自动找到父类 进而调用方法 假设继承了多个父类，那么会按照顺序逐个去找，然后再调用
        self.weight=90
        self.height=80
        pass
    def __str__(self):
        return '{}的颜色是{} 他的身高是{}cm 体重是：{}'.format(self.name,self.color,self.height,self.weight)
    def bark(self):
        print('叫的跟神一样')
        print(self.name)
    pass

kj=keji('柯基犬','黄色')
print(kj)
