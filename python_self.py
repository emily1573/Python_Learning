class Person:
    def __init__(self,pro,name,food):
        '''

        :param pro: 专业
        '''
        self.pro=pro
        self.name=name
        self.food=food
        print('-------init 函数的执行-----------')
        pass

    '''
    定义类
    '''
    def eat(self,name,food):
        '''
        实例方法
        :return:
        '''
        # print('self=%s',id(self))
        print('%s 喜欢吃 %s 修的专业是：%s'%(self.name,self.food,self.pro))
        pass
    def __str__(self):
        '''
        打印对象 自定义对象 是内容格式的
        :return:
        '''
        return '%s 喜欢吃 %s 修的专业是：%s'%(self.name,self.food,self.pro)
    def __new__(cls, *args, **kwargs):
        '''
        创建对象实例的方法 每调用一次就会生成一个新的对象 cls就是class的缩写

        场景：可以控制创建对象的一些属性限定 经常用来做单例模式的时候来使用
        :param args:
        :param kwargs:
        '''
        print('-------new 函数的执行-----------')
        return object.__new__(cls) # 在这里是真正创建对象实例的
        pass
    pass

xw=Person('计算机','小王','榴莲')
# print('xw=%s'%(id(xw)))
# xw.eat('小王','榴莲')
print(xw)

# 小结 self特点
# self只有在类中定义 实例方法的时候才有意义，在调用时候不必传入相应的参数 而是由解释器 自动去指向
# self的名称是可以更改的，并不是严格意义上的关键字 可以定义成其他的名字，只是约定俗称的定义成self
# self指的是 类实例对象本身，相当于Java中的this

# __new__  和 __init__函数的区别
# __new__类的实例化方法 必须要返回该实例 否则对象就创建不成功
# __init__用来做数据属性的初始化工作 也可以认为是实例的构造方法 接受类实例 self 并对其进行构造
#  __new__ 至少有一个参数是cls 代表要实例化的类， 此参数在实例化时由python解释器自动提供
# __new__ 函数执行要早于 __init__ 函数