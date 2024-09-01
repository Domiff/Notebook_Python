class View:
    
    def contact_with_user(self):
        print("Список команд: ")
        print("1. Создание заметки")
        print("2. Удаление заметки")
        print("3. Редактирование заметки")
        print("4. Чтение заметки")
        choice = int(input("Выберите операцию: " ))
        return choice