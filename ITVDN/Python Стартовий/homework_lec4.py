# Завдання 1
# Вивести у консоль перші 100 чисел Фібоначчі (див. у рекомендованих ресурсах)
a = 0
b = 1

for _ in range(100):
    print(a, end=' ')
    a, b = b, a + b
# Завдання 2
# У пропозиції “Hello world” замінити всі літери “o” на “a”, а літери “l” на “e”.

text = "Hello world"
result = ""

for ch in text:
    if ch == 'o':
        result += 'a'
    elif ch == 'l':
        result += 'e'
    else:
        result += ch

print(result)

# Завдання 3
# Створіть будь-який змінний рядок і помістіть будь-який текст. Зробіть так, щоб усі непарні по
# порядку ліворуч на право символи стали "_", а всі символи, розташування яких парне і які рівні
# "a" - стали "b". Наприклад "Ham is tasty" => "_b_ _s_t_s_y".
text = "Ham is tasty"
result = ""

for i in range(len(text)):
    if i % 2 == 0:
        result += "_"
    elif text[i] == 'a':
        result += "b"
    else:
        result += text[i]

print(result)