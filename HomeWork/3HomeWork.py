class Employee:
    name = ""
    position = ""
    salary = 0

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        print(f"Заробітня плата працівника {self.name}: {self.salary} $")

People1 = Employee("Тоні Старк", "Гений", 1000000)
People1.get_salary_info()