# Steffen Troeger 2023
"""
Programm zur Digitalisierung von Fragebögen
"""
import sys
from PyQt5.QtWidgets import QApplication, QCheckBox
from window import Widget
from database import Database
from checkboxdict import CheckBoxDict
from datafielddict import DataFieldDict
from datadict import DataDict


def clear():
    """
    function to reset the window widgets
    :return: none
    """
    for item in widget.findChildren(QCheckBox):
        item.setChecked(False)
    widget.ui.lineEdit_jahr.setText('2022')
    widget.ui.lineEdit_monat.setText('')
    widget.ui.lineEdit_monat.setCursorPosition(0)


def save():
    """
    function to save the data  to the database
    :return: none
    """
    field_data['jahr'] = widget.ui.lineEdit_jahr.text()
    field_data['monat'] = str(int(widget.ui.lineEdit_monat.text())
                              ) if widget.ui.lineEdit_monat.text() != '' else ''
    if cbdict_geschlecht[0].isChecked():
        field_data['geschlecht'] = 'männlich'
    elif cbdict_geschlecht[1].isChecked():
        field_data['geschlecht'] = 'weiblich'
    else:
        field_data['geschlecht'] = ''
    try:
        field_data['lokal'] = [['Knie', 'Hüfte', 'Schulter', 'keine Angaben'][c] for c, _ in enumerate(cbdict_lokal) if
                               cbdict_lokal[c].isChecked()][0]
    except IndexError:
        field_data['lokal'] = ''
    field_data['empfarzt'] = str(widget.ui.checkBox_empfarzt.isChecked())
    field_data['empfangeh'] = str(widget.ui.checkBox_empfangeh.isChecked())
    field_data['eigen'] = str(widget.ui.checkBox_eigen.isChecked())
    field_data['wohnort'] = str(widget.ui.checkBox_wohnort.isChecked())
    field_data['andere'] = str(widget.ui.checkBox_andere.isChecked())
    field_data['notearzt'] = cbdict_arzt.note()
    field_data['notepflege'] = cbdict_pflege.note()
    field_data['notephysio'] = cbdict_physio.note()
    field_data['notesozial'] = cbdict_sozial.note()
    field_data['notegesamt'] = cbdict_gesamt.note()
    try:
        field_data['anspruch'] = \
            [['ja', 'vielleicht', 'nein'][c] for c, _ in enumerate(cbdict_anspruch) if cbdict_anspruch[c].isChecked()][
                0]
    except IndexError:
        field_data['anspruch'] = ''
    try:
        field_data['empfehlen'] = \
            [['ja', 'vielleicht', 'nein'][c] for c, _ in enumerate(cbdict_empfehl) if cbdict_empfehl[c].isChecked()][0]
    except IndexError:
        field_data['empfehlen'] = ''
    output = 'insert into befragung ('
    for counter, _ in enumerate(field_type):  # generating field string
        out = field_type[counter][1]
        out = out + ',' if field_type[counter][0] != 15 else out + ') values ('  # letztes Feld
        output += out
    for counter, _ in enumerate(field_type):  # generating value string
        out = field_data[field_type[counter][1]]
        out = "'" + out + "'" if field_type[counter][2] == 0 else out
        out = out + ',' if field_type[counter][0] != 15 else out + ')'  # letztes Feld
        output += out
    patbef.open_db()
    patbef.execute(output)
    patbef.close_db()
    clear()
    start()


def change_monat():
    """
    function to check the input of the lineEdit text for the month
    :return: none
    """
    if widget.ui.lineEdit_monat.text() not in [str(x + 1) for x in range(12)]:
        widget.ui.lineEdit_monat.setText('')
        widget.ui.lineEdit_monat.setCursorPosition(0)


def start():
    """
    function to write the actual state of the database into the form
    :return: none
    """
    patbef.open_db()
    read = patbef.fetchone('select max(id) from befragung;')  # ID zur Datenbankpflege
    widget.ui.label_id.setText('ID: ' + str(read[0]))
    read = patbef.fetchall('select id from befragung;')
    widget.ui.label_anzahl.setText('Anzahl: ' + str(len(read)))  # Anzahl der aktuellen Datensätze
    patbef.close_db()


