import sys
import argparse
# print('参数个数为：', len(sys.argv),'个参数')
# print('参数列表：', str(sys.argv[1:]))

# 创建一个解析器对象
parse=argparse.ArgumentParser(prog='系统登录',usage='%(prog)s [options] usage',
                              description='编写自定义命令行的文件',epilog='my-epilog')
# 添加位置参数【必选参数】
parse.add_argument('loginType',type=str,help='登陆系统类型')
# parse.add_argument('age',type=str,help='你的年龄')

# 添加可选参数
# parse.add_argument('-s','--sex',action='append',type=str,help='你的性别')

# 限定范围
parse.add_argument('-u',dest='user',type=str,help='你的用户名')
parse.add_argument('-p',dest='pwd',type=str,help='你的密码')


result=parse.parse_args()  # 开始解析参数
# print(result.name,result.age,result.sex)

# print(parse.print_help())

if (result.user=='root' and result.pwd=='111111'):
    print('login sucess!')
else:
    print('login failed!')