# Словарь - тип данных, где можно хранить пару элементов. Хранится ключ и значение. {'ключ': 'значение'}. Создаются в {} скобках.
# student = {'name': 'Olya', 'age': 21, 'hobbi': 'Tenis'}
# print(student['name'])
# print(student['hobbi']) 

# # Нельзя использовать индекс, только с помощью ключа
# print(student)
# student['city'] = "Osh" #Добовляем новый элемент с помощью ключа
# print(student)

# student['age']= 22 #Меняем значение ключа
# print(student)

# student.pop('hobbi') #Удаляем внутри словаря
# print(student)

# del student['hobbi'] # Второй вариант удаления из словаря
# print(student)

# my = {"name": "Geeks", "age": 19, "city": "Osh"}
# print(f"Привет, меня зовут {my['name']}, мне {my['age']}. Я живу в городе {my['city']}")  

#set, fronzenset 
# Не хранят дубликатов
# Создается с помощью фигурных скобок
# Не имеют стуктуру и порядок и поэтому меняются местами
# Нельзя использовать индексы и срезы
# set() - Изменяемы тип данных
# fronzenset() - не изменяемы тип данных
# user = {"Nurbolot", "Musu", "Kutbuhan", "Beksultan", "Islam", "Geeks"}
# print(user)
# # print(user[0]) не работает

# user.add("Nurai") #Добавление нового элемента
# print(user)

# # user.remove("Musu") #Первый метод удаления
# # print(user)    #Показывает ошибку при удаление несуществующего объекта

# user.discard("Kutbuhan") #Второй метод удалния
# print(user)     #Игнорирует ошибку при удаление несуществующего объекта

# users = frozenset(["Nirbolot", "Vlad", "Olya", "Ira"])
# print(users)
# users.add("Geeks")  Не работает так как не изменяемый тип данных



import random

users_health = 5
bot_health = 5
while True:
    if users_health ==0:
        print("Игра окончена, у вас осталось 0 попыток")
        break
    elif bot_health ==0:
        print("Игра окончена, у бота осталось 0 попыток")
        break
    else:
        bot = random.choice(["Камень", "Ножницы", "Бумага"])
        user = input("Введите ваш выбор: ")
        if user == "Камень":
            if bot == "Камень":
                print(f"Ничья.У вас: {users_health} попыток, у бота: {bot_health}")
            elif bot == "Ножницы":
                bot_health -=1
                print(f"Вы выиграли. У вас: {users_health} попыток, у бота: {bot_health}")
            elif bot =="Бумага":
                users_health -=1
                print(f"Вы проиграли. У вас: {users_health} попыток, у бота: {bot_health}")
        elif user =="Ножницы":
            if bot == "Камень":
                users_health -=1
                print(f"Вы проиграли. У вас: {users_health} попыток, у бота: {bot_health}")
            elif bot == "Ножницы":
                print(f"Ничья.У вас: {users_health} попыток, у бота: {bot_health}")
            elif bot =="Бумага":
                bot_health -=1
                print(f"Вы выиграли. У вас: {users_health} попыток, у бота: {bot_health}")
        elif user =="Бумага":
            if bot == "Камень":
                bot_health -=1
                print(f"Вы выиграли. У вас: {users_health} попыток, у бота: {bot_health}")
            elif bot == "Ножницы":
                users_health -=1
                print(f"Вы проиграли. У вас: {users_health} попыток, у бота: {bot_health}")
            elif bot =="Бумага":
                print(f"Ничья.У вас: {users_health} попыток, у бота: {bot_health}")
        else:
            print("Неверный вариант, введи снова!!!")
