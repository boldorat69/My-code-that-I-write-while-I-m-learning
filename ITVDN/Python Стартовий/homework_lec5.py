# Завдання 1
# Є список а = [2, 4, 65, 32, 2, 6, 0, -1, 3]. Вивести всі значення менше 5 у консоль.


a = [2, 4, 65, 32, 2, 6, 0, -1, 3]

for x in a:
    if x < 5:
        print(x)

# Завдання 2
# "aabbаа" - паліндром. Як це перевірити?


#v1
s = "aabbаа"
if s == s[::-1]:
    print("Паліндром")
else:
    print("Не паліндром")

#v2
s = "aabbаа"
is_palindrome = True

for i in range(len(s) // 2):
    if s[i] != s[-i - 1]:
        is_palindrome = False
        break

print(is_palindrome)

# Завдання 3
# Є список a = [1, 3, 9, 13, 7, 8, 13, 32, 44, 59, 19].
# Виведіть всі елементи, які мають менше 6.

a = [1, 3, 9, 13, 7, 8, 13, 32, 44, 59, 19]

for x in a:
    if x < 6:
        print(x)

# Завдання 4
# На основі списку a = ['red', 'yellow', 'blue', 'bread']
# Створити список, у якому буде лише слово, зайве у списку a.

a = ['red', 'yellow', 'blue', 'bread']
colors = ['red', 'yellow', 'blue']

extra = []

for word in a:
    if word not in colors:
        extra.append(word)

print(extra)