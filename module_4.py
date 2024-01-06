from pathlib import Path
from random import randint
import sys

'''Сртуктури даних'''
# str_1 = []
# str_1.append('Space')
# str_1.append('Sky')
# print(str_1)
# for i in str_1:
#     print(i)

# chars = {'a': 1, 'b': 2}
# c_idx = chars.get('c', -1)
# print(c_idx)  # -1

# chars = {'a': 1, 'b': 2}
# chars_copy = chars.copy()
# print(chars_copy == chars)  # True

""""Створення пустої множини"""
# a = set()
# print(a) #set()

""""Створення заповненої множини"""
# a = set('hello')
# print(a)    # {'e', 'h', 'l', 'o'}

""""Створення заповненої множини-2"""
# numbers = {1, 2, 3, 1, 2, 3}
# print(numbers)    # {1, 2, 3}

"""Tuple"""
# points = {
#     (0, 0): "O",
#     (1, 1): "A",
#     (2, 2): "B"
# }
# print(points)

"""Рядки"""
# s = "Hello world"
# print(s.title())

"""pathlib"""
#p = Path()
#p = Path('\GoIT\Module')
# print(f'p -> {p}')
# print(f'p.suffix -> {p.suffix}')
# print(f'p.is_dir() -> {p.is_dir()}')
# print(f'p.cwd() -> {p.cwd()}')
#
# for i in p.iterdir():
#     print(i.name) # якщо ми ще вказали .name, то повертає лише ім'я

"""Додатковий матеріал_1. Отримати список слів із строки"""
# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# words = []
# start = 0
# for indx, chr in enumerate(text):
#     if not chr.lower() in alphabet:
#         word = text[start:indx]
#         words.append(word.strip())
#         start = indx
# print(words)

# """Скільки разів елемент входить в строку"""
# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# dict_counter = {}
# for char in text:
#     try:
#         count = dict_counter[char] #Отримаємо значення по ключу
#     except KeyError:
#         count = 0
#     count += 1
#     dict_counter[char] = count #Записуємо значення по ключу
# print(dict_counter)

# """Те саме, але методом get()"""
# text = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.'
# dict_counter = {}
# for char in text:
#     count = dict_counter.get(char, 0)
#     count += 1
#     dict_counter[char] = count  # Записуємо значення по ключу
# print(dict_counter)

"""get() метод роботи з словниками"""
# lst_1 = {"Coconut": 0, "Banana": 1, "Apple": 2}
# val_1 = lst_1.get('Apple')
# print(val_1) #2

"""Tuple"""
# a = ()
# print(type(a))
# b = []
# print(type(b))
# c = {}
#print(type(c))

# tp = 'asdf',
# print(tp)

"""Словники"""
# d_1 = {True: 'goal', False: 'no goal'}
# print(d_1)

"""pathlib_2"""
# curr = Path()
# print(curr.cwd())

"""Практичні заняття"""
'''Генератор'''
# nums = [x for x in range(21) if x % 2 == 0]
# print(nums)
#
# nums_1 = [x**2 for x in range(21)]
# print(nums_1)

# names = ['Bob', 'Bill', 'Jack']
# names_2 = [s for s in names if 'a' in s]
# print(names_2)

# nums_3 = [x for x in range(21) if x % 2 == 0 if x % 5 == 0]
# print(nums_3)

# a = ["Yes" if x % 2 == 0 else "No" for x in range(10)]
# print(a)

# l = [1, 2, 3, 4, 5]
# b = ['Yes' if x == 1 else 'No' if x == 2 else 'some another' for x in l]
# print(b)

# customers = ['Donna', 'Lusia', 'Merylin']
# dict_cust = {customer:random.randint(1, 100) for customer in customers}
# print(dict_cust)

"""Task_1"""
# a = 'adkfgwluih1l3245426n 787sf'
# b = [int(num) for num in a if num.isdigit()]
# print(b)
# print(sum(b))

"""Task_2"""
# num_lst = [item for item in range(0, 200) if item % 30 == 0 or item % 35 == 0]
# print(num_lst)

