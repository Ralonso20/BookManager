#Este archivo va a ejecutar la ventana principal
from PySide6.QtWidgets import QApplication
from controllers.main_window import BookdepositoryWindow

if __name__=="__main__":
    app = QApplication() #almacenamos un objeto de la clase application
    window = BookdepositoryWindow()
    window.show() #ejecuta la ventana
    app.exec_()  #ejecuta la aplicacion