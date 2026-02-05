#3. ООП – Інкапсуляція та поліморфізм

# Завдання 1
# Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані?
# Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set).

class Car:
    def __init__(self, brand, model, year, color):
        self.__brand = brand     # приватний атрибут
        self.__model = model     # приватний атрибут
        self.__year = year       # приватний атрибут
        self.__color = color     # приватний атрибут

    # ===== Getters =====
    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    # ===== Setters =====
    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        if year > 1885:  # перший автомобіль з'явився в 1886 році
            self.__year = year
        else:
            print("Невірний рік випуску!")

    def set_color(self, color):
        self.__color = color

    # ===== Метод для виведення інформації =====
    def info(self):
        return f"{self.__brand} {self.__model}, {self.__year}, Color: {self.__color}"

car1 = Car("Toyota", "Camry", 2020, "White")

# Виводимо інформацію
print(car1.info())  # Toyota Camry, 2020, Color: White

# Змінюємо атрибути через сеттери
car1.set_color("Black")
car1.set_year(2021)

# Отримуємо атрибути через геттери
print("Brand:", car1.get_brand())
print("Year:", car1.get_year())
print(car1.info())

# Завдання 2
# Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting().
# Обидва створюють різні привітання. Створіть два відповідні об'єкти з двох класів вище та викличте дії цих двох об'єктів
# в одній функції (функція hello_friend).

# Клас англійської мови
class English:
    def greeting(self):
        return "Hello!"

# Клас іспанської мови
class Spanish:
    def greeting(self):
        return "¡Hola!"

# Функція, яка приймає два об'єкти і викликає їх методи greeting
def hello_friend(obj1, obj2):
    print(obj1.greeting())
    print(obj2.greeting())

# Створюємо об'єкти
english_speaker = English()
spanish_speaker = Spanish()

# Викликаємо функцію
hello_friend(english_speaker, spanish_speaker)

# Завдання 3
# Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції, як властивості.
# Ознайомтеся з декоратором property у Python. Створіть клас, що описує температуру і дозволяє задавати та
# отримувати температуру за шкалою Цельсія та Фаренгейта, причому дані можуть бути задані в одній шкалі, а отримані в іншій.

class Temperature:
    def __init__(self, celsius=0.0):
        self._celsius = celsius  # внутрішнє зберігання в Цельсіях

    # ===== Властивість для Цельсія =====
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._celsius = value

    # ===== Властивість для Фаренгейта =====
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

temp = Temperature()

# Встановлюємо температуру в Цельсіях
temp.celsius = 25
print("Celsius:", temp.celsius)       # 25
print("Fahrenheit:", temp.fahrenheit) # 77.0

# Встановлюємо температуру у Фаренгейтах
temp.fahrenheit = 212
print("Celsius:", temp.celsius)       # 100.0
print("Fahrenheit:", temp.fahrenheit) # 212.0

# Завдання 4
# Опишіть два класи Base та його спадкоємця Child з методами method(), який виводить на консоль фрази відповідно
# "Hello from Base" та "Hello from Child", using classmethod (@classmethod) decorator.

# Базовий клас
class Base:
    @classmethod
    def method(cls):
        print("Hello from Base")

# Спадкоємець
class Child(Base):
    @classmethod
    def method(cls):
        print("Hello from Child")

Base.method()   #Hello from Base
Child.method()  #Hello from Child

# Завдання 5
# Ознайомившись з кодом файлу example_7.py, створіть додаткові класи-нащадки Cone та Paraboloid від класу Shape.
# Перевизначте їх методи. Створіть екземпляри відповідних класів за скористайтеся всіма методами.
# В результаті повинно з’явитися зображення. Перегляньте їх.

