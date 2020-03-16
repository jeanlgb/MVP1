# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pathologie_Degeneratif.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

glb_dege_FN_radiculaire = True
glb_dege_FN_radicoMedullaire = False
glb_dege_FN_medullaire = False
glb_dege_FN_non = False
dege_vertebre1 = int(1)
dege_vertebre2 =int(2)
dege_recalibrage_oui = False
dege_recalibrage_hernie = True
dege_recalibrage_non = False
glb_dege_cote_gauche = False
glb_dege_cote_droit = False
glb_dege_cote_bilateral = False
dege_arthrodese_oui = False
dege_arthrodese_non = True

class Ui_Frame_Degeneratif(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(840, 681)
        self.pushButton_valider = QtWidgets.QPushButton(Frame)
        self.pushButton_valider.setGeometry(QtCore.QRect(560, 610, 130, 30))
        self.pushButton_valider.setObjectName("pushButton_valider")
        self.pushButton_annuler = QtWidgets.QPushButton(Frame)
        self.pushButton_annuler.setGeometry(QtCore.QRect(710, 10, 61, 30))
        self.pushButton_annuler.setObjectName("pushButton_annuler")
        self.pushButton_ajouterIntervention = QtWidgets.QPushButton(Frame)
        self.pushButton_ajouterIntervention.setGeometry(QtCore.QRect(90, 610, 130, 30))
        self.pushButton_ajouterIntervention.setObjectName("pushButton_ajouterIntervention")
        self.pushButton_retour = QtWidgets.QPushButton(Frame)
        self.pushButton_retour.setGeometry(QtCore.QRect(30, 10, 61, 30))
        self.pushButton_retour.setObjectName("pushButton_retour")
        self.groupBox_finaliteNeurologique = QtWidgets.QGroupBox(Frame)
        self.groupBox_finaliteNeurologique.setGeometry(QtCore.QRect(30, 50, 751, 91))
        self.groupBox_finaliteNeurologique.setObjectName("groupBox_finaliteNeurologique")
        self.radioButton_radicoMedullaire = QtWidgets.QRadioButton(self.groupBox_finaliteNeurologique)
        self.radioButton_radicoMedullaire.setGeometry(QtCore.QRect(50, 60, 301, 30))
        self.radioButton_radicoMedullaire.setObjectName("radioButton_radicoMedullaire")
        self.radioButton_non = QtWidgets.QRadioButton(self.groupBox_finaliteNeurologique)
        self.radioButton_non.setGeometry(QtCore.QRect(480, 60, 201, 30))
        self.radioButton_non.setObjectName("radioButton_non")
        self.radioButton_medullaire = QtWidgets.QRadioButton(self.groupBox_finaliteNeurologique)
        self.radioButton_medullaire.setGeometry(QtCore.QRect(480, 20, 241, 30))
        self.radioButton_medullaire.setObjectName("radioButton_medullaire")
        self.radioButton_radiculaire = QtWidgets.QRadioButton(self.groupBox_finaliteNeurologique)
        self.radioButton_radiculaire.setGeometry(QtCore.QRect(50, 20, 301, 30))
        self.radioButton_radiculaire.setChecked(True)
        self.radioButton_radiculaire.setObjectName("radioButton_radiculaire")
        self.groupBox_Niveau = QtWidgets.QGroupBox(Frame)
        self.groupBox_Niveau.setGeometry(QtCore.QRect(30, 160, 751, 91))
        self.groupBox_Niveau.setObjectName("groupBox_Niveau")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_Niveau)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(330, 60, 60, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_niveau = QtWidgets.QLabel(self.groupBox_Niveau)
        self.label_niveau.setGeometry(QtCore.QRect(220, 30, 491, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_niveau.setFont(font)
        self.label_niveau.setObjectName("label_niveau")
        self.label_niveauCalcul = QtWidgets.QLabel(self.groupBox_Niveau)
        self.label_niveauCalcul.setGeometry(QtCore.QRect(220, 60, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_niveauCalcul.setFont(font)
        self.label_niveauCalcul.setObjectName("label_niveauCalcul")
        self.spinBox_nombre1 = QtWidgets.QSpinBox(self.groupBox_Niveau)
        self.spinBox_nombre1.setGeometry(QtCore.QRect(410, 30, 51, 21))
        self.spinBox_nombre1.setMinimum(1)
        self.spinBox_nombre1.setMaximum(32)
        self.spinBox_nombre1.setObjectName("spinBox_nombre1")
        self.spinBox_nombre2 = QtWidgets.QSpinBox(self.groupBox_Niveau)
        self.spinBox_nombre2.setGeometry(QtCore.QRect(480, 30, 51, 21))
        self.spinBox_nombre2.setMinimum(2)
        self.spinBox_nombre2.setMaximum(33)
        self.spinBox_nombre2.setObjectName("spinBox_nombre2")
        self.label_patho = QtWidgets.QLabel(self.groupBox_Niveau)
        self.label_patho.setEnabled(False)
        self.label_patho.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_patho.setText("")
        self.label_patho.setObjectName("label_patho")
        self.groupBox_recalibrage = QtWidgets.QGroupBox(Frame)
        self.groupBox_recalibrage.setGeometry(QtCore.QRect(30, 270, 751, 91))
        self.groupBox_recalibrage.setObjectName("groupBox_recalibrage")
        self.pushButton_recalibrageSuivant = QtWidgets.QPushButton(self.groupBox_recalibrage)
        self.pushButton_recalibrageSuivant.setGeometry(QtCore.QRect(520, 50, 61, 30))
        self.pushButton_recalibrageSuivant.setObjectName("pushButton_recalibrageSuivant")
        self.radioButton_herniePure = QtWidgets.QRadioButton(self.groupBox_recalibrage)
        self.radioButton_herniePure.setGeometry(QtCore.QRect(230, 20, 281, 30))
        self.radioButton_herniePure.setChecked(True)
        self.radioButton_herniePure.setObjectName("radioButton_herniePure")
        self.radioButton_recalibrageNon = QtWidgets.QRadioButton(self.groupBox_recalibrage)
        self.radioButton_recalibrageNon.setChecked(False)
        self.radioButton_recalibrageNon.setGeometry(QtCore.QRect(100, 60, 121, 30))
        self.radioButton_recalibrageNon.setObjectName("radioButton_recalibrageNon")
        self.radioButton_recalibrageOui = QtWidgets.QRadioButton(self.groupBox_recalibrage)
        self.radioButton_recalibrageOui.setGeometry(QtCore.QRect(100, 20, 71, 30))
        self.radioButton_recalibrageOui.setObjectName("radioButton_recalibrageOui")
        self.groupBox_cote = QtWidgets.QGroupBox(Frame)
        self.groupBox_cote.setGeometry(QtCore.QRect(30, 380, 751, 91))
        self.groupBox_cote.setObjectName("groupBox_cote")
        self.label_bilateral = QtWidgets.QLabel(self.groupBox_cote)
        self.label_bilateral.setGeometry(QtCore.QRect(100, 50, 121, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_bilateral.setFont(font)
        self.label_bilateral.setObjectName("label_bilateral")
        self.label_unilateral = QtWidgets.QLabel(self.groupBox_cote)
        self.label_unilateral.setGeometry(QtCore.QRect(100, 10, 121, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_unilateral.setFont(font)
        self.label_unilateral.setObjectName("label_unilateral")
        self.radioButton_bilateral = QtWidgets.QRadioButton(self.groupBox_cote)
        self.radioButton_bilateral.setGeometry(QtCore.QRect(230, 50, 261, 30))
        self.radioButton_bilateral.setObjectName("radioButton_bilateral")
        self.radioButton_gauche = QtWidgets.QRadioButton(self.groupBox_cote)
        self.radioButton_gauche.setGeometry(QtCore.QRect(350, 10, 141, 30))
        self.radioButton_gauche.setObjectName("radioButton_gauche")
        self.radioButton_Droit = QtWidgets.QRadioButton(self.groupBox_cote)
        self.radioButton_Droit.setEnabled(True)
        self.radioButton_Droit.setGeometry(QtCore.QRect(230, 10, 141, 30))
        self.radioButton_Droit.setObjectName("radioButton_Droit")
        self.groupBox_arthrodese = QtWidgets.QGroupBox(Frame)
        self.groupBox_arthrodese.setGeometry(QtCore.QRect(30, 490, 751, 91))
        self.groupBox_arthrodese.setObjectName("groupBox_arthrodese")
        self.radioButton_arthrodeseNon = QtWidgets.QRadioButton(self.groupBox_arthrodese)
        self.radioButton_arthrodeseNon.setGeometry(QtCore.QRect(100, 50, 121, 30))
        self.radioButton_arthrodeseNon.setChecked(True)
        self.radioButton_arthrodeseNon.setObjectName("radioButton_arthrodeseNon")
        self.radioButton_arthrodeseOui = QtWidgets.QRadioButton(self.groupBox_arthrodese)
        self.radioButton_arthrodeseOui.setGeometry(QtCore.QRect(100, 20, 101, 30))
        self.radioButton_arthrodeseOui.setObjectName("radioButton_arthrodeseOui")
        self.pushButton_arthrodeseSuivant = QtWidgets.QPushButton(self.groupBox_arthrodese)
        self.pushButton_arthrodeseSuivant.setEnabled(False)
        self.pushButton_arthrodeseSuivant.setGeometry(QtCore.QRect(530, 50, 61, 30))
        self.pushButton_arthrodeseSuivant.setObjectName("pushButton_arthrodeseSuivant")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(30, 140, 751, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Frame)
        self.line_2.setGeometry(QtCore.QRect(30, 250, 751, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Frame)
        self.line_3.setGeometry(QtCore.QRect(30, 360, 751, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Frame)
        self.line_4.setGeometry(QtCore.QRect(30, 470, 751, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_titre = QtWidgets.QLabel(Frame)
        self.label_titre.setGeometry(QtCore.QRect(120, -10, 551, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_titre.setFont(font)
        self.label_titre.setObjectName("label_titre")
        self.label_titre.raise_()
        self.groupBox_cote.raise_()
        self.groupBox_arthrodese.raise_()
        self.groupBox_recalibrage.raise_()
        self.groupBox_Niveau.raise_()
        self.groupBox_finaliteNeurologique.raise_()
        self.pushButton_valider.raise_()
        self.pushButton_annuler.raise_()
        self.pushButton_ajouterIntervention.raise_()
        self.pushButton_retour.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_valider.setText(_translate("Frame", "Valider"))
        self.pushButton_annuler.setText(_translate("Frame", "Annuler"))
        self.pushButton_ajouterIntervention.setText(_translate("Frame", "Ajouter intervention"))
        self.pushButton_retour.setText(_translate("Frame", "Retour"))
        self.groupBox_finaliteNeurologique.setTitle(_translate("Frame", "1 - Finalité neurologique"))
        self.radioButton_radicoMedullaire.setText(_translate("Frame", "Décompression radico-médullaire"))
        self.radioButton_non.setText(_translate("Frame", "Non"))
        self.radioButton_medullaire.setText(_translate("Frame", "Décompression médullaire"))
        self.radioButton_radiculaire.setText(_translate("Frame", "Décompression radiculaire"))
        self.groupBox_Niveau.setTitle(_translate("Frame", "2 - Niveau(x)"))
        self.label_niveau.setText(_translate("Frame", "Intervention de la vertèbre           à             ."))
        self.label_niveauCalcul.setText(_translate("Frame", "Espace vertèbre : "))
        self.groupBox_recalibrage.setTitle(_translate("Frame", "3 - Recalibrage"))
        self.pushButton_recalibrageSuivant.setText(_translate("Frame", "Suivant"))
        self.radioButton_herniePure.setText(_translate("Frame", "Hernie discale pure"))
        self.radioButton_recalibrageNon.setText(_translate("Frame", "Non"))
        self.radioButton_recalibrageOui.setText(_translate("Frame", "Oui"))
        self.groupBox_cote.setTitle(_translate("Frame", "4 - Côté"))
        self.label_bilateral.setText(_translate("Frame", "Bilatéral :"))
        self.label_unilateral.setText(_translate("Frame", "Unilatéral :"))
        self.radioButton_bilateral.setText(_translate("Frame", "Bilatéral"))
        self.radioButton_gauche.setText(_translate("Frame", "Gauche"))
        self.radioButton_Droit.setText(_translate("Frame", "Droit"))
        self.groupBox_arthrodese.setTitle(_translate("Frame", "5 - Arthrodèse"))
        self.radioButton_arthrodeseNon.setText(_translate("Frame", "Non"))
        self.radioButton_arthrodeseOui.setText(_translate("Frame", "Oui"))
        self.pushButton_arthrodeseSuivant.setText(_translate("Frame", "Suivant"))
        self.label_titre.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Pathologie Dégénérative</span></p></body></html>"))

class MainWindow_Degeneratif(QtWidgets.QWidget, Ui_Frame_Degeneratif):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()
    switch_window6 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)


        # valeur des radiobuttons finalité neuro
        self.radioButton_radiculaire.toggled.connect(self.radiobtn_FN_radiculaire)
        self.radioButton_radicoMedullaire.toggled.connect(self.radiobtn_FN_radicoMedullaire)
        self.radioButton_medullaire.toggled.connect(self.radiobtn_FN_medullaire)
        self.radioButton_non.toggled.connect(self.radiobtn_FN_non)

        # récupération nombre de vertèbres
        self.nombre1 = self.spinBox_nombre1.valueChanged.connect(self.countVertebres)
        self.nombre2 = self.spinBox_nombre2.valueChanged.connect(self.countVertebres)

        # valeur des radiobuttons recalibrage et arthrodèse
        self.radioButton_herniePure.toggled.connect(self.radiobtnRecalibrage_hernie)
        self.radioButton_recalibrageNon.toggled.connect(self.radiobtnRecalibrage_non)
        self.radioButton_recalibrageOui.toggled.connect(self.radiobtnRecalibrage_oui)
        self.radioButton_arthrodeseNon.toggled.connect(self.radiobtnArthrodese_non)
        self.radioButton_arthrodeseOui.toggled.connect(self.radiobtnArthrodese_oui)

        # valeur des radiobuttons côté
        self.radioButton_bilateral.toggled.connect(self.radiobtnCote_bilateral)
        self.radioButton_Droit.toggled.connect(self.radiobtnCote_droit)
        self.radioButton_gauche.toggled.connect(self.radiobtnCote_gauche)

        # controlleur pour les boutons
        self.pushButton_retour.clicked.connect(self.retourEtape2)
        self.pushButton_annuler.clicked.connect(self.annulerCreationDP)
        self.pushButton_recalibrageSuivant.clicked.connect(self.suivantRecalibrage)
        self.pushButton_arthrodeseSuivant.clicked.connect(self.suivantArthrodese)
        self.pushButton_ajouterIntervention.clicked.connect(self.ajouterIntervention)
        self.pushButton_valider.clicked.connect(self.valider) #Ne change pas d'interface mais récupère uniquement les valeurs pour lineedit de creationDP

    def radiobtn_FN_radiculaire(self):
        global glb_dege_FN_medullaire, glb_dege_FN_non,glb_dege_FN_radicoMedullaire,glb_dege_FN_radiculaire
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_dege_FN_radiculaire = True
            glb_dege_FN_radicoMedullaire = False
            glb_dege_FN_medullaire = False
            glb_dege_FN_non = False

    def radiobtn_FN_radicoMedullaire(self):
        global glb_dege_FN_medullaire, glb_dege_FN_non,glb_dege_FN_radicoMedullaire,glb_dege_FN_radiculaire
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_dege_FN_radiculaire = False
            glb_dege_FN_radicoMedullaire = True
            glb_dege_FN_medullaire = False
            glb_dege_FN_non = False
            print("4")

    def radiobtn_FN_medullaire(self):
        global glb_dege_FN_medullaire, glb_dege_FN_non,glb_dege_FN_radicoMedullaire,glb_dege_FN_radiculaire
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_dege_FN_radiculaire = False
            glb_dege_FN_radicoMedullaire = False
            glb_dege_FN_medullaire = True
            glb_dege_FN_non = False
            print("FN choix fait")

    def radiobtn_FN_non(self):
        global glb_dege_FN_medullaire, glb_dege_FN_non,glb_dege_FN_radicoMedullaire,glb_dege_FN_radiculaire
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_dege_FN_radiculaire = False
            glb_dege_FN_radicoMedullaire = False
            glb_dege_FN_medullaire = False
            glb_dege_FN_non = True
            print("FN choix fait")

    def countVertebres(self):
        global dege_vertebre1, dege_vertebre2

        dege_vertebre1 = self.spinBox_nombre1.value()
        dege_vertebre2 = self.spinBox_nombre2.value()
        print("5")
        self.soustraction = int(dege_vertebre2) + int(-dege_vertebre1)
        self.lineEdit.setText(str(self.soustraction))

    def retourEtape2(self):
        global glb_dege_FN_radiculaire, glb_dege_FN_radicoMedullaire, glb_dege_FN_medullaire, glb_dege_FN_non, dege_vertebre1, dege_vertebre2, dege_recalibrage_oui
        global dege_recalibrage_hernie, dege_recalibrage_non, glb_dege_cote_gauche, glb_dege_cote_droit, glb_dege_cote_bilateral, dege_arthrodese_oui, dege_arthrodese_non

        glb_dege_FN_radiculaire = True
        glb_dege_FN_radicoMedullaire = False
        glb_dege_FN_medullaire = False
        glb_dege_FN_non = False
        dege_vertebre1 = int(1)
        dege_vertebre2 = int(2)
        dege_recalibrage_oui = False
        dege_recalibrage_hernie = True
        dege_recalibrage_non = False
        glb_dege_cote_gauche = False
        glb_dege_cote_droit = False
        glb_dege_cote_bilateral = False
        dege_arthrodese_oui = False
        dege_arthrodese_non = True

        self.switch_window1.emit()

    def annulerCreationDP(self):
        global glb_dege_FN_radiculaire, glb_dege_FN_radicoMedullaire, glb_dege_FN_medullaire, glb_dege_FN_non, dege_vertebre1, dege_vertebre2, dege_recalibrage_oui
        global dege_recalibrage_hernie, dege_recalibrage_non, glb_dege_cote_gauche, glb_dege_cote_droit, glb_dege_cote_bilateral, dege_arthrodese_oui, dege_arthrodese_non

        glb_dege_FN_radiculaire = True
        glb_dege_FN_radicoMedullaire = False
        glb_dege_FN_medullaire = False
        glb_dege_FN_non = False
        dege_vertebre1 = int(1)
        dege_vertebre2 = int(2)
        dege_recalibrage_oui = False
        dege_recalibrage_hernie = True
        dege_recalibrage_non = False
        glb_dege_cote_gauche = False
        glb_dege_cote_droit = False
        glb_dege_cote_bilateral = False
        dege_arthrodese_oui = False
        dege_arthrodese_non = True
        self.switch_window2.emit()

    def radiobtnRecalibrage_oui(self):
        global dege_recalibrage_oui, dege_recalibrage_hernie, dege_recalibrage_non
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            dege_recalibrage_oui = True
            dege_recalibrage_hernie = False
            dege_recalibrage_non = False
            print("6")
            self.pushButton_recalibrageSuivant.setEnabled(True)
            self.groupBox_cote.setEnabled(True)

    def radiobtnRecalibrage_hernie(self):
        global dege_recalibrage_oui, dege_recalibrage_hernie, dege_recalibrage_non
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            dege_recalibrage_oui = False
            dege_recalibrage_hernie = True
            dege_recalibrage_non = False
            self.pushButton_recalibrageSuivant.setEnabled(True)
            self.groupBox_cote.setEnabled(True)

    def radiobtnRecalibrage_non(self):
        global dege_recalibrage_oui, dege_recalibrage_hernie, dege_recalibrage_non
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            dege_recalibrage_oui = False
            dege_recalibrage_hernie = False
            dege_recalibrage_non = True
            self.pushButton_recalibrageSuivant.setEnabled(False)
            self.groupBox_cote.setEnabled(False)

    def suivantRecalibrage(self):
        self.switch_window3.emit()

    def radiobtnCote_bilateral(self):
        global glb_dege_cote_bilateral, glb_dege_cote_droit, glb_dege_cote_gauche
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_dege_cote_droit = False
            glb_dege_cote_gauche = False
            glb_dege_cote_bilateral = True
            print("7")

    def radiobtnCote_droit(self):
        global glb_dege_cote_bilateral, glb_dege_cote_droit, glb_dege_cote_gauche
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_dege_cote_droit = True
            glb_dege_cote_gauche = False
            glb_dege_cote_bilateral = False

    def radiobtnCote_gauche(self):
        global glb_dege_cote_bilateral, glb_dege_cote_droit, glb_dege_cote_gauche
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_dege_cote_droit = False
            glb_dege_cote_gauche = True
            glb_dege_cote_bilateral = False

    def radiobtnArthrodese_non(self):
        global dege_arthrodese_non, dege_arthrodese_oui
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            dege_arthrodese_non = True
            dege_arthrodese_oui = False
            self.pushButton_arthrodeseSuivant.setEnabled(False)

    def radiobtnArthrodese_oui(self):
        global dege_arthrodese_non, dege_arthrodese_oui
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            dege_arthrodese_oui = True
            dege_arthrodese_non = False
            print("8")
            self.pushButton_arthrodeseSuivant.setEnabled(True)

    def suivantArthrodese(self):
        self.switch_window4.emit()


    def ajouterIntervention(self):
        self.switch_window5.emit()

    def valider(self):
        print("9")
        self.switch_window6.emit() #faute de mieux