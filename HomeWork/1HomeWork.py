ball = input("Який бал ви отримали: ")
ball = int(ball)
if ball < 0 or ball > 100:
    print("Ви не можете отримати такий бал")
elif ball < 50:
    print("Незадовільно")
elif ball < 70 and ball > 49:
    print("Задовільно")
elif ball < 90 and ball > 69:
    print("Добре")
elif ball < 101 and ball > 89:
    print("Відмінно")

