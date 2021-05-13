# 文件的操作
# 打开文件 open
# 默认的编码是gbk 这个是中文编码，最好的习惯是在打开文件的时候指定一个编码类型
# fobj=open('./test.txt','w',encoding='utf-8')
# # 开始操作 读、写操作
# fobj.write('hello Python !')
# fobj.write('hello world !')
# fobj.close()

# 以二进制的形式去写数据
# fobj=open('test_1.txt','wb') # str--->bytes
# fobj.write('在乌云和大海之间'.encode('utf-8'))
# fobj.close()

# fobj=open('test.txt','a') # 用于追加数据
# fobj.write('在乌云和大海之间\r\n')
# fobj.write('海燕像黑色的闪电\r\n')
# fobj.close()

# fobj=open('test.txt','a') # 用于追加数据
# fobj.write('在乌云和大海之间')
# fobj.write('海燕像黑色的闪电')
# fobj.write('清明时节雨纷纷\n')
# fobj.write('路上行人欲断魂\n')
# fobj.close()

# 读数据
# f=open('test.txt','rb')
# data=f.read()
# print(data)
# print(data.decode('gbk')) # 读取所有的数据
# print(f.read(12))
# print(f.read())
# print(f.readline()) # 读一行数据
# print(f.readlines(1)) # 返回一个列表数据
# f.close() # 文件对象关闭掉

# with的使用：上下文管理对象
# 优点 自动释放打开关联的对象
with open('test.txt','a') as f:
    # print(f.read())
    f.write('我觉得python非常的好')


# 小结
# 文件读写的几种操作方式
# read r r+ rb rb+
# r r+只读 使用普通读取场景
# rb rb+ 适用于文件 图片 视频 音频 这样文件读取
# write w w+ wb+ wb a ab
# w wb+ w+ 每次都会去创建文件
# 二进制读写的时候 要注意编码问题 默认情况下 我们写入文件的编码是gbk
# a ab a+ 在原有文件的基础之后去【文件指针的末尾】去追加，
# 并不会每次都去创建一个新的文件