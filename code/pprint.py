#! python3

import pprint

message = 'Hello world.I am learning python.It is like javascript.'
countMap = {}
for char in message: 
    countMap.setdefault(char, 0)
    countMap[char] += 1

pprint.pprint(countMap)
print(pprint.pformat(countMap))