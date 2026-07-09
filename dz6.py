# Task1
summa = 0
while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    summa = summa + num
print("Итоговая сумма:", summa)



# Task2
while True:
    parol = input("Введите пароль: ")
    if parol == "python123":
        print("Успешный вход")
        break



# Task3
kniga = {
    "название": "Капитанская дочка",
    "автор": "Александр Пушкин",
    "год выпуска": 1836
}
print(kniga.keys())
print(kniga.values())



# Task4
student = {
    "name": "Асан",
    "age": 17,
    "city": "Ош"
}
student["group"] = "Geeks"
student["age"] = 18
student.pop("city")
print(student)



# Task5
imena = set()
for i in range(10):
    imya = input("Введите имя: ")
    imena.add(imya)
print("Количество уникальных имен:", len(imena))



# Task6
set1 = {"Асан", "Иван", "Али"}
set2 = {"Анна", "Али", "Иван"}
print(set1.intersection(set2))



# Task7
months = frozenset(["Январь", "Февраль", "Июнь", "Июль"])
if "Июнь" in months:
    print("Содержится")
else:
    print("Не содержится")



# Task8
mnojestvo = {1, 2, 3}
zamorojennoe = frozenset([1, 2, 3])

mnojestvo.add(4)
print("Обычное множество после add:", mnojestvo)

print("Объяснение: В обычное множество элемент добавился, а при попытке добавить в frozenset выйдет ошибка AttributeError, потому что frozenset неизменяемый!")



# Task9
def square(number):
    return number * number



# Task10
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
