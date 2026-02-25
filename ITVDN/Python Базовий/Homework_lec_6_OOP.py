#№6 Работа с рекурсией
"""
Завдання: Рекурсивний аналіз тексту
Створіть клас TextAnalyzer, який дозволяє аналізувати текст, використовуючи рекурсію.
Клас повинен мати наступні атрибути:
● text: текст, який буде аналізуватися (рядок).
● _words: список слів, отриманих із тексту (захищений атрибут).
Клас повинен містити наступні методи:
● __split_text(): приватний метод, який ділить текст на слова та зберігає їх у _words. Викликається під час ініціалізації об'єкта.
● count_word_occurrences(word, index=0): рекурсивний метод, який підраховує кількість входжень заданого слова в _words.
● find_longest_word(index=0, longest=""): рекурсивний метод, який знаходить найдовше слово в _words.
● get_word_list(): публічний метод, який повертає список слів із _words.
Створіть об'єкт класу TextAnalyzer та протестуйте методи:
1. Ініціалізуйте об'єкт із довільним текстом.
2. Використайте count_word_occurrences(), щоб підрахувати, скільки разів певне слово зустрічається в тексті.
3. Викличте find_longest_word(), щоб знайти найдовше слово в тексті.
4. Використайте get_word_list(), щоб отримати список слів.
"""

class TextAnalyzer:
    def __init__(self, text, words):
        self.text = text
        self._words = []
        self.__split_text()


    def __split_text(self):
        clean_text = self.text.replace(",", "").replace(".", "").lower()
        self._words = clean_text.split()

    def count_word_occurrences(self, word, index=0):
        if index == len(self._words):
            return 0

        current_count = 1 if self._words[index] == word.lower() else 0

        return current_count + self.count_word_occurrences(word, index + 1)

    def find_longest_word(self, index=0, longest=""):
        if index == len(self._words):
            return longest

        current_word = self._words[index]
        if len(current_word) > len(longest):
            longest = current_word

        return self.find_longest_word(index + 1, longest)

    def get_word_list(self):
        return self._words

text_example = "Python is great and Python is fast. Python is a powerful language."
analyzer = TextAnalyzer(text_example)

print(f"{analyzer.get_word_list()=}")


word_to_find = "python"
count = analyzer.count_word_occurrences(word_to_find)
print(f"Слово '{word_to_find}' зустрічається {count} разів")


longest = analyzer.find_longest_word()
print(f"Найдовше слово: '{longest}'")

"""
Завдання 1: Перевірка паліндрома за допомогою рекурсії
Створіть клас PalindromeChecker, який містить метод is_palindrome(text), що перевіряє, чи є заданий рядок паліндромом. 
Реалізуйте перевірку рекурсивно: порівнюйте перший і останній символи, поступово звужуючи діапазон.
"""
class PalindromeChecker:
    def __init__(self,text):
        self.text = text

    def is_palindrome(self, text= None):
        if text is None:
            text = self.text
        if len(text) <= 1:
            return True
        if text[0] != text[-1]:
            return False
        return self.is_palindrome(text[1:-1])


some_text_1 = PalindromeChecker("qwerttrewq")
some_text_2 = PalindromeChecker("qwerqwer")

print(f"{some_text_1.text} is palindrome: {some_text_1.is_palindrome()}")
print(f"{some_text_2.text} is palindrome: {some_text_2.is_palindrome()}")



"""
Завдання 2: Підрахунок суми цифр числа
Створіть клас DigitSum, який має метод sum_digits(n), що рекурсивно обчислює суму цифр числа. 
Наприклад, sum_digits(1234) має повернути 10 (1+2+3+4).
"""

class DigitSum:
    def __init__(self, ):
        self.n = n

    def sum_digits(self, n=None):
        if n is None:
            n = self.n
        if n < 10:
            return n
        return (n % 10) + self.sum_digits(n // 10)


some_number_1 = DigitSum(1234)
some_number_2 = DigitSum(3456)

print(f"{some_number_1.n=}, sum={some_number_1.sum_digits()}")
print(f"{some_number_2.n=}, sum={some_number_2.sum_digits()}")

"""
Завдання 3: Побудова вкладених дужок
Створіть клас BracketGenerator, який містить метод generate_brackets(n), що рекурсивно будує рядок із n пар круглих 
дужок. Наприклад, generate_brackets(3) має повернути "((()))".
"""

class BracketGenerator:
    def __init__(self, n):
        self.n = n

    def generate_brackets(self, n= None):
        if n is None:
            n = self.n
        if n == 0:
            return ""
        return "(" + self.generate_brackets(n - 1) + ")"



some_bracket_1 = BracketGenerator(3)
some_bracket_2 = BracketGenerator(9)

some_bracket_1.generate_brackets()
some_bracket_2.generate_brackets()


