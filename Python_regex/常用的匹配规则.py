# . 点的使用 匹配除了换行符之外的字符
import re
data='a1aaa'
names='李达','李明','小王','小李'
pattern='李.'  # 匹配规则

for name in names:
    res=re.match(pattern,name)
    if res:
        print(res.group())