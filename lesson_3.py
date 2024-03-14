# LIST-список (хранит любые типы данных)(строки, числа, или же другие списки)
# Для создания списка используются-[]
# name = [1,2,3,4,5,6,7,8,9,10]
# print(type(name))

# users = ['Geeks', 'Beksultan', 'Nurbek', 'Anton']
# print(users [1])
# print(users [0 : 3])

# # type_data = [5, "Пять", 5.5, True, [1,2,3,4,5], 5]
# # print(type_data)

# #  Для добавления В КОНЕЦ СПИСКА - .append
# users = ['Geeks', 'Beksultan', 'Geeks', 'Nurbek', 'Anton']
# user_list = ["Nuray", 'Geeks',"Kutbuhan", "Muha", 'Geeks']
# print (users)
# users.append("Aigul")
# print(users)
# #  Для добавления по индексу; в любое место(в начало, в середину, в любое место в списке)
# users.insert(1, "Musu")
# print(users)

# # Для удаления из списка
# users.remove("Nurbek")
# print(users)

# users.pop(3)  #Для удаления по индексу
# print(users)
# users.extend(user_list) #Для объединения двух списков
# print(users)
# # third_elem = users[2] #Доступ к какому-то элементу по индексу
# # print(third_elem)
# # print(users.index("Nuray")) # Для нахождения индекса среди списка

# print(users.count ('Geeks')) #Для нахождения количества элемент

# users.reverse()  #Перевернуть список
# print(users)

# users.sort() # ДЛя сортировки элементов по алфавиту
# print(users)

# users.clear() #Очищает список
# print(users)


# print(users[::-1]) #Превернуть список с помощью индекса элемента

# text = input ("Введите имя:")
# text2 = int (input ("Введите свой возрост:"))
# users = ()
# if text2 >= 18:
#     print(" Добро пожаловать!")
#     users.append(text)
#     print(f"Список пользователей: {users}")
# elif text2 <= 18:
#      print(" Добро пожаловать!")
# else:
#       print("Доступ запрещен!")
#       print(f"Список пользователей: {users}")

# cars = ["Mersedes", "BMW", "Kia", "Tayota", "Supre", "Nissan", "Huanday", "Tiko", "Matiz"]
# name = input("Введите Ваше имя: ")
# auto = input ("Введите название авто:")
# if auto in cars:
#     print(f" Уважаемый, {name}, Выш выбор у нас есть в наличи. Ваш выбор {auto} ")
# else:
#     print(f"Уважаемый, {name}, Вашего выбора у нас нет в наличии. Ваш выбор {auto}")