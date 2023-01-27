# Steffen Troeger 2023
import sys
import psycopg2
from datetime import datetime

from PyQt5.QtWidgets import *  # QApplication, QWidget
from PyQt5.QtGui import *
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)


class CheckBoxDict(dict):
    def __init__(self):
        super().__init__(self)

    def append(self, position, ckb):
        self[position] = ckb

    def check(self, position):
        if 1 <= position <= len(self):
            self[position].setChecked(True)
            for i in range(len(self)):
                if i + 1 != position:
                    self[i + 1].setChecked(False)

    def toggle(self, position):
        if 1 <= position <= len(self):
            self[position].setChecked(
                False) if self[position].checked else self[position].setChecked(True)

    def bind(self, position):
        self[position].clicked.connect(lambda: self.check(position))

    def bindToToggle(self, position):
        self[position].clicked.connect(lambda: self.bindToToggle(position))

    def note(self):
        for i in range(len(self)):
            if self[i + 1].isChecked():
                return [1, 2, 3, 4, 5][i]
        return 9


class Database:
    """
    Datenbank-Klasse
    """

    def __init__(self, host, dbname, username, password):
        self.host = host
        self.dbname = dbname
        self.username = username
        self.password = password
        self.conn, self.cur = None, None

    def name(self):
        return self.dbname

    def open_db(self):
        try:  # Datenbankfehler abfangen...
            self.conn = psycopg2.connect(
                "host=" + self.host + " dbname=" + self.dbname + " user=" + self.username + " password=" + self.password)
            self.cur = self.conn.cursor()
        except psycopg2.OperationalError as e:
            self.protocol('-- ' + str(e))
            sys.exit(1)

    def close_db(self):
        try:  # Datenbankfehler abfangen...
            self.cur.close()
            self.conn.close()
        except psycopg2.OperationalError as e:
            self.protocol('-- ' + str(e))
            sys.exit(1)

    def fetchall(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def fetchone(self, sql):
        self.cur.execute(sql)
        return self.cur.fetchone()

    def execute(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
        return None

    def update(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
        return None

    def insert(self, sql):
        self.cur.execute(sql)
        self.conn.commit()
        return None

    def protocol(self, text: str):
        log = open(self.dbname + '.log', 'a')
        log.write('-- ' + str(datetime.datetime.now()) + '\n')
        log.write(text + '\n')
        log.flush()
        log.close()


def clear():
    for it in widget.findChildren(QCheckBox):
        it.setChecked(False)
    for it in widget.findChildren(QLineEdit):
        it.setText('')
    widget.ui.lineEdit_jahr.setText('2022')
    widget.ui.lineEdit_monat.setText('')
    widget.ui.lineEdit_monat.setCursorPosition(0)


def save():
    # id, jahr, monat, geschlecht, lokal, empfarzt, empfangeh, eigen, wohnort, andere, notearzt, notepflege, notephysio, notesozial, notegesamt, anspruch, empfehlen
    jahr = widget.ui.lineEdit_jahr.text()
    monat = str(int(widget.ui.lineEdit_monat.text())
                ) if widget.ui.lineEdit_monat.text() != '' else ''
    if cbdict_geschlecht[1].isChecked():
        geschlecht = 'männlich'
    elif cbdict_geschlecht[2].isChecked():
        geschlecht = 'weiblich'
    else:
        geschlecht = 'keine Angaben'
    lokal = ''
    for i in range(len(cbdict_lokal)):
        if cbdict_lokal[i + 1].isChecked():
            lokal = ['Knie', 'Hüfte', 'Schulter', 'keine Angaben'][i]
    empfarzt = widget.ui.checkBox_empfarzt.isChecked()
    empfangeh = widget.ui.checkBox_empfangeh.isChecked()
    eigen = widget.ui.checkBox_eigen.isChecked()
    wohnort = widget.ui.checkBox_wohnort.isChecked()
    andere = widget.ui.checkBox_andere.isChecked()
    notearzt = cbdict_arzt.note()
    notepflege = cbdict_pflege.note()
    notephysio = cbdict_physio.note()
    notesozial = cbdict_sozial.note()
    notegesamt = cbdict_gesamt.note()
    anspruch = ''
    for i in range(len(cbdict_anspruch)):
        if cbdict_anspruch[i + 1].isChecked():
            anspruch = ['ja', 'vielleicht', 'nein'][i]
    empfehlen = ''
    for i in range(len(cbdict_empfehl)):
        if cbdict_empfehl[i + 1].isChecked():
            empfehlen = ['ja', 'vielleicht', 'nein'][i]
    sql = "insert into befragung (jahr, monat, geschlecht, lokal, empfarzt, empfangeh, eigen, wohnort, andere, notearzt, notepflege, notephysio, notesozial, notegesamt, anspruch, empfehlen) values ("
    sql += "'" + jahr + "',"
    sql += "'" + monat + "',"
    sql += "'" + geschlecht + "',"
    sql += "'" + lokal + "',"
    sql += str(empfarzt) + ","
    sql += str(empfangeh) + ","
    sql += str(eigen) + ","
    sql += str(wohnort) + ","
    sql += str(andere) + ","
    sql += str(notearzt) + ","
    sql += str(notepflege) + ","
    sql += str(notephysio) + ","
    sql += str(notesozial) + ","
    sql += str(notegesamt) + ","
    sql += "'" + anspruch + "',"
    sql += "'" + empfehlen + "');"
    patbef.open_db()
    patbef.execute(sql)
    patbef.close_db()
    clear()
    start()


def changeMonat():
    if widget.ui.lineEdit_monat.text() not in [str(x + 1) for x in range(12)]:
        widget.ui.lineEdit_monat.setText('')
        widget.ui.lineEdit_monat.setCursorPosition(0)


def start():
    patbef.open_db()
    read = patbef.fetchone('select max(id) from befragung;')
    widget.ui.label_id.setText('ID: ' + str(read[0]))
    read = patbef.fetchall('select id from befragung;')
    widget.ui.label_anzahl.setText('Anzahl: ' + str(len(read)))
    patbef.close_db()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    widget = Widget()
    cbdict_geschlecht = CheckBoxDict()
    cbdict_lokal = CheckBoxDict()
    cbdict_wahl = CheckBoxDict()
    cbdict_arzt = CheckBoxDict()
    cbdict_pflege = CheckBoxDict()
    cbdict_physio = CheckBoxDict()
    cbdict_sozial = CheckBoxDict()
    cbdict_gesamt = CheckBoxDict()
    cbdict_anspruch = CheckBoxDict()
    cbdict_empfehl = CheckBoxDict()
    cbdict_geschlecht.append(1, widget.ui.checkBox_m)
    cbdict_geschlecht.append(2, widget.ui.checkBox_w)
    for i in range(2):
        cbdict_geschlecht.bind(i + 1)
    cbdict_lokal.append(1, widget.ui.checkBox_knie)
    cbdict_lokal.append(2, widget.ui.checkBox_huefte)
    cbdict_lokal.append(3, widget.ui.checkBox_schulter)
    cbdict_lokal.append(4, widget.ui.checkBox_keine)
    for i in range(4):
        cbdict_lokal.bind(i + 1)
    cbdict_wahl.append(1, widget.ui.checkBox_empfarzt)
    cbdict_wahl.append(2, widget.ui.checkBox_empfangeh)
    cbdict_wahl.append(3, widget.ui.checkBox_eigen)
    cbdict_wahl.append(4, widget.ui.checkBox_wohnort)
    cbdict_wahl.append(5, widget.ui.checkBox_andere)
    for i in range(5):
        cbdict_wahl.bindToToggle(i + 1)
    cbdict_arzt.append(1, widget.ui.checkBox_11)
    cbdict_arzt.append(2, widget.ui.checkBox_12)
    cbdict_arzt.append(3, widget.ui.checkBox_13)
    cbdict_arzt.append(4, widget.ui.checkBox_14)
    cbdict_arzt.append(5, widget.ui.checkBox_15)
    cbdict_pflege.append(1, widget.ui.checkBox_21)
    cbdict_pflege.append(2, widget.ui.checkBox_22)
    cbdict_pflege.append(3, widget.ui.checkBox_23)
    cbdict_pflege.append(4, widget.ui.checkBox_24)
    cbdict_pflege.append(5, widget.ui.checkBox_25)
    cbdict_physio.append(1, widget.ui.checkBox_31)
    cbdict_physio.append(2, widget.ui.checkBox_32)
    cbdict_physio.append(3, widget.ui.checkBox_33)
    cbdict_physio.append(4, widget.ui.checkBox_34)
    cbdict_physio.append(5, widget.ui.checkBox_35)
    cbdict_sozial.append(1, widget.ui.checkBox_41)
    cbdict_sozial.append(2, widget.ui.checkBox_42)
    cbdict_sozial.append(3, widget.ui.checkBox_43)
    cbdict_sozial.append(4, widget.ui.checkBox_44)
    cbdict_sozial.append(5, widget.ui.checkBox_45)
    cbdict_gesamt.append(1, widget.ui.checkBox_51)
    cbdict_gesamt.append(2, widget.ui.checkBox_52)
    cbdict_gesamt.append(3, widget.ui.checkBox_53)
    cbdict_gesamt.append(4, widget.ui.checkBox_54)
    cbdict_gesamt.append(5, widget.ui.checkBox_55)
    for i in range(5):
        cbdict_arzt.bind(i + 1)
        cbdict_pflege.bind(i + 1)
        cbdict_physio.bind(i + 1)
        cbdict_sozial.bind(i + 1)
        cbdict_gesamt.bind(i + 1)
    cbdict_anspruch.append(1, widget.ui.checkBox_ansprja)
    cbdict_anspruch.append(2, widget.ui.checkBox_ansprvll)
    cbdict_anspruch.append(3, widget.ui.checkBox_ansprnicht)
    cbdict_empfehl.append(1, widget.ui.checkBox_weiterja)
    cbdict_empfehl.append(2, widget.ui.checkBox_weitervllt)
    cbdict_empfehl.append(3, widget.ui.checkBox_weiternein)
    for i in range(3):
        cbdict_anspruch.bind(i + 1)
        cbdict_empfehl.bind(i + 1)
    clear()
    widget.ui.pushButton_clear.clicked.connect(clear)
    widget.ui.pushButton_save.clicked.connect(save)
    widget.ui.lineEdit_monat.textChanged.connect(changeMonat)
    widget.ui.lineEdit_monat.setInputMask('99')
    if sys.platform == 'win32':  # Klinikrechner Windows
        patbef = Database('139.64.201.9', 'epz', 'postgres', 'SuperUser2012')
    else:  # eigener Rechner MacOSX
        patbef = Database('localhost', 'epz', 'postgres', 'postgres')
    start()
    widget.show()
    sys.exit(app.exec())
