#2. ООП – Спадкування. Абстракція. Абстрактні класи та методи

# Завдання 1
# Створіть клас Editor, який містить методи view_document та edit_document.
# ехай метод edit_document виводить на екран інформацію про те, що редагування документів недоступне для
# безкоштовної версії. Створіть підклас ProEditor, у якому цей метод буде перевизначено. Введіть ліцензійний к
# люч із клавіатури і, якщо він коректний, створіть екземпляр класу ProEditor, інакше Editor. Викликайте методи
# перегляду та редагування документів.

# Базовий клас Editor
class Editor:
    def view_document(self):
        print("Перегляд документу доступний.")

    def edit_document(self):
        print("Редагування документів недоступне для безкоштовної версії.")

# Підклас ProEditor
class ProEditor(Editor):
    def edit_document(self):
        print("Редагування документів доступне. Вносьте зміни!")


# Введення ліцензійного ключа
license_key = input("Введіть ліцензійний ключ: ")
VALID_KEY = "PRO1234"

# Створюємо об'єкт відповідно до ліцензії
if license_key == VALID_KEY:
    editor = ProEditor()
else:
    editor = Editor()


editor.view_document()
editor.edit_document()

# Завдання 2
# Опишіть класи графічного об'єкта, прямокутника та об'єкта, який може обробляти натискання миші.
# Опишіть клас кнопки. Створіть об'єкт кнопки та звичайного прямокутника. Викличте метод натискання на кнопку.

# Базовий клас графічного об'єкта
class GraphicObject:
    def draw(self):
        print("Малюємо графічний об'єкт.")

# Прямокутник, успадковується від GraphicObject
class Rectangle(GraphicObject):
    def draw(self):
        print("Малюємо прямокутник.")

# Клас для об'єктів, що реагують на натискання
class Clickable:
    def click(self):
        print("Об'єкт натиснутий.")

# Кнопка — одночасно графічний об'єкт і клікабельний
class Button(Rectangle, Clickable):
    def draw(self):
        print("Малюємо кнопку.")

rect = Rectangle()
button = Button()
rect.draw()
button.draw()

# Викликаємо натискання на кнопку
button.click()

# Завдання 3
# Створіть ієрархію класів із використанням множинного успадкування.
# Виведіть на екран порядок вирішення методів для кожного класу.
# Поясніть, чому лінеаризація даних класів виглядає саме так.

class A:
    def show(self):
        print("Метод з A")

class B(A):
    def show(self):
        print("Метод з B")

class C(A):
    def show(self):
        print("Метод з C")

# Множинне успадкування
class D(B, C):
    pass

d = D()
d.show() #Метод з B

print(D.mro())
#[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

#Пояснення:
# D(B, C) — множинне успадкування.
# Python використовує алгоритм C3 лінеаризації:
# Перевіряє спочатку сам клас → D
# Далі — перший батько → B
# Потім — другий батько → C
# Потім — спільний предок обох батьків → A
# І на завершення — object (базовий клас у Python)
# Тому при виклику d.show() Python бере метод першого класу у порядку MRO, тобто з B.

# Завдання 4
# Створіть UML-діаграми до завдань 1, 3 та 7. Збережіть їх у форматі *.uml.

# Завдання 5
# Використовуючи код example_10, створіть декоратор @staticmethod для визначення повноліття людини в Україні та Америки.

#examlpe_10:
# from datetime import date
#
# class MyClass1:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def fromBirthYear(cls, surname, name, birthYear):
#         return cls(surname, name, date.today().year - birthYear)
#
#     def print_info(self):
#         print(self.surname + " " + self.name + "'s age is: " + str(self.age))
#
#
# class MyClass2(MyClass1):
#     color = 'White'
#
#
# m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
# m_per1.print_info()
#
# m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan',  2000)
# m_per2.print_info()
#
# m_per3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2010)
# print(isinstance(m_per3, MyClass2))
#
# m_per4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2001)
# print(isinstance(m_per4, MyClass1))
#
# print(issubclass(MyClass1, MyClass2))
# print(issubclass(MyClass2, MyClass1))

from datetime import date

class MyClass1:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    def print_info(self):
        print(f"{self.surname} {self.name}'s age is: {self.age}")

    # === Статические методы для проверки повноліття ===
    @staticmethod
    def is_adult_ukraine(age):
        """В Украине повноліття = 18"""
        return age >= 18

    @staticmethod
    def is_adult_usa(age):
        """В США повноліття = 21"""
        return age >= 21


class MyClass2(MyClass1):
    color = 'White'

m_per1 = MyClass1('Ivanenko', 'Ivan', 19)
m_per1.print_info()
print("Adult in Ukraine:", MyClass1.is_adult_ukraine(m_per1.age))
print("Adult in USA:", MyClass1.is_adult_usa(m_per1.age))

m_per2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan', 2005)
m_per2.print_info()
print("Adult in Ukraine:", MyClass1.is_adult_ukraine(m_per2.age))
print("Adult in USA:", MyClass1.is_adult_usa(m_per2.age))

# Можно вызывать и через экземпляр
print("Adult in Ukraine:", m_per2.is_adult_ukraine(m_per2.age))

# Завдання 6
# Використовуючи код example_10, створіть декоратори @classmethod для формування переліку об'єктів,
# які підрахують кількість повнолітніх людей в Україні та Америці.

from datetime import date

class MyClass1:
    all_people = []  # список всіх об'єктів класу

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age
        # Додаємо об'єкт у загальний список
        MyClass1.all_people.append(self)

    @classmethod
    def fromBirthYear(cls, surname, name, birthYear):
        return cls(surname, name, date.today().year - birthYear)

    def print_info(self):
        print(f"{self.surname} {self.name}'s age is: {self.age}")

    # === Статичні методи для перевірки повноліття ===
    @staticmethod
    def is_adult_ukraine(age):
        return age >= 18

    @staticmethod
    def is_adult_usa(age):
        return age >= 21

    # === Класові методи для підрахунку повнолітніх ===
    @classmethod
    def count_adults_ukraine(cls):
        return sum(1 for person in cls.all_people if cls.is_adult_ukraine(person.age))

    @classmethod
    def count_adults_usa(cls):
        return sum(1 for person in cls.all_people if cls.is_adult_usa(person.age))


class MyClass2(MyClass1):
    color = 'White'

# Створюємо людей
p1 = MyClass1('Ivanenko', 'Ivan', 19)
p2 = MyClass1.fromBirthYear('Dovzhenko', 'Bogdan', 2005)
p3 = MyClass2.fromBirthYear('Sydorchuk', 'Petro', 2000)
p4 = MyClass2.fromBirthYear('Makuschenko', 'Dmytro', 2010)

# Виводимо інформацію
for p in MyClass1.all_people:
    p.print_info()

# Кількість повнолітніх
print("Adults in Ukraine:", MyClass1.count_adults_ukraine())
print("Adults in USA:", MyClass1.count_adults_usa())

# Завдання 7
# Створіть ієрархію класів транспортних засобів. У загальному класі опишіть загальні всім транспортних засобів поля,
# у спадкоємцях – специфічні їм. Створіть кілька екземплярів. Виведіть інформацію щодо кожного транспортного засобу.