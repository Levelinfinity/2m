from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, brand, model, year, fuel=100):
        if year < 0:
            raise ValueError("Год выпуска не может быть меньше нуля.")
        self.id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = 0
        self.__fuel = fuel if 0 <= fuel <= 100 else 100
        self.engine_started = False

    def start_engine(self):
        self.engine_started = True
        print(f"Двигатель {self.brand} {self.model} запущен.")

    def stop_engine(self):
        self.engine_started = False
        print(f"Двигатель {self.brand} {self.model} остановлен.")

    def get_mileage(self):
        return self.__mileage

    def get_fuel(self):
        return self.__fuel

    def refuel(self, amount):
        if amount < 0:
            print("Количество топлива не может быть меньше 0%.")
            return
        if self.__fuel + amount > 100:
            print("Нельзя заправить топлива больше чем 100%.")
            return
        self.__fuel += amount
        print(f"Заправлена на {self.__fuel}%")

    def consume_fuel(self, amount):
        if self.__fuel - amount < 0:
            return False
        self.__fuel -= amount
        return True

    def drive(self, km):
        if km < 0:
            print("Расстояние поездки не может быть меньше 0.")
            return
        if not self.engine_started:
            print("Сначала нужно запустить двигатель.")
            return
        if self.__fuel <= 0:
            print("Нет топлива.")
            return

        fuel_needed = km * 0.1
        if self.consume_fuel(fuel_needed):
            self.__mileage += km
            print(f"Проехали {km} км. Новый пробег: {self.__mileage} км. Остаток топлива: {self.__fuel:.1f}%")
        else:
            print("Недостаточно топлива для совершения этой поездки.")

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def service(self):
        pass


class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, doors, body_type, fuel=100):
        super().__init__(vehicle_id, brand, model, year, fuel)
        self.doors = doors
        self.body_type = body_type

    def info(self):
        print(f"Легковой автомобиль {self.brand} {self.model} | ID: {self.id} | Год: {self.year} | Пробег: {self.get_mileage()} | Топливо: {self.get_fuel()}% | Дверей: {self.doors} | Тип кузова: {self.body_type}")

    def service(self):
        print(f"Обслуживание легкового автомобиля {self.brand} {self.model}: Замена масла")


class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, max_load, fuel=100):
        super().__init__(vehicle_id, brand, model, year, fuel)
        self.max_load = max_load

    def info(self):
        print(f"Грузовик {self.brand} {self.model} | ID: {self.id} | Год: {self.year} | Пробег: {self.get_mileage()} | Топливо: {self.get_fuel()}% | Макс. нагрузка: {self.max_load} тонн")

    def service(self):
        print(f"Обслуживание грузовика {self.brand} {self.model}: Замена масла и проверка гидравлики")


class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, engine_volume, fuel=100):
        super().__init__(vehicle_id, brand, model, year, fuel)
        self.engine_volume = engine_volume

    def info(self):
        print(f"Мотоцикл {self.brand} {self.model} | ID: {self.id} | Год: {self.year} | Пробег: {self.get_mileage()} | Топливо: {self.get_fuel()}% | Объем двигателя: {self.engine_volume} куб.см")

    def service(self):
        print(f"Обслуживание мотоцикла {self.brand} {self.model}: Замена цепи")


