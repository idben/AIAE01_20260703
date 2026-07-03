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

list5 = ["a", "b", "c", "d"]
list5[-1] = "z"
print(list5[-1]) # 最後一個