def init_dicts():
    """
    initialize a DataFieldDictionary and a DataDictionary
    :return: none
    """
    field_list = [[0, 'jahr', 0],
                  [1, 'monat', 0],
                  [2, 'geschlecht', 0],
                  [3, 'lokal', 0],
                  [4, 'empfarzt', 1],
                  [5, 'empfangeh', 1],
                  [6, 'eigen', 1],
                  [7, 'wohnort', 1],
                  [8, 'andere', 1],
                  [9, 'notearzt', 1],
                  [10, 'notepflege', 1],
                  [11, 'notephysio', 1],
                  [12, 'notesozial', 1],
                  [13, 'notegesamt', 1],
                  [14, 'anspruch', 0],
                  [15, 'empfehlen', 0]]  # list of lists // position, field name, field type
    for item in field_list:
        field_type.append(item[0], item)
        field_data.append(item[1], '')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    widget = Widget()
    cbdict_geschlecht = CheckBoxDict({0: widget.ui.checkBox_m, 1: widget.ui.checkBox_w})
    cbdict_lokal = CheckBoxDict({0: widget.ui.checkBox_knie,
                                 1: widget.ui.checkBox_huefte,
                                 2: widget.ui.checkBox_schulter,
                                 3: widget.ui.checkBox_keine})
    cbdict_wahl = CheckBoxDict({0: widget.ui.checkBox_empfarzt,
                                1: widget.ui.checkBox_empfangeh,
                                2: widget.ui.checkBox_eigen,
                                3: widget.ui.checkBox_wohnort,
                                4: widget.ui.checkBox_andere})
    cbdict_arzt = CheckBoxDict({0: widget.ui.checkBox_11,
                                1: widget.ui.checkBox_12,
                                2: widget.ui.checkBox_13,
                                3: widget.ui.checkBox_14,
                                4: widget.ui.checkBox_15})
    cbdict_pflege = CheckBoxDict({0: widget.ui.checkBox_21,
                                  1: widget.ui.checkBox_22,
                                  2: widget.ui.checkBox_23,
                                  3: widget.ui.checkBox_24,
                                  4: widget.ui.checkBox_25})
    cbdict_physio = CheckBoxDict({0: widget.ui.checkBox_31,
                                  1: widget.ui.checkBox_32,
                                  2: widget.ui.checkBox_33,
                                  3: widget.ui.checkBox_34,
                                  4: widget.ui.checkBox_35})
    cbdict_sozial = CheckBoxDict({0: widget.ui.checkBox_41,
                                  1: widget.ui.checkBox_42,
                                  2: widget.ui.checkBox_43,
                                  3: widget.ui.checkBox_44,
                                  4: widget.ui.checkBox_45})
    cbdict_gesamt = CheckBoxDict({0: widget.ui.checkBox_51,
                                  1: widget.ui.checkBox_52,
                                  2: widget.ui.checkBox_53,
                                  3: widget.ui.checkBox_54,
                                  4: widget.ui.checkBox_55})
    cbdict_anspruch = CheckBoxDict({0: widget.ui.checkBox_ansprja,
                                    1: widget.ui.checkBox_ansprvll,
                                    2: widget.ui.checkBox_ansprnicht})
    cbdict_empfehl = CheckBoxDict({0: widget.ui.checkBox_weiterja,
                                   1: widget.ui.checkBox_weitervllt,
                                   2: widget.ui.checkBox_weiternein})
    cbdict_geschlecht.bindall()
    cbdict_lokal.bindall()
    cbdict_arzt.bindall()
    cbdict_pflege.bindall()
    cbdict_physio.bindall()
    cbdict_sozial.bindall()
    cbdict_gesamt.bindall()
    cbdict_anspruch.bindall()
    cbdict_empfehl.bindall()
    field_type = DataFieldDict()
    field_data = DataDict()
    init_dicts()
    clear()
    widget.ui.pushButton_clear.clicked.connect(clear)
    widget.ui.pushButton_save.clicked.connect(save)
    widget.ui.lineEdit_monat.textChanged.connect(change_monat)
    widget.ui.lineEdit_monat.setInputMask('99')
    if sys.platform == 'win32':  # Klinikrechner Windows
        config_read = open('config.txt', 'r')  # config.txt
        ip_address = config_read.readline().strip()
        password = config_read.readline().strip()
        config_read.close()
        patbef = Database("'" + ip_address + "'", 'epz', 'postgres', "'" + password + "'")
    else:  # eigener Rechner MacOSX
        patbef = Database('localhost', 'epz', 'postgres', 'postgres')
    start()
    widget.show()
    sys.exit(app.exec())
