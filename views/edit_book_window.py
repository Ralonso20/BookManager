# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_book_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTextEdit,
    QWidget)

class EditBookForm(object):
    def setupUi(self, newBookWindow):
        if not newBookWindow.objectName():
            newBookWindow.setObjectName(u"newBookWindow")
        newBookWindow.resize(400, 470)
        self.label = QLabel(newBookWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 380, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(newBookWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 60, 61, 16))
        self.titleLineEdit = QLineEdit(newBookWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(10, 80, 380, 20))
        self.categoryLineEdit = QLineEdit(newBookWindow)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(10, 130, 380, 20))
        self.label_3 = QLabel(newBookWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 110, 71, 21))
        self.label_4 = QLabel(newBookWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 160, 71, 21))
        self.pagQtySpinBox = QSpinBox(newBookWindow)
        self.pagQtySpinBox.setMaximum(2000)
        self.pagQtySpinBox.setObjectName(u"pagQtySpinBox")
        self.pagQtySpinBox.setGeometry(QRect(10, 190, 126, 21))
        self.label_5 = QLabel(newBookWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 220, 71, 21))
        self.filePathLineEdit = QLineEdit(newBookWindow)
        self.filePathLineEdit.setObjectName(u"filePathLineEdit")
        self.filePathLineEdit.setGeometry(QRect(10, 250, 271, 20))
        self.selectPathButton = QPushButton(newBookWindow)
        self.selectPathButton.setObjectName(u"selectPathButton")
        self.selectPathButton.setGeometry(QRect(300, 250, 91, 21))
        self.selectPathButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.selectPathButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        self.selectPathButton.setFlat(False)
        self.label_6 = QLabel(newBookWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 280, 91, 21))
        self.descriptionTextEdit = QTextEdit(newBookWindow)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")
        self.descriptionTextEdit.setGeometry(QRect(10, 310, 380, 110))
        self.editButton = QPushButton(newBookWindow)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(200, 440, 91, 21))
        self.editButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:#0069c0;\n"
"	color:white;\n"
"}")
        self.editButton.setFlat(False)
        self.cancelButton = QPushButton(newBookWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(300, 440, 91, 21))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.cancelButton.setStyleSheet(u"QPushButton\n"
"{	\n"
"	height: 2em;\n"
" 	border-style: solid;\n"
"	border-width: 2px;\n"
" 	border-color: grey;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"   	background-color:grey;\n"
"	color:white;\n"
"}")
        self.cancelButton.setFlat(False)
        self.pagQtySpinBox_2 = QSpinBox(newBookWindow)
        self.pagQtySpinBox_2.setMaximum(2000)
        self.pagQtySpinBox_2.setObjectName(u"pagQtySpinBox_2")
        self.pagQtySpinBox_2.setGeometry(QRect(160, 190, 126, 21))
        self.label_7 = QLabel(newBookWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 160, 81, 21))

        self.retranslateUi(newBookWindow)

        QMetaObject.connectSlotsByName(newBookWindow)
    # setupUi

    def retranslateUi(self, newBookWindow):
        newBookWindow.setWindowTitle(QCoreApplication.translate("newBookWindow", u"New Book", None))
        self.label.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Edit Book</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Title:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Category:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Pages:</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Select file:</span></p></body></html>", None))
        self.selectPathButton.setText(QCoreApplication.translate("newBookWindow", u"Select", None))
        self.label_6.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Description:</span></p></body></html>", None))
        self.editButton.setText(QCoreApplication.translate("newBookWindow", u"Edit", None))
        self.cancelButton.setText(QCoreApplication.translate("newBookWindow", u"Cancel", None))
        self.label_7.setText(QCoreApplication.translate("newBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Pages read:</span></p></body></html>", None))
    # retranslateUi

