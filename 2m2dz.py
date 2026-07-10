class Delivery:
    def __init__(self, sender, receiver, distance):
        self.sender = sender
        self.receiver = receiver
        self.distance = distance

    def calculate_price(self):
        pass

    def deliver(self):
        print(f"Доставка от {self.sender} к {self.receiver} на расстоянии {self.distance} км.")
    
    def estimated_time(self):
        pass


class CarDelivery(Delivery):
    def calculate_price(self):
        return self.distance * 15

    def estimated_time(self):
        return self.distance / 60


class AirDelivery(Delivery):
    def calculate_price(self):
        return self.distance * 50 + 500


    def estimated_time(self):
        return self.distance / 700


class DroneDelivery(Delivery):
    def calculate_price(self):
        if self.distance > 30:
            print("Дрон не может доставить на такое расстояние")
            return 0
        return self.distance * 30
    

    def estimated_time(self):
        if self.distance > 30:
            return 0
        return self.distance / 40
    


deliveries = [
    CarDelivery("Алексей", "Иван", 50),
    AirDelivery("Бишкек", "Ош", 600),
    DroneDelivery("ПВЗ", "Дом 1", 12),
    DroneDelivery("Аман", "Манас", 35),
    CarDelivery("KFC", "Дом 5",10)
]

print("легкий тест доставки")
for d in deliveries:
    d.deliver()
    price = d.calculate_price()
    time = d.estimated_time()
    print(f"Стоимость доставки: {price}, Время: {round(time, 2)} ч.")
    print("-" * 25)



class DeliveryManager:
    def __init__(self):
        self.deliveries = []

    def add_delivery(self, delivery):
        self.deliveries.append(delivery)

    def show_all(self):
        print("\n=== ВСЕ ДОСТАВКИ ===")
        for d in self.deliveries:
            d.deliver()

    def total_income(self):
        total = 0
        for d in self.deliveries:
            total += d.calculate_price()
        return total

    def most_expensive_delivery(self):
        if len(self.deliveries) == 0:
            return None
                
        expensive = self.deliveries[0]
        for d in self.deliveries:
            if d.calculate_price() > expensive.calculate_price():
                expensive = d
        return expensive
    

manager = DeliveryManager()

manager.add_delivery(CarDelivery("Ош", "Кара-Суу", 25))
manager.add_delivery(AirDelivery("Бишкек", "Ош", 650))
manager.add_delivery(DroneDelivery("Кафе", "Парк", 5))
manager.add_delivery(DroneDelivery("Склад", "Алай", 45))

manager.show_all()

print(f"\nОбщая выручка: {manager.total_income()}")

best = manager.most_expensive_delivery()
if best:
    print("\nСамая дорогая доставка:")
    best.deliver()
    print(f"Цена: {best.calculate_price()}")