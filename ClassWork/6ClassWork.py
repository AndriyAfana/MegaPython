def input_int(message="Введіть число:"):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("Введено некоректне значення, спробуйте ще раз")

while True:
    try:
        a = input_int("Введіть число а: ")
        b = input_int("Введіть число b: ")
        print(f"Результат ділення: {a} / {b} = {a / b}")
    except ZeroDivisionError:
        print("На нуль ділити не можна! Введіть інше значення для числа b.")
        b = input_int("Введіть число b: ")
        print(f"Результат ділення: {a} / {b} = {a / b}")
        continue
    except Exception as pomulochka:
        print(f"Щось пішло не так: {pomulochka}")

    hz = input("Хочете продовжити (так/ні): ").lower()
    if hz != "так":
        print("Ну і йди звідси.")
        break
        