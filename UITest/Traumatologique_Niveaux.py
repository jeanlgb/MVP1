from PyQt5 import QtCore, QtGui, QtWidgets

compteur = int(0)
compteur_recuperation = "0"

glb_niveaux_cervicales = False
glb_niveaux_dorsales = False
glb_niveaux_lombaires = False
glb_niveaux_sacro = False

TF_C1 = False
TF_C2 = False
TF_C3 = False
TF_C4 = False
TF_C5 = False
TF_C6 = False
TF_C7 = False
TF_D1 = False
TF_D2 = False
TF_D3 = False
TF_D4 = False
TF_D5 = False
TF_D6 = False
TF_D7 = False
TF_D8 = False
TF_D9 = False
TF_D10 = False
TF_D11 = False
TF_D12 = False
TF_L1 = False
TF_L2 = False
TF_L3 = False
TF_L4 = False
TF_L5 = False
TF_S1 = False
TF_S2 = False
TF_S3 = False
TF_S4 = False
TF_S5 = False
TF_S6 = False
TF_S7 = False
TF_S8 = False
TF_S9 = False

glb_C1 = ""
glb_C2 = ""
glb_C3 = ""
glb_C4 = ""
glb_C5 = ""
glb_C6 = ""
glb_C7 = ""

glb_D1 = ""
glb_D2 = ""
glb_D3 = ""
glb_D4 = ""
glb_D5 = ""
glb_D6 = ""
glb_D7 = ""
glb_D8 = ""
glb_D9 = ""
glb_D10 = ""
glb_D11 = ""
glb_D12 = ""

glb_L1 = ""
glb_L2 = ""
glb_L3 = ""
glb_L4 = ""
glb_L5 = ""

glb_S1 = ""
glb_S2 = ""
glb_S3 = ""
glb_S4 = ""
glb_S5 = ""
glb_S6 = ""
glb_S7 = ""
glb_S8 = ""
glb_S9 = ""

glb_zoneCDLS = ""
glb_zoneC = ""
glb_zoneD = ""
glb_zoneL = ""
glb_zoneS = ""

validerNiveaux = False


