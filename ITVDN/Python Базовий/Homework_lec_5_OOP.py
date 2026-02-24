#№5 Абстракция

"""
Завдання: Реалізація системи оплати для різних способів платежів
Створити абстрактний клас PaymentMethod, який буде визначати загальні методи для всіх
способів оплати.
Клас PaymentMethod повинен містити:
• Абстрактний метод process_payment(amount: float), який буде обробляти платіж на задану
суму.
• Абстрактний метод get_payment_details(), який повертатиме інформацію про платіжний
метод.
Створити підкласи для різних типів оплат:
• CreditCardPayment
• Додає атрибути card_number (номер картки) та card_holder (власник картки).
• Реалізує метод process_payment(), що імітує зняття коштів.
• Реалізує метод get_payment_details(), який повертає інформацію про картку
(заради безпеки лише останні 4 цифри).
• PayPalPayment
• Має атрибут email (адреса користувача PayPal).
• Реалізує метод process_payment(), що імітує проведення платежу через PayPal.
• Реалізує метод get_payment_details(), який повертає e-mail користувача.
• CryptoPayment
• Має атрибут wallet_address (адреса криптовалютного гаманця).
• Реалізує метод process_payment(), що імітує проведення транзакції в
криптовалюті.
• Реалізує метод get_payment_details(), який повертає гаманець користувача.
Створити об'єкти всіх трьох типів оплат, викликати для кожного методи process_payment() та
get_payment_details(), щоб продемонструвати роботу поліморфізму та абстракції.
"""

from abc import ABC,abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

    @abstractmethod
    def get_payment_details(self):
        pass


class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def process_payment(self, amount: float):
        return f"Зняття коштів з картки {self.card_number} на суму {amount}."

    def get_payment_details(self):
        return f"Карта **** **** **** {self.card_number[-4:]}"

class PayPalPayment(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount: float):
        return f"Платіж через PayPal на суму {amount}"

    def get_payment_details(self):
        return f"PayPal: {self.email}"

class CryptoPayment(PaymentMethod):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def process_payment(self, amount: float):
        return f"Транзакція в криптовалюті на суму {amount}"

    def get_payment_details(self):
        return f"Гаманець: {self.wallet_address}"

credit_pay = CreditCardPayment("1234 5678 8765 4321", "Valera")
paypal_pay = PayPalPayment("boldorat@ukr.net")
crypto_pay = CryptoPayment("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")

payments = [credit_pay, paypal_pay, crypto_pay]

for payment in payments:
    print(payment.process_payment(100))
    print(payment.get_payment_details())

print("-" * 30)
"""
Завдання 1: Реалізація системи замовлень у ресторані
Створіть абстрактний клас Order, який має атрибут table_number та абстрактний метод
calculate_total(). Створіть підкласи FoodOrder та DrinkOrder, які мають власний набір продуктів і
реалізують метод для підрахунку загальної суми замовлення.
"""

class Order(ABC):
    def __init__(self, table_number):
        self.table_number = table_number

    @abstractmethod
    def calculate_total(self):
        pass

class FoodOrder(Order):
    def __init__(self, table_number, products):
        super().__init__(table_number)
        self.products = products

    def calculate_total(self):
        return len(self.products)

class DrinkOrder(Order):
    def __init__(self, table_number, drinks):
        super().__init__(table_number)
        self.drinks = drinks

    def calculate_total(self):
        return len(self.drinks)

food_order = FoodOrder(1, ["Салат", "М'ясо", "Риба", "Закуски"])
drink_order = DrinkOrder(5,["Пиво", "Сік", "Вода мінеральна", "Вода негазована", "Чай"])

orders = [food_order, drink_order]
for order in orders:
    print(f"Стіл № {order.table_number}, кількість позицій: {order.calculate_total()}")

print("-" * 30)
"""
Завдання 2: Реалізація системи зберігання файлів
Створіть інтерфейс StorageInterface, який містить методи save(data: str) та load(). Реалізуйте
підкласи LocalStorage (збереження у файл) та CloudStorage (імітація збереження в хмару) з
відповідною логікою.
"""

class StorageInterface(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def save(self, data: str):
        pass

    @abstractmethod
    def load(self):
        pass

class LocalStorage(StorageInterface):
    def __init__(self, filename):
        super().__init__(filename)

    def save(self):
        return f"Файл {self.filename} збережено у локальній папці."

    def load(self):
        return f"Файл {self.filename} завантажено з локальної папки"

class CloudStorage(StorageInterface):
    def __init__(self, filename):
        super().__init__(filename)

    def save(self):
        return f"Файл {self.filename} збережено у хмарі."

    def load(self):
        return f"Файл {self.filename} завантажено з хмару"

local_storage = LocalStorage("address.doc")
cloud_storage = CloudStorage("settings.xml")

saves = [local_storage, cloud_storage]
for save in saves:
    print(save.save())
    print(save.load())

print("-" * 30)


"""
Завдання 3: Реалізація транспортної системи
Створіть абстрактний клас Transport, який має атрибути speed та capacity і метод move().
Реалізуйте підкласи Car, Bike та Bus, що перевизначають метод move(), демонструючи різні типи
транспорту.
"""

class Transport(ABC):
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    @abstractmethod
    def move(self):
        pass

class Car(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed, capacity)

    def move(self):
        return f"Автомобіль вмістимістю {self.capacity} людей рухається з швидкістю {self.speed} км/год"

class Bike(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed, capacity)

    def move(self):
        return f"Мотоцикл вмістимістю {self.capacity} людей рухається з швидкістю {self.speed} км/год"

class Bus(Transport):
    def __init__(self, speed, capacity):
        super().__init__(speed, capacity)

    def move(self):
        return f"Автобус вмістимістю {self.capacity} людей рухається з швидкістю {self.speed} км/год"

car = Car(90, 5)
bike = Bike(20,2)
bus = Bus(50,30)

transports = [car, bike, bus]
for transport in transports:
    print(transport.move())

print("-" * 30)

"""
Завдання 4: Реалізація пристроїв для друку
Створіть інтерфейс Printable, який містить метод print_document(content: str). Реалізуйте класи
LaserPrinter та InkjetPrinter, які реалізують цей метод відповідно до свого типу принтера
"""

class Printable(ABC):
    @abstractmethod
    def print_document(self, content: str):
        pass

class LaserPrinter(Printable):
    def __init__(self, name):
        self.name = name
    def print_document(self, content: str):
        return f"Документ {content} роздруковано на лазерному принтері {self.name}"

class InkjetPrinter(Printable):
    def __init__(self, name):
        self.name = name
    def print_document(self, content: str):
        return f"Документ {content} роздруковано на струйному принтері {self.name}"

laser_print = LaserPrinter("110 кабінет")
inkjet_print = InkjetPrinter("210 кабінет")

printers = [laser_print,inkjet_print]
for printed in printers:
    print(printed.print_document("Якась таблиця"))