"""Task_3"""
# p = Path(sys.argv[1])
# def parse_folder_recursion(path):
#     for element in path.iterdir():
#         if element.is_dir:
#             print(f'This is folder {element.name}')
#             parse_folder_recursion(element)
#         else:
#             print(f'This is file {element.name}')
#
# if __name__ == '__main__':
#     parse_folder_recursion(p)

"""Task_4"""
# def if_else(operator, x, y):
#     return {
#         '+': lambda: x + y,
#         '-': lambda: x - y,
#         '*': lambda: x * y,
#         '/': lambda: x / y
#     }.get(operator, lambda:"This is not valid operation")()
#
# r = if_else('+', 9, 5)
# print(r)

'''Словники'''
# lang = {"Python": 1991, "Java": 1995}
# java = lang.get("Java", 1991)  # 1995
# js = lang.get("JS", 1995)  # 1995
# pascal = lang.get("Pascal")  # None
# print(f'java is {java}')
# print(f'js is {js}')
# print(f'pascal is {pascal}')
# print(f'lang -> {lang}')


"""Homework_4_2"""
# def prepare_data(data):
#    data.remove(max(data))
#    data.remove(min(data))
#    data.sort()
#    return data
#d = [4, 9, 15, 7, 11, 2]
#print(max(data))
#print(min(data))
#print(prepare_data(d))
#print(prepare_data(d))

"""Homework_4_3"""
'''Напишіть функцію format_ingredients, яка прийматиме на вхід список
  з інгредієнтів ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"] та повертатиме
  рядок зібраний з його елементів в описаний вище спосіб -> 2 eggs, 1 liter sugar, 1 tsp salt and vinegar <-
 Ваша функція має вміти обробляти списки будь-якої довжини.'''
# def format_ingredients(items):
#    if not items:
#       return ""
#    elif len(items) != 1:
#       ing_1 = items.pop(-1)
#       ing = ", ".join(items)
#       return f"{ing} and {ing_1}"
#    else:
#       return ''.join(items)
# ingridients = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
# print(format_ingredients(ingridients))

"""Homework_4_4. Сучасна система оцінювання"""

# def get_grade(key):
#    mark = marks.get(key)
#    if mark != None:
#       return mark[0]
#    else:
#       return None
#
# def get_description(key):
#    mark = marks.get(key)
#    if mark != None:
#       return mark[1]
#    else:
#       return None
#
# marks = {
#    'F':(1, 'Unsatisfactorily'),
#    'FX':(2, 'Unsatisfactorily'),
#    'E':(3, 'Enough'),
#    'D':(3, 'Satisfactorily'),
#    'C':(4, 'Good'),
#    'B':(5, 'Very good'),
#    'A':(5, 'Perfectly')
# }
# print(f'Mark for accouting = {get_grade("C")}')
# print(f'Mark for E-book  = {get_description("C")}')

"""Homework 4_5"""
# def lookup_key(data, value):
#    lst = list()
#    for key, val in data.items():
#       if val == value:
#          lst.append(key)
#    return lst
#
# data = {1:'Bob', 'Uno':2000, 'Key':'It is our', 'Goro':2000}
# print(lookup_key(data, 2000))

"""Homework_4_6"""
'''У нас є список показників студентів групи – це список з отриманими балами з тестування. 
Необхідно поділити список на дві частини. Напишіть функцію split_list, яка приймає список 
(цілі числа), знаходить середнє значення бала у списку та ділить його на два списки. У перший 
потрапляють значення менше середнього, включаючи середнє значення, тоді як у другий — строго більше 
від середнього. Функція повертає кортеж цих двох списків. Для порожнього списку повертаємо два порожні списки.'''
# def split_list(grade):
#    if grade:
#       big = []
#       low = []
#       for i in grade:
#          if i <= sum(grade) / len(grade):
#             low.append(i)
#          else:
#             big.append(i)
#       return (low, big)
#    else:
#       return ([],[])
# students = [5, 8, 9, 10, 10, 12, 9, 12, 11, 12, 8]
# print(split_list(students))

