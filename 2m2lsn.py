# class Animal:
#     def eat(self):
#         print(f"{self.name} ест")

# class cat(Animal):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color

#     def meow(self):
#         print(f"{self.name} мяукает")

# class dog(Animal):
#     def bark(self):
#         print(f"{self.name} лает")

# cat = cat("Барсик", "Серый")
# dog = dog("Шарик")

# print(cat.name)
# print(cat.color)

# cat.eat()
# cat.meow()
# dog.bark()
# dog.eat() 


# class Animal:
#     def sound(self):
#         pass

# class cat(Animal):
#     def sound(self):
#         print("мяу")
        
# class dog(Animal):
#     def sound(self):
#         print("гав")

# cat = cat()
# cat.sound()
# dog = dog()
# dog.sound()


class payment:
    def pay(self):
        pass

class card(payment):
    def pay(self):
        print("Оплата произведена картой")

class cash(payment):
    def pay(self):
        print("Oплата произведена наличкой")

class paypal(payment):
    def pay(self):
        print("Оплата произведена через PayPal")

payments_list = (card, cash, paypal)

for payment_method in payments_list:
    payment_method.pay(payment)


print("Запуск обработки платежей")
print("-" * 30)