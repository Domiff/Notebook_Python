import os


class Note:
    
    def make_note(self) -> str:
        theme = input("Введите тему заметки: " + '\n')
        data = input("Введите дату заметки: " + '\n')
        text = input("Введите содержание заметки: " + '\n')
        file_name = f'{theme}.txt'
        note_path = os.path.join('notes', file_name)
                 
        with open(note_path, 'w', encoding='utf-8') as note:
            note.write('\n')
            note.write("Тема заметки: " + theme + '\n')
            note.write("Дата заметки: " + data + '\n')
            note.write("Содержание заметки: " + text + '\n')
            
        print(f"Заметка {theme} была создана в файле {note_path}.")  
               
    def delete_note(self, theme):  
        file_name = f"{theme}.txt"
        note_path = os.path.join('notes', file_name)
        
        if os.path.exists(note_path):
            os.remove(note_path)
            print(f"Заметка {theme}.txt была успешно удалена")
        else:
            print(f"Заметка {theme}.txt не была найдена")
            
    def reduct_note(self, theme):
        with open(f'notes\{theme}.txt', 'w', encoding="utf-8") as note:
            note.write('\n')
            note.write(input("Введите новую тему " + '\n') + '\n')
            note.write(input("Введите новую дату " + '\n') + '\n')
            note.write(input("Введите новое содержание заметки " + '\n') + '\n')
        print(f"Заметка {theme} была изменена") 
    
    def read_note(self, theme):
        with open(f'notes\{theme}.txt', 'r', encoding="utf-8") as note:
            print(f"Ниже представлен текст заметки {theme} ")
            print(note.read())
    
    
    