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