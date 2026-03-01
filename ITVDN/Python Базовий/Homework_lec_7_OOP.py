# №7 Структуры данных
"""
Завдання: Управління контактами
Створіть клас ContactManager, який дозволяє керувати контактами в телефонній книзі за
допомогою різних структур даних.
Вимоги:
1. Використовуйте список для збереження всіх контактів у вигляді кортежів (ім'я, номер).
2. Використовуйте множину для збереження унікальних номерів телефонів, щоб уникнути
дублікатів.
3. Використовуйте словник для швидкого пошуку контактів за іменем.
4. Реалізуйте наступні методи:
○ add_contact(name: str, phone: str): додає контакт, якщо номер не існує.
○ remove_contact(name: str): видаляє контакт за іменем, якщо такий є.
○ find_contact(name: str): знаходить і повертає номер телефону за ім’ям.
○ list_contacts(): виводить усі збережені контакти.
Тестування:
1. Створіть екземпляр ContactManager та додайте кілька контактів.
2. Видаліть один контакт і перевірте, що його більше немає.
3. Виконайте пошук контакту та перевірте, чи повертається правильний номер.
4. Виведіть усі збережені контакти.
"""


class ContactManager:
    def __init__(self):
        self.contacts = []
        self.unique_numbers = set()
        self.contact_dict = {}

    def add_contact(self, name, phone):
        if phone not in self.unique_numbers:
            self.contacts.append((name, phone))
            self.unique_numbers.add(phone)
            self.contact_dict[name] = phone
            print(f"Контакт {name} додано.")
        else:
            print(f"Помилка: Номер {phone} вже використовується.")

    def remove_contact(self, name):
        if name in self.contact_dict:
            phone = self.contact_dict[name]
            self.contacts.remove((name, phone))
            self.unique_numbers.remove(phone)
            del self.contact_dict[name]
            print(f"Контакт {name} видалено.")
        else:
            print(f"Контакт {name} не знайдено.")

    def find_contact(self, name):
        return self.contact_dict.get(name)

    def list_contacts(self):
        if not self.contacts:
            print("Телефонна книга порожня.")
            return

        print("\n--- Список контактів ---")
        for name, phone in self.contacts:
            print(f"👤 {name}:  {phone}")
        print("------------------------\n")



manager = ContactManager()

manager.add_contact("Valera", "+380991112233")
manager.add_contact("Anton", "+380994445566")
manager.add_contact("Oleg", "+380991112233")  # Повтор номера

manager.list_contacts()

search_name = "Valera"
result = manager.find_contact(search_name)
print(f"Пошук '{search_name}': {result}")

manager.remove_contact("Anton")
manager.list_contacts()

"""
Завдання 1: Управління чергою завдань
Створіть клас TaskQueue, який реалізує чергу завдань. Використовуйте collections.deque для
ефективного додавання та видалення елементів.
Реалізуйте методи:
● add_task(task: str): додає завдання в кінець черги.
● process_task(): видаляє та повертає перше завдання в черзі.
● is_empty(): повертає True, якщо черга порожня.
"""
from collections import deque


class TaskQueue:
    def __init__(self):
        self.queue = deque()

    def add_task(self, task):
        self.queue.append(task)

    def process_task(self):
        if self.is_empty():
            print("Черга порожня, немає чого обробляти.")
            return None
        task = self.queue.popleft()
        print(f"Обробка завдання: {task}")
        return task

    def is_empty(self):
        return not self.queue



tasks = TaskQueue()

tasks.add_task("Полагодити монітор")
tasks.add_task("Написати код на Python")
tasks.add_task("Налаштувати MikroTik")

print(f"{tasks.is_empty()=}")

tasks.process_task()
tasks.process_task()

tasks.process_task()
tasks.process_task()

"""
Завдання 2: Стек операцій
Створіть клас OperationStack, який реалізує стек операцій. Використовуйте список для збереження
операцій.
Реалізуйте методи:
● push(operation: str): додає операцію до стеку.
● pop(): видаляє та повертає останню операцію.
● peek(): повертає останню операцію без видалення.
"""
class OperationStack:
    def __init__(self):
        self.stack = []

    def push(self, operation):
        self.stack.append(operation)
        print(f"Додано операцію: {operation}")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        print("Помилка: Стек порожній!")
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        print("Помилка: Стек порожній!")
        return None

    def is_empty(self):
        return len(self.stack) == 0


stack = OperationStack()

stack.push("add")  # Стек: ["add"]
stack.push("multiply")  # Стек: ["add", "multiply"]
stack.push("subtract")  # Стек: ["add", "multiply", "subtract"]

print(f"Остання операція (peek): {stack.peek()}")  # subtract

print(f"Видалено (pop): {stack.pop()}")  # subtract
print(f"Тепер остання (peek): {stack.peek()}")  # multiply

stack.pop()  # удаляем multiply
stack.pop()  # удаляем add
print(f"Результат pop на порожньому стеку: {stack.pop()}")

"""
Завдання 3: Аналіз тексту з множинами
Напишіть функцію unique_words(text: str), яка приймає рядок та повертає множину унікальних слів
у тексті.
Тестування:
1. Використайте текст із повторюваними словами.
2. Перевірте, що результат містить лише унікальні слова
"""

def unique_words(text):
    clean_text = text.lower().replace(".", "").replace(",", "")
    words = clean_text.split()
    return set(words)

test_text = "Python це круто, тому що Python швидкий. Це факт!"

print(unique_words(test_text))
print(f"Текст: {test_text}")
print(f"Унікальні слова: {result}")
print(f"Кількість унікальних слів: {len(result)}")