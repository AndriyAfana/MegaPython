import requests

url = "https://meowfacts.herokuapp.com/"

language = input("Мова: (ukr або eng): ").strip().lower()

while language not in ["ukr", "eng"]:
    print("Невірна мова! Оберіть 'ukr' або 'eng'.")
    language = input("Мова: (ukr або eng): ").strip().lower()


count = int(input("Кількість фактів (1-5): "))

while not 1 <= count <= 5:
    count = int(input("Кількість фактів (1-5): "))



response = requests.get(url, params={
    'lang': language,
    'count': count
})

if response.ok:
    as_json = response.json()
    facts = as_json['data']

    print('Факти:')
    for fact in facts:
        print(f"· {fact}")
else:
    print(f"Сталася помилка під час отримання данних)")
