#Начало работы с ООП: обзор классов
"""
Завдання: Розробка класу для керування замовленнями
Створіть клас Order, який буде моделювати замовлення в інтернет-магазині. Клас повинен мати
наступні характеристики та методи:
• Атрибути класу:
• order_id (ціле число) - унікальний ідентифікатор замовлення.
• customer_name (рядок) - ім'я клієнта, що робить замовлення.
• items (список рядків) - список товарів у замовленні.

Методи класу:
• __init__(self, order_id, customer_name): Конструктор класу, який приймає order_id і
customer_name та ініціалізує атрибути.
• add_item(self, item): Додає товар до списку items.
• remove_item(self, item): Видаляє вказаний товар зі списку items, якщо він
присутній.
• print_order_details(self): Виводить деталі замовлення, включаючи order_id,
customer_name та список товарів.
• Завдання для виконання:
• Створіть об'єкт класу Order з довільним order_id і customer_name.
• Додайте декілька товарів до замовлення за допомогою методу add_item.
• Видаліть один або декілька товарів за допомогою методу remove_item.
• Виведіть деталі замовлення за допомогою методу print_order_details.
"""
print('-' * 30)
class Order:
    def __init__(self, order_id, customer_name, items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items

    def add_item(self, item):
        self.items.append(item)
        print(f"Added item: {item}")

    def remove_item(self, item):
        self.items.remove(item)
        print(f"Removed item: {item}")

    def print_order_details(self):
        print(f"Details of order: {self.order_id}:\n"
              f"Customer: {self.customer_name}\n"
              f"Items: {', '.join(self.items)}")

order = Order(
    order_id= 627315,
    customer_name="Valera",
    items=["Bread","Milk", "Coffee"]
)

order.print_order_details()
order.add_item("Eggs")
order.print_order_details()
order.remove_item("Bread")
order.print_order_details()

"""
Завдання 1: Реалізація класу для керування книгами в бібліотеці
Створіть клас Book, який має атрибути title, author, genre та status (доступна/вибрана). Додайте
методи для видачі книги (borrow_book()), повернення книги (return_book()) та виведення
інформації про книгу (print_details()).
"""
print('-' * 30)
class Book:
    def __init__(self, title, author, genre, status):
        self.title = title
        self.author = author
        self.genre = genre
        self.status = status

    def borrow_book(self):
        self.status = "видана"
        print(f"Зміна статусу. Книга {self.title} - {self.status}")

    def return_book(self):
        self.status = "доступна"
        print(f"Зміна статусу. Книга {self.title} - {self.status}")

    def print_details(self):
        print(f"Details of book {self.title}:\n"
              f"Author: {self.author}\n"
              f"Genre: {self.genre}\n"
              f"Status: {self.status}")


book = Book(
    title = "Кобзар",
    author = "Т. Шевченко",
    genre = "Худ. Література",
    status = "доступна"
)

book.borrow_book()
book.print_details()
book.return_book()
book.print_details()

"""
Завдання 2: Реалізація класу для керування банківським рахунком
Створіть клас BankAccount, який має атрибути account_number, account_holder, balance. Реалізуйте
методи для зняття коштів (withdraw()), внесення коштів (deposit()), перевірки балансу
(check_balance()) та виведення інформації про рахунок (print_account_details())
"""
print('-' * 30)

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdraw amount: {amount}.\n"
              f"Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit amount: {self.balance}.\n"
              f"Balance: {self.balance}")

    def check_balance(self):
        print(f"Balance of investor {self.account_holder} is: {self.balance}.")

    def print_account_details(self):
        print(f"Details of account {self.account_number}:\n"
              f"Account Number: {self.account_number}\n"
              f"Account Holder: {self.account_holder}\n"
              f"Balance: {self.balance}.")

investor = BankAccount(
    account_number= 783041,
    account_holder = "Valera",
    balance = 10000
)

investor.print_account_details()
investor.withdraw(1500)
investor.check_balance()
investor.deposit(3500)
investor.print_account_details()