"""Homework_4_7"""
# points = {
#     (0, 1): 2,
#     (0, 2): 3.8,
#     (0, 3): 2.7,
#     (1, 2): 2.5,
#     (1, 3): 4.1,
#     (2, 3): 3.9,
# }
#
# def calculate_distance(coordinates):
#    sum_c = 0
#    len_c = len(coordinates)
#    if len_c > 1:
#       i = 0
#       while i != len_c - 1:
#          x = coordinates[i]
#          y = coordinates[i + 1]
#          if x < y:
#             sum_c += points.get((x, y))
#          else:
#             x, y = y, x
#             sum_c += points.get((x, y))
#          i += 1
#       return sum_c
#    else:
#       return 0
#
# print(calculate_distance([0, 1, 3, 2]))
# #print(calculate_distance([0]))

"""Homework_4_8"""
'''Для цього списку і початкової енергії рівної 1 гравець поглине з першого списку перші два значення 
і залишить його, зустрівши значення 5, через те, що на цей момент матиме енергію в 3. Другий список 
пропустить відразу, а третій повністю поглине та отримає остаточну енергію в 6.'''
# def game(terra, power):
#     if terra:
#         for val in terra:
#             for eng in val:
#                 if eng <= power:
#                     power += eng
#                 else:
#                     break
#     return power
# terra = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
# print(game(terra, 1))

"""Homework_4_9"""
# def is_valid_pin_codes(pin_codes):
#     if pin_codes:
#         len_p = len(pin_codes)
#         mn_p = set()
#         for val in pin_codes:
#             if val.isdigit() and len(val) == 4:
#                 mn_p.add(val)
#             else:
#                 return False
#         len_m = len(mn_p)
#         if len_p == len_m:
#             return True
#         else:
#             return False
#     else:
#         return False
# pin = ['1101', '9034', '0011']
# print(is_valid_pin_codes(pin))

"""Homework_4_10. Створення паролю генератором випадкових чисел"""
# def get_random_password():
#     num = ""
#     for _ in range(8):
#         num += chr(randint(40, 126))
#     print(num)
#     return num
# psw = get_random_password()


"""Homework_4_11.Перевірка на надійність створеного паролю"""
# def is_valid_password(password):
#     if len(password) != 8:
#         return False
#     u_p = False
#     l_w = False
#     d_g = False
#     for val in password:
#         if val.isupper():
#             u_p = True
#         elif val.isnumeric():
#             d_g = True
#         elif val.islower():
#             l_w = True
#     return u_p and d_g and l_w
# print(is_valid_password(psw))


"""Варіант написання коду Homework_4_10 nf 4_11 Академії"""
"""Homework_4_12"""
# def get_random_password():
#     result = ""
#     count = 0
#     while count < 8:
#         random_symbol = chr(randint(40, 126))
#         result = result + random_symbol
#         count = count + 1
#     return result
#
# def is_valid_password(password):
#     if len(password) != 8:
#         return False
#
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if ch.isupper():
#             has_upper = True
#         elif ch.islower():
#             has_lower = True
#         elif ch.isdigit():
#             has_num = True
#
#     return has_upper and has_lower and has_num
#
# def get_password():
#     count = 0
#     while count < 100:
#         password = get_random_password()
#         count += 1
#         if is_valid_password(password):
#             break
#         else:
#             continue
#     if count == 100:
#         return "Not password"
#     return password
#
# print(get_password())

"""Homework_4_13"""
# def parse_folder(path):
#     files = []
#     folders = []
#     for i in path.iterdir():
#         if i.is_file():
#             files.append(i.name)
#         else:
#             folders.append(i.name)
#     return files, folders
# p = Path('\GoIT\Module')
# print(parse_folder(p))

"""Homework_4_14"""
# def parse_args():
#     result = ""
#     for arg in sys.argv[1:]:
#         result += arg + ' '
#     return result.rstrip()
# print(parse_args())