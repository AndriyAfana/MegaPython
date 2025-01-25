import random

class Person:
    def __init__(self, name, health, mood, money):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return (f"                   \n"
                f"    {self.name}    \n"
                f"Здоров'я: {self.health}\n"
                f"Настрій: {self.mood}\n"
                f"Капітал: {self.money}"
                f"                   \n")

    def change_state(self, health=0, mood=0, money=0):
        self.health += health
        self.mood += mood
        self.money += money

        if self.health > 300:
            self.health = 300
        if self.health < 0:
            raise Exception(f"                   \n"
                            f"Людина померла\n"
                            f"                   \n")
        if self.mood < 0:
            raise Exception(f"                   \n"
                            f"Людина впала в депресію\n"
                            f"                   \n")
        if self.money < 0:
            raise Exception(f"                   \n"
                            f"Людина збанкрутувала\n"
                            f"                   \n")

    def do(self, action):
        if type(action) == Action:
            self.change_state(health=action.health, mood=action.mood, money=action.money)
        elif type(action) == Work:
            money_gain = action.money * 1.1 if self.mood > 90 else action.money
            self.change_state(health=action.health, mood=action.mood, money=money_gain)
        elif type(action) == Rest:
            mood_gain = action.mood * 0.8 if self.health < 40 else action.mood
            self.change_state(health=action.health, mood=mood_gain, money=action.money)

class Action:
    def __init__(self, name, health, mood, money):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class Work(Action):
    pass

class Rest(Action):
    pass

persons = [
    Person(name="Luffy", health=100, mood=100, money=50),
    Person(name="Nami", health=80, mood=90, money=30),
    Person(name="Zoro", health=70, mood=85, money=20)
]

actions = [
    Work(name="Піти на завод", health=-10, mood=-15, money=100),
    Rest(name="Сходити в парк", health=5, mood=20, money=-5),
    Action(name="Піти в лікарню", health=20, mood=-5, money=-20)
]

while persons:
    for person in persons[:]:
        try:
            action = random.choice(actions)
            person.do(action)
            print(person)
        except Exception as e:
            print(f"{person.name} вилетів: {e}")
            persons.remove(person)
    print("\n-------------------------------------\n")
