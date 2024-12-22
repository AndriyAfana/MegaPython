def input_int(message="Введіть індекс: "):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError:
            print("Введено некоректне значення, спробуйте ще раз.")

fruits = ["","Яблуко", "Банан", "Апельсин", "Ківі", "Виноград"]

print("Список фруктів:")
for chislo in range(1, len(fruits)):
    print(f"{chislo}: {fruits[chislo]}")

while True:
    try:
        index = input_int("Введіть індекс фрукта, який хочете обрати: ")


        print(f"Ви обрали: {fruits[index]}")
        break

    except IndexError:
        print("Немає фрукта з таким індексом. Спробуйте ще раз.")

    except Exception as pomulochka:
        print(f"Звемо вчителя щоб розібрати помилку: {pomulochka}")