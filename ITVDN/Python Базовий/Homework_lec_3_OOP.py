#№3 Инкапсуляция

"""
Завдання: Розробка класу для роботи з банківським рахунком
Створити клас BankAccount:
• Клас повинен мати наступні атрибути:
• Публічний атрибут account_holder (ім'я власника рахунку).
• Захищений атрибут _balance (баланс рахунку).
• Приватний атрибут __account_number (номер рахунку).

• Клас повинен мати наступні методи:
• Приватний метод __generate_account_number(), який генерує випадковий номер
рахунку довжиною 10 цифр при створенні нового об'єкту класу.
• Публічний метод deposit(amount: float), який дозволяє поповнювати рахунок на
вказану суму.
• Публічний метод withdraw(amount: float), який дозволяє знімати кошти з рахунку,
якщо достатньо коштів на рахунку.
• Публічний метод get_balance(), який повертає поточний баланс рахунку.
• Публічний метод get_account_number(), який повертає номер рахунку
(використовуючи приватний атрибут).

Створити екземпляр класу BankAccount:
• Створити об'єкт класу BankAccount з ім'ям власника рахунку.
• Використати методи deposit() та withdraw(), щоб продемонструвати роботу з балансом
рахунку.
• Викликати методи get_balance() та get_account_number(), щоб отримати поточний баланс
та номер рахунку.
"""

import random

class BankAccount:
    def __init__(self, account_holder="", balance=0):
        self.account_holder = account_holder
        self._balance = balance
        self.__account_number = self.__generate_account_number()

    def deposit(self, amount: float):
        self._balance += amount
        print(f"Added to deposit: {amount}.\n"
              f"Your balance is {self._balance}")

    def withdraw(self, amount: float):
        if amount <= self._balance:
            self._balance -= amount
            print(f"Withdrawn {amount}."
                  f"Your balance is {self._balance}")
        else:
            print("Not enough funds!")

    def get_balance(self):
        return self._balance

    def get_account_number(self):
        return self.__account_number

    def __generate_account_number(self):
        self.__account_number = random.randint(1000000000, 9999999999)
        return self.__account_number


user = BankAccount(
    account_holder="Valera",
    balance=10000
)

user.deposit(500)
user.withdraw(2000)
print(f"Balance of user {user.account_holder} is {user.get_balance()}. ")
print(f"Account number of user {user.account_holder} is {user.get_account_number()}.")

"""
Завдання 1: Реалізація класу для обробки даних студентів
Створіть клас Student, який має атрибути name (ім'я студента), _grades (список оцінок, захищений
атрибут) та приватний атрибут __id (унікальний ідентифікатор студента). 

Реалізуйте методи для додавання оцінки (add_grade()), отримання середньої оцінки (get_average_grade()) та виведення
інформації про студента (print_details()).
"""

print('-' * 30)
class Student:
    def __init__(self, name, grades, id):
        self.name = name
        self._grades = grades
        self.__id = id

    def add_grade(self, grade):
        self._grades.append(grade)
        print(f"Added grade {grade} for student {self.name}.")

    def get_average_grade(self):
        average = sum(self._grades) / len(self._grades)
        print(f"Average grade for student {self.name} is {average}.")

    def print_details(self):
        print(f"Name of student: {self.name}\n"
              f"Grades: {self._grades} \n"
              f"ID: {self.__id}")


student = Student(
    name="Valera",
    grades=[95, 85, 100],
    id=150
)

student.add_grade(90)
student.get_average_grade()
student.print_details()

"""
Завдання 2: Реалізація класу для керування продуктами в магазині
Створіть клас Product, який має атрибути name, price (захищений атрибут) та приватний атрибут
__sku (унікальний код товару). Реалізуйте методи для встановлення ціни (set_price()), отримання
ціни (get_price()) та виведення інформації про продукт (print_details()).
"""

print('-' * 30)
class Product:
    def __init__(self, name, price, sku):
        self.name = name
        self._price = price
        self.__sku = sku

    def set_price(self, price):
        self._price = price
        print(f"Added price {price} to product {self.name}.")

    def get_price(self):
        print(f"Price of product is {self._price}.")

    def print_details(self):
        print(f"Details of product {self.name}:\n"
              f"Price: {self._price} \n"
              f"SKU: {self.__sku}\n"
              )


product = Product(
    name="Bottle of water",
    price=10,
    sku=158261
)

product.set_price(20)
product.get_price()
product.print_details()


"""
Завдання 3: Реалізація класу для керування транспортними засобами
Створіть клас Vehicle, який має атрибути mark (марка), model (модель) та захищений атрибут
_mileage (пробіг). Додайте методи для оновлення пробігу (update_mileage()), отримання пробігу
(get_mileage()) та виведення інформації про транспортний засіб (print_details()).
"""

print('-' * 30)
class Vehicle:
    def __init__(self, mark, model, mileage):
        self.mark = mark
        self.model = model
        self._mileage = mileage

    def update_mileage(self, mileage):
        self._mileage += mileage
        print(f"Updated mileage, now is {self._mileage}.")

    def get_mileage(self):
        print(f"Mileage of vehicle is {self._mileage}.")

    def print_details(self):
        print(f"Details of vehicle: {self.mark}\n"
              f"Model: {self.model}\n"
              f"Mileage: {self._mileage}\n")

vehicle = Vehicle(
    mark = "Toyota",
    model = "Corolla",
    mileage = 15000
)
vehicle.update_mileage(1000)
vehicle.get_mileage()
vehicle.print_details()






class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email
        self.sent_messages = []

    def get_contact(self):
        return f"{self.name} {self.surname}, phone: {self.mob_phone}, email: {self.email}"

    def send_message(self, message):
        self.sent_messages.append(message)
        print(f"Message '{message}' sent to {self.name} {self.surname}.")



class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def send_message(self, message):
        self.sent_messages.append(message)
        print(f"[UpdateContact] Message '{message}' sent to {self.name} {self.surname}.")



contact1 = Contact("Ivanov", "Ivan", 30, "+380501234567", "ivan@mail.com")
contact2 = UpdateContact("Petrov", "Petr", 28, "+380501112233", "petr@mail.com", "Developer")

# Test methods
print(contact1.get_contact())
contact1.send_message("Hello Ivan!")

print(contact2.get_contact())
contact2.send_message("Hello Petr!")


print("\nState of contact1:")
print("Attributes:", contact1.__dict__)
print("Base class:", contact1.__class__.__base__)
print("Bases:", contact1.__class__.__bases__)

print("\nState of contact2:")
print("Attributes:", contact2.__dict__)
print("Base class:", contact2.__class__.__base__)
print("Bases:", contact2.__class__.__bases__)
