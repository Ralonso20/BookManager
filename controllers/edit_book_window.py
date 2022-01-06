from PySide6.QtWidgets import QWidget
from views.edit_book_window import EditBookForm

class NewBookWindow(QWidget, EditBookForm):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def populate_imputus(self): #cuando editemos el libro llamara a los imputs con las informaciones
        pass

    def select_file(self):
        pass

    def check_imput(self):
        pass

    def edit_book(self): #llamara a la consulta para editar el libro
        pass

    
