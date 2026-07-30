import sys
from services import LibraryService
from models import Librarian
from utils import show_information


def print_menu():
    print("\n" + "=" * 35)
    print("  СИСТЕМА УПРАВЛЕНИЯ БИБЛИОТЕКОЙ  ")
    print("=" * 35)
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Изменить книгу")
    print("4. Показать все книги")
    print("5. Зарегистрировать пользователя")
    print("6. Показать пользователей")
    print("7. Выдать книгу")
    print("8. Вернуть книгу")
    print("9. История выдачи")
    print("10. Статистика")
    print("11. Выход")
    print("=" * 35)


def main():
    service = LibraryService()
    librarian = Librarian("Боб", 30, 45000, "Главный библиотекарь", person_id=1)

    print("Добро пожаловать в библиотеку!")
    print("Ответственный сотрудник:")
    show_information(librarian)

    while True:
        print_menu()
        choice = input("Выберите действие (1-11): ").strip()

        if choice == "1":
            try:
                title = input("Введите название книги: ")
                author = input("Введите автора: ")
                genre = input("Введите жанр: ")
                year = int(input("Введите год издания: "))
                pages = int(input("Введите количество страниц: "))

                service.add_book(title, author, year, genre, pages)
                print("Успех: Книга добавлена в библиотеку!")
            except ValueError as e:
                print(f"Ошибка ввода: {e}")

        elif choice == "2":
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                service.remove_book(book_id)
                print("Успех: Книга удалена!")
            except ValueError:
                print("Ошибка: Введен некорректный ID.")

        elif choice == "3":
            try:
                book_id = int(input("Введите ID книги для изменения: "))
                title = input("Введите новое название: ")
                author = input("Введите нового автора: ")
                genre = input("Введите новый жанр: ")
                year = int(input("Введите новый год издания: "))
                pages = int(input("Введите новое количество страниц: "))

                service.edit_book(book_id, title, author, genre, year, pages)
                print("Успех: Информация о книге обновлена!")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "4":
            books = service.show_all_books()
            if not books:
                print("Библиотека пока пуста.")
            else:
                print(f"\nВсего книг в системе (len): {len(service.library)}")
                for book in books:
                    print(book.info())

        elif choice == "5":
            try:
                name = input("Введите имя пользователя: ")
                age = int(input("Введите возраст (>10): "))
                phone = input("Введите телефон (начиная с +996): ")

                service.register_user(name, age, phone)
                print("Успех: Читатель успешно зарегистрирован!")
            except ValueError as e:
                print(f"Ошибка ввода: {e}")

        elif choice == "6":
            users = service.show_all_users()
            if not users:
                print("Зарегистрированных читателей нет.")
            else:
                print("\nСписок пользователей:")
                for user in users:
                    show_information(user)

        elif choice == "7":
            try:
                user_id = int(input("Введите ID пользователя: "))
                book_id = int(input("Введите ID книги: "))
                success, msg = service.borrow_book(user_id, book_id)
                print(msg)
            except ValueError:
                print("Ошибка: ID должен быть целым числом.")

        elif choice == "8":
            try:
                user_id = int(input("Введите ID пользователя: "))
                book_id = int(input("Введите ID книги: "))
                success, msg = service.return_book(user_id, book_id)
                print(msg)
            except ValueError:
                print("Ошибка: ID должен быть целым числом.")

        elif choice == "9":
            history = service.get_borrow_history()
            if not history:
                print("История выдачи книг пока пуста.")
            else:
                print("\nИстория аренды (JOIN):")
                for item in history:
                    ret_date = item[3] if item[3] else "Еще у читателя"
                    print(f"Читатель: {item[0]} | Книга: '{item[1]}' | Взял: {item[2]} | Возврат: {ret_date}")

        elif choice == "10":
            stats = service.get_statistics()
            aggs = stats["aggs"]

            print("\n" + "=" * 20 + " СТАТИСТИКА БИБЛИОТЕКИ " + "=" * 20)
            if aggs and aggs[0] > 0:
                print(f"Всего книг: {aggs[0]}")
                print(f"Всего читателей: {stats['total_users']}")
                print(f"Сумма всех страниц (SUM): {aggs[1]}")
                print(f"Средний объем книги (AVG): {round(aggs[2] or 0, 1)} стр.")
                print(f"Самая старая книга (MIN year): {aggs[3]} г.")
                print(f"Самая новая книга (MAX year): {aggs[4]} г.")
                print(f"Максимальный объем страницы (MAX pages): {aggs[5]}")

                print("\n--- Количество книг по жанрам (GROUP BY) ---")
                for row in stats["by_genre"]:
                    print(f"  {row[0]}: {row[1]} шт.")

                print("\n--- Количество книг по авторам (GROUP BY) ---")
                for row in stats["by_author"]:
                    print(f"  {row[0]}: {row[1]} шт.")

                print("\n--- Среднее число страниц по жанрам (GROUP BY + AVG) ---")
                for row in stats["avg_pages_genre"]:
                    print(f"  {row[0]}: {round(row[1], 1)} стр.")

                print("\n--- Жанры с более чем 3 книгами (HAVING COUNT > 3) ---")
                if stats["genres_gt3"]:
                    for row in stats["genres_gt3"]:
                        print(f"  {row[0]}: {row[1]} шт.")
                else:
                    print("  (Жанров с > 3 книгами пока нет)")

                print("\n--- Top 5 самых новых книг (ORDER BY year DESC LIMIT 5) ---")
                for b in stats["top_newest"]:
                    print(f"  '{b[1]}' ({b[4]} г.) - {b[2]}")

                print("\n--- Top 3 самых длинных книг (ORDER BY pages DESC LIMIT 3) ---")
                for b in stats["top_longest"]:
                    print(f"  '{b[1]}' ({b[5]} стр.) - {b[2]}")

                print("\n--- Книги с объемом выше среднего (Вложенный запрос) ---")
                for b in stats["above_avg"]:
                    print(f"  '{b[1]}' ({b[5]} стр.)")

                print("\n--- Самый активный читатель (Вложенный запрос + JOIN) ---")
                if stats["most_active"]:
                    print(f"  {stats['most_active'][0]} (взял книг: {stats['most_active'][1]})")
                else:
                    print("  (Выдач пока не производилось)")
            else:
                print("Данных нет. Заполните базу данными через меню!")
            print("=" * 63)

        elif choice == "11":
            print("Завершение работы программы. До свидания!")
            sys.exit(0)

        else:
            print("Неверный пункт меню! Выберите число от 1 до 11.")


if __name__ == "__main__":
    main()