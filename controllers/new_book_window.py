from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt
from views.new_book_window import NewBookForm
import shutil
import os
from db.books import insert_book

class NewBookWindow(QWidget, NewBookForm):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window) #coloca al frente la ventana

        self.addButton.clicked.connect(self.add_book)
        self.selectPathButton.clicked.connect(self.select_file)
        self.cancelButton.clicked.connect(self.close) #Por defeto tenemos una funcion close


    def check_imput(self): #valida la entrada del usuario
        #debemos obtener los respectivos valores para validarlos
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        page_qty = self.pagQtySpinBox.value()
        path = self.filePathLineEdit.text()

        #Creamos una variable global que contara los errores que cometio el usuario
        error_count = 0

        if title == "":
            print("The title field is required")
            error_count += 1
        
        if category == "":
            print("The category field is required")
            error_count += 1

        if path == "":
            print("You must select a valid PATH")
            error_count += 1

        return error_count == 0



    def add_book(self):#llamara a la consulta para agregar un nuevo libro
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        page_qty = self.pagQtySpinBox.value()
        path = self.filePathLineEdit.text()
        description = self.descriptionTextEdit.toPlainText() #Usamos plaintext al ser un textedit

        #llamamos a la funcion check imput para evaluar que esten los campos completos
        if self.check_imput:
            #siendo verdadero estableceremos un path para almacenar los libros con la libreria shutil
            new_path = shutil.copy(path, "book_files") #Toma dos valores, el path por el usuario y donde guardara el libro

            #almacenamos los datos que guardaremos en la db, importando la funcion del modulo db.books
            data = (title, category, page_qty, new_path, description)

            #en caso de que la insercion sea exitosa limpiamos los imputs
            if insert_book(data):
                self.clean_imput()
            else:
                #cambiamos el path para poder borrar la insercion en caso de error
                self.filePathLineEdit.setText(new_path)
                self.undo()



    def clean_imput(self):#limpiara todos los imputs una vez agregado el libro
        self.titleLineEdit.clear()
        self.categoryLineEdit.clear()
        self.pagQtySpinBox.setValue(0)
        self.filePathLineEdit.clear()
        self.descriptionTextEdit.clear()

    def select_file(self):
        #la seleccion del path la haremos con Qfiledialog
        file_path = QFileDialog.getOpenFileName()[0] #retorna una lista, en este caso necesitamos el primer elemento el PATH
        self.filePathLineEdit.setText(file_path) #Mostramos la direccion en el line edit 

    def undo(self): #La funcion se encarga de borrar el libro en caso de que haya algun error
        file_path = self.filePathLineEdit.text()
        
        #Si el path del archivo no esta vacio lo removemos
        if file_path != "":
            os.remove(file_path)

