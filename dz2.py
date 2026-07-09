age = int(input("Введите ваш возраст: "))

print("Возраст больше или равен 18?")
print(age >= 18)

print("Возраст меньше 60?")
print(age < 60)

print("Возраст от 18 до 60?")
print(age >= 18 and age <= 60)


name = input("Введите имя: ")
age = int(input("Введите возраст: "))
homew = int(input("Введите количество выполненных дз : "))

print("Имя пользователя:", name)

print("Тип переменной name:", type(name))
print("Тип переменной age:", type(age))
print("Тип переменной homew:", type(homew))

print("Возраст больше 16 лет?")
print(age > 16)

print("Количество дз больше 5?")
print(homew > 5)

if age < 16:
    print("Вам меньше 16")
if homew < 5:
    print("У вас недостаточно дз")
if age > 16 and homew > 5:
    print(f"Ваш ник {name}")
