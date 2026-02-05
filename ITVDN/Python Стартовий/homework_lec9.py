# Завдання 1
# Напишіть функцію, яка змінює значення глобальної змінної.


counter = 0

def increase_counter():
    global counter
    counter += 1

print(counter)      # 0
increase_counter()
increase_counter()
print(counter)      # 2

# Завдання 2
# Напишіть рекурсивну функцію для того, щоб порахувати значення факторіалу числа, що
# передається аргументом (див. рекомендовані ресурси).

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120