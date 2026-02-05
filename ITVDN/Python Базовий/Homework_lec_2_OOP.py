#№2 Наследование
"""
Завдання: Розробка класу для керування персоналом
Створіть систему класів, яка моделюватиме структуру персоналу в організації. Почніть зі
створення базового класу Employee, а потім розширте його для різних типів працівників.
Клас Employee
Атрибути екземпляру класу:
• name (рядок): Ім'я працівника.
• age (ціле число): Вік працівника.
• salary (число з плаваючою точкою): Заробітна плата працівника.
Методи класу:
• __init__(self, name, age, salary): Конструктор класу, який приймає name, age і salary та
ініціалізує відповідні атрибути.
• get_details(self): Повертає рядок із деталями працівника (ім'я, вік, заробітна плата).
Клас Manager (спадкоємець класу Employee)
Додаткові атрибути екземпляру класу:
• team (список об'єктів класу Employee): Список працівників, які підпорядковуються
менеджеру.
Додаткові методи:
• __init__(self, name, age, salary, team): Конструктор класу, який приймає додатково список
працівників для ініціалізації атрибута team.
• add_employee(self, employee): Додає працівника до списку team.
• remove_employee(self, employee): Видаляє працівника зі списку team.
• get_team_details(self): Виводить інформацію про всіх працівників у команді менеджера.
Завдання для виконання:
• Створіть об'єкт класу Employee з довільним іменем, віком і зарплатою.
• Створіть об'єкт класу Manager з довільним іменем, віком, зарплатою та порожнім
списком team.
Додайте декілька об'єктів класу Employee до команди менеджера за допомогою методу
add_employee.
• Видаліть одного працівника з команди менеджера за допомогою методу
remove_employee.
• Виведіть деталі менеджера та його команди за допомогою методів get_details та
get_team_details.
"""


class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def get_details(self):
        print(f"Details of employee:"
              f"Name: {self.name},\n "
              f"Age: {self.age},\n"
              f"Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, age, salary, team):
        super().__init__(name, age, salary)
        self.team = team

    def add_employee(self, employee):
        self.team.append(employee)
        print(f"Employee {employee.name} has been added.")

    def remove_employee(self, employee):
        self.team.remove(employee)
        print(f"Employee {employee.name} has been removed.")

    def get_team_details(self):
        print(f"Employees of manager {self.name}:")
        for emp in self.team:
            emp.get_details()


e1 = Employee("Vasiliy", 28, 30000)
e2 = Employee("Petro", 30, 32000)
e3 = Employee("Andriy", 26, 28000)

manager = Manager("Valera", 32, 100000, team=[])

manager.add_employee(e1)
manager.add_employee(e2)
manager.add_employee(e3)
manager.get_team_details()

"""
Завдання 1: Реалізація класу для обробки геометричних фігур
Створіть клас Shape, який буде мати атрибут name (назва фігури) і метод area(), який повертатиме
площу фігури (за замовчуванням - 0). Створіть підкласи Rectangle і Circle, які успадковуватимуть
клас Shape і перевизначатимуть метод area() для обчислення площі прямокутника і кола
відповідно.
"""
print('-' * 30)

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, a, b):
        super().__init__("Rectangle")  # имя фигуры
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

rect = Rectangle(5, 10)
print(f"{rect.name} area: {rect.area()}")

circle = Circle(7)
print(f"{circle.name} area: {circle.area()}")



class Circle(Shape):
    def __init__(self, radius):
        super().__init__(name)
        self.radius = raduis

    def area(self, radius):
        return 3.14 * radius ** 2


"""
Завдання 2: Реалізація класу для обробки транспортних засобів
Створіть базовий клас Vehicle, який матиме атрибут speed (швидкість) і метод move(), який
виводить повідомлення про рух зі вказаною швидкістю. Створіть підкласи Car і Bicycle, які
успадковуватимуть клас Vehicle і перевизначатимуть метод move() для виведення
спеціалізованого повідомлення, відповідного до типу транспортного засобу.
"""
print('-' * 30)

class Vehicle:
    def __init__(self, speed):
        self.speed = speed
    def move(self,direction):
        print(f"Object is moved with {self.speed} to {direction}")

class Car(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)
    def move(self, direction):
        print(f"Car is moved with {self.speed} km/h to {direction}")

class Bicycle(Vehicle):
    def __init__(self, speed):
        super().__init__(speed)
    def move(self, direction):
        print(f"Bicycle is moved with {self.speed} km/h to {direction}")

v = Vehicle(50)
v.move("north")

c = Car(120)
c.move("east")

b = Bicycle(25)
b.move("south")

