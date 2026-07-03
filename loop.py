# 迴圈的終止
nums = list(range(1, 12, 2))
ans = 7
for num in nums:
    print(f"正在檢查數字: {num}")
    if num == ans:
        print(f"找到了!目標是 {ans}")
        break

print("-"*30)
datas = [
    {"id": 1, "name": "Ben", "cell": "0988777888"},
    {"id": 2, "name": "May", "cell": "0938222111"},
    {"id": 3, "name": "John", "cell": "0933456789"}
]

for data in datas:
    if data["cell"].startswith("0988"):
        print(f"姓名是: {data["name"]}")
        break
print("-"*30)

# 迴圈的跳過
for i in range(1, 6):
    if i == 3:
        continue
    print(f"正在處理的數字是: {i}")

# 奇數相加, 用 continue 跳過偶數
total = 0
for num in range(1, 21):
    if num % 2 == 0:
        continue
    total += num
print(f"total = {total}")