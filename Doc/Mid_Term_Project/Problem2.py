import numpy as np
#Step 1
def step_one():
    ran_num = np.abs(np.random.normal(500,150,(150,150)))
    #put the data in diagonal as 0, since the distance to itself should be 0
    np.fill_diagonal(ran_num, 0)
    file = open("Distances.csv","w")
    for i in ran_num:
            file.write(",".join(str(round(item)) for item in i) + "\n")
#Step 2
'''
1. Total_Value: Random integer between 3000 and 15000 for Product A, 4000 to 20000 for 
Product B, and 2000 to 12000 for Product C.
2. Total_Weight: Random integer between 500 and 3000 for Product A, 1000 to 5000 for Product 
B, and 700 to 3500 for Product C.
'''
def step_two():
    total_info = {}
    for i in range(150):
        tv_pa = np.random.randint(3000,15000)
        tv_pb = np.random.randint(4000, 20000)
        tv_pc = np.random.randint(2000, 12000)
    
        tw_pa = np.random.randint(500,3000)
        tw_pb = np.random.randint(1000, 5000)
        tw_pc = np.random.randint(700, 3500)
        total_info[i] = {"Total Value_A":tv_pa, "Total Weight_A":tw_pa,"Total Value_B":tv_pb, "Total Weight_B":tw_pb,"Total Value_C":tv_pc, "Total Weight_C":tw_pc}
    return total_info

#Value_Per_Weight = Total_Value/Total_Weight - Distance * Transportation_Cost
#Transportation fee: 0.012 per distance.
#Step 3
def cal_ratio(dic_data,out_stock_warehouse,help_num,pro_type):
    transportation_cost = 0.12
    file = open('Distances.csv',"r")
    distance_data = [[int(distance) for distance in item.strip().split(',')] for item in file.readlines()]
    # print(distance_data[out_stock_warehouse][help_num])
    distance = distance_data[out_stock_warehouse][help_num]
    total_value = dic_data[help_num].get("Total Value_" + pro_type)
    total_weight = dic_data[help_num].get("Total Weight_" + pro_type)
    ratio = total_value/total_weight - distance * transportation_cost
    return ratio

def step_three(out_warehouse,data_set,pro_type):
    ratio_dic = {}
    for i in range(150):
        if i != ran_warehouse:
            ratio = cal_ratio(data_set, out_warehouse, i, pro_type)
            ratio_dic[i] = ratio

    vw_order_list = []
    len_num = 0
    while len_num < len(ratio_dic):
        max_ratio = -1000000
        max_ratio_key = None
        for key, value in ratio_dic.items():
            # print(key,value)
            # 检查 key 是否已在 vw_order_list 中
            if key in vw_order_list:
                continue
            elif value > max_ratio:
                max_ratio = value
                max_ratio_key = key
        vw_order_list.append(max_ratio_key)
        len_num += 1
    top_three_helper = [[i,ratio_dic[i]] for i in vw_order_list[:3]]
    return top_three_helper

step_one()
ini_data = step_two()
# result = cal_best_ratio(ini_data,0,1,"A")
# #generate random warehouse num
ran_warehouse = np.random.randint(0,149)
for i in ["A","B","C"]:
    Top_three = step_three(ran_warehouse,ini_data,i)
    num = 1
    for item in Top_three:
        warehouse_num, value_per_weight = item[0],item[1]
        print(f"Top {num} helper for the out_of_stock warehouse No:{ran_warehouse} for product {i} is No:{warehouse_num}, which has value per weight as {value_per_weight}")
        num += 1

