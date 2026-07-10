# class BankAccount:
#     def __init__(self):
#       self.__balance = 1000

#     def deposit(self, amount):
#        self.__balance += amount

#     def get_balance(self):
#        return self.__balance
    
# acc = BankAccount()
# acc.deposit(500)
# print(acc.get_balance())
# # acc.balance = -50000
# # print(acc.balance)


# class User:
#     def __init__(self):
#         self.__age = 18

#     @property
#     def age(self):
#        return self.__age
    
#     @age.setter
#     def age(self, value):
#        if value >= 0:
#           self.__age = value

# user = User()
# user.age = 25
# print(user.age)    

# from abc import ABC, abstractmethod

# class Animal(ABC):
#    @abstractmethod
#    def sound(self):
#       pass
   
# class Dog(Animal):
#    def sound(self):
#       print("гав")


# class Cat(Animal):
#    def sound(self):
#       print("мяу")


# dog = Dog()
# dog.sound()

# cat = Cat()
# cat.sound()

# публичный - self.age 
# защищенный - self._age
# приватный - self.__age

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def __init__(self, name, salary):
        self.name = name 
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary


    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Зарплата не может быть отрицательной!")
            raise Exception("Отрицательная зарплата")
        else:
            self.__salary = value

    @abstractmethod
    def work(self):
        pass
class Programmer(Employee):
    def work(self):
        return self.name + "Пишет код"

class Designer(Employee):
    def work(self):
        return self.name + "Делает дизайн"

class Manager(Employee):
    def work(self):
        return self.name + "Менеджер"


workers = [
    Programmer("Аман", 100000),
    Designer("Райана", 70000),
    Manager("Аяна", 50000)
]

print("Кто как работает:")
for i in workers:
    print(i.work())

print("-" * 26)

aman = workers[0]
print(f"Текущая зарплата Амана составляет {aman.salary}")

aman.salary = 110000
print("Новая зарплата Амана составляет: {aman.salary}")

print("Отрицательное значение зарплаты для амана")
try:
    aman.salary = -100000
except Exception as oshibka:
    print(f"Ошибка {oshibka}")