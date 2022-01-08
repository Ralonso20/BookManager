from PySide6.QtWidgets import QWidget, QTableWidgetItem #se refiere al tipo de ventana creada en QTdesigner
from views.main_window import Bookdepository
from db.books import select_all_books

class BookdepositoryWindow(QWidget, Bookdepository): #Heredamos de estas dos clases
    def __init__(self):
        super().__init__()

        #Esta intruccion de super se utilizaba en versiones anteriores de python3
        #super(BookdepositoryWindow, self).__init__()

        self.setupUi(self) #se llama a la funcion para crear los componentes de la interfaz
        #para que aparezcan los iconos correctamente hay que corregir los paths de los views

        #debemos enlazar open_new_book_window con el boton que abre la ventana
        self.open_new_book_button.clicked.connect(self.open_new_book_window)
        self.open_edit_book_button.clicked.connect(self.open_edit_book_window)

        self.table_config()
        self.populate_table(select_all_books())

    def open_book(self):
        pass

    def open_new_book_window(self):
        from controllers.new_book_window import NewBookWindow
        window = NewBookWindow(self) #recive como parametro la instancia de la clase padre
        #asi que en new_book_window debemos agregar ese parametro
        window.show()

    def open_edit_book_window(self):
        from controllers.edit_book_window import EditBookWindow
        window = EditBookWindow(self)
        window.show()

    def remove_book(self):
        pass

    def table_config(self): #colocaremos la configuraciones de la tabla, captura el ojeto de la tabla
        colum_headers = ("Book_ID", "Title", "Category", "Page Qty", "Read page Qty", "PATH", "Description")
        self.listbooktable.setColumnCount(len(colum_headers))
        self.listbooktable.setHorizontalHeaderLabels(colum_headers) #Enviamos los textos de cada columna

    def populate_table(self,data): #esta funcion va a cargar los datos en la tabla
        self.listbooktable.setRowCount(len(data)) #necesitamos la cantidad de registros de la tabla

        for(index_row, row) in enumerate(data): #recive el indice y los datos de cada fila, enumarate retorna las filas y los datos
            for(index_cell, cell) in enumerate(row): #recive el index de la celda y el dato de esa celda
                #La funcion setItem utiliza 3 elementos, el 3ro son los datos para eso usamos la libreria Qtablewidgetitem
                self.listbooktable.setItem(index_row, index_cell, QTableWidgetItem(str(cell))) #cada celda debemos convertitrla en strig


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