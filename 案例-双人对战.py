# 决战紫禁之巅有两个人物，西门吹雪以及叶孤城
# 属性：
# name 玩家的名字
# blood 玩家血量
#
# 方法：
# tong（）捅对方一刀，对方掉血10滴
# kanren（）砍对方一刀，对方掉血15滴
# chiyao（）吃一颗药，补血10滴
# __str__ 打印玩家状态
#
# 第一步 需要先去定义一个类【角色类】
import time
class Role:
    def __init__(self,name,hp):
        '''
        构造初始化函数
        :param name:角色名
        :param hp:血量
        '''
        self.name=name
        self.hp=hp
        pass
    def tong(self,enemy):
        '''
        捅一刀
        :param enemy:敌人
        :return:
        '''
        # 敌人减掉10滴血
        enemy.hp-=10
        info='【%s】捅了【%s】一刀'%(self.name,enemy.name)
        print(info)
        pass
    def kanren(self,enemy):
        '''
        砍人
        :param enemy: 敌人
        :return:
        '''
        # 敌人减掉15滴血
        enemy.hp -= 15
        info = '【%s】砍了【%s】一刀' % (self.name, enemy.name)
        print(info)
        pass
    def chiyao(self):
        '''
        吃药
        :return:
        '''
        self.hp+=10
        info = '【%s】吃了一颗补血药，增了10滴血' % (self.name)
        print(info)
        pass
    def __str__(self):
        return  '%s 还剩下 %s 的血量'%(self.name,self.hp)
    pass

# 创建2个【西门吹雪、叶孤城】实例化对象
xmcx=Role('西门吹雪',100)
ygc=Role('叶孤城',100)
while True:
    if xmcx.hp<=0 or ygc.hp<=0:
        #满足条件就退出循环
        break
    xmcx.tong(ygc)  # 西门吹雪捅了叶孤城一刀
    print(ygc)
    print(xmcx)
    print('**************************')
    ygc.kanren(xmcx)
    print(ygc)
    print(xmcx)
    print('**************************')
    xmcx.chiyao()
    print(ygc)
    print(xmcx)
    time.sleep(1)
    pass
print('对战结束')




