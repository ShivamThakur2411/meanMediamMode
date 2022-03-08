import csv

with open("height_weight.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

total=0
for x in new_data:
    total = total + x

n = len(new_data)

mean = total/n
print("Mean of the data is - " + str(mean))