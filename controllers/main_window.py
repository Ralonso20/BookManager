from PySide6.QtWidgets import QWidget #se refiere al tipo de ventana creada en QTdesigner
from views.main_window import Bookdepository

class BookdepositoryWindow(QWidget, Bookdepository): #Heredamos de estas dos clases
    def __init__(self):
        super().__init__()

        #Esta intruccion de super se utilizaba en versiones anteriores de python3
        #super(BookdepositoryWindow, self).__init__()

        self.setupUi(self) #se llama a la funcion para crear los componentes de la interfaz
        #para que aparezcan los iconos correctamente hay que corregir los paths de los views

    def open_book(self):
        pass

    def open_new_book_window(self):
        pass

    def open_edit_book_window(self):
        pass

    def remove_book(self):
        pass

    def populate_list(self): #esta funcion va a cargar los datos en la tabla
        pass

    def populate_combobox(self): #esta funcion nos va a dar las opciones para filtrar los libros
        pass

    def search_book_by_title(self):
        pass

    def search_book_by_category(self):
        pass

    def search(self): #en base a lo que seleccionamos la funcion va a llamar a buscar por titulo o categoria
        pass

    def record_qty(self): #cuenta la cantidad de filas de la tabla para la cantidad de libros
        pass