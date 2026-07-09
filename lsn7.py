#Anonim functions 

# def numbers():
#     num1 = int(input("VVedite pervoe chislo"))
#     num2 = int(input("VVedite vtoroe chislo"))
#     print(num1+num2)
    

# def info():
#     name = "Nurbolot"
#     age = 25
#     print(f"Imya: {name}, vozrast: {age}")
    
    
# def info(name,age):
#     print(f"imya:, {name}, vozrast: {age}")
    
# info("Geeks", 9)
# info("Osh", 30)

# def results():
#     chislo = int(input("VVedite chislo: "))
#     if chislo % 2 == 0:
#         print("chislo chetnoe")
#     else:
#         print("ne chet")
# results()

# def results(chislo):
#     if chislo % 2 == 0:
#         print("Chislo chetnoe")
#     else:
#         print("ne chet")
# results(67)


# lambda - анонимная функция 
# функция пишется в одной строке 

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10.)

# for i in numbers:
#     print(i*2)

# def result(numbers_list):
#     for i in numbers:
#         print(i*2)
        
# result(numbers)

# result_lambda = list(map(lambda i: i*2, numbers))
# print(result_lambda)

# num1 = 4
# num2 = 4
# print(num1+num2)

# result = lambda num1,num2: num1 +num2
# print(result(4,2))

# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# result = list(filter(lambda i: i % 2 == 0, numbers))
# print(result)


# filter - замена для условных операторов и цикла 
# map - выполняет работу цикла (обращается к каждому обьекту)

# num1 = 85 
# print((lambda x: x*2)(num1))