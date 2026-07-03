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

# zip 同時走訪
# 走訪的串列長度不同時, 會以較短的為主, 不會產生錯誤
# 同時走訪的組數不限
names = ["Ben", "Amy", "Kai", "Tom"]
scores = [90, 80, 100]
grades = ["甲", "乙", "優"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name} 的分數是 {score}，{grade}等")


# 推導式
# 傳統寫法, 參考的串列和迴圈分兩塊來寫
nums = [1, 2, 3]
squares = []

for num in nums:
    squares.append(num * num)

# 推導式
squares2 = [num*num  for num in nums]

print(squares)
print(squares2)

print([str(n) for n in range(1, 21)])

# 收集 1~20 可以被 3 整除的
print([n for n in range(1, 21) if n % 3 == 0])


words = ["hello", "world"]
print([w.upper() for w in words])

words = ["apple", "banana", "cherry"]
print([len(w) for w in words])

print([num for num in range(1, 21) if num % 2 == 0])
print([num for num in range(1, 21) if num % 2 == 1])

numbers = [-3, -1, 0, 2, 5, -7, 8]
print([number  for number in numbers if number >= 0])