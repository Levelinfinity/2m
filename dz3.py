number = int(input("Введите число: "))
if number > 100:
    print("Большое число")
elif number < 100:
    print("Маленькое число")
else:
    print("Ровно 100")
 

age = int(input("Введите возраст: "))
if age < 18:
    print("Несовершеннолетний")
else:
    print("Совершеннолетний")
 

chislo = int(input("Введите число: "))
if chislo % 3 == 0:
    print("Делится на 3")
else:
    print("Не делится на 3")
 

films = ["Naruto", "One Piece", "Death Note", "Tokyo Ghoul", "Attack on Titan"]
print("Весь список:", films)
print("Первый элемент:", films[0])
print("Последний элемент:", films[-1])
 

gorod = ['Bishkek','Manas','Naryn']
gorod.append('Talas')
gorod.insert(2, 'Osh')
print(gorod)

 

numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
numbers.remove(50)
print(numbers)
 

names = ["Nurbolot", "Islam", "Adina", "Beksultan"] 
names.sort()
names.reverse()
print(names)


colors = ('Красный', 'Зеленый', 'Синий', 'Желтый', 'Фиолетовый')
print(colors)
print(colors[2])
print(len(colors))


zapros1 = int(input("Введите первое число: "))
zapros2 = int(input("Введите второе число: "))
print("Сумма", zapros1 + zapros2)
print("Разность", zapros1 - zapros2)
print("Произведение", zapros1 * zapros2)
print("Результат деления", zapros1 / zapros2)

 

zapros = int(input("Введите число от 1 до 7: "))

if zapros == 1:
    print("Понедельник")
elif zapros == 2:
    print("Вторник")
elif zapros == 3:
    print("Среда")
elif zapros == 4:
    print("Четверг")
elif zapros == 5:
    print("Пятница")
elif zapros == 6:
    print("Суббота")
elif zapros == 7:
    print("Воскресенье")
else:
    print("Ошибка") 