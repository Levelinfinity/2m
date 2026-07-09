# Задание 1
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a > b:
    print("Большее число:", a)
else:
    print("Большее число:", b)



# Задание 2
num = int(input("Введите число: "))

if num % 2 == 0:
    print("Число чётное")
else:
    print("Число нечётное")



# Задание 3

goroda = ["Ош", "Бишкек", "Джалал-Абад", "Нарын", "Каракол"]

print("Второй:", goroda[1])
print("Четвертый:", goroda[3])



# Задание 4
names = ["Али", "Анна", "Иван", "Мария"]

names.insert(0, "Алексей")

print(names)



# Задание 5
chisla = [10, 20, 30, 40, 50]

chisla.remove(20)

print(chisla)



# Задание 6
strani = ("Кыргызстан", "Казахстан", "Китай", "Турция", "Италия")

print("Первый:", strani[0])
print("Последний:", strani[-1])



# Задание 7
ocenka = int(input("Введите оценку (от 1 до 5): "))

if ocenka == 5:
    print("Отлично")
elif ocenka == 4:
    print("Хорошо")
elif ocenka == 3:
    print("Удовлетворительно")
elif ocenka == 2 or ocenka == 1:
    print("Неудовлетворительно")
else:
    print("Такой оценки нет")



# Задание 8
langs = ["Python", "Java", "C++", "JavaScript"]

index = langs.index("C++")

print("Индекс:", index)
