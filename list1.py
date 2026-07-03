# 巢狀 list
list1 = [
    [1,2,3],
    [4,5,6]
]
print(list1[0][0])
print(list1[1][1])
print(list1[1][0])

# list() 建立或轉型
print(list("abc"))
print(list("建立或轉型"))
print(list(range(3)))
print(list((11,22))) # tuple 轉 list 
print(list({"name": "Ben", "phone": "0223255678"})) # 字典轉 list, 是把 key 取出而已

# 重複建立
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]

list2 = [0] * 10
print(list2)
list3 = [[0] * 10] * 2 # 巢狀 list 的複製(重複), 會指向同一個記憶體位置
print(list3)
list3[0][9] = 9
print(list3)

list4 = [[0] * 10 for _ in range(2)] # 推導式
list4[0][9] = 9
print(list4)

list5 = ["a", "b", "b", "b", "c", "d"]
list5[-1] = "z"
print(list5[-1]) # 最後一個
print(len(list5))
print("d" in list5)
print("d" not in list5)
# print(list5.index("d")) # 找不到, 會出錯
print(list5.index("a"))
print(list5.index("z"))
print(list5.count("b"))



# 新增元素
list6 = [1, 2, 3, 4]

# append 加到串列最後
list6.append("a")
list6.append("b")

# extend 搭平加到串列最後
# list6.append(["c", "d"])
list6.extend(["c", "d"])


# 插入
list6.insert(0, "e")

print(list6)

# 刪除元素

list7 = list(range(1, 11))

# 移除 by 值
list7.remove(2)

# 移除 by 索引
del list7[2]
del list7[2:5]

# pop 刪除尾端
list7.pop()
list7.pop(0)
list7.pop(1)

# 清除全部
list7.clear()

print(list7)

# 合併
list8 = [1,2,3]
list9 = [4,5,6]
print(list8 + list9)

list8 += list9
print(list8)

# 解包
list10 = [10, 20, 30]
money1, money2, money3 = list10
print(f"money1 是 {money1}")
print(f"money2 是 {money2}")
print(f"money3 是 {money3}")

# 解包快速實現變數互換
money1, money2 = [money2, money1]
print(f"money1 是 {money1}")
print(f"money2 是 {money2}")

# 傳統變數互換
temp_var = money1
money1 = money2
money2 = temp_var
print(f"money1 是 {money1}")
print(f"money2 是 {money2}")

# 解包與收集剩餘元素(星號解包)
list11 = list(range(1, 11))
# _x1, _x2, *useful_lst = list11
_, _, *useful_lst = list11
print(useful_lst)
*useful_lst2, _, _ = useful_lst
print(useful_lst2)


people = ["Ben", "May", "John", "Cindy"]
leader, *members = people
print(leader)
print(members)

# print(members[3]) # 取用超出索引, 會有 indexError

s = "a,b,c"
list12 = s.split(",")
print(list12)
print(" ".join(list12))


# 邊跑迴圈邊移除有可能會遇到索引位移
# 解決是複製一份出來跑迴圈
# 對原始串列做移除
# .copy() 複製 list (淺拷貝)
# .deepcopy() (深拷貝)
lst = [2, 4, 6, 8]
for num in lst.copy():
    if num % 2 == 0:
        lst.remove(num)

print(lst)
