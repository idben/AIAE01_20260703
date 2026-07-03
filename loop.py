# 迴圈的終止
nums = list(range(1, 12, 2))
ans = 7
for num in nums:
    print(f"正在檢查數字: {num}")
    if num == ans:
        print(f"找到了!目標是 {ans}")
        break
    