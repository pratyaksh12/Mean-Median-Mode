import csv
with open('dt.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data=[]
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(float(n_num))
n=len(new_data)
tot=0
for i in new_data:
    tot+=i
mean=tot/n
print('mean of the given data is:',mean)