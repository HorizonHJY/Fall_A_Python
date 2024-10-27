def Read_the_dataset(data_path):
    row_num = 1
    result = []
    file = open("Products.csv", 'r')
    # This reads all the lines from the file into a list
    lines = file.readlines()
    #Q1
    for line in lines:
        if row_num % 3 == 0:
            pass
        else:
            store_str = line.strip().split(",")
            result.append(store_str)
        row_num += 1
    return result

#Capicity 850
def get_max_value(weight_list,value_list): #data_set should be a list
    results = {}
    for item in range(len(weight_list)):
        value_of_product =float(value_list[item])
        weight_of_product = float(weight_list[item])
        value_weight_ratio = value_of_product / weight_of_product
    # Store the information for each product and calculate value/weight ratio.
    # Result[product_number]{value,weight,vw_ratio}
        results[item] = {"value": value_of_product, "weight":weight_of_product, "vw_ratio":value_weight_ratio}
    vw_order_list = []
    len_num = 0
    while len_num < len(results):
        max_ratio = 0
        for key, value in results.items():
            print(key, value)
            if key in vw_order_list:
                pass
            else:
                if value['vw_ratio'] > max_ratio:
                    max_ratio = value['vw_ratio']
                    vw_order_list.append(key)
        # for i in results:
        #     if i not in vw_order_list and max_ratio < results[i].get("vw_ratio"):
        #         max_ratio = results[i].get("vw_ratio")
        #         max_product_num = i
        #         vw_order_list.append(max_product_num)
        #     else:
        #         pass
        len_num += 1
    print(vw_order_list)

    #initial for the sum of the result of weight and value
    total_weight = 0
    total_value = 0
    fin_prod_list = []
    stop_loop = True
    while stop_loop is True:
        for item in vw_order_list:
            if total_weight + results[item].get("weight")< 850:
                total_weight += results[item].get("weight")
                total_value += results[item].get("value")
                # fin_prod_list.append(item)
                fin_prod_list.append(results[item].get("vw_ratio"))
            else:
                stop_loop = False
    return fin_prod_list,total_value,total_weight


data_set = Read_the_dataset("Products.csv")
summary = {}
warehouse_num = 1

for i in range(0,len(data_set),2):
    warehouse_pro_list, warehouse_value,warehouse_weight = get_max_value(data_set[i],data_set[i+1])
    summary[warehouse_num] = {"warehouse_pro_list":warehouse_pro_list,"warehouse_value":warehouse_value,"warehouse_weight":warehouse_weight}
    warehouse_num +=1

for i in summary:
    print(i,summary[i].values())