class Bus(Vehicle):
    def __init__(self, vehicle_id, brand, model, year, seats, fuel=100):
        super().__init__(vehicle_id, brand, model, year, fuel)
        self.seats = seats

    def info(self):
        print(f"Автобус {self.brand} {self.model} | ID: {self.id} | Год: {self.year} | Пробег: {self.get_mileage()} | Топливо: {self.get_fuel()}% | Мест: {self.seats}")

    def service(self):
        print(f"Обслуживание автобуса {self.brand} {self.model}: Проверка пассажирских сидений")

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.vehicles.append(vehicle)
            print(f"Транспорт {vehicle.brand} {vehicle.model} успешно добавлен.")
        else:
            print("Ошибка добавления транспорта.")

    def remove_vehicle(self, vehicle_id):
        vehicle = self.find_vehicle(vehicle_id)
        if vehicle:
            self.vehicles.remove(vehicle)
            print(f"Транспорт с ID {vehicle_id} успешно удален.")
            return True
        print("Транспорт с таким ID не найден.")
        return False

    def find_vehicle(self, vehicle_id):
        for v in self.vehicles:
            if v.id == vehicle_id:
                return v
        return None

    def show_all(self):
        if not self.vehicles:
            print("Автопарк пуст.")
            return
        for v in self.vehicles:
            v.info()

    def service_all(self):
        if not self.vehicles:
            print("Нет транспорта для обслуживания.")
            return
        for v in self.vehicles:
            v.service()

    def drive_vehicle(self, vehicle_id, km):
        vehicle = self.find_vehicle(vehicle_id)
        if vehicle:
            vehicle.start_engine()
            vehicle.drive(km)
            vehicle.stop_engine()
        else:
            print("Транспорт с таким ID не найден.")

    def sort_by_year(self):
        self.vehicles.sort(key=lambda x: x.year)
        print("Транспорт отсортирован по году выпуска.")

    def sort_by_mileage(self):
        self.vehicles.sort(key=lambda x: x.get_mileage())
        print("Транспорт отсортирован по пробегу.")

class Driver:
    def __init__(self, fullname, age, experience, license_category):
        self.fullname = fullname
        self.age = age
        self.experience = experience
        self.license_category = license_category
        self.assigned_vehicle = None

    def assign_vehicle(self, vehicle):
        if isinstance(vehicle, Vehicle):
            self.assigned_vehicle = vehicle
            print(f"Водителю {self.fullname} назначен транспорт {vehicle.brand} {vehicle.model} (ID: {vehicle.id}).")
        else:
            print("Ошибка назначения транспорта.")

    def remove_vehicle(self):
        if self.assigned_vehicle:
            print(f"С водителя {self.fullname} снят транспорт {self.assigned_vehicle.brand} {self.assigned_vehicle.model}.")
            self.assigned_vehicle = None
        else:
            print(f"У водителя {self.fullname} нет назначенного транспорта.")

    def show_vehicle(self):
        if self.assigned_vehicle:
            print(f"Водитель {self.fullname} закреплен за транспортом:")
            self.assigned_vehicle.info()
        else:
            print(f"У водителя {self.fullname} нет назначенного транспорта.")


