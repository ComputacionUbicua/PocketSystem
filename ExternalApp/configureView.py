from dialog2 import Ui_Dialog
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class configureView(QWidget, Ui_Dialog):
    def __init__(self, parent):
        super().__init__()
        Ui_Dialog.setupUi(self,self)
        self.pushButton.clicked.connect(self.confirm)
        self.parent = parent

    def confirm(self):
        self.hide()
        frecuency = self.lineEdit.text()
        filterArgument = self.lineEdit_2.text()
        unit = self.lineEdit_3.text()
        sensor = self.comboBox.currentText()
        filterSelected = self.comboBox_2.currentText()
        print(sensor)
        self.main.configure(bytes(sensor + ' ' + frecuency +  ' ' + filterSelected +  ' ' + filterArgument, 'utf-8'))
        self.main.show()

    def setMain(self, view):
        self.main = view

