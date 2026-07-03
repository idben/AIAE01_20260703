# list 的切片

list1 = list(range(0, 6))
print(list1[1:4])
print(list1[:3])
print(list1[3:])
print(list1[::2])
print(list1[::-1]) # 返轉


# list1[1:3] = [] # 刪除串列指定區間
# list1[1:3] = ["a", "b"] # 取代
# list1[1:3] = ["a", "b", "c"] # 取代個數不同時, 會自動調整
list1[1:1] = ["a", "b", "c"] # 插入

print(list1)


# enumerate
# 第二個參數是起始的索引
list2 = ["a", "b", "c"]
for index, value  in enumerate(list2, 101):
    print(f"{index}. {value}")