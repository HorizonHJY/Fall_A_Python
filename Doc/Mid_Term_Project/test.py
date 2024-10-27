products = {
    'product1': {'weight': 10, 'value': 100, 'ratio': 11},
    'product2': {'weight': 20, 'value': 150, 'ratio': 7.5},
    'product3': {'weight': 5, 'value': 50, 'ratio': 13},
    # 更多产品...
}
# 初始化最大ratio和对应的键
max_ratio = float('-inf')
max_ratio_key = None

vw_order_list = []
len_num = 0

while len_num < len(products):
    max_ratio = 0
    max_ratio_key = None
    for key, value in products.items():
        print(key, value)
        # 检查 key 是否已在 vw_order_list 中
        if key in vw_order_list:
            continue
        elif value['ratio'] > max_ratio:
            max_ratio = value['ratio']
            max_ratio_key = key
    # 在找到的最大 ratio 对应的键不为空的情况下，将其添加到列表
    # if max_ratio_key:
    vw_order_list.append(max_ratio_key)
    len_num += 1

print(vw_order_list)
