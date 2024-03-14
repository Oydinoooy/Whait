
# Цикл не тип данных. 
# функция- это опредеоенный код 
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = lambda i: i [::-1]
# print(result(numbers))

# users = ["Anton", "Vlad", "Geeks", "Mirbek"]
# result = list(map(lambda num: f"{num} - {len(num)} букв ", users))
# for res in result:
#     print(res)

# result = list(map(lambda x: x[0], users))
# print(result)

# result = list(map(lambda x: x.upper(), users))
# print(result)


# Работа с файлами
# 1 способ - обычная функция
# file_write = open("geeks.txt", "w")
# file_write.write("Привет меня зовут Оля!")

# file_read = open ("test.txt", "r")
# result = file_read.read()
# print(result)

# Что такое лямбда в Python?

# nurbo = open("nurbo.txt", "r")
# result = nurbo.read()
# print(result)

# kani = open("kani.txt", "w")
# kani.write(result)
# print(kani)


# 2 способ -как функция
# names = ["Mergul", "Erbol", "Yryskeldi", "Beishen", "Omonboi", "Nurai", "Bakai"]

# with open ("names.txt", "w") as file_write:
#     for i in names:
#         file_write.write(f"Имя: {i}\n")

# with open ("geeks.txt", "r") as reader:
#     result = reader.read()
#     print(result)

