import sqlite3


class Database:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books(
                id integer primary key autoincrement,
                title text,
                author text, 
                genre text, 
                year integer, 
                pages integer,
                available boolean
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id integer primary key autoincrement,
                name text,
                age integer,
                phone text
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS borrow_history(
                id integer primary key autoincrement,
                user_id integer,
                book_id integer,
                borrow_date text,
                return_date text,
                FOREIGN KEY(user_id) references user(id),
                FOREIGN KEY(book_id) references books(id)
            )
        """)

        cursor.execute("""
            CREATE VIEW IF NOT EXISTS available_books AS
            SELECT * FROM books where available = 1
        """)

        conn.commit()
        conn.close()

    def add_book(self, title, author, genre, year, pages):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO books (title, author, genre, year, pages, available)
            VALUES (?, ?, ?, ?, ?, 1)
        """, (title, author, genre, year, pages))
        book_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return book_id

    def get_all_books(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_book_by_id(self, book_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE id = ?", (book_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def update_book(self, book_id, title, author, genre, year, pages):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE books
            SET title = ?, author = ?, genre = ?, year = ?, pages = ?
            WHERE id = ?
        """, (title, author, genre, year, pages, book_id))
        conn.commit()
        conn.close()

    def delete_book(self, book_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()

    def add_user(self, name, age, phone):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (name, age, phone)
            VALUES (?, ?, ?)
        """, (name, age, phone))
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return user_id

    def get_all_users(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_user_by_id(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        return row

    def update_user(self, user_id, name, age, phone):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE users
            SET name = ?, age = ?, phone = ?
            WHERE id = ?
        """, (name, age, phone, user_id))
        conn.commit()
        conn.close()

    def delete_user(self, user_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()

    def get_available_books_view(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM available_books")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_books_by_author(self, author):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE author LIKE ?", (f"%{author}%",))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_books_by_genre(self, genre):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books WHERE genre LIKE ?", (f"%{genre}%",))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def borrow_book_record(self, user_id, book_id, date_str):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET available = 0 WHERE id = ?", (book_id,))
        cursor.execute("""
            INSERT INTO borrow_history (user_id, book_id, borrow_date)
            VALUES (?, ?, ?)
        """, (user_id, book_id, date_str))
        conn.commit()
        conn.close()

    def return_book_record(self, user_id, book_id, date_str):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("UPDATE books SET available = 1 WHERE id = ?", (book_id,))
        cursor.execute("""
            UPDATE borrow_history
            SET return_date = ?
            WHERE user_id = ? AND book_id = ? AND return_date IS NULL
        """, (date_str, user_id, book_id))
        conn.commit()
        conn.close()

    def get_borrow_history_join(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT users.name, books.title, borrow_history.borrow_date, borrow_history.return_date
            FROM borrow_history
            JOIN users ON borrow_history.user_id = users.id
            JOIN books ON borrow_history.book_id = books.id
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_statistics_aggregates(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                COUNT(*),
                SUM(pages),
                AVG(pages),
                MIN(year),
                MAX(year),
                MAX(pages)
            FROM books
        """)
        row = cursor.fetchone()
        conn.close()
        return row

    def get_total_users_count(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM users")
        res = cursor.fetchone()[0]
        conn.close()
        return res

    def get_books_count_by_genre(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT genre, COUNT(*) FROM books GROUP BY genre")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_books_count_by_author(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT author, COUNT(*) FROM books GROUP BY author")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_avg_pages_by_genre(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT genre, AVG(pages) FROM books GROUP BY genre")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_genres_having_more_than(self, min_count=3):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT genre, COUNT(*)
            FROM books
            GROUP BY genre
            HAVING COUNT(*) > ?
        """, (min_count,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_top_newest_books(self, limit=5):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books ORDER BY year DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_top_longest_books(self, limit=3):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM books ORDER BY pages DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_books_pages_above_average(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM books
            WHERE pages > (SELECT AVG(pages) FROM books)
        """)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def get_user_with_most_borrows(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
            SELECT users.name, COUNT(borrow_history.id)
            FROM users
            JOIN borrow_history ON users.id = borrow_history.user_id
            GROUP BY users.id
            ORDER BY COUNT(borrow_history.id) DESC
            LIMIT 1
        """)
        row = cursor.fetchone()
        conn.close()
        return row