class Animal:
    def __init__(self):
        self.color='红色'
        pass
    # python中，如果不重写__new__默认结构如下
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
        return object().__new__(cls, *args, **kwargs)
    pass

tigger=Animal() # 实例化的过程会自动调用 __new__去创建实例

# 在新式类中__new__才是真正的实例化方法，为类提供外壳制造出实例框架，然后调用该框架的构造方法__init__进行丰满操作
# 比喻建房子__new__方法负责开发地皮 打地基 并将原料存放在工地，而__init__方法负责从工地取材料建造出地皮
