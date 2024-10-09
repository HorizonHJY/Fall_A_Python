from IPython.utils.coloransi import value

def Read_the_dataset(data_path):
    row_num = 1
    result = []
    file = open("Products.csv", 'r')
    lines = file.readlines()# This reads all the lines from the file into a list
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
def get_max_value(data_set): #data_set should be a list
    weight_list = data_set[0]
    value_list = data_set[1]
    for item in range(len(weight_list)):
        value_of_product =float(value_list[item])
        weight_of_product = float(weight_list[item])
        value_weight_ratio = value_of_product / weight_of_product
        print(value_weight_ratio)
    # print(data_set[2:])

data_set = Read_the_dataset("Products.csv")
get_max_value(data_set)