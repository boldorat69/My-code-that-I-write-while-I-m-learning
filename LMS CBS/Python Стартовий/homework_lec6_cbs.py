# Завдання 1
# Створіть список та введіть його значення. Знайдіть найбільший та найменший елемент списку, а також суму та середнє
# арифметичне його значень.
# v1
some_list = [1, 2, 6, 25, 76, 12, 5]
max_element = some_list[0]
min_element = some_list[0]
for i in some_list:
    if i > max_element:
        max_element = i
    if i < min_element:
        min_element = i
average = (max_element + min_element) / 2
print(f"Максимальний елемент: {max_element}")
print(f"Мінімальний елемент: {min_element}")
print("Сума елементів: ", sum(some_list))
print(f"Середнє арифметичне: {average}")

# v2
some_list = [1, 2, 6, 25, 76, 12, 5]
print("Максимальний елемент:", max(some_list))
print("Мінімальний елемент:", min(some_list))
print("Сума елементів:", sum(some_list))
print("Середнє арифметичне:", sum(some_list) / len(some_list))

# Завдання 2
# Є два списки, які наповнюються користувачем з клавіатури. Сформувати список, в якому будуть міститися унікальні значення
# першого відносно другого списку та навпаки без повторень. Роздрукувати підсумковий обєкт на екран в прямій послідовності,
# зворотній, а також виконати сортування за зростанням та спаданням.)
some_list_1 = list(input("Введіть 1й список: ").split())
some_list_2 = list(input("Введіть 2й список: ").split())
set1 = set(some_list_1)
set2 = set(some_list_2)
# унікальні значення кожного списку відносно іншого
unique_1 = set1 - set2  # тільки у першому
unique_2 = set2 - set1  # тільки у другому
result = set1.union(set2)  # об’єднання двох множин
print("Унікальні елементи:", result)
print("У зворотному порядку:", result[::-1])
print("За зростанням:", sorted(result))
print("За спаданням:", sorted(result, reverse=True))

# Завдання 3
# Простим називається число, яке ділиться націло лише на одиницю і на саме себе. Число 1 не вважається простим.
# Напишіть програму, яка знаходить усі прості числа в заданому проміжку, виводить їх на екран, а потім на вимогу
# користувача виводить їхню суму або добуток.
a = int(input("Введіть 1е число проміжку: "))
b = int(input("Введіть 2е число проміжку: "))
some_list = list(range(a, b + 1))

for element in some_list:
    if element > 1:  # 1 не є простим
        for d in range(2, int(element ** 0.5) + 1):
            if element % d == 0:
                break
        else:
            primes.append(element)

print("Прості числа:", primes)
choice = input("Введіть 'sum' для суми або 'mul' для добутку: ")
if choice == 'sum':
    print("Сума простих чисел: ", sum(primes))
elif choice == 'mul':
    product = 1
    for p in primes:
        product *= p
    print("Добуток простих чисел: ", product)
else:
    print("Невірний вибір")

# Завдання 4
# Створіть цілочисельний список, введіть кількість його елементів і самі значення. Передбачити меню, в якому: після
# натискання клавіші 1 ці значення виведуться на екран у зворотному порядку, а після натискання клавіші 2 – за зростанням.
n = int(input("Введіть кількість елементів списку: "))
some_list = []
for i in range(n):
    num = int(input(f"Введіть елемент {i+1}: "))
    some_list.append(num)

copy_of_some_list = some_list.copy()
choise = int(input("Введіть вибір: "))

if choise == 1:
    copy_of_some_list.reverse()
    print(copy_of_some_list.reverse())
elif choise == 2:
    copy_of_some_list.sort()
    print(copy_of_some_list.sort())
else:
    print("Невірний вибір")
# Завдання 5
# Створіть список натуральних чисел int_list. Кожне непарне значення списку додайте до нового списку new_list.
# Користувач вводить з клавіатури кількість повторів списку repeat. Здійсніть дублювання списку new_list, repeat
# кількість разів. Очистіть список int_list.

int_list = range(1,25)
new_list = []
for element in int_list:
    if element % 2 != 0:
        new_list.append(element)
repeat = int(input("Введіть кіл-ть повторів: "))
new_list = new_list * repeat
int_list.clear()
print("Новий список: ", new_list)
print("int_list після очищення: ", int_list)

# Завдання 6
# Для цього завдання вихідний список значень беремо з підсумкового списку new_list завдання 5.
# Користувач вводить з клавіатури значення; якщо таке є у цьому списку — вивести кількість його повторів
# та його позицію у цьому списку.

choise = int(input("Введіть значення: "))
if choise in new_list:
    count = new_list.count(choise)# скільки разів зустрічається
    position = new_list.index(choise)# позиція першого входження
    print(f"Кількість повторів: {count}")
    print(f"Позиція першого входження: {position}")
else:
    print("Такого значення немає у списку.")