# __init__
# __str__
# __repr__
# __len__
# __add__
# __eq__

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.music = []

#     def __str__ (self):
#         return f"User(name={self.name}, age={self.age})"
    
#     def add(self, song):
#         self.music.append(song)

#     def __len__(self):
#         return len(self.music)
    
#     def __add__(self, other):
#         if isinstance(other, User):
#             return User(self.name + " & " + other.name, self.age + other.age)
#         return NotImplemented
    
#     def __eq__(self, other):
#         if isinstance(other, User):
#             return self.name == other.name and self.age == other.age
#         return NotImplemented
    
# user = User("Bob", 30)
# print(user)
# user1 = User("Alice", 25)
# user.add("song 1")
# user.add("song 2")
# print(len(user))


# class Nath:

#     @staticmethod
#     def add(a, b):
#         return a + b

# # n = Nath()

# print(nath.add(5, 5))

# def age(func):
#     def a(*args, *kwargs):
#         print("До вызова функ")
#         func(*args, **kwargs)
#         print("После вызова функ")
#     return a

# @age
# def user(user = "Bob"):
#     print(user)

# print(user("alice"))

# print(result)

# class User:
#     users = 0
#     def __init__(self, name):
#         self.name = name
#         User.users += 1

#     @classmethod
#     def total_user(cls):
#         return cls.users
# user1 = User("bob")
# user2 = User("Alice")

# print(User.total_user())

# class Fly:
#     def fly(self):
#       print("летает")

# class Swim:
#     def swim(self):
#         print("плавает")

# class Duck(Fly, Swim):
#     pass

# duck = Duck()

# duck.fly()
# duck.swim()

# class A:
#     def hello(self):
#         print("A")

# class B(A):
#     def hello(self):
#         print("B")

# class C(A):
#     def hello(self):
#         print("C")

# class D(B, C):
#     pass

# class E(A):
#     pass

# e = E()
# e.hello

# d = D()
# d.hello
# d.mro

class Camera:
    def take_photo(self):
        print("сфоткал")
class Phone:
    def call(self, number):
        print(f"позвонил по номеру {number}")
class Smartphone(Camera, Phone):
    pass

smp = Smartphone()
smp.take_photo()
smp.call("+996777777777")
