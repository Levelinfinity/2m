# Task1

student = dict(name="Азамат", age=17, group="Geeks-41", avrgpnt=4.5)

print(student)
print("Имя:", student["name"])
print("Средний балл:", student["avrgpnt"])


# Task 2

tovari = {
    "Хлеб": 30,
    "молоко": 70,
    "яблоки": 120,
    "альпенголд": 100,
    "сок": 110
}
max_tovar = ""
max_cena = 0
min_tovar = ""
min_cena = 999999
summa_cen = 0

for tovar, cena in tovari.items():
    summa_cen = summa_cen + cena
    
    if cena > max_cena:
        max_cena = cena
        max_tovar = tovar
        
    if cena < min_cena:
        min_cena = cena
        min_tovar = tovar

srednyaya_cena = summa_cen / len(tovari)

print("Самый дорогой товар:", max_tovar, "-", max_cena)
print("Самый дешевый товар:", min_tovar, "-", min_cena)
print("Средняя цена всех товаров:", srednyaya_cena)


# Task 3

slova = set()
for i in range(5):
    slovo = input("Введите слово: ")
    slova.add(slovo)

print("Уникальные слова:", slova)
print("Количество уникальных слов:", len(slova))




# Task4

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

obshie = set()

for x in a:
    if x in b:
        obshie.add(x)
print("Общие элементы:", obshie)

tolko_a = set()
for x in a:
    if x not in b:
        tolko_a.add(x)
print("Только в a:", tolko_a)

tolko_b = set()
for x in b:
    if x not in a:
        tolko_b.add(x)
print("Только в b:", tolko_b)


vse = list(a) + list(b)
print("Объединение множеств:", set(vse))


# Task 5

jurnal = {
    "Ислам": [5, 4, 5],
    "Исхак": [3, 4, 4],
    "Рамзан": [5, 5, 5]
}

for name, ocenki in jurnal.items():
    summa_ocenok = 0
    for ocenka in ocenki:
        summa_ocenok = summa_ocenok + ocenka
    srednyaya = summa_ocenok / len(ocenki)
    print("Средняя оценка студента", name, ":", srednyaya)




# Task 6
stroka = input("Введите строку: ")
bukvi_dict = {}

for bukva in stroka:
    if bukva in bukvi_dict:
        bukvi_dict[bukva] = bukvi_dict[bukva] + 1
    else:
        bukvi_dict[bukva] = 1

print(bukvi_dict)



# Task 7
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]

clear_numbers = list(set(numbers))
print(clear_numbers)


# Task 8

student1subjects = {"Математика", "Физика", "История"}
student2subjects = {"Программирование", "Физика", "Английский"}

print("Одинаковые предметы:", student1subjects.intersection(student2subjects))
print("Предметы первого студента:", student1subjects)
print("Предметы второго студента:", student2subjects)


# Task 9
kvadrat = lambda x: x * x

chisla = [2, 4, 6, 8]

rezultat = list(map(kvadrat, chisla))
print(rezultat)


# Task 10
chislo = int(input("Введите число: "))

for i in range(1, 11):
    print(chislo, "x", i, "=", chislo * i)