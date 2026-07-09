# number = 0
# while True:
#     number += 9999
#     print(number)
# while True:
#     number = int(input("Privet vvedi chislo"))
#     if number % 2 == 0:
#         print("Chetnoe")
#     else:
#         print("Ne chetnoe")

# int - celye 
# float - ne chet
# bool - logicheskiy
# str - stroki

# turlpe - korteji ne izmenyaemyi ()
# list - spisok izmenyaemyi []


# set - 
# frozenset - 

# dict - slovar' {}
# данные хранятся ключом в значении 
# Ключ всегда пишется str внутри ковычек  
# Значение можно указывать в разном варианте типов данных
# Индексы не работают вместо них ключи в кавычках
# переменная = {"ключ":"значение", "age":99, }

# student = {"name":"Nurbolot", "age":99, }
# print(student)
# print(student["name"])
# print(student["age"])
# student["hobby"] = "Football"
# print(student)

# student["name"] = "Beksultan"
# print(student)

# # del student["age"]
# # print(student)

# # student.pop("hobby")
# # print(student)

# # keys = Выводит только ключи
# print(student.keys())

# # values - выводит только значения
# print(student.values())

# # items - Выводит оба обьекта 
# print(student.items())

# Множества
# set
# frozenset 

# set = {}
# Изменяемый
# не имеет определенного порядка
# не имеет индексов
# не имеет дубликатов

# students = {"Aziza", "Nursultan", "Beka", "Ruslan"}
# print(students)

# students.add("Dinara")    #метод для добавления
# print(students)

# students.remove("Aziza")   #метод для удаления (вызывает ошибку)
# print(students)

# students.discard("Beksultan")  # метод удаления не вызывая ошибки 
# print(students)


# frozenset точно такой же но по другому создается не изменяемый внутри круглого любые скобки

# n = frozenset({"sss"})


# Функции
# Встроенные функции
# Исскусственные (Обычные)
# Анонимные функции

# Встроенные функции 

# print()
# input()
# len()
# max
# min


# Исскусственные 

# def test():
#     print("Hello World")

# test()