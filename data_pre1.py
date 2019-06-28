import os
import sys
import matplotlib.pyplot as plt
path = "/media/dell/dell/data/遥感/train"
dirs = sorted(os.listdir(path))
files = {}
for index, dir in enumerate(dirs):
    path_ = path + "/" + dir + "/"
    files[str(dir)] = []
    for file in os.listdir(path_):
        files[str(dir)].append(path_+file)
    sys.stdout.write('\r>> Loading data %d/%d'%(index+1, 45))
    sys.stdout.flush()
sys.stdout.write("\n") 
print(len(files['停机坪']))
file1=[]
for key,value in files.items():
    file1.append(key)
print(file1)

file_num = []
for i in file1:
    file_num.append(len(files[i]))
print(file_num)
plt.bar(range(len(file_num)),file_num)
plt.xlabel('class_id')
plt.ylabel('amount')
plt.ylim(0, 11000)
for x,y in zip(range(len(file_num)),file_num):
    plt.text(x, y+100, '%d' % y, ha='center', va= 'bottom')
plt.show()

import random
f = open("/home/dell/Desktop/train.txt", "w+")
valid_data = {}
train_data = {}
for i in file1:
    #valid_data[i] = random.sample(files[i], 200)
    #train_data[i] = list(set(files[i]) - set(valid_data[i]))
    train_data[i] = list(set(files[i]))
    for item in train_data[i]:
        print(item)
        f.write(item+"\n")
f.close()

file_num_ = {}
for i in file1:
    file_num_[i]=(len(train_data[i]))
print(file_num_)
print(len(file_num_))

max_amount = max(file_num_.values())
for i in file1:
    for j in range(max_amount-len(train_data[i])):
        train_data[i].append(train_data[i][random.randint(0, file_num_[i])])

file_num_ = []
for i in file1:
    file_num_.append(len(train_data[i]))
print(file_num_)
plt.bar(range(len(file_num_)), file_num_)
plt.xlabel('class_id')
plt.ylabel('amount')
plt.ylim(0, 12000)
for x,y in zip(range(len(file_num_)), file_num_):
    plt.text(x, y+100, '%d' % y, ha='center', va= 'bottom')
plt.show()

f = open("/home/dell/Desktop/train_oversampling.txt", "w+")
for i in file1:
    for item in train_data[i]:
        print(item)
        f.write(item+"\n")
f.close()










































