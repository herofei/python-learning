#! python3

import re

phoneReg = re.compile(r'(\d{3})-\d{3}-\d{4}')
match = phoneReg.search('My number is 415-555-4545!!!444-666-5555!!!')

# 匹配成功会返回一个Match对象，匹配失败会返回None
print(match)

# 返回匹配后的字符串(只返回找到的第一个字符串)
print(match.group())

# 返回匹配字符串中的捕获组
print(match.group(1))

# 返回所有匹配的字符串列表, 如果有捕获组就返回元组列表
print(phoneReg.findall('My number is 415-555-4545!!!444-666-5555!!!'))
