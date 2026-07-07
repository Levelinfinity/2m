class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages 
    
    def info(self):
        print(f"Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}")
    
    def read(self):
        print(f"Читаем книгу: {self.title}")


book = Book("Гарри Поттер", "Джоан Роулинг", 500)
book.info()
book.read()


class Player:
    def __init__(self, name, health=100, level=1):
        self.name = name 
        self.health = health
        self.level = level

    def show_info(self):
        print(f"--- Игрок: {self.name} ---")
        print(f"Уровень: {self.level}")
        print(f"Здоровье: {self.health}")
        print("-" * 20)
    
    def take_damage(self, damage):
        self.health = self.health - damage
        print(f"{self.name} получил {damage} урона. Здоровье: {self.health}")
        if self.health <= 0:
            self.health = 0
            print(f"{self.name} получил {damage} урона. Текущее здоровье: {self.health}")
            print("Игрок погиб!")
        else:
            print(f"{self.name} получил {damage} урона. Текущее здоровье: {self.health}")

    
    def heal(self, amount):
        self.health = self.health + amount
        print(f"{self.name} восстановил {amount} здоровья. Текущее здоровье: {self.health}")

    def level_up(self):
        self.level = self.level + 1
        print(f"Поздравляем {self.name} поднял уровень до {self.level}")
    

player = Player("Knight")
player.show_info()
player.take_damage(30)
player.heal(20)
player.level_up()

player.show_info()

player.take_damage(100)



class OnlineStore:
    def __init__(self, name):
        self.name = name
        self.products = []  

    def add_product(self, product):
        self.products.append(product)
        print(f"Товар '{product}' успешно добавлен в магазин {self.name}.")

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            print(f"Товар '{product}' удален из магазина.")
        else:
            print("Такого товара нет!")

    def show_products(self):
        print(f"\n--- Список товаров магазина {self.name} ---")
        if self.products:
            for item in self.products:
                print(f"- {item}")
        else:
            print("Магазин пока пуст.")
        print("-" * 35)

    def count_products(self):
        kolichestvo = len(self.products)
        print(f"Всего товаров в магазине: {kolichestvo}")


store = OnlineStore("Tech Store")

store.add_product("Ноутбук")
store.add_product("Мышка")
store.add_product("Клавиатура")

store.show_products()
store.count_products()

store.remove_product("Мышка")
store.show_products()

store.remove_product("Самокат")