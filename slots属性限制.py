# 作用
# 限制要添加的实例属性
# 节约内存空间

class Student(object):
    __slots__ = ('name','age','score')
    def __str__(self):
        return '{}....{}'.format(self.name,self.age)
    pass

xw=Student()
xw.name='小王'
xw.age=20
xw.score=60 # 没有在范围内 所以报错
# print(xw.__dict__) # 所有可以用的属性都在这里存着 不足的地方就是占用内存空间打
# 可以看到 在定义了slots变量之后 student类的实例已经不能随意创建不在__slots__定义的属性了
# 同时还可以看到实例当中也不再有__dict__
# print(xw)

# 在继承关系当中使用 __slots__
# 子类未声明 __slots__时，那么是不会继承父类的 __slots__,此时子类是可以随意的为属性赋值的
# 子类声明了 __slots__时，继承父类的__slots__。也就是子类__slots__的范围是为其自身+父类的slots

class subStudent(Student):
    __slots__ = ('gender','pro')
    pass

ln=subStudent()
ln.gender='男'
ln.pro='计算机'
print(ln.gender,ln.pro)