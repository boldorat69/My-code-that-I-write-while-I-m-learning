# Завдання 4
# Створіть магазин канцтоварів використовуючи списки для зберігання елементів. Для додавання елементів створіть функцію,
# яка буде запитувати дані в користувача і зібрані дані у вигляді кортежу додавати у створений список на початку.
# Результат вивести на екран. Під час створення дотримуйтесь правил специфікації PEP 8.
def add_item(store_items):
    """Додає новий товар у вигляді кортежу на початок списку."""
    name = input("Назва товару: ")
    price = float(input("Ціна товару (грн): "))
    quantity = int(input("Кількість на складі: "))

    item = (name, price, quantity)
    store_items.insert(0, item)  # вставляємо елемент на початок списку

    print("Товар успішно додано!")


def show_all_items(store_items):
    """Виводить усі товари магазину."""
    if not store_items:
        print("Список товарів порожній.")
    else:
        print("Список товарів у магазині:")
        for name, price, qty in store_items:
            print(f"• {name} — {price:.2f} грн, {qty} шт.")


store = []

while True:
    print("=== МЕНЮ ===")
    print("1 - Додати товар")
    print("2 - Переглянути всі товари")
    print("0 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        add_item(store)
    elif choice == "2":
        show_items(store)
    elif choice == "0":
        print("Програму завершено.")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")