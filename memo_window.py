from PyQt5 import QtCore, QtWidgets
from memo import Ui_DialogMemo as Memo_Dialog


class Memo(QtWidgets.QDialog, Memo_Dialog):  # Dialog-Klasse

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushbutton_ok.clicked.connect(self.button_ok)

    def button_ok(self):
        self.close()

    def closeEvent(self, event):
        super().closeEvent(event)
        event.accept()