class Ui_Frame_Niveau(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(782, 467)
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
        self.checkBox_C6 = QtWidgets.QCheckBox(self.frame_cervicale)
        self.checkBox_C6.setGeometry(QtCore.QRect(60, 230, 70, 17))
        self.checkBox_C6.setObjectName("checkBox_C6")
        self.checkBox_C7 = QtWidgets.QCheckBox(self.frame_cervicale)
        self.checkBox_C7.setGeometry(QtCore.QRect(60, 270, 70, 17))
        self.checkBox_C7.setObjectName("checkBox_C7")
        self.frame_dorsale = QtWidgets.QFrame(Frame)
        self.frame_dorsale.setEnabled(False)
        self.frame_dorsale.setGeometry(QtCore.QRect(210, 100, 171, 291))
        self.frame_dorsale.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_dorsale.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_dorsale.setObjectName("frame_dorsale")
        self.checkBox_7 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_7.setGeometry(QtCore.QRect(60, 30, 70, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_10 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_10.setGeometry(QtCore.QRect(60, 90, 70, 17))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_6 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_6.setGeometry(QtCore.QRect(60, 10, 70, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_8 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_8.setGeometry(QtCore.QRect(60, 50, 70, 17))
        self.checkBox_8.setObjectName("checkBox_9")
        self.checkBox_9 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_9.setGeometry(QtCore.QRect(60, 70, 70, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_12 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_12.setGeometry(QtCore.QRect(60, 130, 70, 17))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_13.setGeometry(QtCore.QRect(60, 150, 70, 17))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_14.setGeometry(QtCore.QRect(60, 170, 70, 17))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_15.setGeometry(QtCore.QRect(60, 190, 70, 17))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_11 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_11.setGeometry(QtCore.QRect(60, 110, 70, 17))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_17 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_17.setGeometry(QtCore.QRect(60, 230, 70, 17))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_16 = QtWidgets.QCheckBox(self.frame_dorsale)
        self.checkBox_16.setGeometry(QtCore.QRect(60, 210, 70, 17))
        self.checkBox_16.setObjectName("checkBox_16")
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
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(190, 80, 20, 311))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Frame)
        self.line_2.setGeometry(QtCore.QRect(380, 80, 20, 311))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Frame)
        self.line_3.setGeometry(QtCore.QRect(570, 80, 20, 311))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
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
        self.checkBox_5.setText(_translate("Frame", "C5"))
        self.checkBox_C6.setText(_translate("Frame", "C6"))
        self.checkBox_C7.setText(_translate("Frame", "C7"))
        self.checkBox_6.setText(_translate("Frame", "D1"))
        self.checkBox_7.setText(_translate("Frame", "D2"))
        self.checkBox_8.setText(_translate("Frame", "D3"))
        self.checkBox_9.setText(_translate("Frame", "D4"))
        self.checkBox_10.setText(_translate("Frame", "D5"))
        self.checkBox_11.setText(_translate("Frame", "D6"))
        self.checkBox_12.setText(_translate("Frame", "D7"))
        self.checkBox_13.setText(_translate("Frame", "D8"))
        self.checkBox_14.setText(_translate("Frame", "D9"))
        self.checkBox_15.setText(_translate("Frame", "D10"))
        self.checkBox_16.setText(_translate("Frame", "D11"))
        self.checkBox_17.setText(_translate("Frame", "D12"))
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
        self.checkBox_cervicales.setText(_translate("Frame", "Cervicales (7)"))
        self.checkBox_dorsales.setText(_translate("Frame", "Dorsales (12)"))
        self.pushButton_calcul.setText(_translate("Frame", "Calcul Nombre Vertèbres :"))

class MainWindow_Niveau(QtWidgets.QWidget, Ui_Frame_Niveau):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        global compteur
        compteur = int(0)

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
        self.checkBox_C6.stateChanged.connect(self.checkBoxChangeAction_C6)
        self.checkBox_C7.stateChanged.connect(self.checkBoxChangeAction_C7)

        # controlleur pour les boutons
        self.pushButton_retour.clicked.connect(self.retourTraumato)
        self.pushButton_valider.clicked.connect(self.validerTraumato)
        self.pushButton_calcul.clicked.connect(self.compteurVertebres)

    def checkBoxChangeAction_cervicale(self, state):
        global glb_niveaux_cervicales
        if ( state == QtCore.Qt.Checked):
            self.frame_cervicale.setEnabled(True)
            glb_niveaux_cervicales = True
        else:
            self.frame_cervicale.setEnabled(False)
            self.checkBox.setChecked(False)
            self.checkBox_2.setChecked(False)
            self.checkBox_3.setChecked(False)
            self.checkBox_4.setChecked(False)
            self.checkBox_5.setChecked(False)
            self.checkBox_C6.setChecked(False)
            self.checkBox_C7.setChecked(False)
            glb_niveaux_cervicales = False


    def checkBoxChangeAction_dorsale(self, state):
        global glb_niveaux_dorsales
        if ( state == QtCore.Qt.Checked):
            self.frame_dorsale.setEnabled(True)
            glb_niveaux_dorsales  = True
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
            glb_niveaux_dorsales = False


    def checkBoxChangeAction_lombaire(self, state):
        global glb_niveaux_lombaires
        if ( state == QtCore.Qt.Checked):
            self.frame_lombaire.setEnabled(True)
            glb_niveaux_lombaires  = True
        else:
            self.frame_lombaire.setEnabled(False)
            self.checkBox_18.setChecked(False)
            self.checkBox_19.setChecked(False)
            self.checkBox_20.setChecked(False)
            self.checkBox_21.setChecked(False)
            self.checkBox_22.setChecked(False)
            glb_niveaux_lombaires = False


    def checkBoxChangeAction_sacro(self, state):
        global glb_niveaux_sacro
        if ( state == QtCore.Qt.Checked):
            self.frame_sacroCoccygiennes.setEnabled(True)
            glb_niveaux_sacro = True
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
            glb_niveaux_sacro = False


    def checkBoxChangeAction_1(self, state):
        global compteur
        global glb_C1, TF_C1
        if ( state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_C1  = "C1 "
            TF_C1 = True
        else:
            compteur = compteur - 1
            glb_C1 = ""
            TF_C1 = False

    def checkBoxChangeAction_2(self, state):
        global compteur
        global glb_C2, TF_C2
        if ( state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_C2  = "C2 "
            TF_C2 = True
        else:
            compteur = compteur - 1
            glb_C2 = ""
            TF_C2 = False


    def checkBoxChangeAction_3(self, state):
        global compteur
        global glb_C3, TF_C3
        if ( state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_C3 = "C3 "
            TF_C3 = True
        else:
            compteur = compteur - 1
            glb_C3 = ""
            TF_C3 = False


    def checkBoxChangeAction_4(self, state):
        global compteur
        global glb_C4, TF_C4
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_C4 = "C4 "
            TF_C4 = True
        else:
            compteur = compteur - 1
            glb_C4 = ""
            TF_C4 = False

    def checkBoxChangeAction_5(self, state):
        global compteur
        global glb_C5, TF_C5
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_C5 = "C5 "
            TF_C5 = True
        else:
            compteur = compteur - 1
            glb_C5 = ""
            TF_C5 = False


    def checkBoxChangeAction_6(self, state):
        global compteur
        global glb_D1, TF_D1
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_D1 = "D1 "
            TF_D1 = True
        else:
            compteur = compteur - 1
            glb_D1 = ""
            TF_D1 = False

    def checkBoxChangeAction_7(self, state):
        global compteur
        global glb_D2, TF_D2
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_D2 = "D2 "
            TF_D2 = True
        else:
            compteur = compteur - 1
            glb_D2 = ""
            TF_D2 = False

    def checkBoxChangeAction_8(self, state):
        global compteur
        global glb_D3, TF_D3
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_D3 = "D3 "
            TF_D3 = True
        else:
            compteur = compteur - 1
            glb_D3 = ""
            TF_D3 = False

    def checkBoxChangeAction_9(self, state):
        global compteur
        global glb_D4, TF_D4
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_D4 = "D4 "
            TF_D4 = True
        else:
            compteur = compteur - 1
            glb_D4 = ""
            TF_D4 = False

    def checkBoxChangeAction_10(self, state):
        global compteur
        global glb_D5, TF_D5
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_D5 = "D5 "
            TF_D5 = True
        else:
            compteur = compteur - 1
            glb_D5 = ""
            TF_D5 = False

    def checkBoxChangeAction_11(self, state):
        global compteur
        global glb_D6, TF_D6
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_D6 = "D6 "
            TF_D6 = True
        else:
            compteur = compteur - 1
            glb_D6 = ""
            TF_D6 = False

    def checkBoxChangeAction_12(self, state):
        global compteur
        global glb_D7, TF_D7
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_D7 = "D7 "
            TF_D7 = True
        else:
            compteur = compteur - 1
            glb_D7 = ""
            TF_D7 = False

    def checkBoxChangeAction_13(self, state):
        global compteur
        global glb_D8, TF_D8
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_D8 = "D8 "
            TF_D8 = True
        else:
            compteur = compteur - 1
            glb_D8 = ""
            TF_D8 = False

    def checkBoxChangeAction_14(self, state):
        global compteur
        global glb_D9, TF_D9
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_D9 = "D9 "
            TF_D9 = True
        else:
            compteur = compteur - 1
            glb_D9 = ""
            TF_D9 = False

    def checkBoxChangeAction_15(self, state):
        global compteur
        global glb_D10, TF_D10
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_D10 = "D10 "
            TF_D10 = True
        else:
            compteur = compteur - 1
            glb_D10 = ""
            TF_D10 = False

    def checkBoxChangeAction_16(self, state):
        global compteur
        global glb_D11, TF_D11
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_D11 = "D11 "
            TF_D11 = True
        else:
            compteur = compteur - 1
            glb_D11 = ""
            TF_D11 = False

    def checkBoxChangeAction_17(self, state):
        global compteur
        global glb_D12, TF_D12
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_D12 = "D12 "
            TF_D12 = True
        else:
            compteur = compteur - 1
            glb_D12 = ""
            TF_D12 = False

    def checkBoxChangeAction_18(self, state):
        global compteur
        global glb_L1, TF_L1
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_L1 = "L1 "
            TF_L1 = True
        else:
            compteur = compteur - 1
            glb_L1 = ""
            TF_L1 = False

    def checkBoxChangeAction_19(self, state):
        global compteur
        global glb_L2, TF_L2
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_L2 = "L2 "
            TF_L2 = True
        else:
            compteur = compteur - 1
            glb_L2 = ""
            TF_L2 = False

    def checkBoxChangeAction_20(self, state):
        global compteur
        global glb_L3, TF_L3
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_L3 = "L3 "
            TF_L3 = True
        else:
            compteur = compteur - 1
            glb_L3 = ""
            TF_L3 = False

    def checkBoxChangeAction_21(self, state):
        global compteur
        global glb_L4, TF_L4
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_L4 = "L4 "
            TF_L4 = True
        else:
            compteur = compteur - 1
            glb_L4 = ""
            TF_L4 = False

    def checkBoxChangeAction_22(self, state):
        global compteur
        global glb_L5, TF_L5
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_L5 = "L5 "
            TF_L5 = True
        else:
            compteur = compteur - 1
            glb_L5 = ""
            TF_L5 = False

    def checkBoxChangeAction_23(self, state):
        global compteur
        global glb_S1, TF_S1
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_S1 = "S1 "
            TF_S1 = True
        else:
            compteur = compteur - 1
            glb_S1 = ""
            TF_S1 = False

    def checkBoxChangeAction_24(self, state):
        global compteur
        global glb_S2, TF_S2
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_S2 = "S2 "
            TF_S2 = True
        else:
            compteur = compteur - 1
            glb_S2 = ""
            TF_S2 = False

    def checkBoxChangeAction_25(self, state):
        global compteur
        global glb_S3, TF_S3
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_S3 = "S3 "
            TF_S3 = True
        else:
            compteur = compteur - 1
            glb_S3 = ""
            TF_S3 = False

    def checkBoxChangeAction_26(self, state):
        global compteur
        global glb_S4, TF_S4
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_S4 = "S4 "
            TF_S4 = True
        else:
            compteur = compteur - 1
            glb_S4 = ""
            TF_S4 = False

    def checkBoxChangeAction_27(self, state):
        global compteur
        global glb_S5, TF_S5
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_S5 = "S5 "
            TF_S5 = True
        else:
            compteur = compteur - 1
            glb_S5 = ""
            TF_S5 = False

    def checkBoxChangeAction_28(self, state):
        global compteur
        global glb_S6, TF_S6
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_S6 = "S6 "
            TF_S6 = True
        else:
            compteur = compteur - 1
            glb_S6 = ""
            TF_S6 = False

    def checkBoxChangeAction_29(self, state):
        global compteur
        global glb_S7, TF_S7
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_S7 = "S7 "
            TF_S7 = True
        else:
            compteur = compteur - 1
            glb_S7 = ""
            TF_S7 = False


    def checkBoxChangeAction_30(self, state):
        global compteur
        global glb_S8, TF_S8
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_S8 = "S8 "
            TF_S8 = True
        else:
            compteur = compteur - 1
            glb_S8 = ""
            TF_S8 = False


    def checkBoxChangeAction_31(self, state):
        global compteur
        global glb_S9, TF_S9
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_S9 = "S9 "
            TF_S9 = True
        else:
            compteur = compteur - 1
            glb_S9 = ""
            TF_S9 = False

    def checkBoxChangeAction_C6(self, state):
        global compteur
        global glb_C6, TF_C6
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_C6 = "C6 "
            TF_C6 = True
        else:
            compteur = compteur - 1
            glb_C6= ""
            TF_C6 = False

    def checkBoxChangeAction_C7(self, state):
        global compteur
        global glb_C7, TF_C7
        if (state == QtCore.Qt.Checked):
            compteur = compteur + 1
            glb_C7 = "C7 "
            TF_C7 = True
        else:
            compteur = compteur - 1
            glb_C7 = ""
            TF_C7 = False

    def compteurVertebres(self):
        global compteur
        global compteur_recuperation
        global glb_niveaux_sacro, glb_niveaux_dorsales, glb_niveaux_lombaires, glb_niveaux_cervicales
        global glb_C1, glb_C2, glb_C3, glb_C4, glb_C5, glb_C6, glb_C7
        global glb_D1, glb_D2, glb_D3, glb_D4, glb_D5, glb_D6, glb_D7, glb_D8, glb_D9, glb_D10, glb_D11, glb_D12
        global glb_L1, glb_L2, glb_L3, glb_L4, glb_L5
        global glb_S1, glb_S2, glb_S3, glb_S4, glb_S5, glb_S6, glb_S7, glb_S8, glb_S9
        global glb_zoneCDLS, glb_zoneC, glb_zoneD, glb_zoneL, glb_zoneS

        self.count = compteur
        print(self.count)
        self.lineEdit_compte.setText(str(self.count))
        self.countRecuperation = self.lineEdit_compte.text()
        compteur_recuperation = self.countRecuperation


        if glb_niveaux_cervicales == True:
            glb_zoneCDLS = "cervicale(s):"
        if glb_niveaux_dorsales == True:
            glb_zoneCDLS = "dorsale(s):"
        if glb_niveaux_lombaires == True:
            glb_zoneCDLS = "lombaire(s):"
        if glb_niveaux_sacro == True:
            glb_zoneCDLS = "sacro-coccygienne(s):"

        if (glb_niveaux_cervicales == True and glb_niveaux_dorsales == True):
            glb_zoneCDLS = "cervicale(s) et dorsale(s):"
        if (glb_niveaux_dorsales == True and glb_niveaux_lombaires == True):
            glb_zoneCDLS = "dorsale(s) et lombaire(s):"
        if (glb_niveaux_lombaires == True and glb_niveaux_sacro == True):
            glb_zoneCDLS = "lombaire(s) et sacro-coccygienne(s):"


        glb_zoneC = glb_C1 + glb_C2 + glb_C3 + glb_C4 + glb_C5 + glb_C6 + glb_C7
        glb_zoneD = glb_D1 + glb_D2 + glb_D3 + glb_D4 + glb_D5 + glb_D6 + glb_D7 + glb_D8 + glb_D9 + glb_D10 + glb_D11 + glb_D12
        glb_zoneL = glb_L1 + glb_L2 + glb_L3 + glb_L4 + glb_L5
        glb_zoneS = glb_S1 + glb_S2 + glb_S3 + glb_S4 + glb_S5 + glb_S6 + glb_S7 + glb_S8 + glb_S9


        self.pushButton_valider.setEnabled(True)

    def retourTraumato(self):
        global glb_zoneCDLS, glb_zoneC, glb_zoneD, glb_zoneL, glb_zoneS
        global compteur_recuperation
        global validerNiveaux

        validerNiveaux = False

        compteur_recuperation = ""
        glb_zoneCDLS = ""
        glb_zoneC = ""
        glb_zoneD = ""
        glb_zoneL = ""
        glb_zoneS = ""

        self.switch_window1.emit()

    def validerTraumato(self):
        global validerNiveaux
        global glb_niveaux_sacro, glb_niveaux_dorsales, glb_niveaux_lombaires, glb_niveaux_cervicales
        global TF_C1, TF_C2,TF_C3, TF_C4, TF_C5, TF_C6, TF_C7, TF_L1, TF_L2, TF_L3, TF_L4, TF_L5
        global TF_D1, TF_D2,TF_D3, TF_D4, TF_D5, TF_D6, TF_D7, TF_D8, TF_D9, TF_D10, TF_D11, TF_D12
        global TF_S1, TF_S2,TF_S3, TF_S4, TF_S5, TF_S6, TF_S7, TF_S8, TF_S9
        glb_niveaux_cervicales = False
        glb_niveaux_dorsales = False
        glb_niveaux_lombaires = False
        glb_niveaux_sacro = False

        TF_C1 = False
        TF_C2 = False
        TF_C3 = False
        TF_C4 = False
        TF_C5 = False
        TF_C6 = False
        TF_C7 = False
        TF_D1 = False
        TF_D2 = False
        TF_D3 = False
        TF_D4 = False
        TF_D5 = False
        TF_D6 = False
        TF_D7 = False
        TF_D8 = False
        TF_D9 = False
        TF_D10 = False
        TF_D11 = False
        TF_D12 = False
        TF_L1 = False
        TF_L2 = False
        TF_L3 = False
        TF_L4 = False
        TF_L5 = False
        TF_S1 = False
        TF_S2 = False
        TF_S3 = False
        TF_S4 = False
        TF_S5 = False
        TF_S6 = False
        TF_S7 = False
        TF_S8 = False
        TF_S9 = False

        validerNiveaux = True
        self.switch_window2.emit()