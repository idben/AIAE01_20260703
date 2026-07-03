# while 迴圈的基本使用

count = 0

while count <= 5:
    print(f"這是第 {count} 次的執行")
    count += 1
print("-"*30)


answer = 8
guess = 0

while answer != guess:
    guess = int(input("猜數字 1~10："))
    if answer != guess:
        print("猜錯了!! 再試一次")
print("恭喜過關")