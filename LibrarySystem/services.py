from datetime import datetime
from database import Database
from models import Book, User, Library


class LibraryService:
    def __init__(self):
        self.db = Database()
        self.library = Library()
        self.sync_from_db()

    def sync_from_db(self):
        self.library.books.clear()
        self.library.users.clear()

        db_books = self.db.get_all_books()
        for row in db_books:
            b = Book(
                title=row[1],
                author=row[2],
                genre=row[3],
                year=row[4],
                pages=row[5],
                available=bool(row[6]),
                book_id=row[0]
            )
            self.library.add_book(b)

        db_users = self.db.get_all_users()
        for row in db_users:
            u = User(
                name=row[1],
                age=row[2],
                phone=row[3],
                user_id=row[0]
            )
            self.library.register_user(u)

    def add_book(self, title, author, year, genre, pages):
        Book(title, author, year, genre, pages)
        book_id = self.db.add_book(title, author, genre, year, pages)
        self.sync_from_db()
        return book_id

    def remove_book(self, book_id):
        self.db.delete_book(book_id)
        self.sync_from_db()

    def edit_book(self, book_id, title, author, year, genre, pages):
        Book(title, author, year, genre, pages)
        self.db.update_book(book_id, title, author, genre, year, pages)
        self.sync_from_db()

    def register_user(self, name, age, phone):
        User(name, age, phone)
        user_id = self.db.add_user(name, age, phone)
        self.sync_from_db()
        return user_id

    def borrow_book(self, user_id, book_id):
        book = self.db.get_book_by_id(book_id)
        user = self.db.get_user_by_id(user_id)
        if not book or not user:
            return False, "Пользователь или книга не найдены в системе."
        if not book[6]:
            return False, "Эта книга в данный момент выдана другому читателю."

        today = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.db.borrow_book_record(user_id, book_id, today)
        self.sync_from_db()
        return True, "Книга успешно выдана!"

    def return_book(self, user_id, book_id):
        book = self.db.get_book_by_id(book_id)
        user = self.db.get_user_by_id(user_id)
        if not book or not user:
            return False, "Пользователь или книга не найдены в системе."
        if book[6]:
            return False, "Эта книга уже числится в библиотеке."

        today = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.db.return_book_record(user_id, book_id, today)
        self.sync_from_db()
        return True, "Книга успешно возвращена!"

    def show_all_books(self):
        return self.library.books

    def show_all_users(self):
        return self.library.users

    def get_borrow_history(self):
        return self.db.get_borrow_history_join()

    def get_statistics(self):
        aggs = self.db.get_statistics_aggregates()
        total_users = self.db.get_total_users_count()
        by_genre = self.db.get_books_count_by_genre()
        by_author = self.db.get_books_count_by_author()
        avg_pages_genre = self.db.get_avg_pages_by_genre()
        genres_gt3 = self.db.get_genres_having_more_than(3)
        top_newest = self.db.get_top_newest_books(5)
        top_longest = self.db.get_top_longest_books(3)
        above_avg = self.db.get_books_pages_above_average()
        most_active = self.db.get_user_with_most_borrows()

        return {
            "aggs": aggs,
            "total_users": total_users,
            "by_genre": by_genre,
            "by_author": by_author,
            "avg_pages_genre": avg_pages_genre,
            "genres_gt3": genres_gt3,
            "top_newest": top_newest,
            "top_longest": top_longest,
            "above_avg": above_avg,
            "most_active": most_active
        }