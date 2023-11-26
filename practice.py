# result = 0
# try:
#     value_1 = int(input("Please set first value: "))
#     value_2 = int(input("Please set second value: "))
#     result = value_1 / value_2
# except ZeroDivisionError as err:
#     #print("You can't divide by zero!")
#     print(f" We have the ERROR: {err}")
# except ValueError:
#     print("Wrong value!")
# else:
#     print(f"result = {result}")

# a = 0
# while a < 6:
#     a += 1
#     if not a % 2:
#         continue
#     print(a)
'''Task 2.1'''
# while True:
#     try:
#         number = int(input("Please set number: "))
#     except ValueError as err:
#         print(f"You have an error -> {err}")
#         continue
#     if number < 10:
#         continue
#     elif number > 100:
#         break
#     else:
#         print(number)

'''Task 2.2'''
# a = int(input("Please set a: "))
# b = int(input("Please set b: "))
# i = 0
# j = 0
# for num in range(a, b + 1):
#    #if not num % 3:
#    if num % 3 == 0:
#       j += 1
#       i += num
# print(f'Sum = {i / j}')

'''Task 2.3 - Найменший спільний дільник'''
# x = int(input("Please set Java: "))
# y = int(input("Please set Python: "))
# d = 1
# while True:
#     if d % x == 0 and d % y == 0:
#         break
#     else:
#         d += 1
# print(d)

'''Task 2.4 - Здвиг повідомлення по алфавіту на задану кількість символів'''
# message = input("Введіть повідомлення: ")
# offset = int(input("Введіть здвиг: "))
# encoded_message = ""
# for ch in message:
#     if "a"<= ch <= "z":
#         pos = ord(ch) - ord("a")
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("a"))
#         encoded_message = encoded_message + new_char
#     elif "A"<= ch <= "Z":
#         pos = ord(ch) - ord("A")
#         pos = (pos + offset) % 26
#         new_char = chr(pos + ord("A"))
#         encoded_message = encoded_message + new_char
#     else:
#         encoded_message = encoded_message + ch
# print(encoded_message)

'''Найбільший спільний дільник'''

# x = int(input("Please set first number: "))
# y = int(input("Please set second number: "))
# while x * y != 0:
#     if x >= y:
#         x = x % y
#     else:
#         y = y % x
# print(f"Найбільший спільний дільник = {x + y}")

'''Найбільший спільний дільник - 2'''
# first = int(input("Enter the first integer: "))
# second = int(input("Enter the second integer: "))
# gcd = first if first < second else second
# while True:
#     if first % gcd == 0 and second % gcd == 0:
#         break
#     else:
#         gcd -= 1
# print(gcd)

"""Homework 2.10"""
# num = int(input("Enter integer (0 for output): "))
# sum = 0
# while num != 0:
#     for i in range(num + 1):
#         sum += i
#     num = int(input("Enter integer (0 for output): "))
# print(sum)


'''Homework 2.15'''
# result = 0.0
# wait_for_number = True
# operator = None
# operand = None
# while True:
#     try:
#         if wait_for_number:
#             operand = float(input('Enter the number: '))
#     except ValueError:
#         print('Is not a number! Try again.')
#         continue
#     if not operator:
#         result += operand
#     else:
#         if operator == '+':
#             result += operand
#         elif operator == '-':
#             result -= operand
#         elif operator == '*':
#             result *= operand
#         elif operator == '/':
#             result /= operand
#     wait_for_number = False
#
#     if not wait_for_number:
#         operator = input('Operator: ')
#         if operator == '+' or operator == '-' or operator == '*' or operator == '/' or operator == '=':
#             wait_for_number = True
#         else:
#             print("Isn't an operator!")
#     if operator == '=':
#         print(f'Result = {result}')
#         break






