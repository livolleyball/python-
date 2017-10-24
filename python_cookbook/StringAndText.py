# coding:utf8

# line='abc fjdk; adef, hhda,    foo'
# import re
# print(re.split(r'[;,\s]\s*',line))
# # comma(,),semicolon(;) or whitespace followed by any amount of extra whitespace
# fields=re.split(r'(;|,|\s)\s*',line)
# print(fields)
# values=fields[::2]
# delimiters=fields[1::2]
# print(values)
# print(delimiters)


filename = 'spam.txt'
print(filename[-4:] == '.txt')
url = 'http://wwww.baidu.com'
print(url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:')

import re

print(re.match('http:|https:|ftp:', url))
m = re.match('http:|https:|ftp:', url)
if m:
    print(m.group(0))
else:
    print('not match')


a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0))  # 123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(1))  # 123
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(2))  # abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(3))  # 456

# 究其因
# 1. 正则表达式中的三组括号把匹配结果分成三组
#  group() 同group（0）就是匹配正则表达式整体结果
#  group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。
# 2. 没有匹配成功的，re.search（）返回None
# 3. 当然郑则表达式中没有括号，group(1)肯定不对了。
