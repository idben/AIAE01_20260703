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
print("-"*30)

# 巢狀迴圈

for outside in range(1, 10):
    # print(f"外層 = {outside}")
    for inside in range(1, 10):
        # print(f"  內層 = {inside}")
        print(f"{outside} x {inside} = {outside * inside}")
    print("-"*15)


# 實際應用
products = [
    {"name": "筆電", "price": 35000, "category": "3C"},
    {"name": "滑鼠", "price": 800, "category": "3C"},
    {"name": "咖啡豆", "price": 450, "category": "食品"},
    {"name": "鍵盤", "price": 1500, "category": "3C"}
]
print("-"*30)

# 想要搜尋出分類是 3c 的所有資料
# 想要搜尋出單價是 1000 元以下的所有資料
# 想要搜尋出分類是 3c 而且單價是 1000 元的所有資料

results1 = []
results2 = []
results3 = []
for product in products:
    if product["category"] == "3C":
        results1.append(product)
    if product["price"] < 1000:
        results2.append(product)
    if product["category"] == "3C" and product["price"] < 1000:
        results3.append(product)

print(results1)
print(results2)
print(results3)
print("-"*30)

# 實際應用: 改檔名
filenames = ["vacation.jpg", "notes.txt", "dinner.png", "selfie.jpg"]
file_prefix = "2026-07-03_"

results4 = []
for filename in filenames:
    if filename.endswith(".jpg") or filename.endswith(".png"):
        new_filename = f"{file_prefix}{filename}"
        results4.append(new_filename)
print(results4)