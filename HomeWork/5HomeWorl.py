result = []

def divider(a, b):
    if a < b:
        raise ValueError("a < b")
    if b > 100:
        raise IndexError("b > 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key in data:
    try:
        a = int(key)
        b = int(data[key])
        res = divider(a, b)
        result.append(res)
    except ZeroDivisionError:
        print(f"На нуль ділити не можна. Ділення {key} на {data[key]} неможливе.")
    except ValueError  as e:
        print(f"Ділене менше ніж дільник. Ділення {key} на {data[key]} неможливе.")
    except TypeError  as e:
        print(f"Інформація некоректна. Ділення {key} на {data[key]} неможливе.")

print(result)