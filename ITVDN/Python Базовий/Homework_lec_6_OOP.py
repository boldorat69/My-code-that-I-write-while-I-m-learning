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
        self._words = words

    def __split_text(self, _words, text):
        self._words = self.text.split()

    def count_word_occurrences(word, index=0):
        pass

    def find_longest_word(index=0, longest=""):
        pass

    def get_word_list(self):
        pass



"""
Завдання 1: Перевірка паліндрома за допомогою рекурсії
Створіть клас PalindromeChecker, який містить метод is_palindrome(text), що перевіряє, чи є заданий рядок паліндромом. 
Реалізуйте перевірку рекурсивно: порівнюйте перший і останній символи, поступово звужуючи діапазон.
"""
class PalindromeChecker:
    def __init__(self,text):
        self.text = text

    def is_palindrome(text):
        pass



"""
Завдання 2: Підрахунок суми цифр числа
Створіть клас DigitSum, який має метод sum_digits(n), що рекурсивно обчислює суму цифр числа. 
Наприклад, sum_digits(1234) має повернути 10 (1+2+3+4).
"""

class DigitSum:
    def __init__(self, n):
        self.n = n

    def sum_digits(self, n):
        pass

"""
Завдання 3: Побудова вкладених дужок
Створіть клас BracketGenerator, який містить метод generate_brackets(n), що рекурсивно будує рядок із n пар круглих 
дужок. Наприклад, generate_brackets(3) має повернути "((()))".
"""

class BracketGenerator:
    def __init__(self, n):
        self.n = n

    def generate_brackets(self, n):
        pass