def main():
    fleet = Fleet()
    drivers = []

    while True:
        print("\n--- Меню автопарка ---")
        print("1. Добавить транспорт")
        print("2. Удалить транспорт")
        print("3. Показать транспорт")
        print("4. Найти транспорт")
        print("5. Отправить на обслуживание")
        print("6. Заправить машину")
        print("7. Проехать расстояние")
        print("8. Назначить водителя")
        print("9. Показать водителей")
        print("10. Сортировка")
        print("0. Выход")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            print("\nВыберите тип транспорта:")
            print("1 - Машина, 2 - Фура, 3 - Мотоцикл, 4 - Автобус")
            t_type = input().strip()

            try:
                vehicle_id = int(input("Введите ID: "))
                if fleet.find_vehicle(vehicle_id):
                    print("Транспорт с таким ID уже существует!")
                    continue
                brand = input("Марка: ")
                model = input("Модель: ")
                year = int(input("Год выпуска: "))
                if year < 0:
                    print("Ошибка: год не может быть отрицательным!")
                    continue
                fuel = int(input("Начальный уровень топлива (0-100): "))
                if fuel < 0 or fuel > 100:
                    print("Ошибка: неверный уровень топлива!")
                    continue
                if t_type == "1":
                    doors = int(input("Количество дверей: "))
                    body_type = input("Тип кузова: ")
                    fleet.add_vehicle(Car(vehicle_id, brand, model, year, doors, body_type, fuel))
                elif t_type == "2":
                    max_load = float(input("Максимальный вес (тонны): "))
                    fleet.add_vehicle(Truck(vehicle_id, brand, model, year, max_load, fuel))
                elif t_type == "3":
                    engine_volume = int(input("Объем двигателя: "))
                    fleet.add_vehicle(Motorcycle(vehicle_id, brand, model, year, engine_volume, fuel))
                elif t_type == "4":
                    seats = int(input("Количество мест: "))
                    fleet.add_vehicle(Bus(vehicle_id, brand, model, year, seats, fuel))
                else:
                    print("Неверный выбор типа транспорта.")
            except ValueError:
                print("Ошибка ввода числовых данных.")
        elif choice == "2":
            try:
                vehicle_id = int(input("Введите ID транспорта для удаления: "))
                fleet.remove_vehicle(vehicle_id)
            except ValueError:
                print("Некорректный ID.")

        elif choice == "3":
            fleet.show_all()

        elif choice == "4":
            try:
                vehicle_id = int(input("Введите ID для поиска: "))
                vehicle = fleet.find_vehicle(vehicle_id)
                if vehicle:
                    vehicle.info()
                else:
                    print("Транспорт не найден.")
            except ValueError:
                print("Некорректный ID.")

        elif choice == "5":
            print("1 - Обслужить конкретный транспорт, 2 - Обслужить весь парк")
            sub_choice = input().strip()
            if sub_choice == "1":
                try:
                    vehicle_id = int(input("Введите ID транспорта: "))
                    vehicle = fleet.find_vehicle(vehicle_id)
                    if vehicle:
                        vehicle.service()
                    else:
                        print("Транспорт не найден.")
                except ValueError:
                    print("Некорректный ID.")
            elif sub_choice == "2":
                fleet.service_all()

        elif choice == "6":
            try:
                vehicle_id = int(input("Введите ID транспорта: "))
                vehicle = fleet.find_vehicle(vehicle_id)
                if vehicle:
                    amount = int(input("Сколько топлива добавить: "))
                    vehicle.refuel(amount)
                else:
                    print("Транспорт не найден.")
            except ValueError:
                print("Некорректный ввод.")

        elif choice == "7":
            try:
                vehicle_id = int(input("Введите ID транспорта: "))
                km = float(input("Введите расстояние (км): "))
                fleet.drive_vehicle(vehicle_id, km)
            except ValueError:
                print("Некорректный ввод.")
  
        elif choice == "8":
            fullname = input("ФИО водителя: ")
            try:
                age = int(input("Возраст водителя: "))
                experience = int(input("Стаж: "))
                license_category = input("Категория прав: ")
                driver = Driver(fullname, age, experience, license_category)
                
                vehicle_id = int(input("Введите ID транспорта для назначения: "))
                vehicle = fleet.find_vehicle(vehicle_id)
                if vehicle:
                    driver.assign_vehicle(vehicle)
                    drivers.append(driver)
                else:
                    print("Транспорт с таким ID не найден. Водитель не создан.")
            except ValueError:
                print("Некорректный ввод параметров водителя.")

        elif choice == "9":
            if not drivers:
                print("Список водителей пуст.")
            for d in drivers:
                print(f"Водитель: {d.fullname} | Возраст: {d.age} | Стаж: {d.experience} | Категория: {d.license_category}")
                d.show_vehicle()
                print("-" * 20)

        elif choice == "10":
            print("1 - Сортировка по году выпуска, 2 - Сортировка по пробегу")
            sort_choice = input().strip()
            if sort_choice == "1":
                fleet.sort_by_year()
            elif sort_choice == "2":
                fleet.sort_by_mileage()
            else:
                print("Неверный выбор.")

        elif choice == "0":
            print("Завершение работы программы.")
            break
        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()