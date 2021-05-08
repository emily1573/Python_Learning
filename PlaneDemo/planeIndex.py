#
# plane pro 需求描述：
# 存在4个对象：
# 我方飞机、敌方飞机、我方子弹、敌方子弹
#
# 功能：
#
# 我方飞机可以移动【根据按键来控制】
# 敌方飞机也可以移动【随机的自动移动】
#
# 双方飞机都可以发送子弹
#
# 步骤：
# 1.创建一个窗口
# 2.创建一个我方飞机 根据方向键左右的移动
# 3.给我方飞机添加发射子弹的功能【按下空格键去发送】
# 4.创建一个敌人飞机
# 5.敌人飞机可以自由的移动
# 6.敌人飞机可以自动的发射子弹
#
# 在安装pygame模块时尤其要注意一下
# 如果在pycharm中安装不成功，如下错误：
#   EOFError:EOF when reading a line
# 此时我们就换种思路
# 1.确保在系统层面的python环境里面 已经安装了pygame 一般都可以安装成功
# 2.我们就可以把已经安装好的pygame模块的文件夹拷贝到venv虚拟环境里面

import pygame #引用第三方的模块
from pygame.locals import *
import random
import time

'''
1.实现飞机的显示 并且可以控制飞机的移动【面向对象】
'''
class HeroPlane(object):
    def __init__(self,screen):
        '''
        初始化函数
        :param screen: 主窗体对象
        '''
        self.x=150
        self.y=450
        # 设置要显示内容的窗口
        self.screen=screen
        # 生成飞机的图片对象
        self.imageName='./feiji/hero.jpg'
        self.image=pygame.image.load(self.imageName)
        # 用来存放子弹的列表
        self.bulletList=[]
        pass
    def moveleft(self):
        '''
        左移
        :return:
        '''
        if self.x>0:
            self.x-=10
        pass
    def moveright(self):
        '''
        右移
        :return:
        '''
        if self.x<350-40:
            self.x+=10
        pass
    def display(self):
        '''
        在主窗口中显示飞机
        :return:
        '''
        self.screen.blit(self.image,(self.x,self.y))
        # 完善子弹的展示逻辑
        needDelItemList=[]
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass
        # 重新遍历一下
        for i in needDelItemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display() # 显示子弹的位置
            bullet.move() # 让这个子弹进行移动 下次再显示的时候就会看到子弹在修改后的位置
        pass
    # 发射子弹
    def faBullet(self):
        newBullet=Bullet(self.x,self.y,self.screen)
        self.bulletList.append(newBullet)
        pass
    pass

'''
创建子弹类
'''
class Bullet(object):
    def __init__(self,x,y,screen):
        '''

        :param x:
        :param y:
        :param screen:
        '''
        self.x=x+13
        self.y=y-20
        self.screen=screen
        self.image=pygame.image.load('./feiji/bullet.jpg')
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):
        self.y-=1
        pass
    def judge(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y<0:
            return True
        else:
            return False
    pass

'''
创建敌机类
'''
class EnemyPlane:
    def __init__(self,screen):
        '''
        初始化函数
        :param screen: 主窗体对象
        '''
        # 默认设置一个方向
        self.direction='right'
        # 飞机的默认位置
        self.x = 0
        self.y = 0
        # 设置要显示内容的窗口
        self.screen=screen
        self.bulletList=[]
        # 生成飞机的图片对象
        self.imageName='./feiji/enemy.jpg'
        self.image=pygame.image.load(self.imageName)
        pass
    def display(self):
        '''
        显示敌机以及位置 子弹的信息
        :return:
        '''
        self.screen.blit(self.image,(self.x,self.y))
        # 完善子弹的展示逻辑
        needDelItemList = []
        for item in self.bulletList:
            if item.judge():
                needDelItemList.append(item)
                pass
            pass
        # 重新遍历一下
        for i in needDelItemList:
            self.bulletList.remove(i)
            pass
        for bullet in self.bulletList:
            bullet.display()  # 显示子弹的位置
            bullet.move()  # 让这个子弹进行移动 下次再显示的时候就会看到子弹在修改后的位置
        pass
    def faBullet(self):
        '''
        敌机随机的发射子弹
        :return:
        '''
        num=random.randint(1,50)
        if num==3:
            newBullet=EnemyBullet(self.x,self.y,self.screen)
            self.bulletList.append(newBullet)
        pass
    def move(self):
        '''
        敌机移动随机的
        :return:
        '''
        if self.direction=='right':
            self.x+=1
            pass
        elif self.direction=='left':
            self.x-=1
            pass
        if self.x>350-40:
            self.direction='left'
            pass
        elif self.x<0:
            self.direction='right'
            pass
        pass
    pass

# 敌机的子弹类
class EnemyBullet(object):
    def __init__(self,x,y,screen):
        '''

        :param x:
        :param y:
        :param screen:
        '''
        self.x=x
        self.y=y+10
        self.screen=screen
        self.image=pygame.image.load('./feiji/ebullet.jpg')
        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):
        self.y+=1
        pass
    def judge(self):
        '''
        判断子弹是否越界
        :return:
        '''
        if self.y>500:
            return True
        else:
            return False
    pass

def key_control(HeroObj):
    '''
    定义普通的函数 用来实现键盘检测
    :param HeroObj:
    :return:
    '''
    # 获取键盘事件
    eventList = pygame.event.get()
    for event in eventList:
        if event.type == QUIT:
            print('退出')
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.type == K_a or event.key == K_LEFT:
                print('left')
                HeroObj.moveleft()
                pass

            elif event.type == K_d or event.key == K_RIGHT:
                print('right')
                HeroObj.moveright()
                pass
            elif event.key == K_SPACE:
                print('按下了空格键 SPACE 发射子弹')
                HeroObj.faBullet()
            pass


def main():
    # 首先创建一个窗口 用来显示内容
    screen=pygame.display.set_mode((350,500),depth=32)
    # 设定一个背景图片对象
    background=pygame.image.load('./feiji/background.jpg')
    # 设置一个title
    pygame.display.set_caption('阶段总结-飞机小游戏')

    # 添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./feiji/background.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1) # 循环次数 -1表示无限循环

    # 创建一个飞机对象
    hero=HeroPlane(screen)
    #创建一个敌机对象
    enemyplane=EnemyPlane(screen)

    # 设定要显示的内容
    while True:
        screen.blit(background,(0,0))
        # 显示玩家飞机的图片
        hero.display()
        enemyplane.display() # 显示敌机
        enemyplane.move() # 敌机移动
        enemyplane.faBullet() # 敌机发射子弹
        # 获取键盘事件
        key_control(hero)
        # 更新显示内容
        pygame.display.update()
        # time.sleep(0.5)
        # pygame.time.Clock().tick(30)
    pass
if __name__ == '__main__':
    main()
