import time，

list = input('列表:').split(",")
list =[int(list[i]) for i in range(len(list))]
list1 = list.copy()
print(list)
print("简单选择排序：")
for i in range(0, len(list)):
    min_num = list[i]
    for j in range(i, len(list)):
        if min_num >= list[j]:
            min_num = list[j]
            min_loc = j
    list.insert(i,min_num)
    del list[min_loc+1]
    print(i+1,":",list)

list = list1.copy()
print("\n冒泡排序:")
for i in range(0, len(list)):
    for j in range(0, len(list)-i-1):
        if list[j] >= list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp
    print(i+1,":",list)

time.sleep(1)
