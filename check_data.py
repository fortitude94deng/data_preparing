
# coding: utf-8

import os
import sys
import matplotlib.pyplot as plt
#将全部数据索引至字典中
path = "/media/dell/dell/data/remote_sensing/remote/train_image"
dirs = sorted(os.listdir(path))
print(dirs)
files = {}
for index, dir in enumerate(dirs):
    path_ = path + "/" + dir + "/"
    files[int(dir)] = []
    for file in os.listdir(path_):
        files[int(dir)].append(path_+file)
    sys.stdout.write('\r>> Loading data %d/%d'%(index+1, 9))
    sys.stdout.flush()
sys.stdout.write("\n")    
#print(len(files))
#查看各种数据所占比例
file_num = []
for i in range(1, 10):
    file_num.append(len(files[i]))
print(file_num)
plt.bar(range(len(file_num)),file_num)
plt.xlabel('class_id')
plt.ylabel('amount')
plt.ylim(0, 11000)
for x,y in zip(range(len(file_num)),file_num):
    plt.text(x, y+100, '%d' % y, ha='center', va= 'bottom')
plt.show()
#写入valid数据
import random
f = open("./valid.txt", "w+")
valid_data = {}
train_data = {}
for i in range(1, 10):
    valid_data[i] = random.sample(files[i], 200)
    train_data[i] = list(set(files[i]) - set(valid_data[i]))
    for item in valid_data[i]:
        print(item)
        f.write(item+"\n")
f.close()
#查看除去valid的数据
file_num_ = []
for i in range(1, 10):
    file_num_.append(len(train_data[i]))
print(file_num_)
plt.bar(range(len(file_num_)), file_num_)
plt.xlabel('class_id')
plt.ylabel('amount')
plt.ylim(0, 11000)
for x,y in zip(range(len(file_num_)), file_num_):
    plt.text(x, y+100, '%d' % y, ha='center', va= 'bottom')
plt.show()
#写入train数据
f = open("./train.txt", "w+")
for i in range(1, 10):
    for item in train_data[i]:
        print(item)
        f.write(item+"\n")
f.close()
#进行过采样
max_amount = max(file_num_)
for i in range(1, 10):
    for j in range(max_amount-len(train_data[i])):
        train_data[i].append(train_data[i][random.randint(0, file_num_[i-1]-1)])
#可视化数据比例
file_num_ = []
for i in range(1, 10):
    file_num_.append(len(train_data[i]))
print(file_num_)
plt.bar(range(len(file_num_)), file_num_)
plt.xlabel('class_id')
plt.ylabel('amount')
plt.ylim(0, 11000)
for x,y in zip(range(len(file_num_)), file_num_):
    plt.text(x, y+100, '%d' % y, ha='center', va= 'bottom')
plt.show()
#写入过采样的数据
f = open("./train_oversampling.txt", "w+")
for i in range(1, 10):
    for item in train_data[i]:
        print(item)
        f.write(item+"\n")
f.close()

