from collections import Counter
import csv
with open('dt.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data=list()
for i in range(len(file_data)):
    n_num=file_data[i][1]
    new_data.append(n_num)
data=Counter(new_data)
mode_data_for_range={
    '50-60':0,
    '60-70':0,
    '70-80':0
}
for height,occurence in data.items():
    if 50<float(height)<60:
        mode_data_for_range['50-60']+=occurence
    elif 60<float(height)<70:
        mode_data_for_range['60-70']+=occurence
    elif 70<float(height)<80:
        mode_data_for_range['70-80']+=occurence
modrange,modoccurence=0,0
for range,occurence in mode_data_for_range.items():
    if occurence>modoccurence:
        modrange,modoccurence=[int(range.split('-')[0]),int(range.split('_')[1])],occurence
mode=float(modrange[0]+modrange[1]/2)
print(f'mode is->{mode:2f}')



