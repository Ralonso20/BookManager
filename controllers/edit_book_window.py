from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt
from views.edit_book_window import EditBookForm
from db.books import select_book_by_id, update_book
import re
import os
import shutil

class EditBookWindow(QWidget, EditBookForm):
    def __init__(self, parent = None, _id = None):
        self._id = _id
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.populate_imputs()

        self.editButton.clicked.connect(self.edit_book)
        self.cancelButton.clicked.connect(self.close)
        self.selectPathButton.clicked.connect(self.select_file)


    def populate_imputs(self): #cuando editemos el libro llamara a los imputs con las informaciones
        data = select_book_by_id(self._id)
        self.titleLineEdit.setText(data[1])
        self.categoryLineEdit.setText(data[2])
        self.pagQtySpinBox.setValue(data[3])
        self.pagQtySpinBox_2.setValue(data[4])
        self.filePathLineEdit.setText(data[5])
        self.descriptionTextEdit.setPlainText(data[6])

    def select_file(self):
        #Debemos almacenar el path viejo para eliminar el archivo que ya tenemos
        self.oldPath = self.filePathLineEdit.text()
        #la seleccion del path la haremos con Qfiledialog
        file_path = QFileDialog.getOpenFileName()[0] #retorna una lista, en este caso necesitamos el primer elemento el PATH
        self.filePathLineEdit.setText(file_path) #Mostramos la direccion en el line edit 

    def check_imput(self):
        #debemos obtener los respectivos valores para validarlos
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        page_qty = self.pagQtySpinBox.value()
        path = self.filePathLineEdit.text()

        #Creamos una variable global que contara los errores que cometio el usuario
        error_count = True

        if title == "":
            print("The title field is required")
            error_count = False
        
        if category == "":
            print("The category field is required")
            error_count = False

        if path == "":
            print("You must select a valid PATH")
            error_count = False

        return error_count

    def edit_book(self): #llamara a la consulta para editar el libro
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        page_qty = self.pagQtySpinBox.value()
        page_qty_read = self.pagQtySpinBox_2.value()
        path = self.filePathLineEdit.text()
        description = self.descriptionTextEdit.toPlainText()

        data = [title, category, page_qty, page_qty_read, path, description]

        if self.check_imput():
            #debemos verificar si en la carpeta ya existe un archivo igual al que quizo editar el usuario
            #en caso de existir es como si el usuario no hubiera ingresado nada
            #poner dos \\ para interpretarla como una
            path_to_check = "book_files\\" + re.split("/|\\\\", path)[-1]
            #split me va a divir el path en / o en \\\\ que significa un \
            #al devolvelor como una lista en este caso el valor que nos interesa es el utilomo [-1]
            result = os.path.exists(path_to_check)
            if result == False:
                data[4] = shutil.copy(path, "book_files")
                os.remove(self.oldPath)
            
            if update_book(self._id, data):
               self.close()




    
