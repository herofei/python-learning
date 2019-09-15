### 列表与字典

```python
mapA = {
    'name': 'hello',
    'value': 'world'
}

mapB = {
    'value': 'world',
    'name': 'hello'
}

listA = ['hello', 'world']
listB = ['hello', 'world']
listC = ['world', 'hello']

# 打印出来是True
print(mapA == mapA)

# 打印出来是True
print(listA == listB)

# 打印出来是False
print(listA == listC)
```

不同的列表和字典可以进行比较，只要对应的键值对都一样，则返回为True