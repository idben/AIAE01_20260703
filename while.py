# while 迴圈的基本使用

count = 0

while count <= 5:
    print(f"這是第 {count} 次的執行")
    count += 1
print("-"*30)

# while 猜數字
answer = 8
guess = 0

# while answer != guess:
#     guess = int(input("猜數字 1~10："))
#     if answer != guess:
#         print("猜錯了!! 再試一次")
print("恭喜過關")
print("-"*30)

# while 待辦事項
todo_list = ["買惡魔雞排", "買五桐號", "買炸雞屁股"]
# todo_list.pop() # 刪除 list 的最後一項
#while len(todo_list) > 0:
while todo_list:
    print(todo_list.pop()) # .pop()刪除 list 的最後一項而且會回傳

print(todo_list)