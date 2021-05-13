# tell 返回指针当前所在的位置
# 对于中文，每次读取到的汉字占用2个字符
# with open('test.txt','r') as f:
#     print(f.read(3))
#     print(f.tell())
#     print(f.read(2))
#     print(f.tell())
#     pass
# truncate 可以对源文件进行截取操作
# fobjB=open('test.txt','r')
# print(fobjB.read())
# fobjB.close()
# print('截取之后的数据---------')
#
# fobjA=open('test.txt','r+')
# fobjA.truncate(15) # 保留前15个字符
# print(fobjA.read())
# fobjA.close()

# seek 可以控制光标所在的位置
with open('test.txt','rb') as f:
    f.seek(4,0) # 光标从0的位置开始 向前移动4个字符
    data=f.read(2)
    print(data.decode('gbk'))
    f.seek(-2,1) # 1表示从当前位置开始移动，相当于光标又设到了0的位置
    print(f.read(6).decode('gbk'))
    f.seek(-6,2) # 表示光标移到了末尾处
    print(f.read(6).decode('gbk'))

# 对于这种情况，用‘r'这种模式打开文件，在文本文件中，
# 没有使用二进制的选项打开文件，只允许从文件的开头计算相对位置
# 从文件尾部或者当前计算的话，就会出现异常