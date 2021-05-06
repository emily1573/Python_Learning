# 序列操作 str 元组 list
# all（） 对象中的元素除了是0，空，false外都算true，所有的元素都为True 结果才为True
# 可以判断数据类型是不是我们需要的，结果类型是boole值
# print(all([])) # TRUE
# print(all(())) # TRUE
# print(all([1,2,4,False]))
# print(all([1,2,4]))
# print(all((3,4,0)))
# any 类似于逻辑运算符or 的判断，只要有一个元素为True 结果就为True
# print(any(('',False,0))) # False
# print(any((3,4,5,0)))
# sort 和 sorted
li=[2,45,1,67,23,10]
# li.sort() # list的排序方法 直接修改的原始对象
tupArray=(2,45,1,67,23,10)
# print('---------排序之前---------{}'.format(li))
# # varList=sorted(li) # 升序排列
# varList=sorted(li,reverse=True) # 降序排列
# print('---------排序之hou---------{}'.format(varList))
# varRs=sorted(tupArray,reverse=False)
# print(varRs)
# zip() 就是用来打包的
# s1=['a','b','c','d','e']
# s2=['你','我','他','和']
# # print(list(zip(s1))) # 压缩一个数据，里边的数据都是以元组类型压缩
# zipList=zip(s1,s2)  # 两个参数
# print(list(zipList))
def printBookInfo():
    '''
    zip函数的使用
    :return:
    '''
    books=[] #存储所有的图书信息
    id=input('请输入编号：每个项以空格分隔')
    bookname = input('请输入书名：每个项以空格分隔')
    bookPos = input('请输入位置：每个项以空格分隔')
    idList=id.split(' ')
    nameList = bookname.split(' ')
    posList = bookPos.split(' ')

    bookInfo=zip(idList,nameList,posList)
    for bookItem in bookInfo:
        '''
        遍历图书信息进行存储
        '''
        dictInfo={'编号':bookItem[0],'书名':bookItem[1],'位置':bookItem[2]}
        books.append(dictInfo) # 将字典对象添加到list容器
        pass
    for item in books:
        print(item)

# printBookInfo()
# enumerate 函数用于将一个可遍历的数据对象
# （如列表、元组或字符串）组合为一个索引序列，同时列出数据和数据下标，
# 一般用在for循环当中

listObj=['a','b','c']
# for index,item in enumerate(listObj,5):
#     print(index,item)
#     pass
dicObj={}
dicObj['name']='李易峰'
dicObj['hobby']='唱歌'
dicObj['pro']='艺术设计'
# print(dicObj)
for item in enumerate(dicObj):
    print(item[0])