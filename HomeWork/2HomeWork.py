a = input("Введіть число a: ")
b = input("Введіть число b: ")
a = int(a)
b = int(b)
с = input("Яку дію будемо здійснювати: ")
summa = a + b
riznuzya = a - b
dobytok = a * b
chastka = a / b
if с == "+":
    print(summa)
elif с == "-":
    print(riznuzya)
elif с == "*":
    print(dobytok)
elif с == "/":
    if b == 0:
        print("ДІЛИТИ НА НУЛЬ НЕ МОЖНА ТИ ЩО ЦЕЖ 2 КЛАС")
    print(chastka)
else:
    print("Не може такого бути")
