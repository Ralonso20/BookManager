from PySide6.QtWidgets import QWidget
from views.new_book_window import NewBookForm

class NewBookWindow(QWidget, NewBookForm):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def check_imput(self): #valida la entrada del usuario
        pass

    def add_book(self):#llamara a la consulta para agregar un nuevo libro
        pass

    def clean_imput(self):#limpiara todos los imputs una vez agregado el libro
        pass

    def select_file(self):
        pass

    def undo(self):
        pass

