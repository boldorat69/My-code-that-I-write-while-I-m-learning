#1. ООП – Класи, атрибути, методи, конструктор
# Завдання 1
# Створіть клас, який описує книгу. Він повинен містити інформацію про автора, назву, рік видання та жанр.
# Створіть кілька різних книжок. Визначте для нього методи _repr_ та _str_.

class Book:
    def __init__(self, author, title, year, genre):
        self.author = author
        self.title = title
        self.year = year
        self.genre = genre
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews_text(self):
        if not self.reviews:
            return "Відгуків поки немає."
        return "\n".join(review.to_string() for review in self.reviews)

    def __str__(self):
        return (
            f"Книга: {self.title}\n"
            f"Автор: {self.author}\n"
            f"Рік: {self.year}\n"
            f"Жанр: {self.genre}\n"
            f"Відгуки:\n{self.get_reviews_text()}"
        )

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"

book = Book("Джордж Орвелл", "1984", 1949, "Антиутопія")
print(book)

# Завдання 2
# Створіть клас, який описує відгук до книги. Додайте до класу книги поле – список відгуків.
# Зробіть так, щоб при виведенні книги на екран за допомогою функції print також виводилися відгуки до неї.

class Review:
    def __init__(self, author, text, rating):
        self.author = author
        self.text = text
        self.rating = rating

    def to_string(self):
        return f"{self.author} ({self.rating}/5): {self.text}"

review1 = Review("Анна", "Дуже сильна книга")
review2 = Review("Олег", "Змусила замислитись")

book.add_review(review1)
book.add_review(review2)

# Завдання 3
# Ознайомтеся зі спеціальними методами в Python, використовуючи посилання в кінці уроку, і навчіться використовувати
# ті з них, призначення яких ви можете зрозуміти. Повертайтеся до цієї теми протягом усього курсу та вивчайте спеціальні
# методи, що відповідають темам кожного уроку.

class NumberBox:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return NumberBox(self.value + other.value)

    def __len__(self):
        return self.value

    def __str__(self):
        return f"NumberBox({self.value})"

a = NumberBox(5)
b = NumberBox(3)
c = a + b

print(c)        # NumberBox(8)
print(len(c))   # 8

# Завдання 4
# Створіть клас, який описує автомобіль. Створіть клас автосалону, що містить в собі список автомобілів, доступних
# для продажу, і функцію продажу заданого автомобіля.

class Car:
    def __init__(self, brand, model, year, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def get_info(self):
        return f"{self.brand} {self.model} ({self.year}) — {self.price}$"

    def __repr__(self):
        return f"Car({self.brand}, {self.model}, {self.year}, {self.price})"

class CarSalon:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        if not self.cars:
            print("Автомобілі відсутні")
        for car in self.cars:
            print(car.get_info())

    def sell_car(self, brand, model):
        for car in self.cars:
            if car.brand == brand and car.model == model:
                self.cars.remove(car)
                print(f"Продано: {car.get_info()}")
                return
        print("Автомобіль не знайдено")

salon = CarSalon()

car1 = Car("Toyota", "Camry", 2020, 20000)
car2 = Car("BMW", "X5", 2019, 35000)

salon.add_car(car1)
salon.add_car(car2)

salon.show_cars()
salon.sell_car("Toyota", "Camry")
salon.show_cars()