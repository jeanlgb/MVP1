# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Formulaire_Recalibrage.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

glb_recalibrage_posterieur = False
glb_recalibrage_anterieur = False
glb_recalibrage_interlamaire = False
glb_recalibrage_interEpineux = False
glb_recalibrage_arthrectomie = False
glb_recalibrage_laminectomie = False
glb_recalibrage_foraminotomie = False
glb_recalibrage_uncusectomie = False
glb_recalibrage_osteophytique = False
glb_recalibrage_corporectomie = False
glb_recalibrage_aucun = False
glb_recalibrage_aucun2 = False
glb_recalibrage_hernie_oui = False
glb_recalibrage_hernie_non = False

glb_reca_postAnt = ""
glb_reca_infos = ""
glb_reca_hernie_associer = ""

validerRecalibrage = False
annulerRecalibrage= False

class Ui_Frame_Recalibrage(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(651, 540)
        self.frame_haut = QtWidgets.QFrame(Frame)
        self.frame_haut.setGeometry(QtCore.QRect(20, 10, 621, 131))
        self.frame_haut.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_haut.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_haut.setObjectName("frame_haut")
        self.radioButton_posterieure = QtWidgets.QRadioButton(self.frame_haut)
        self.radioButton_posterieure.setGeometry(QtCore.QRect(60, 60, 241, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_posterieure.setFont(font)
        self.radioButton_posterieure.setObjectName("radioButton_posterieure")
        self.radioButton_anterieure = QtWidgets.QRadioButton(self.frame_haut)
        self.radioButton_anterieure.setGeometry(QtCore.QRect(380, 60, 221, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_anterieure.setFont(font)
        self.radioButton_anterieure.setObjectName("radioButton_anterieure")
        self.pushButton_retour = QtWidgets.QPushButton(self.frame_haut)
        self.pushButton_retour.setGeometry(QtCore.QRect(10, 20, 61, 30))
        self.pushButton_retour.setObjectName("pushButton_retour")
        self.pushButton_annuler = QtWidgets.QPushButton(self.frame_haut)
        self.pushButton_annuler.setGeometry(QtCore.QRect(520, 20, 61, 30))
        self.pushButton_annuler.setObjectName("pushButton_annuler")
        self.label_haut_massacre = QtWidgets.QLabel(self.frame_haut)
        self.label_haut_massacre.setEnabled(False)
        self.label_haut_massacre.setGeometry(QtCore.QRect(280, 10, 2, 2))
        self.label_haut_massacre.setText("")
        self.label_haut_massacre.setObjectName("label_haut_massacre")
        self.frame_gauche = QtWidgets.QFrame(Frame)
        self.frame_gauche.setEnabled(False)
        self.frame_gauche.setGeometry(QtCore.QRect(20, 150, 301, 231))
        self.frame_gauche.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_gauche.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gauche.setObjectName("frame_gauche")
        self.checkBox_interlamaire = QtWidgets.QCheckBox(self.frame_gauche)
        self.checkBox_interlamaire.setGeometry(QtCore.QRect(10, 10, 281, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_interlamaire.setFont(font)
        self.checkBox_interlamaire.setObjectName("checkBox_interlamaire")
        self.checkBox_interEpineux = QtWidgets.QCheckBox(self.frame_gauche)
        self.checkBox_interEpineux.setGeometry(QtCore.QRect(10, 50, 281, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_interEpineux.setFont(font)
        self.checkBox_interEpineux.setObjectName("checkBox_interEpineux")
        self.checkBox_laminectomie = QtWidgets.QCheckBox(self.frame_gauche)
        self.checkBox_laminectomie.setGeometry(QtCore.QRect(10, 90, 281, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_laminectomie.setFont(font)
        self.checkBox_laminectomie.setObjectName("checkBox_laminectomie")
        self.checkBox_arthrectomie = QtWidgets.QCheckBox(self.frame_gauche)
        self.checkBox_arthrectomie.setGeometry(QtCore.QRect(10, 130, 281, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_arthrectomie.setFont(font)
        self.checkBox_arthrectomie.setObjectName("checkBox_arthrectomie")
        self.radioButton_aucun = QtWidgets.QRadioButton(self.frame_gauche)
        self.radioButton_aucun.setGeometry(QtCore.QRect(10, 170, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_aucun.setFont(font)
        self.radioButton_aucun.setObjectName("radioButton_aucun")
        self.label_choix_massacre = QtWidgets.QLabel(self.frame_gauche)
        self.label_choix_massacre.setEnabled(False)
        self.label_choix_massacre.setGeometry(QtCore.QRect(260, 210, 2, 2))
        self.label_choix_massacre.setText("")
        self.label_choix_massacre.setObjectName("label_choix_massacre")
        self.frame_bas = QtWidgets.QFrame(Frame)
        self.frame_bas.setGeometry(QtCore.QRect(19, 389, 621, 141))
        self.frame_bas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bas.setObjectName("frame_bas")
        self.radioButton_non = QtWidgets.QRadioButton(self.frame_bas)
        self.radioButton_non.setGeometry(QtCore.QRect(250, 70, 91, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_non.setFont(font)
        self.radioButton_non.setObjectName("radioButton_non")
        self.label = QtWidgets.QLabel(self.frame_bas)
        self.label.setGeometry(QtCore.QRect(10, 50, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_suivant = QtWidgets.QPushButton(self.frame_bas)
        self.pushButton_suivant.setGeometry(QtCore.QRect(490, 50, 61, 30))
        self.pushButton_suivant.setObjectName("pushButton_suivant")
        self.radioButton_oui = QtWidgets.QRadioButton(self.frame_bas)
        self.radioButton_oui.setGeometry(QtCore.QRect(250, 30, 81, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_oui.setFont(font)
        self.radioButton_oui.setObjectName("radioButton_oui")
        self.label_hernie_massacre = QtWidgets.QLabel(self.frame_bas)
        self.label_hernie_massacre.setEnabled(False)
        self.label_hernie_massacre.setGeometry(QtCore.QRect(570, 120, 2, 2))
        self.label_hernie_massacre.setText("")
        self.label_hernie_massacre.setObjectName("label_hernie_massacre")
        self.frame_droite = QtWidgets.QFrame(Frame)
        self.frame_droite.setEnabled(False)
        self.frame_droite.setGeometry(QtCore.QRect(329, 149, 311, 231))
        self.frame_droite.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_droite.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_droite.setObjectName("frame_droite")
        self.radioButton_aucun2 = QtWidgets.QRadioButton(self.frame_droite)
        self.radioButton_aucun2.setGeometry(QtCore.QRect(10, 170, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_aucun2.setFont(font)
        self.radioButton_aucun2.setObjectName("radioButton_aucun2")
        self.checkBox_uncusectomie = QtWidgets.QCheckBox(self.frame_droite)
        self.checkBox_uncusectomie.setGeometry(QtCore.QRect(10, 50, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_uncusectomie.setFont(font)
        self.checkBox_uncusectomie.setObjectName("checkBox_uncusectomie")
        self.checkBox_osteophytiques = QtWidgets.QCheckBox(self.frame_droite)
        self.checkBox_osteophytiques.setGeometry(QtCore.QRect(10, 90, 271, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_osteophytiques.setFont(font)
        self.checkBox_osteophytiques.setObjectName("checkBox_osteophytiques")
        self.checkBox_foraminotomie = QtWidgets.QCheckBox(self.frame_droite)
        self.checkBox_foraminotomie.setGeometry(QtCore.QRect(10, 10, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_foraminotomie.setFont(font)
        self.checkBox_foraminotomie.setObjectName("checkBox_foraminotomie")
        self.checkBox_corporectomie = QtWidgets.QCheckBox(self.frame_droite)
        self.checkBox_corporectomie.setGeometry(QtCore.QRect(10, 130, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_corporectomie.setFont(font)
        self.checkBox_corporectomie.setObjectName("checkBox_corporectomie")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(30, 140, 601, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Frame)
        self.line_2.setGeometry(QtCore.QRect(315, 160, 20, 201))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Frame)
        self.line_3.setGeometry(QtCore.QRect(30, 380, 601, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.radioButton_posterieure.setText(_translate("Frame", "Voie postérieure"))
        self.radioButton_anterieure.setText(_translate("Frame", "Voie antérieure"))
        self.pushButton_retour.setText(_translate("Frame", "Retour"))
        self.pushButton_annuler.setText(_translate("Frame", "Annuler"))
        self.checkBox_interlamaire.setText(_translate("Frame", "Recalibrage par abord interlamaire"))
        self.checkBox_interEpineux.setText(_translate("Frame", "Recalibrage par abord inter-épineux"))
        self.checkBox_laminectomie.setText(_translate("Frame", "Recalibrage par laminectomie"))
        self.checkBox_arthrectomie.setText(_translate("Frame", "Recalibrage par arthrectomie"))
        self.radioButton_aucun.setText(_translate("Frame", "Aucun"))
        self.radioButton_non.setText(_translate("Frame", "Non"))
        self.label.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Hernie discale associée :</p></body></html>"))
        self.pushButton_suivant.setText(_translate("Frame", "Suivant"))
        self.radioButton_oui.setText(_translate("Frame", "Oui"))
        self.radioButton_aucun2.setText(_translate("Frame", "Aucun"))
        self.checkBox_uncusectomie.setText(_translate("Frame", "Uncusectomie"))
        self.checkBox_osteophytiques.setText(_translate("Frame", "Résection des barres ostéophytiques"))
        self.checkBox_foraminotomie.setText(_translate("Frame", "Foraminotomie"))
        self.checkBox_corporectomie.setText(_translate("Frame", "Corporectomie"))


class MainWindow_FormRecalibrage(QtWidgets.QWidget, Ui_Frame_Recalibrage):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        # récupération des valeurs des checkbox
        self.checkBox_interlamaire.stateChanged.connect(self.checkBoxChangeAction_interlamaire)
        self.checkBox_interEpineux.stateChanged.connect(self.checkBoxChangeAction_interEpineux)
        self.checkBox_laminectomie.stateChanged.connect(self.checkBoxChangeAction_laminectomie)
        self.checkBox_arthrectomie.stateChanged.connect(self.checkBoxChangeAction_arthrectomie)
        self.checkBox_foraminotomie.stateChanged.connect(self.checkBoxChangeAction_foraminotomie)
        self.checkBox_uncusectomie.stateChanged.connect(self.checkBoxChangeAction_uncusectomie)
        self.checkBox_osteophytiques.stateChanged.connect(self.checkBoxChangeAction_osteophytiques)
        self.checkBox_corporectomie.stateChanged.connect(self.checkBoxChangeAction_corporectomie)



        # valeur des radiobuttons
        self.radioButton_anterieure.toggled.connect(self.radiobtnFrame_Haut_anterieur)
        self.radioButton_posterieure.toggled.connect(self.radiobtnFrame_Haut_posterieur)


        self.radioButton_aucun.toggled.connect(self.radiobtnFrame_Gauche)
        self.radioButton_aucun2.toggled.connect(self.radiobtnFrame_Droite)

        self.radioButton_oui.toggled.connect(self.radiobtnFrame_BasOui)
        self.radioButton_non.toggled.connect(self.radiobtnFrame_BasNon)

        # controlleur pour les boutons
        self.pushButton_retour.clicked.connect(self.retourEtapePrecedente)
        self.pushButton_annuler.clicked.connect(self.annulerCreationDP)
        self.pushButton_suivant.clicked.connect(self.suivant) #Ne change pas d'interface mais récupère uniquement les valeurs pour lineedit de creationDP

    def retourEtapePrecedente(self):
        global validerRecalibrage, annulerRecalibrage
        validerRecalibrage= False
        annulerRecalibrage = False
        self.switch_window1.emit()

    def annulerCreationDP(self):
        global validerRecalibrage, annulerRecalibrage
        validerRecalibrage = False
        annulerRecalibrage = True
        self.switch_window2.emit()

    def radiobtnFrame_Haut_anterieur(self):
        global glb_recalibrage_anterieur, glb_recalibrage_posterieur
        global glb_reca_postAnt
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_recalibrage_anterieur = True
            glb_recalibrage_posterieur = False
            self.frame_gauche.setEnabled(False)
            self.frame_droite.setEnabled(True)
            glb_reca_postAnt = " Recalibrage voie antérieure"

    def radiobtnFrame_Haut_posterieur(self):
        global glb_recalibrage_anterieur, glb_recalibrage_posterieur
        global glb_reca_postAnt
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_recalibrage_anterieur = False
            glb_recalibrage_posterieur = True
            self.frame_gauche.setEnabled(True)
            self.frame_droite.setEnabled(False)
            glb_reca_postAnt = " Recalibrage voie postérieure"

    def radiobtnFrame_Gauche(self):
        global glb_recalibrage_aucun, glb_recalibrage_laminectomie, glb_recalibrage_interEpineux, glb_recalibrage_interlamaire, glb_recalibrage_arthrectomie
        global glb_reca_infos
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_recalibrage_aucun = True
            glb_recalibrage_laminectomie = False
            glb_recalibrage_interEpineux = False
            glb_recalibrage_interlamaire = False
            glb_recalibrage_arthrectomie = False
            self.checkBox_interlamaire.setChecked(False)
            self.checkBox_interEpineux.setChecked(False)
            self.checkBox_laminectomie.setChecked(False)
            self.checkBox_arthrectomie.setChecked(False)
            glb_reca_infos = ""

    def radiobtnFrame_Droite(self):
        global glb_recalibrage_aucun2, glb_recalibrage_foraminotomie, glb_recalibrage_uncusectomie, glb_recalibrage_osteophytique, glb_recalibrage_corporectomie
        global glb_reca_infos
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_recalibrage_aucun2 = True
            glb_recalibrage_foraminotomie = False
            glb_recalibrage_uncusectomie = False
            glb_recalibrage_osteophytique = False
            glb_recalibrage_corporectomie = False
            self.checkBox_foraminotomie.setChecked(False)
            self.checkBox_uncusectomie.setChecked(False)
            self.checkBox_osteophytiques.setChecked(False)
            self.checkBox_corporectomie.setChecked(False)
            glb_reca_infos = ""

    def radiobtnFrame_BasOui(self):
        global glb_recalibrage_hernie_non, glb_recalibrage_hernie_oui
        global glb_reca_hernie_associer
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_recalibrage_hernie_non = False
            glb_recalibrage_hernie_oui = True
            glb_reca_hernie_associer = "Avec hernie discale associée"

    def radiobtnFrame_BasNon(self):
        global glb_recalibrage_hernie_non, glb_recalibrage_hernie_oui
        global glb_reca_hernie_associer
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_recalibrage_hernie_non = True
            glb_recalibrage_hernie_oui = False
            glb_reca_hernie_associer = ""

    def checkBoxChangeAction_interlamaire(self, state):
        global glb_recalibrage_aucun, glb_recalibrage_laminectomie, glb_recalibrage_interEpineux, glb_recalibrage_interlamaire, glb_recalibrage_arthrectomie
        global glb_reca_infos
        if (state == QtCore.Qt.Checked):
            glb_recalibrage_aucun = False
            glb_recalibrage_laminectomie = False
            glb_recalibrage_interEpineux = False
            glb_recalibrage_interlamaire = True
            glb_recalibrage_arthrectomie = False
            self.radioButton_aucun.setChecked(False)
            glb_reca_infos = "par abord interlamaire"
        else:
            glb_reca_infos = ""

    def checkBoxChangeAction_interEpineux(self, state):
        global glb_recalibrage_aucun, glb_recalibrage_laminectomie, glb_recalibrage_interEpineux, glb_recalibrage_interlamaire, glb_recalibrage_arthrectomie
        global glb_reca_infos
        if (state == QtCore.Qt.Checked):
            glb_recalibrage_aucun = False
            glb_recalibrage_laminectomie = False
            glb_recalibrage_interEpineux = True
            glb_recalibrage_interlamaire = False
            glb_recalibrage_arthrectomie = False
            self.radioButton_aucun.setChecked(False)
            glb_reca_infos = "par abord inter-épineux"
        else:
            glb_reca_infos = ""

    def checkBoxChangeAction_laminectomie(self, state):
        global glb_recalibrage_aucun, glb_recalibrage_laminectomie, glb_recalibrage_interEpineux, glb_recalibrage_interlamaire, glb_recalibrage_arthrectomie
        global glb_reca_infos
        if (state == QtCore.Qt.Checked):
            glb_recalibrage_aucun = False
            glb_recalibrage_laminectomie = True
            glb_recalibrage_interEpineux = False
            glb_recalibrage_interlamaire = False
            glb_recalibrage_arthrectomie = False
            self.radioButton_aucun.setChecked(False)
            glb_reca_infos = "par laminectomie"
        else:
            glb_reca_infos = ""

    def checkBoxChangeAction_arthrectomie(self, state):
        global glb_recalibrage_aucun, glb_recalibrage_laminectomie, glb_recalibrage_interEpineux, glb_recalibrage_interlamaire, glb_recalibrage_arthrectomie
        global glb_reca_infos
        if (state == QtCore.Qt.Checked):
            glb_recalibrage_aucun = False
            glb_recalibrage_laminectomie = False
            glb_recalibrage_interEpineux = False
            glb_recalibrage_interlamaire = False
            glb_recalibrage_arthrectomie = True
            self.radioButton_aucun.setChecked(False)
            glb_reca_infos = "par arthrectomie"
        else:
            glb_reca_infos = ""

    def checkBoxChangeAction_foraminotomie(self, state):
        global glb_recalibrage_aucun2, glb_recalibrage_foraminotomie, glb_recalibrage_uncusectomie, glb_recalibrage_osteophytique, glb_recalibrage_corporectomie
        global glb_reca_infos
        if (state == QtCore.Qt.Checked):
            glb_recalibrage_aucun2 = False
            glb_recalibrage_foraminotomie = True
            glb_recalibrage_uncusectomie = False
            glb_recalibrage_osteophytique = False
            glb_recalibrage_corporectomie = False
            self.radioButton_aucun2.setChecked(False)
            glb_reca_infos = "par foraminotomie"
        else:
            print("unchecked")

    def checkBoxChangeAction_uncusectomie(self, state):
        global glb_recalibrage_aucun2, glb_recalibrage_foraminotomie, glb_recalibrage_uncusectomie, glb_recalibrage_osteophytique, glb_recalibrage_corporectomie
        global glb_reca_infos
        if (state == QtCore.Qt.Checked):
            glb_recalibrage_aucun2 = False
            glb_recalibrage_foraminotomie = False
            glb_recalibrage_uncusectomie = True
            glb_recalibrage_osteophytique = False
            glb_recalibrage_corporectomie = False
            self.radioButton_aucun2.setChecked(False)
            glb_reca_infos = "par uncusectomie"
        else:
            glb_reca_infos = ""

    def checkBoxChangeAction_osteophytiques(self, state):
        global glb_recalibrage_aucun2, glb_recalibrage_foraminotomie, glb_recalibrage_uncusectomie, glb_recalibrage_osteophytique, glb_recalibrage_corporectomie
        global glb_reca_infos
        if (state == QtCore.Qt.Checked):
            glb_recalibrage_aucun2 = False
            glb_recalibrage_foraminotomie = False
            glb_recalibrage_uncusectomie = False
            glb_recalibrage_osteophytique = True
            glb_recalibrage_corporectomie = False
            self.radioButton_aucun2.setChecked(False)
            glb_reca_infos = "par résection des barres ostéophytiques"
        else:
            glb_reca_infos = ""

    def checkBoxChangeAction_corporectomie(self, state):
        global glb_recalibrage_aucun2, glb_recalibrage_foraminotomie, glb_recalibrage_uncusectomie, glb_recalibrage_osteophytique, glb_recalibrage_corporectomie
        global glb_reca_infos
        if (state == QtCore.Qt.Checked):
            glb_recalibrage_aucun2 = False
            glb_recalibrage_foraminotomie = False
            glb_recalibrage_uncusectomie = False
            glb_recalibrage_osteophytique = False
            glb_recalibrage_corporectomie = True
            self.radioButton_aucun2.setChecked(False)
            glb_reca_infos = "par corporectomie"
        else:
            glb_reca_infos = ""


    def suivant(self):
        global validerRecalibrage, annulerRecalibrage
        global glb_recalibrage_anterieur, glb_recalibrage_posterieur
        global glb_recalibrage_aucun2, glb_recalibrage_foraminotomie, glb_recalibrage_uncusectomie, glb_recalibrage_osteophytique, glb_recalibrage_corporectomie
        global glb_recalibrage_aucun, glb_recalibrage_laminectomie, glb_recalibrage_interEpineux, glb_recalibrage_interlamaire, glb_recalibrage_arthrectomie
        global glb_recalibrage_hernie_non, glb_recalibrage_hernie_oui

        glb_recalibrage_posterieur = False
        glb_recalibrage_anterieur = False
        glb_recalibrage_interlamaire = False
        glb_recalibrage_interEpineux = False
        glb_recalibrage_arthrectomie = False
        glb_recalibrage_laminectomie = False
        glb_recalibrage_foraminotomie = False
        glb_recalibrage_uncusectomie = False
        glb_recalibrage_osteophytique = False
        glb_recalibrage_corporectomie = False
        glb_recalibrage_aucun = False
        glb_recalibrage_aucun2 = False
        glb_recalibrage_hernie_oui = False
        glb_recalibrage_hernie_non = False

        validerRecalibrage = True
        annulerRecalibrage = False
        self.switch_window3.emit() #faute de mieux
