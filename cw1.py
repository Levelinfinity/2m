number1 = (int(input("Введите первое число:")))
number2 = (int(input("Введите второе число:")))

if number1 > number2:
     print("Первое число больше второго")
elif number2 > number1:
     print("Второе число больше первого")
else:
     print("Числа равны")

if number1 > 0 and number2 > 0:
     print("Оба числа положительные")


chislo = int(input("Введите число: "))
if chislo >= 1 and chislo <= 10:
    print("Число в диапазоне 1-10")
elif chislo >= 11 and chislo <= 100:
    print("Число в диапазоне 11-100")
else:
    print("Число вне диапазона")


imya = input("Введите свое имя: ")
print(f"{len(imya)}-букв")
if len(imya) < 5:
    print("короткое имя")
elif len(imya) >= 5 and len(imya) < 8:
    print("среднее имя")
elif len(imya) > 8:
    print("длинное имя")



numbers = [7, 3, 15, 2]
print(numbers)
print(numbers[1])
print(numbers[-1])
numbers[0], numbers[3] = numbers[3], numbers[0]
print(numbers)


summa = int(input("Введите сумму покупки: "))
if summa >= 5000:
    print("Vasha skidka sostavlyaet 10%")
    summas = summa / 100 * 10
    print(f"Итоговая сумма после скидки составляет: {summa - summas}")
elif summa >=2000 and summa < 5000:
     print("vasha skidka sostavlyaet 5%")
     summas2 = summa / 100 * 5 
     print(f"Итоговая сумма после скидки составляет: {summa - summas2}")
else:
    print("Скидки нет")
    print(f"Итоговая сумма составляет: {summa} ")