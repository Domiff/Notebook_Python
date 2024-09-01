import View.View as views
import Model.Notebook as note_book


class Presenter:
    
    def choice_function(self):
        
        view = views.View()
        choice = view.contact_with_user()
    
        note = note_book.Note()
        
        while True:
            if choice == 1:
                note.make_note()
                break
            elif choice == 2:
                note.delete_note(input("Выберите заметку, которую хотите удалить "))
                break
            elif choice == 3:
                note.reduct_note(input(f"Выберите заметку, которую хотите редактировать "))
                break
            elif choice == 4:
                note.read_note(input(f"Выберите заметку, которую хотите прочитать "))
                break
            else:
                print("Была введена некоректная команда.")
                break
        
    
    