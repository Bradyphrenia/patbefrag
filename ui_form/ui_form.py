# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(800, 651)
        self.checkBox_m = QtWidgets.QCheckBox(Widget)
        self.checkBox_m.setGeometry(QtCore.QRect(30, 40, 85, 20))
        self.checkBox_m.setObjectName("checkBox_m")
        self.checkBox_w = QtWidgets.QCheckBox(Widget)
        self.checkBox_w.setGeometry(QtCore.QRect(30, 60, 85, 20))
        self.checkBox_w.setObjectName("checkBox_w")
        self.lineEdit_monat = QtWidgets.QLineEdit(Widget)
        self.lineEdit_monat.setGeometry(QtCore.QRect(130, 60, 21, 21))
        self.lineEdit_monat.setMaxLength(2)
        self.lineEdit_monat.setObjectName("lineEdit_monat")
        self.lineEdit_jahr = QtWidgets.QLineEdit(Widget)
        self.lineEdit_jahr.setGeometry(QtCore.QRect(200, 60, 41, 21))
        self.lineEdit_jahr.setMaxLength(4)
        self.lineEdit_jahr.setObjectName("lineEdit_jahr")
        self.frame = QtWidgets.QFrame(Widget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 601, 131))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.checkBox_knie = QtWidgets.QCheckBox(self.frame)
        self.checkBox_knie.setGeometry(QtCore.QRect(20, 100, 85, 20))
        self.checkBox_knie.setObjectName("checkBox_knie")
        self.checkBox_huefte = QtWidgets.QCheckBox(self.frame)
        self.checkBox_huefte.setGeometry(QtCore.QRect(120, 100, 85, 20))
        self.checkBox_huefte.setObjectName("checkBox_huefte")
        self.checkBox_schulter = QtWidgets.QCheckBox(self.frame)
        self.checkBox_schulter.setGeometry(QtCore.QRect(230, 100, 85, 20))
        self.checkBox_schulter.setObjectName("checkBox_schulter")
        self.checkBox_keine = QtWidgets.QCheckBox(self.frame)
        self.checkBox_keine.setGeometry(QtCore.QRect(340, 100, 121, 20))
        self.checkBox_keine.setObjectName("checkBox_keine")
        self.label_monat = QtWidgets.QLabel(self.frame)
        self.label_monat.setGeometry(QtCore.QRect(120, 30, 58, 16))
        self.label_monat.setObjectName("label_monat")
        self.label_jahr = QtWidgets.QLabel(self.frame)
        self.label_jahr.setGeometry(QtCore.QRect(190, 30, 58, 16))
        self.label_jahr.setObjectName("label_jahr")
        self.frame_2 = QtWidgets.QFrame(Widget)
        self.frame_2.setGeometry(QtCore.QRect(10, 150, 601, 161))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.checkBox_empfarzt = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_empfarzt.setGeometry(QtCore.QRect(20, 10, 141, 20))
        self.checkBox_empfarzt.setObjectName("checkBox_empfarzt")
        self.checkBox_empfangeh = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_empfangeh.setGeometry(QtCore.QRect(20, 40, 251, 20))
        self.checkBox_empfangeh.setObjectName("checkBox_empfangeh")
        self.checkBox_eigen = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_eigen.setGeometry(QtCore.QRect(20, 70, 191, 20))
        self.checkBox_eigen.setObjectName("checkBox_eigen")
        self.checkBox_wohnort = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_wohnort.setGeometry(QtCore.QRect(20, 100, 141, 20))
        self.checkBox_wohnort.setObjectName("checkBox_wohnort")
        self.checkBox_andere = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox_andere.setGeometry(QtCore.QRect(20, 130, 111, 20))
        self.checkBox_andere.setObjectName("checkBox_andere")
        self.frame_3 = QtWidgets.QFrame(Widget)
        self.frame_3.setGeometry(QtCore.QRect(10, 320, 601, 161))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.checkBox_11 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_11.setGeometry(QtCore.QRect(360, 10, 31, 20))
        self.checkBox_11.setCheckable(True)
        self.checkBox_11.setChecked(False)
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_12.setGeometry(QtCore.QRect(400, 10, 31, 20))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_13.setGeometry(QtCore.QRect(440, 10, 31, 20))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_14.setGeometry(QtCore.QRect(480, 10, 31, 20))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_15.setGeometry(QtCore.QRect(520, 10, 31, 20))
        self.checkBox_15.setObjectName("checkBox_15")
        self.label_arzt = QtWidgets.QLabel(self.frame_3)
        self.label_arzt.setGeometry(QtCore.QRect(20, 10, 58, 16))
        self.label_arzt.setObjectName("label_arzt")
        self.label_pflege = QtWidgets.QLabel(self.frame_3)
        self.label_pflege.setGeometry(QtCore.QRect(20, 40, 58, 16))
        self.label_pflege.setObjectName("label_pflege")
        self.label_physio = QtWidgets.QLabel(self.frame_3)
        self.label_physio.setGeometry(QtCore.QRect(20, 70, 91, 16))
        self.label_physio.setObjectName("label_physio")
        self.label_sozial = QtWidgets.QLabel(self.frame_3)
        self.label_sozial.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.label_sozial.setObjectName("label_sozial")
        self.line = QtWidgets.QFrame(self.frame_3)
        self.line.setGeometry(QtCore.QRect(0, 30, 611, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.frame_3)
        self.line_2.setGeometry(QtCore.QRect(0, 60, 601, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setGeometry(QtCore.QRect(0, 90, 601, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_gesamt = QtWidgets.QLabel(self.frame_3)
        self.label_gesamt.setGeometry(QtCore.QRect(20, 130, 101, 16))
        self.label_gesamt.setObjectName("label_gesamt")
        self.line_4 = QtWidgets.QFrame(self.frame_3)
        self.line_4.setGeometry(QtCore.QRect(0, 120, 601, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.checkBox_21 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_21.setGeometry(QtCore.QRect(360, 40, 99, 20))
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_22 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_22.setGeometry(QtCore.QRect(400, 40, 99, 20))
        self.checkBox_22.setObjectName("checkBox_22")
        self.checkBox_23 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_23.setGeometry(QtCore.QRect(440, 40, 99, 20))
        self.checkBox_23.setObjectName("checkBox_23")
        self.checkBox_24 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_24.setGeometry(QtCore.QRect(480, 40, 99, 20))
        self.checkBox_24.setObjectName("checkBox_24")
        self.checkBox_25 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_25.setGeometry(QtCore.QRect(520, 40, 99, 20))
        self.checkBox_25.setObjectName("checkBox_25")
        self.checkBox_31 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_31.setGeometry(QtCore.QRect(360, 70, 99, 20))
        self.checkBox_31.setObjectName("checkBox_31")
        self.checkBox_32 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_32.setGeometry(QtCore.QRect(400, 70, 99, 20))
        self.checkBox_32.setObjectName("checkBox_32")
        self.checkBox_33 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_33.setGeometry(QtCore.QRect(440, 70, 99, 20))
        self.checkBox_33.setObjectName("checkBox_33")
        self.checkBox_34 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_34.setGeometry(QtCore.QRect(480, 70, 99, 20))
        self.checkBox_34.setObjectName("checkBox_34")
        self.checkBox_35 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_35.setGeometry(QtCore.QRect(520, 70, 99, 20))
        self.checkBox_35.setObjectName("checkBox_35")
        self.checkBox_41 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_41.setGeometry(QtCore.QRect(360, 100, 99, 20))
        self.checkBox_41.setObjectName("checkBox_41")
        self.checkBox_42 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_42.setGeometry(QtCore.QRect(400, 100, 99, 20))
        self.checkBox_42.setObjectName("checkBox_42")
        self.checkBox_43 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_43.setGeometry(QtCore.QRect(440, 100, 99, 20))
        self.checkBox_43.setObjectName("checkBox_43")
        self.checkBox_44 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_44.setGeometry(QtCore.QRect(480, 100, 99, 20))
        self.checkBox_44.setObjectName("checkBox_44")
        self.checkBox_45 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_45.setGeometry(QtCore.QRect(520, 100, 99, 20))
        self.checkBox_45.setObjectName("checkBox_45")
        self.checkBox_51 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_51.setGeometry(QtCore.QRect(360, 130, 99, 20))
        self.checkBox_51.setObjectName("checkBox_51")
        self.checkBox_52 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_52.setGeometry(QtCore.QRect(400, 130, 99, 20))
        self.checkBox_52.setObjectName("checkBox_52")
        self.checkBox_53 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_53.setGeometry(QtCore.QRect(440, 130, 99, 20))
        self.checkBox_53.setObjectName("checkBox_53")
        self.checkBox_54 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_54.setGeometry(QtCore.QRect(480, 130, 99, 20))
        self.checkBox_54.setObjectName("checkBox_54")
        self.checkBox_55 = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox_55.setGeometry(QtCore.QRect(520, 130, 99, 20))
        self.checkBox_55.setObjectName("checkBox_55")
        self.frame_4 = QtWidgets.QFrame(Widget)
        self.frame_4.setGeometry(QtCore.QRect(10, 490, 601, 101))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.checkBox_ansprja = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_ansprja.setGeometry(QtCore.QRect(10, 30, 201, 20))
        self.checkBox_ansprja.setCheckable(True)
        self.checkBox_ansprja.setChecked(False)
        self.checkBox_ansprja.setObjectName("checkBox_ansprja")
        self.checkBox_ansprvll = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_ansprvll.setGeometry(QtCore.QRect(10, 50, 211, 20))
        self.checkBox_ansprvll.setObjectName("checkBox_ansprvll")
        self.checkBox_ansprnicht = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_ansprnicht.setGeometry(QtCore.QRect(10, 70, 191, 20))
        self.checkBox_ansprnicht.setObjectName("checkBox_ansprnicht")
        self.label_anspr = QtWidgets.QLabel(self.frame_4)
        self.label_anspr.setGeometry(QtCore.QRect(10, 10, 271, 16))
        self.label_anspr.setObjectName("label_anspr")
        self.label_empf = QtWidgets.QLabel(self.frame_4)
        self.label_empf.setGeometry(QtCore.QRect(300, 10, 301, 16))
        self.label_empf.setObjectName("label_empf")
        self.line_5 = QtWidgets.QFrame(self.frame_4)
        self.line_5.setGeometry(QtCore.QRect(270, 0, 20, 101))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.checkBox_weiterja = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_weiterja.setGeometry(QtCore.QRect(320, 30, 131, 20))
        self.checkBox_weiterja.setObjectName("checkBox_weiterja")
        self.checkBox_weitervllt = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_weitervllt.setGeometry(QtCore.QRect(320, 50, 181, 20))
        self.checkBox_weitervllt.setObjectName("checkBox_weitervllt")
        self.checkBox_weiternein = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_weiternein.setGeometry(QtCore.QRect(320, 70, 161, 20))
        self.checkBox_weiternein.setObjectName("checkBox_weiternein")
        self.pushButton_save = QtWidgets.QPushButton(Widget)
        self.pushButton_save.setGeometry(QtCore.QRect(660, 210, 100, 261))
        self.pushButton_save.setObjectName("pushButton_save")
        self.label_id = QtWidgets.QLabel(Widget)
        self.label_id.setGeometry(QtCore.QRect(640, 130, 131, 21))
        self.label_id.setAutoFillBackground(False)
        self.label_id.setText("")
        self.label_id.setIndent(-4)
        self.label_id.setObjectName("label_id")
        self.label_anzahl = QtWidgets.QLabel(Widget)
        self.label_anzahl.setGeometry(QtCore.QRect(640, 160, 131, 21))
        self.label_anzahl.setText("")
        self.label_anzahl.setObjectName("label_anzahl")
        self.pushButton_clear = QtWidgets.QPushButton(Widget)
        self.pushButton_clear.setGeometry(QtCore.QRect(650, 30, 113, 32))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.pushButtonMemo = QtWidgets.QPushButton(Widget)
        self.pushButtonMemo.setGeometry(QtCore.QRect(480, 600, 121, 41))
        self.pushButtonMemo.setObjectName("pushButtonMemo")
        self.frame.raise_()
        self.checkBox_m.raise_()
        self.checkBox_w.raise_()
        self.lineEdit_monat.raise_()
        self.lineEdit_jahr.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.pushButton_save.raise_()
        self.label_id.raise_()
        self.label_anzahl.raise_()
        self.pushButton_clear.raise_()
        self.pushButtonMemo.raise_()

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Patientenbefragung EPZ"))
        self.checkBox_m.setText(_translate("Widget", "männlich"))
        self.checkBox_w.setText(_translate("Widget", "weiblich"))
        self.lineEdit_monat.setInputMask(_translate("Widget", "99"))
        self.lineEdit_jahr.setInputMask(_translate("Widget", "9999"))
        self.checkBox_knie.setText(_translate("Widget", "Knie"))
        self.checkBox_huefte.setText(_translate("Widget", "Hüfte"))
        self.checkBox_schulter.setText(_translate("Widget", "Schulter"))
        self.checkBox_keine.setText(_translate("Widget", "keine Angaben"))
        self.label_monat.setText(_translate("Widget", "Monat"))
        self.label_jahr.setText(_translate("Widget", "Jahr"))
        self.checkBox_empfarzt.setText(_translate("Widget", "Empfehlung Arzt"))
        self.checkBox_empfangeh.setText(_translate("Widget", "Empfehlung Angehöriger / Bekannter"))
        self.checkBox_eigen.setText(_translate("Widget", "eigene positive Erfahrungen"))
        self.checkBox_wohnort.setText(_translate("Widget", "Nähe zum Wohnort"))
        self.checkBox_andere.setText(_translate("Widget", "andere Gründe"))
        self.checkBox_11.setText(_translate("Widget", "1"))
        self.checkBox_12.setText(_translate("Widget", "2"))
        self.checkBox_13.setText(_translate("Widget", "3"))
        self.checkBox_14.setText(_translate("Widget", "4"))
        self.checkBox_15.setText(_translate("Widget", "5"))
        self.label_arzt.setText(_translate("Widget", "Arzt"))
        self.label_pflege.setText(_translate("Widget", "Pflege"))
        self.label_physio.setText(_translate("Widget", "Physiotherapie"))
        self.label_sozial.setText(_translate("Widget", "Sozialdienst"))
        self.label_gesamt.setText(_translate("Widget", "Gesamteindruck"))
        self.checkBox_21.setText(_translate("Widget", "1"))
        self.checkBox_22.setText(_translate("Widget", "2"))
        self.checkBox_23.setText(_translate("Widget", "3"))
        self.checkBox_24.setText(_translate("Widget", "4"))
        self.checkBox_25.setText(_translate("Widget", "5"))
        self.checkBox_31.setText(_translate("Widget", "1"))
        self.checkBox_32.setText(_translate("Widget", "2"))
        self.checkBox_33.setText(_translate("Widget", "3"))
        self.checkBox_34.setText(_translate("Widget", "4"))
        self.checkBox_35.setText(_translate("Widget", "5"))
        self.checkBox_41.setText(_translate("Widget", "1"))
        self.checkBox_42.setText(_translate("Widget", "2"))
        self.checkBox_43.setText(_translate("Widget", "3"))
        self.checkBox_44.setText(_translate("Widget", "4"))
        self.checkBox_45.setText(_translate("Widget", "5"))
        self.checkBox_51.setText(_translate("Widget", "1"))
        self.checkBox_52.setText(_translate("Widget", "2"))
        self.checkBox_53.setText(_translate("Widget", "3"))
        self.checkBox_54.setText(_translate("Widget", "4"))
        self.checkBox_55.setText(_translate("Widget", "5"))
        self.checkBox_ansprja.setText(_translate("Widget", "erneut in Anspruch nehmen"))
        self.checkBox_ansprvll.setText(_translate("Widget", "vielleicht in Anspruch nehmen"))
        self.checkBox_ansprnicht.setText(_translate("Widget", "nicht in Anspruch nehmen"))
        self.label_anspr.setText(_translate("Widget", "Ich werde das EPZ bei ähnlichen Eingriffen..."))
        self.label_empf.setText(_translate("Widget", "Ich werde das EPZ Angehörigen und Bekannten..."))
        self.checkBox_weiterja.setText(_translate("Widget", "weiterempfehlen"))
        self.checkBox_weitervllt.setText(_translate("Widget", "vielleicht weiterempfehlen"))
        self.checkBox_weiternein.setText(_translate("Widget", "nicht weiterempfehlen"))
        self.pushButton_save.setText(_translate("Widget", "Speichern"))
        self.pushButton_clear.setText(_translate("Widget", "Löschen"))
        self.pushButtonMemo.setText(_translate("Widget", "Bemerkungen"))
