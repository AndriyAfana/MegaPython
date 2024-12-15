class Car:
    make = ""
    model = ""
    year = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        print(f"{self.make}, {self.model}, {self.year}")

car1 = Car("Тесла", "model S", 2024)
car1.get_info()