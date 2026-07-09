# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.golos = golos

#     def info(self):
#         return f"{self.name} ему {self.age} года он мяукает {golos}"

# cat1 = Cat("Bob", 3)
# print(cat1)
# print(cat1.name)
# print(cat1.age)
# print(golos)
# print(cat1.info())


# class Student:
#     def __init__(self, name, age):
#         self.age = age
        
#     def info(self):
#         print(f"Имя студента {self.name}")
#         print(f"Возраст студента {self.age}")

#     def change_age(self, new_age):
#         self.age = new_age
#         print(f"Возраст студента {self.name} изменен на {self.age}")

#     def change_name(self, new_name):
#         self.name = new_name
#         print(f"Имя студента изменено на {self.name}")

# student1 = Student("Alice", 20)
# student2 = Student("Bob", 22)
# student3 = Student("Abdulloh", 16)

# student1.info()
# student2.info()
# student3.info()
# student1.change_age(21)
# student1.change_name("Davidson")

# class BancAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Депозит успешно выполнен! {amount}")

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Недостаточно средств на счете!")
#         else:
#             self.balance -= amount
#             print(f"Снятие успешно выполнено! {amount}")

#     def show_balance(self):
#         print(f"Баланс : {self.balance}")

# account = BancAccount("Alice", 1000)
# account.show_balance()
# account.deposit(500)
# account.withdraw(300)
# account.show_balance()

