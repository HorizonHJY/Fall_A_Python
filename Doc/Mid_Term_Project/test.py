products = {
    'product1': {'weight': 10, 'value': 100, 'ratio': 11},
    'product2': {'weight': 20, 'value': 150, 'ratio': 7.5},
    'product3': {'weight': 5, 'value': 50, 'ratio': 13},
    # 更多产品...
}
# 初始化最大ratio和对应的键
max_ratio = float('-inf')
max_ratio_key = None

# 遍历字典，找到最大ratio对应的键
for key, value in products.items():
    print(key,value)
    if value['ratio'] > max_ratio:
        max_ratio = value['ratio']
        max_ratio_key = key

# 输出最大ratio对应的键
print(max_ratio_key)
