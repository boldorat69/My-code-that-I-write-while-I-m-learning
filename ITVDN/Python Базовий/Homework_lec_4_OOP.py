#№4 Полиморфизм

"""
Завдання: Звуки тварин
Створіть базовий клас Animal, який містить метод make_sound(), що повертає рядок "The animal
makes a sound".
Реалізуйте підкласи:
• Doп
• Перевизначає метод make_sound(), повертаючи "Woof-woof".
• Cat
• Перевизначає метод make_sound(), повертаючи "Meow".
• Cow
• Перевизначає метод make_sound(), повертаючи "Moo".
Створіть список об'єктів різних тварин та викличте метод make_sound() для кожного,
демонструючи поліморфізм у дії.
"""


class Animal:
    def make_sound(self):
        return "The animal makes a sound"


class Dog(Animal):
    def make_sound(self):
        return "Woof-woof"


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Cow(Animal):
    def make_sound(self):
        return "Moo"


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.make_sound())

"""
Завдання 1: Поліморфізм через перевизначення методів
Створіть базовий клас Transport, який має метод move(), що повертає "The transport is moving".
Створіть підкласи Car, Bike та Airplane, які перевизначають метод move(), повертаючи відповідні
повідомлення:
• Car: "The car is driving".
• Bike: "The bike is riding".
• Airplane: "The airplane is flying".
"""


class Transport:
    def move(self):
        return "The transport is moving"


class Car:
    def move(self):
        return "The car is driving"


class Bike:
    def move(self):
        return "The bike is riding"


class Airplane:
    def move(self):
        return "The airplane is flying"


transports = [Car(), Bike(), Airplane()]

for transport in transports:
    print(transport.move())

"""
Завдання 2: Поліморфізм через функції
Створіть класи Rectangle та Circle, кожен з яких має метод get_area(), що обчислює площу
відповідної фігури.
Напишіть функцію print_area(shape), яка приймає об'єкт будь-якої фігури та викликає його метод
get_area(), друкуючи результат у форматі:
"The area is: <значення>".
"""

print("-" * 30)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        print(f"The area is: {self.length * self.width}")


class Circle:
    def __init__(self, circle_radius):
        self.circle_radius = circle_radius

    def get_area(self):
        square_circle = 3.1415 * (self.circle_radius ** 2)
        print(f"The area is: {square_circle}")


rectangle = Rectangle(5, 10)
circle = Circle(10)

rectangle.get_area()
circle.get_area()

"""
Завдання 3: Поліморфізм через магічні методи
Створіть класи Vector2D та Vector3D, які представляють вектори у 2D та 3D просторах відповідно.
Реалізуйте для них магічний метод __add__(), який дозволяє складати вектори одного типу через
+.
Переконайтеся, що операція додавання працює коректно для двовимірних та тривимірних
векторів, наприклад:
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
result = v1 + v2
print(result) # Expected output: Vector2D(4, 6)
"""

print("-" * 30)
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Цей метод спрацьовує, коли ми пишемо v1 + v2
    def __add__(self, other):
        # Ми створюємо НОВИЙ об'єкт того ж класу
        # Додаємо x до x, а y до y
        return Vector2D(self.x + other.x, self.y + other.y)

    # Цей метод потрібен, щоб print() виводив гарний текст, а не адресу в пам'яті
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        # Тут додаємо  три координати
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

# Перевірка
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)
result2d = v1 + v2
print(result2d)  # Виведе: Vector2D(4, 6)

v3 = Vector3D(1, 2, 3)
v4 = Vector3D(4, 5, 6)
result3d = v3 + v4
print(result3d)  # Виведе: Vector3D(5, 7, 9)