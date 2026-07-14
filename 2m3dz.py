from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("гав")
        
class Cat(Animal):
    def make_sound(self):
        print("мяу")

class Bird(Animal):
    def make_sound(self):
        print("чик чирик")

animals = [Dog(), Cat(), Bird()]

for animal in animals:
    animal.make_sound()



class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнение на {amount}, баланс составляет: {self.__balance}")
        else:
            print("нельзя пополнить на отрицательную сумму")

    def withdraw(self, amount):
        if amount <= 0:
            print("сумма снятия не может быть меньше нуля!")
        else:
            self.__balance -= amount
            print(f"Снято {amount}. баланс: {self.__balance}")

    def get_balance(self):
        return self.__balance
    
    def calculate_profit(self):
        return 0 
    

class CreditAccount(BankAccount):
    def __init__(self, owner, balance=0, credit_limit=5000):
        super().__init__(owner, balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        total_available  = self.get_balance() + self.credit_limit
        if amount > total_available:
            print("Превышен кредитный лимит!")
        else:
            super().withdraw(amount)

    def calculate_profit(self):
        if self.get_balance() < 0:
            fee = abs(self.get_balance()) * 0.1
            return -fee
        return 0 
    

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def calculate_profit(self):
        profit = self.get_balance() * self.interest_rate
        return profit
    

accounts = [
    CreditAccount("Аман", -1000, 5000),
    SavingsAccount("Андрей", 10000, 0.07)
]

for acc in accounts:
    print(f"Счет: {acc.owner}. Прибыль: {acc.calculate_profit()}")



class Delivery(ABC):
    def __init__(self, address, price):
        self.address = address
        self.price = price

    @abstractmethod
    def deliver(self):
        pass

    def calculate_price(self):
        return self.price


class CourierDelivery(Delivery):
    def __init__(self, address, courier_name, price=200):
        super().__init__(address, price)
        self.courier_name = courier_name

    def deliver(self):
        print(f"Курьер {self.courier_name} несет заказ пешком по адресу: {self.address}")


class CarDelivery(Delivery):
    def __init__(self, address, distance, price_per_km=50):
        self.distance = distance
        self.price_per_km = price_per_km
        super().__init__(address, distance * price_per_km)

    def deliver(self):
        print(f"Машина везет заказ по адресу: {self.address}. Расстояние: {self.distance} км")


class DroneDelivery(Delivery):
    def __init__(self, address, max_weight, order_weight, price=500):
        super().__init__(address, price)
        self.max_weight = max_weight
        self.order_weight = order_weight

    def deliver(self):
        if self.order_weight > self.max_weight:
            print(f"Дрон не может взлететь! Вес заказа ({self.order_weight}кг) превышает лимит ({self.max_weight}кг).")
        else:
            print(f"Дрон летит по воздуху по адресу: {self.address}. Вес в норме.")


class Order:
    def __init__(self, delivery_type: Delivery):
        self.products = []
        self.__total_price = 0  
        self.delivery_type = delivery_type

    def add_product(self, product, price):
        self.products.append(product)
        self.__total_price += price
        print(f"Добавлен товар: '{product}' за {price}")

    def remove_product(self, product, price):
        if product in self.products:
            self.products.remove(product)
            self.__total_price -= price
            print(f"Удален товар: '{product}'")
        else:
            print("Такого товара нет в заказе!")

    def get_total_price(self):
        return self.__total_price + self.delivery_type.calculate_price()


deliveries = [
    CourierDelivery("ул. Ленина 15", "Азиз"),
    CarDelivery("ул. Курманжан Датка 42", 12),
    DroneDelivery("ул. Масалиева 2", max_weight=5, order_weight=3)
]

print("--- Проверка работы доставок ---")
for d in deliveries:
    d.deliver()
    print(f"Стоимость этой доставки: {d.calculate_price()}\n")

print("--- Проверка работы Заказа ---")
order = Order(deliveries[1])  
order.add_product("Пицца", 500)
order.add_product("Кола", 100)
print(f"Итоговая стоимость всего заказа с доставкой: {order.get_total_price()}")