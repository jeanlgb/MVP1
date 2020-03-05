from PyQt5 import QtCore, QtGui, QtWidgets

compteur = int(0)
compteur_recuperation = "0"

class Ui_Frame_Niveau(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(782, 467)
        self.pushButton_valider = QtWidgets.QPushButton(Frame)
        self.pushButton_valider.setEnabled(False)
        self.pushButton_valider.setGeometry(QtCore.QRect(430, 420, 130, 30))
        self.pushButton_valider.setObjectName("pushButton_valider")
        self.pushButton_retour = QtWidgets.QPushButton(Frame)
        self.pushButton_retour.setGeometry(QtCore.QRect(20, 20, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_retour.setFont(font)
        self.pushButton_retour.setObjectName("pushButton_retour")
        self.frame_cervicale = QtWidgets.QFrame(Frame)
        self.frame_cervicale.setEnabled(False)
        self.frame_cervicale.setGeometry(QtCore.QRect(20, 100, 171, 291))
        self.frame_cervicale.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cervicale.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cervicale.setObjectName("frame_cervicale")
        self.checkBox = QtWidgets.QCheckBox(self.frame_cervicale)
        self.checkBox.setGeometry(QtCore.QRect(60, 30, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_cervicale)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 70, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_cervicale)
        self.checkBox_3.setGeometry(QtCore.QRect(60, 110, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.frame_cervicale)
        self.checkBox_4.setGeometry(QtCore.QRect(60, 150, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.frame_cervicale)
        self.checkBox_5.setGeometry(QtCore.QRect(60, 190, 70, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.frame_dorsale = QtWidgets.QFrame(Frame)
        self.frame_dorsale.setEnabled(False)
        self.frame_dorsale.setGeometry(QtCore.QRect(210, 100, 171, 291))
        self.frame_dorsale.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dorsale.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dorsale.setObjectName("frame_dorsale")
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_6.setGeometry(QtCore.QRect(60, 30, 70, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_7.setGeometry(QtCore.QRect(60, 90, 70, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_8.setGeometry(QtCore.QRect(60, 10, 70, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_9.setGeometry(QtCore.QRect(60, 50, 70, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_10.setGeometry(QtCore.QRect(60, 70, 70, 17))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_11.setGeometry(QtCore.QRect(60, 130, 70, 17))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_12.setGeometry(QtCore.QRect(60, 150, 70, 17))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_13.setGeometry(QtCore.QRect(60, 170, 70, 17))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_14.setGeometry(QtCore.QRect(60, 190, 70, 17))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_15.setGeometry(QtCore.QRect(60, 110, 70, 17))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_16.setGeometry(QtCore.QRect(60, 230, 70, 17))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_17.setGeometry(QtCore.QRect(60, 210, 70, 17))
        self.checkBox_17.setObjectName("checkBox_17")
        self.frame_lombaire = QtWidgets.QFrame(Frame)
        self.frame_lombaire.setEnabled(False)
        self.frame_lombaire.setGeometry(QtCore.QRect(400, 100, 171, 291))
        self.frame_lombaire.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lombaire.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lombaire.setObjectName("frame_lombaire")
        self.checkBox_18 = QtWidgets.QCheckBox(self.frame_lombaire)
        self.checkBox_18.setGeometry(QtCore.QRect(60, 70, 70, 17))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(self.frame_lombaire)
        self.checkBox_19.setGeometry(QtCore.QRect(60, 190, 70, 17))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(self.frame_lombaire)
        self.checkBox_20.setGeometry(QtCore.QRect(60, 30, 70, 17))
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_21 = QtWidgets.QCheckBox(self.frame_lombaire)
        self.checkBox_21.setGeometry(QtCore.QRect(60, 110, 70, 17))
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_22 = QtWidgets.QCheckBox(self.frame_lombaire)
        self.checkBox_22.setGeometry(QtCore.QRect(60, 150, 70, 17))
        self.checkBox_22.setObjectName("checkBox_22")
        self.frame_sacroCoccygiennes = QtWidgets.QFrame(Frame)
        self.frame_sacroCoccygiennes.setEnabled(False)
        self.frame_sacroCoccygiennes.setGeometry(QtCore.QRect(590, 100, 171, 291))
        self.frame_sacroCoccygiennes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_sacroCoccygiennes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_sacroCoccygiennes.setObjectName("frame_sacroCoccygiennes")
        self.checkBox_23 = QtWidgets.QCheckBox(self.frame_sacroCoccygiennes)
        self.checkBox_23.setGeometry(QtCore.QRect(60, 40, 70, 17))
        self.checkBox_23.setObjectName("checkBox_23")
        self.checkBox_24 = QtWidgets.QCheckBox(self.frame_sacroCoccygiennes)
        self.checkBox_24.setGeometry(QtCore.QRect(60, 130, 70, 17))
        self.checkBox_24.setObjectName("checkBox_24")
        self.checkBox_25 = QtWidgets.QCheckBox(self.frame_sacroCoccygiennes)
        self.checkBox_25.setGeometry(QtCore.QRect(60, 100, 70, 17))
        self.checkBox_25.setObjectName("checkBox_25")
        self.checkBox_26 = QtWidgets.QCheckBox(self.frame_sacroCoccygiennes)
        self.checkBox_26.setGeometry(QtCore.QRect(60, 70, 70, 17))
        self.checkBox_26.setObjectName("checkBox_26")
        self.checkBox_27 = QtWidgets.QCheckBox(self.frame_sacroCoccygiennes)
        self.checkBox_27.setGeometry(QtCore.QRect(60, 160, 70, 17))
        self.checkBox_27.setObjectName("checkBox_27")
        self.checkBox_28 = QtWidgets.QCheckBox(self.frame_sacroCoccygiennes)
        self.checkBox_28.setGeometry(QtCore.QRect(60, 250, 70, 17))
        self.checkBox_28.setObjectName("checkBox_28")
        self.checkBox_29 = QtWidgets.QCheckBox(self.frame_sacroCoccygiennes)
        self.checkBox_29.setGeometry(QtCore.QRect(60, 190, 70, 17))
        self.checkBox_29.setObjectName("checkBox_29")
        self.checkBox_30 = QtWidgets.QCheckBox(self.frame_sacroCoccygiennes)
        self.checkBox_30.setGeometry(QtCore.QRect(60, 10, 70, 17))
        self.checkBox_30.setObjectName("checkBox_30")
        self.checkBox_31 = QtWidgets.QCheckBox(self.frame_sacroCoccygiennes)
        self.checkBox_31.setGeometry(QtCore.QRect(60, 220, 70, 17))
        self.checkBox_31.setObjectName("checkBox_31")
        self.checkBox_lombaires = QtWidgets.QCheckBox(Frame)
        self.checkBox_lombaires.setGeometry(QtCore.QRect(410, 70, 131, 30))
        self.checkBox_lombaires.setObjectName("checkBox_lombaires")
        self.checkBox_sacroCoccygiennes = QtWidgets.QCheckBox(Frame)
        self.checkBox_sacroCoccygiennes.setGeometry(QtCore.QRect(590, 70, 171, 30))
        self.checkBox_sacroCoccygiennes.setObjectName("checkBox_sacroCoccygiennes")
        self.checkBox_cervicales = QtWidgets.QCheckBox(Frame)
        self.checkBox_cervicales.setGeometry(QtCore.QRect(30, 70, 131, 30))
        self.checkBox_cervicales.setObjectName("checkBox_cervicales")
        self.checkBox_dorsales = QtWidgets.QCheckBox(Frame)
        self.checkBox_dorsales.setGeometry(QtCore.QRect(220, 70, 131, 30))
        self.checkBox_dorsales.setObjectName("checkBox_dorsales")
        self.lineEdit_compte = QtWidgets.QLineEdit(Frame)
        self.lineEdit_compte.setEnabled(False)
        self.lineEdit_compte.setGeometry(QtCore.QRect(250, 420, 81, 20))
        self.lineEdit_compte.setObjectName("lineEdit_compte")
        self.pushButton_calcul = QtWidgets.QPushButton(Frame)
        self.pushButton_calcul.setGeometry(QtCore.QRect(20, 410, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_calcul.setFont(font)
        self.pushButton_calcul.setObjectName("pushButton_calcul")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_valider.setText(_translate("Frame", "Valider"))
        self.pushButton_retour.setText(_translate("Frame", "Retour"))
        self.checkBox.setText(_translate("Frame", "C1"))
        self.checkBox_2.setText(_translate("Frame", "C2"))
        self.checkBox_3.setText(_translate("Frame", "C3"))
        self.checkBox_4.setText(_translate("Frame", "C4"))
        self.checkBox_5.setText(_translate("Frame", "C4"))
        self.checkBox_6.setText(_translate("Frame", "D2"))
        self.checkBox_7.setText(_translate("Frame", "D5"))
        self.checkBox_8.setText(_translate("Frame", "D1"))
        self.checkBox_9.setText(_translate("Frame", "D3"))
        self.checkBox_10.setText(_translate("Frame", "D4"))
        self.checkBox_11.setText(_translate("Frame", "D7"))
        self.checkBox_12.setText(_translate("Frame", "D8"))
        self.checkBox_13.setText(_translate("Frame", "D9"))
        self.checkBox_14.setText(_translate("Frame", "D10"))
        self.checkBox_15.setText(_translate("Frame", "D6"))
        self.checkBox_16.setText(_translate("Frame", "D12"))
        self.checkBox_17.setText(_translate("Frame", "D11"))
        self.checkBox_18.setText(_translate("Frame", "L2"))
        self.checkBox_19.setText(_translate("Frame", "L5"))
        self.checkBox_20.setText(_translate("Frame", "L1"))
        self.checkBox_21.setText(_translate("Frame", "L3"))
        self.checkBox_22.setText(_translate("Frame", "L4"))
        self.checkBox_23.setText(_translate("Frame", "2"))
        self.checkBox_24.setText(_translate("Frame", "5"))
        self.checkBox_25.setText(_translate("Frame", "4"))
        self.checkBox_26.setText(_translate("Frame", "3"))
        self.checkBox_27.setText(_translate("Frame", "6"))
        self.checkBox_28.setText(_translate("Frame", "9"))
        self.checkBox_29.setText(_translate("Frame", "7"))
        self.checkBox_30.setText(_translate("Frame", "1"))
        self.checkBox_31.setText(_translate("Frame", "8"))
        self.checkBox_lombaires.setText(_translate("Frame", "Lombaires (5)"))
        self.checkBox_sacroCoccygiennes.setText(_translate("Frame", "sacro-coccygiennes (5+4)"))
        self.checkBox_cervicales.setText(_translate("Frame", "Cervicales (5)"))
        self.checkBox_dorsales.setText(_translate("Frame", "Dorsales (12)"))
        self.pushButton_calcul.setText(_translate("Frame", "Calcul Nombre Vertèbres :"))

class MainWindow_Niveau(QtWidgets.QWidget, Ui_Frame_Niveau):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        # récupération des valeurs des checkbox
        self.checkBox_cervicales.stateChanged.connect(self.checkBoxChangeAction_cervicale)
        self.checkBox_dorsales.stateChanged.connect(self.checkBoxChangeAction_dorsale)
        self.checkBox_lombaires.stateChanged.connect(self.checkBoxChangeAction_lombaire)
        self.checkBox_sacroCoccygiennes.stateChanged.connect(self.checkBoxChangeAction_sacro)


        self.checkBox.stateChanged.connect(self.checkBoxChangeAction_1)
        self.checkBox_2.stateChanged.connect(self.checkBoxChangeAction_2)
        self.checkBox_3.stateChanged.connect(self.checkBoxChangeAction_3)
        self.checkBox_4.stateChanged.connect(self.checkBoxChangeAction_4)
        self.checkBox_5.stateChanged.connect(self.checkBoxChangeAction_5)
        self.checkBox_6.stateChanged.connect(self.checkBoxChangeAction_6)
        self.checkBox_7.stateChanged.connect(self.checkBoxChangeAction_7)
        self.checkBox_8.stateChanged.connect(self.checkBoxChangeAction_8)
        self.checkBox_9.stateChanged.connect(self.checkBoxChangeAction_9)
        self.checkBox_10.stateChanged.connect(self.checkBoxChangeAction_10)
        self.checkBox_11.stateChanged.connect(self.checkBoxChangeAction_11)
        self.checkBox_12.stateChanged.connect(self.checkBoxChangeAction_12)
        self.checkBox_13.stateChanged.connect(self.checkBoxChangeAction_13)
        self.checkBox_14.stateChanged.connect(self.checkBoxChangeAction_14)
        self.checkBox_15.stateChanged.connect(self.checkBoxChangeAction_15)
        self.checkBox_16.stateChanged.connect(self.checkBoxChangeAction_16)
        self.checkBox_17.stateChanged.connect(self.checkBoxChangeAction_17)
        self.checkBox_18.stateChanged.connect(self.checkBoxChangeAction_18)
        self.checkBox_19.stateChanged.connect(self.checkBoxChangeAction_19)
        self.checkBox_20.stateChanged.connect(self.checkBoxChangeAction_20)
        self.checkBox_21.stateChanged.connect(self.checkBoxChangeAction_21)
        self.checkBox_22.stateChanged.connect(self.checkBoxChangeAction_22)
        self.checkBox_23.stateChanged.connect(self.checkBoxChangeAction_23)
        self.checkBox_24.stateChanged.connect(self.checkBoxChangeAction_24)
        self.checkBox_25.stateChanged.connect(self.checkBoxChangeAction_25)
        self.checkBox_26.stateChanged.connect(self.checkBoxChangeAction_26)
        self.checkBox_27.stateChanged.connect(self.checkBoxChangeAction_27)
        self.checkBox_28.stateChanged.connect(self.checkBoxChangeAction_28)
        self.checkBox_29.stateChanged.connect(self.checkBoxChangeAction_29)
        self.checkBox_30.stateChanged.connect(self.checkBoxChangeAction_30)
        self.checkBox_31.stateChanged.connect(self.checkBoxChangeAction_31)

        # controlleur pour les boutons
        self.pushButton_retour.clicked.connect(self.retourTraumato)
        self.pushButton_valider.clicked.connect(self.validerTraumato)
        self.pushButton_calcul.clicked.connect(self.compteurVertebres)

    def checkBoxChangeAction_cervicale(self, state):
        if ( state == QtCore.Qt.Checked):
            self.frame_cervicale.setEnabled(True)
            print("checked")
        else:
            self.frame_cervicale.setEnabled(False)
            self.checkBox.setChecked(False)
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_4.setChecked(False)
            self.checkBox_5.setChecked(False)
            print("unchecked")

    def checkBoxChangeAction_dorsale(self, state):
        if ( state == QtCore.Qt.Checked):
            self.frame_dorsale.setEnabled(True)
            print("checked")
        else:
            self.frame_dorsale.setEnabled(False)
            self.checkBox_6.setChecked(False)
            self.checkBox_7.setChecked(False)
            self.checkBox_8.setChecked(False)
            self.checkBox_9.setChecked(False)
            self.checkBox_10.setChecked(False)
            self.checkBox_11.setChecked(False)
            self.checkBox_12.setChecked(False)
            self.checkBox_13.setChecked(False)
            self.checkBox_14.setChecked(False)
            self.checkBox_15.setChecked(False)
            self.checkBox_16.setChecked(False)
            self.checkBox_17.setChecked(False)
            print ("unchecked")

    def checkBoxChangeAction_lombaire(self, state):
        if ( state == QtCore.Qt.Checked):
            self.frame_lombaire.setEnabled(True)
            print("checked")
        else:
            self.frame_lombaire.setEnabled(False)
            self.checkBox_18.setChecked(False)
            self.checkBox_19.setChecked(False)
            self.checkBox_20.setChecked(False)
            self.checkBox_21.setChecked(False)
            self.checkBox_22.setChecked(False)
            print ("unchecked")

    def checkBoxChangeAction_sacro(self, state):
        if ( state == QtCore.Qt.Checked):
            self.frame_sacroCoccygiennes.setEnabled(True)
            print("checked")
        else:
            self.frame_sacroCoccygiennes.setEnabled(False)
            self.checkBox_23.setChecked(False)
            self.checkBox_24.setChecked(False)
            self.checkBox_25.setChecked(False)
            self.checkBox_26.setChecked(False)
            self.checkBox_27.setChecked(False)
            self.checkBox_28.setChecked(False)
            self.checkBox_29.setChecked(False)
            self.checkBox_30.setChecked(False)
            self.checkBox_31.setChecked(False)
            print ("unchecked")


    def checkBoxChangeAction_1(self, state):
        global compteur
        if ( state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print ("unchecked")

    def checkBoxChangeAction_2(self, state):
        global compteur
        if ( state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print ("unchecked")

    def checkBoxChangeAction_3(self, state):
        global compteur
        if ( state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print ("unchecked")

    def checkBoxChangeAction_4(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_5(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_6(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_7(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_8(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_9(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_10(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_11(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_12(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_13(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_14(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_15(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_16(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_17(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_18(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_19(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_20(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_21(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_22(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_23(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_24(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_25(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_26(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_27(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_28(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def checkBoxChangeAction_29(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")


    def checkBoxChangeAction_30(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")


    def checkBoxChangeAction_31(self, state):
        global compteur
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            print("checked")
        else:
            compteur = compteur - 1
            print("unchecked")

    def compteurVertebres(self):
        global compteur
        global compteur_recuperation

        self.count = compteur
        print(self.count)
        self.lineEdit_compte.setText(str(self.count))
        self.countRecuperation = self.lineEdit_compte.text()
        compteur_recuperation = self.countRecuperation

        self.pushButton_valider.setEnabled(True)


    def retourTraumato(self):
        self.switch_window1.emit()

    def validerTraumato(self):
        self.switch_window2.emit()