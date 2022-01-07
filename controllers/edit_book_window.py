from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from views.edit_book_window import EditBookForm

class EditBookWindow(QWidget, EditBookForm):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

    def populate_imputus(self): #cuando editemos el libro llamara a los imputs con las informaciones
        pass

    def select_file(self):
        pass

    def check_imput(self):
        pass

    def edit_book(self): #llamara a la consulta para editar el libro
        pass

    
