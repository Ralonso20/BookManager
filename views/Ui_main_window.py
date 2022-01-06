# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Bookdepository(object):
    def setupUi(self, Bookdepository):
        if not Bookdepository.objectName():
            Bookdepository.setObjectName(u"Bookdepository")
        Bookdepository.resize(960, 550)
        Bookdepository.setStyleSheet(u"")
        self.buttonframe = QFrame(Bookdepository)
        self.buttonframe.setObjectName(u"buttonframe")
        self.buttonframe.setGeometry(QRect(10, 10, 940, 90))
        self.buttonframe.setFrameShape(QFrame.StyledPanel)
        self.buttonframe.setFrameShadow(QFrame.Raised)
        self.openBookButton = QPushButton(self.buttonframe)
        self.openBookButton.setObjectName(u"openBookButton")
        self.openBookButton.setGeometry(QRect(20, 10, 50, 50))
        self.openBookButton.setMaximumSize(QSize(70, 50))
        self.openBookButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.openBookButton.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../assets/icons/open-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openBookButton.setIcon(icon)
        self.openBookButton.setIconSize(QSize(50, 50))
        self.openBookButton.setFlat(True)
        self.label = QLabel(self.buttonframe)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 60, 81, 16))
        self.label_2 = QLabel(self.buttonframe)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 60, 81, 16))
        self.openBookButton_2 = QPushButton(self.buttonframe)
        self.openBookButton_2.setObjectName(u"openBookButton_2")
        self.openBookButton_2.setGeometry(QRect(110, 10, 50, 50))
        self.openBookButton_2.setMaximumSize(QSize(70, 50))
        self.openBookButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.openBookButton_2.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../assets/icons/add-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openBookButton_2.setIcon(icon1)
        self.openBookButton_2.setIconSize(QSize(50, 50))
        self.openBookButton_2.setFlat(True)
        self.label_3 = QLabel(self.buttonframe)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 60, 81, 16))
        self.openBookButton_3 = QPushButton(self.buttonframe)
        self.openBookButton_3.setObjectName(u"openBookButton_3")
        self.openBookButton_3.setGeometry(QRect(210, 10, 50, 50))
        self.openBookButton_3.setMaximumSize(QSize(70, 50))
        self.openBookButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.openBookButton_3.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../assets/icons/edit-book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openBookButton_3.setIcon(icon2)
        self.openBookButton_3.setIconSize(QSize(50, 50))
        self.openBookButton_3.setFlat(True)
        self.label_4 = QLabel(self.buttonframe)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 60, 91, 16))
        self.openBookButton_4 = QPushButton(self.buttonframe)
        self.openBookButton_4.setObjectName(u"openBookButton_4")
        self.openBookButton_4.setGeometry(QRect(310, 10, 50, 50))
        self.openBookButton_4.setMaximumSize(QSize(70, 50))
        self.openBookButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.openBookButton_4.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"   	background-color:#bbdefb;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	 	background-color:#0069c0;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../assets/icons/delete-book-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openBookButton_4.setIcon(icon3)
        self.openBookButton_4.setIconSize(QSize(50, 50))
        self.openBookButton_4.setFlat(True)
        self.frame = QFrame(Bookdepository)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 110, 940, 40))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 81, 16))
        self.searchByComboBox = QComboBox(self.frame)
        self.searchByComboBox.setObjectName(u"searchByComboBox")
        self.searchByComboBox.setGeometry(QRect(90, 10, 161, 22))
        self.ParametrelineEdit = QLineEdit(self.frame)
        self.ParametrelineEdit.setObjectName(u"ParametrelineEdit")
        self.ParametrelineEdit.setGeometry(QRect(260, 10, 411, 20))
        self.searchButton = QPushButton(self.frame)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(680, 7, 131, 25))
        icon4 = QIcon()
        icon4.addFile(u"../assets/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon4)
        self.refreshbutton = QPushButton(self.frame)
        self.refreshbutton.setObjectName(u"refreshbutton")
        self.refreshbutton.setGeometry(QRect(810, 7, 121, 25))
        icon5 = QIcon()
        icon5.addFile(u"../assets/icons/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshbutton.setIcon(icon5)
        self.listbooktable = QTableWidget(Bookdepository)
        self.listbooktable.setObjectName(u"listbooktable")
        self.listbooktable.setGeometry(QRect(10, 160, 940, 340))
        self.label_6 = QLabel(Bookdepository)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 520, 131, 19))
        self.booksQtyLabel = QLabel(Bookdepository)
        self.booksQtyLabel.setObjectName(u"booksQtyLabel")
        self.booksQtyLabel.setGeometry(QRect(140, 520, 66, 19))

        self.retranslateUi(Bookdepository)

        QMetaObject.connectSlotsByName(Bookdepository)
    # setupUi

    def retranslateUi(self, Bookdepository):
        Bookdepository.setWindowTitle(QCoreApplication.translate("Bookdepository", u"Library", None))
        self.openBookButton.setText("")
        self.label.setText(QCoreApplication.translate("Bookdepository", u"<html><head/><body><p><span style=\" font-weight:600;\">Open Book</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Bookdepository", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Add Book</span></p><p align=\"center\"><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.openBookButton_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Bookdepository", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Edit Book</span></p></body></html>", None))
        self.openBookButton_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Bookdepository", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Delete Book</span></p></body></html>", None))
        self.openBookButton_4.setText("")
        self.label_5.setText(QCoreApplication.translate("Bookdepository", u"<html><head/><body><p>Buscar por:</p></body></html>", None))
        self.searchButton.setText(QCoreApplication.translate("Bookdepository", u"Search", None))
        self.refreshbutton.setText(QCoreApplication.translate("Bookdepository", u"Refresh", None))
        self.label_6.setText(QCoreApplication.translate("Bookdepository", u"<html><head/><body><p><span style=\" font-weight:600;\">Amount of books:</span></p></body></html>", None))
        self.booksQtyLabel.setText(QCoreApplication.translate("Bookdepository", u"#", None))
    # retranslateUi

