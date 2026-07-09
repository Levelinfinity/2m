# Task 1

while True:
    print("\n--- МЕНЮ ---")
    print("1. Добавить операцию")
    print("2. Посмотреть историю операций")
    print("3. Посчитать баланс")
    print("0. Выход")
    
    choice = input("\nВыберите действие: ")
    
    if choice == "1":
        print("1. Приход")
        print("2. Расход")
        type_choice = input("Выберите тип: ")
        
        if type_choice == "1":
            op_type = "Приход"
        elif type_choice == "2":
            op_type = "Расход"
        else:
            print("Неверный выбор типа!")
            continue
            
        category = input("Введите категорию: ")
        amount = input("Введите сумму: ")
        
        with open("money.txt", "a", encoding="utf-8") as file:
            file.write(op_type + "," + category + "," + amount + "\n")
        print("Операция успешно добавлена!")
        
    elif choice == "2":
        print("\n--- История операций ---")
        with open("money.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    print("Тип: " + parts[0] + " | Категория: " + parts[1] + " | Сумма: " + parts[2])
                    
    elif choice == "3":
        total_income = 0
        total_expense = 0
        
        with open("money.txt", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    op_type = parts[0]
                    amount = int(parts[2])
                    
                    if op_type == "Приход":
                        total_income = total_income + amount
                    elif op_type == "Расход":
                        total_expense = total_expense + amount
                        
        balance = total_income - total_expense
        
        print("\n--- Баланс ---")
        print("Общий доход:", total_income)
        print("Общий расход:", total_expense)
        print("Текущий остаток:", balance)
        
    elif choice == "0":
        print("Выход из программы.")
        break
    else:
        print("Неверный пункт меню!")