# Завдання 1
# Є словник: d = {‘a’:3, ‘b’:0, ‘c’:4, ‘d’:-3}. Знайти найбільше число значень словника.

d = {'a': 3, 'b': 0, 'c': 4, 'd': -3}

max_value = None

for value in d.values():
    if max_value is None or value > max_value:
        max_value = value

print(max_value)

# Завдання 2
# Аналогічно до завдання 1, тільки словник d = {‘a’:3, ‘b’: ‘hello’, ‘c’:4, ‘d’:-3}

d = {'a': 3, 'b': 'hello', 'c': 4, 'd': -3}

max_value = None

for value in d.values():
    if isinstance(value, (int, float)):
        if max_value is None or value > max_value:
            max_value = value

print(max_value)