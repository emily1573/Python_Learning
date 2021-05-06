class Animal:
    def __init__(self,name):
        self.name=name
        print('这是构造初始化方法')
        pass
    def __del__(self):
        # 主要的应用就是来操作 对象的释放 一旦释放完毕 对象便不能再使用
        print('当在某个作用域下面 没有被使用【引用】的情况下 解析器会自动的调用次函数 来释放内存空间')
        print('这是析构方法')
        print('%s 这个对象被彻底清理了，内存空间也释放了'%self.name)
        pass
    pass

cat=Animal('猫')
print(cat.name)
del cat # 手动的去清理删除对象 会指定 del 函数
input('程序等待中。。。。。。')
# print('*'*40)
# dog=Animal('柯基小狗')