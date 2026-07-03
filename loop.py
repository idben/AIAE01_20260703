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