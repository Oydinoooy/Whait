# # Исключение - дальше читает функцию, выведит ошибку и все
# num1 = 9
# num2 = 0
# print(num1/num2)

# try:
#     num1 = 9
#     num2 = 0 
#     print(num1/num2)

# except ZeroDivisionError:
#     print("На 0 делить нельзя!!!")

# while True:
#     try:
#         num1 = int(input('Введите первое число: '))
#         num2 = int(input('Введите второе число: '))
#         print(f'Результат сложения: {num1+num2}')
#         print(f'Результат вычитания: {num1-num2}')
#         print(f'Результат умножения: {num1*num2}')
#         try:
#             print(f'Результат деления: {num1/num2}')
#         except ZeroDivisionError:
#              print("На 0 делить нельзя!!!")
            
#     except ValueError:
#         print("Ошибка. Неправильный тип данных")


# while True:
#     try:
#           name = str(input('Введите имя: '))
#           age = int(input('Введите свой возраст: '))
#           print(f"Ваше имя: {name}")
#           print(f"Ваш возраст: {age}")

#     except ValueError:
#         print(f"Ошибка! Неправильный тип данных")

# лямда функция - анонимная функция - lambda

# sum = lambda num1, num2: num1+num2
# result = sum(7, 5)
# print(f"Результат сложения: {result}")

# sum = lambda num1, num2: num1+num2
# number1 = int(input("Введите первое число: "))
# number2 = int(input("Введите второе число: "))
# result = sum(number1, number2)
# print(f"Результат сложение: {result}")

# num_list = [1,2,3,4,5,6,7]
# result = list(map(lambda i: i*3, num_list))
# print(result)


# names = ['Nurai', 'Olya', 'Nurdan', 'Nurbolot', 'Kutbuhan']   
# names_len = list(map(lambda i: f'{i} - {len(i)} букв', names))
# print(names_len)


# print(list(filter(lambda x : x % 2 == 0, [1,2,3,4,5,6,7,8,9,10,11,12] )))

# square = lambda side: side**2
# side_len = 5
# area = (square(side_len))
# print(area)
# x = float(input("Ширина: "))
# y = float(input("Длина: "))
# print("Площадь: %.2f" % (x*y))

# list_num = [1,52,48,62,45,63,17,22,54]
# result_max = max(list_num, key=lambda x: x)
# result_min = min(list_num, key=lambda x: x)
# print(result_max)
# print(result_min)

