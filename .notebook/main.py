import Model.Directory as dir
import Presenter.Presenter as pres


def main():
    
    directory = dir.Directory()
    directory.make_directory('notes')
    
    presenter = pres.Presenter()
    presenter.choice_function()
    
    return "Программа завершена"
            

if __name__ == '__main__':
    print(main())

    