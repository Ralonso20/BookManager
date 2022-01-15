from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
#se refiere al tipo de ventana creada en QTdesigner
#QTableWidgetItem se utiliza para los datos
#QAbstractItemView la utilizaremos para seleccionar toda las celdas correspondienes al libro
from views.main_window import Bookdepository
from db.books import select_all_books, select_book_by_title, select_book_by_category
import os
import webbrowser

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
        self.populate_combobox()
        self.refreshbutton.clicked.connect(self.populate_table)
        self.open_Book_Button.clicked.connect(self.open_book)
        self.searchButton.clicked.connect(self.search)

    def open_book(self): #Abriremos los libros con la app predefinida del sistema
        select_row = self.listbooktable.selectedItems() #debemos seleccionar primero la fila

        if select_row:
            path = select_row[5].text() #obtenemos el path en la posicion 5 y lo usamos como texto
            #diferente instruccion en caso de mac,linux o windows
            if os.name == 'posix':
                webbrowser.open_new(path)
            elif os.name == 'nt':
                os.startfile(path)
            
            self.listbooktable.clearSelection()


    def open_new_book_window(self):
        from controllers.new_book_window import NewBookWindow
        window = NewBookWindow(self) #recive como parametro la instancia de la clase padre
        #asi que en new_book_window debemos agregar ese parametro
        window.show()

    def open_edit_book_window(self):
        from controllers.edit_book_window import EditBookWindow
        #para editar el libro necesitamos obtener el id
        selected_row = self.listbooktable.selectedItems()
        if selected_row:
            book_id = int(selected_row[0].text())
            window = EditBookWindow(self, book_id)
            window.show()
        
        self.listbooktable.clearSelection() #limpiamos la seleccion de fila
        

    def remove_book(self):
        pass

    def table_config(self): #colocaremos la configuraciones de la tabla, captura el ojeto de la tabla
        colum_headers = ("Book_ID", "Title", "Category", "Page Qty", "Read page Qty", "PATH", "Description")
        self.listbooktable.setColumnCount(len(colum_headers))
        self.listbooktable.setHorizontalHeaderLabels(colum_headers) #Enviamos los textos de cada columna
        self.listbooktable.setSelectionBehavior(QAbstractItemView.SelectRows)

    def populate_table(self, data): #esta funcion va a cargar los datos en la tabla
        self.listbooktable.setRowCount(len(data)) #necesitamos la cantidad de registros de la tabla

        for(index_row, row) in enumerate(data): #recive el indice y los datos de cada fila, enumarate retorna las filas y los datos
            for(index_cell, cell) in enumerate(row): #recive el index de la celda y el dato de esa celda
                #La funcion setItem utiliza 3 elementos, el 3ro son los datos para eso usamos la libreria Qtablewidgetitem
                self.listbooktable.setItem(index_row, index_cell, QTableWidgetItem(str(cell))) #cada celda debemos convertitrla en strig

        self.record_qty()


    def populate_combobox(self): #esta funcion nos va a dar las opciones para filtrar los libros
        cb_options = ("", "Titile", "Category")
        self.searchByComboBox.addItems(cb_options)

    def search_book_by_title(self, title):
        data = select_book_by_title(title)
        self.populate_table(data)

    def search_book_by_category(self, category):
        data = select_book_by_category(category)
        self.populate_table(data)

    def search(self): #en base a lo que seleccionamos la funcion va a llamar a buscar por titulo o categoria
        option_selected = self.searchByComboBox.currentText()
        parameter = self.ParametrelineEdit.text()

        if option_selected == "":
            print("You must select an option")
        else:
            if parameter == "":
                print("You must write your consult")
            else:
                if option_selected == "Title":
                    self.search_book_by_title
                elif option_selected == "Category":
                    self.search_book_by_category
        
        


    def record_qty(self): #cuenta la cantidad de filas de la tabla para la cantidad de libros
        qty_rows = str(self.listbooktable.rowCount()) #Nos devuelve el numero de registros mostrados como entero, pero debemos mandarlo como str
        self.booksQtyLabel.setText(qty_rows)