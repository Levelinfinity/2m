# Task1
n = int(input("Введите число: "))
faktorial = 1

for i in range(1, n + 1):
    faktorial = faktorial * i

print("Факториал равен:", faktorial)



# Task2
num = int(input("Введите число: "))
kolichestvo = 0

for i in range(1, num + 1):
    if num % i == 0:
        kolichestvo = kolichestvo + 1

print("Количество делителей:", kolichestvo)



# Task3
print("Простые числа от 1 до 100:")

for x in range(2, 101):
    prostoye = True
    
    for i in range(2, x):
        if x % i == 0:
            prostoye = False
            break
            
    if prostoye == True:
        print(x, end=" ")
print()



# Task4
n = int(input("Введите число: "))
max_delitel = 1

for i in range(1, n):
    if n % i == 0:
        max_delitel = i

print("Наибольший делитель:", max_delitel)



# Task5
n = int(input("Введите число n: "))
summa = 0

for i in range(1, n + 1):
    summa = summa + i * i

print("Сумма квадратов:", summa)
