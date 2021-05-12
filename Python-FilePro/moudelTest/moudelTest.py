# 模块的制作说明

# __all__魔术变量的作用是 如果在一个文件中存在__all__变量，那么也就意味着
# 变量中的元素会被from XX import * 时会被导入
__all__=['add','diff']

def add(x,y):
    '''
    普通的函数
    :param x:
    :param y:
    :return:
    '''
    return x+y
def diff(x,y):
    return x-y
def printInfo():
    return '这是我自定义模块里的方法'

# 测试
if __name__=='__main__':
    res=add(2,5)
    print('测试模块，%s'%res)
    print('模块__name__变量=%s'%__name__)