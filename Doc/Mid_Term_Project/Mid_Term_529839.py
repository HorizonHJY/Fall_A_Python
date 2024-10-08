file = open("Products.csv", 'r')
lines = file.readlines()  # This reads all the lines from the file into a list
num = 0
for line in lines:
    print(f'No.{num} : {line}')
    print(type(line))
    num += 1

