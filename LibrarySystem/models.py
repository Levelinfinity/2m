from abc import ABC, abstractmethod
from utils import Validator


class LibraryItem(ABC):
    @abstractmethod
    def take(self):
        pass

    @abstractmethod
    def give_back(self):
        pass


class Book(LibraryItem):
    created_books = 0

    def __init__(self, title, author, year, genre, pages, available=True, book_id=None):
        if not title or not str(title).strip():
            raise ValueError("Название книги не может быть пустым")
        if not Validator.validate_pages(pages):
            raise ValueError("Количество страниц не можеть быть меньше нуля")

        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.pages = pages
        self.available = available

        Book.created_books += 1

    @classmethod
    def get_created_books(cls):
        return cls.created_books

    def info(self):
        status = "Доступна" if self.available else "Выдана"
        return f"[{self.id}] '{self.title}' - {self.author} ({self.year}), Жанр: {self.genre}, Стр: {self.pages} | {status}"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def take(self):
        return self.borrow()

    def give_back(self):
        self.return_book()

    def __str__(self):
        return f"'{self.title}' ({self.author})"

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}')"

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.author == other.author
        return False


class Downloadable:
    def download(self):
        return "Книга загружается..."


class DigitalBook(Book, Downloadable):
    def __init__(self, title, author, year, genre, pages, file_size, available=True, book_id=None):
        super().__init__(title, author, year, genre, pages, available, book_id)
        self.file_size = file_size

    def info(self):
        base_info = super().info()
        return f"{base_info} [Цифровая версия, Размер: {self.file_size}MB]"


class Person:
    def __init__(self, name, age, person_id=None):
        self.id = person_id
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 10:
            raise ValueError("Возраст должен быть больше 10 лет")
        self._age = value

    def info(self):
        return f"ID: {self.id} | Имя: {self.name}, Возраст: {self.age}"


class User(Person):
    def __init__(self, name, age, phone, user_id=None):
        super().__init__(name, age, user_id)
        self.phone = phone
        self.__borrowed_books = []

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if not Validator.validate_phone(value):
            raise ValueError("Номер телефона должен начинаться с +996 и состоять из 13 цифр")
        self.__phone = value

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        if book.borrow():
            self.__borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            return True
        return False

    def info(self):
        return f"[Читатель] ID: {self.id} | Имя: {self.name} | Тел: {self.phone} | Книг на руках: {len(self.__borrowed_books)}"


class Librarian(Person):
    def __init__(self, name, age, salary, position, person_id=None):
        super().__init__(name, age, person_id)
        self.salary = salary
        self.position = position

    def info(self):
        return f"[Библиотекарь] ID: {self.id} | Имя: {self.name} | Должность: {self.position} | ЗП: {self.salary} сом"


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        self.books = [b for b in self.books if b.id != book_id]

    def find_book(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def register_user(self, user):
        self.users.append(user)

    def show_books(self):
        for book in self.books:
            print(book.info())

    def show_users(self):
        for user in self.users:
            print(user.info())

    def borrow_book(self, user_id, book_id):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.id == book_id), None)
        if user and book:
            return user.borrow_book(book)
        return False

    def return_book(self, user_id, book_id):
        user = next((u for u in self.users if u.id == user_id), None)
        book = next((b for b in self.books if b.id == book_id), None)
        if user and book:
            return user.return_book(book)
        return False

    def __len__(self):
        return len(self.books)