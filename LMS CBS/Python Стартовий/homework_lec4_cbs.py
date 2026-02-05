# Завдання 1
# Дано числа a і b (a < b). Виведіть суму всіх натуральних чисел від a до b (включно).
a = int(input("Введіть а: "))
b = int(input("Введіть b: "))
sum_total = a
for i in range(a,b+1):
    sum_total+=i
print(f"Сума всіх натуральних чисел від {a} до {b}: {sum_total}")

# Завдання 2
# Факторіалом числа n називається число n!=1∙2∙3∙…∙n. Створіть програму, яка обчислює факторіал введеного користувачем числа.
n = int(input("Введіть число n: "))
f=1
for i in range (1,n+1):
   f=f*i
print(f"n! = {f}")

# Завдання 3
# Використовуючи вкладені цикли та функції print(‘*’, end=’’), print(‘ ‘, end=’’) та print() виведіть на екран прямокутний трикутник

number = int(input("Введіть сторону: "))
print(f"Трикутник зі стороною {number}: ")

for i in range(1,number+1):
    for j in range(0, i):
        print("*", end=" ")
    print()

# Завдання 4
# Дано числа a і b (a < b). Виведіть на екран суму всіх натуральних чисел від a до b (включно),
# які є кратними середньому арифметичному цього проміжку.
a = int(input("Введіть а: "))
b = int(input("Введіть b: "))
count = b - a + 1 # Кількість чисел
total_sum = sum(range(a, b + 1)) # Сума всіх чисел від a до b
avg = total_sum / count # Середнє арифметичне
result = 0
for i in range(a, b + 1):
    if i % avg == 0:  # кратне середньому
        result += i
print(f"Сума чисел, кратних середньому арифметичному: {result}")

# Завдання 5
# Створіть програму, яка малює на екрані прямокутник із зірочок заданою користувачем ширини та висоти.
length = int(input("Введіть довжину: "))
height = int(input("Введіть висоту: "))
for i in range (length):
    for j in range (height):
        print("*", end=" ")
    print()

# Завдання 6
# Створіть програму авторизації, в якій користувачеві дається 3 спроби ввести свої облікові дані (логін та пароль).
# Якщо користувач за меншу кількість спроб ввів вірні дані, програма достроково припиняє своє виконання та виводить
# на екран повідомлення: «Авторизацію успішно пройдено з «№» спроби».

#спосіб через while
const_count = 3
count = const_count
login = "Valera"
password = "1234"
while count > 0:
    login_user = input("Введіть логін: ")
    password_user = input("Введіть пароль: ")
    if login_user == login and password_user == password:
        print(f"Авторизацію успішно пройдено з {const_count - count +1 } спроби")
        break
    else:
        count -=1
        if count > 0:
            print("Неправильний логін або пароль. Повторіть спробу.")
            print(f"Залишилось спроб: {count}\n")
        else:
            print(f"Ви використали всі {const_count} спроб для входу")

#спосіб через for
const_count = 3
login = "Valera"
password = "1234"
for i in range (const_count):
    login_user = input("Введіть логін: ")
    password_user = input("Введіть пароль: ")
    if login_user == login and password_user == password:
        print(f"Авторизацію успішно пройдено з {i +1} спроби")
        break
    else:
        if i<const_count -1:
            print("Неправильний логін або пароль. Повторіть спробу.")
            print(f"Залишилось спроб: {const_count -i - 1}\n")
        else:
            print(f"Ви використали всі {const_count} спроб для входу")