#example_7.py:
# example_7.py
# from PIL import Image, ImageDraw
#
# class Shape:
#     def __init__(self):
#         # Колір тла
#         self.back_color = (155, 213, 117, 100)
#         # Створюємо зображення 500 * 500
#         self.im = Image.new('RGBA', (500, 500), self.back_color)
#         self.draw1 = ImageDraw.Draw(self.im)
#
#     def draw(self):
#         pass
#
#     def erase(self):
#         self.im = Image.new('RGBA', (500, 500), self.back_color)
#         self.draw1 = ImageDraw.Draw(self.im)
#
#     def save(self):
#         print("Background was created")
#         return self.im.save('picture.png', quality=95)
#
#
# class Circle(Shape):
#     def draw(self):
#         self.draw1.ellipse((75, 100, 175, 200), fill='yellow', outline=(255, 255, 255))
#
#     def erase(self):
#         self.draw1.ellipse((75, 100, 175, 200), fill=self.back_color)
#
#     def save(self):
#         print("Image with circle was created")
#         return self.im.save('draw-circle.png', quality=95)
#
#
# class Square(Shape):
#     def draw(self):
#         self.draw1.rectangle((200, 100, 300, 200), fill='blue', outline=(255, 255, 255))
#
#     def erase(self):
#         self.draw1.rectangle((200, 200, 300, 200), fill=self.back_color)
#
#     def save(self):
#         print("Image with square was created")
#         return self.im.save('draw-square.png', quality=95)
#
#
# class Triangle(Shape):
#     def draw(self):
#         self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=(255, 255, 255))
#
#     def erase(self):
#         self.draw1.polygon([(400, 100), (350, 200), (450, 200)], fill=self.back_color)
#
#     def save(self):
#         print("Image with triangle was created")
#         return self.im.save('draw-triangle.png', quality=95)
#
#
# def work_with_obj(obj):
#     obj.draw()
#     obj.save()
#
#
# def update_obj(obj):
#     obj.erase()
#     obj.save()
#
#
# def menu():
#     while True:
#         value = int(input('\nМЕНЮ:\n\t1. Cтворити тло\n\t2. Cтворити коло\n\t3. Cтворити квадрат\n\t4. Cтворити трикутник'
#                           '\n\t5. Зафарбувати коло\n\t6. Зафарбувати квадрат\n\t7. Зафарбувати трикутник\n\t'
#                           '8. Вихід з програми\nОберіть необхідний пункт меню: '))
#         match value:
#             case 1:
#                 s = Shape()
#                 s.save()
#             case 2:
#                 c = Circle()
#                 work_with_obj(c)
#             case 3:
#                 sq = Square()
#                 work_with_obj(sq)
#             case 4:
#                 t = Triangle()
#                 work_with_obj(t)
#             case 5:
#                 c = Circle()
#                 update_obj(c)
#             case 6:
#                 sq = Square()
#                 update_obj(sq)
#             case 7:
#                 t = Triangle()
#                 update_obj(t)
#             case 8:
#                 break
#             case _:
#                 print('Оберіть пункт меню корректно!!!')
#
#
# if __name__ == '__main__':
#     menu()

from PIL import Image, ImageDraw

class Shape:
    def __init__(self):
        self.back_color = (155, 213, 117, 100)
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def draw(self):
        pass

    def erase(self):
        self.im = Image.new('RGBA', (500, 500), self.back_color)
        self.draw1 = ImageDraw.Draw(self.im)

    def save(self, filename='picture.png'):
        self.im.save(filename, quality=95)
        print(f"Image saved as {filename}")


#Конус
class Cone(Shape):
    def draw(self):
        # Малюємо конус як трикутник
        self.draw1.polygon([(250, 100), (150, 400), (350, 400)], fill='orange', outline=(0,0,0))

    def save(self, filename='cone.png'):
        self.im.save(filename, quality=95)
        print(f"Cone image saved as {filename}")


#Параболоїд
class Paraboloid(Shape):
    def draw(self):
        # Малюємо параболоїд як вертикально витягнутий еліпс
        self.draw1.ellipse((150, 100, 350, 400), fill='purple', outline=(0,0,0))

    def save(self, filename='paraboloid.png'):
        self.im.save(filename, quality=95)
        print(f"Paraboloid image saved as {filename}")


cone_obj = Cone()
cone_obj.draw()
cone_obj.save()

paraboloid_obj = Paraboloid()
paraboloid_obj.draw()
paraboloid_obj.save()