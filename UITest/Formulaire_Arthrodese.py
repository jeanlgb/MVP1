# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Formulaire_Arthrodese.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

glb_arthrodese_posterieur = False
glb_arthrodese_anterieur = False
glb_arthrodese_polyaxiales = False
glb_arthrodese_monoaxiales = False
glb_arthrodese_plaque = False
glb_arthrodese_fixationAucune = False
glb_arthrodese_fixationAucune2 = False
glb_arthrodese_2PLIF = False
glb_arthrodese_PLIF = False
glb_arthrodese_TLIF = False
glb_arthrodese_OsSeulement = False
glb_arthrodese_greffeAucune = False
glb_arthrodese_intersomatique = False
glb_arthrodese_corporectomie = False
glb_arthrodese_OsSeulement2 = False
glb_arthrodese_greffeAucune2 = False

glb_arthro_postAnt = ""
glb_arthro_fixation = ""
glb_arthro_greffe = ""

validerArthrodese = False
annulerArthrodese = False

class Ui_Frame_Arthrodese(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(620, 601)
        self.frame_haut = QtWidgets.QFrame(Frame)
        self.frame_haut.setGeometry(QtCore.QRect(20, 20, 591, 81))
        self.frame_haut.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_haut.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_haut.setObjectName("frame_haut")
        self.pushButton_retour = QtWidgets.QPushButton(self.frame_haut)
        self.pushButton_retour.setGeometry(QtCore.QRect(0, 0, 61, 30))
        self.pushButton_retour.setObjectName("pushButton_retour")
        self.pushButton_annuler = QtWidgets.QPushButton(self.frame_haut)
        self.pushButton_annuler.setGeometry(QtCore.QRect(500, 0, 61, 30))
        self.pushButton_annuler.setObjectName("pushButton_annuler")
        self.radioButton_anterieure = QtWidgets.QRadioButton(self.frame_haut)
        self.radioButton_anterieure.setGeometry(QtCore.QRect(370, 40, 221, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_anterieure.setFont(font)
        self.radioButton_anterieure.setObjectName("radioButton_anterieure")
        self.radioButton_posterieure = QtWidgets.QRadioButton(self.frame_haut)
        self.radioButton_posterieure.setGeometry(QtCore.QRect(50, 40, 241, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_posterieure.setFont(font)
        self.radioButton_posterieure.setObjectName("radioButton_posterieure")
        self.label_haut_massacre = QtWidgets.QLabel(self.frame_haut)
        self.label_haut_massacre.setEnabled(False)
        self.label_haut_massacre.setGeometry(QtCore.QRect(270, 10, 2, 2))
        self.label_haut_massacre.setObjectName("label_haut_massacre")
        self.frame_bas = QtWidgets.QFrame(Frame)
        self.frame_bas.setGeometry(QtCore.QRect(20, 550, 591, 41))
        self.frame_bas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bas.setObjectName("frame_bas")
        self.pushButton_suivant = QtWidgets.QPushButton(self.frame_bas)
        self.pushButton_suivant.setEnabled(False)
        self.pushButton_suivant.setGeometry(QtCore.QRect(500, 0, 61, 30))
        self.pushButton_suivant.setObjectName("pushButton_suivant")
        self.frame_gauche1 = QtWidgets.QFrame(Frame)
        self.frame_gauche1.setEnabled(False)
        self.frame_gauche1.setGeometry(QtCore.QRect(20, 110, 291, 181))
        self.frame_gauche1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_gauche1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gauche1.setObjectName("frame_gauche1")
        self.label_2 = QtWidgets.QLabel(self.frame_gauche1)
        self.label_2.setGeometry(QtCore.QRect(303, 80, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_gauche1)
        self.label_3.setGeometry(QtCore.QRect(280, 270, 261, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.radioButton_plaque = QtWidgets.QRadioButton(self.frame_gauche1)
        self.radioButton_plaque.setGeometry(QtCore.QRect(440, 150, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_plaque.setFont(font)
        self.radioButton_plaque.setObjectName("radioButton_plaque")
        self.radioButton_aucune = QtWidgets.QRadioButton(self.frame_gauche1)
        self.radioButton_aucune.setGeometry(QtCore.QRect(30, 140, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_aucune.setFont(font)
        self.radioButton_aucune.setObjectName("radioButton_aucune")
        self.radioButton_monoaxiales = QtWidgets.QRadioButton(self.frame_gauche1)
        self.radioButton_monoaxiales.setGeometry(QtCore.QRect(30, 100, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_monoaxiales.setFont(font)
        self.radioButton_monoaxiales.setObjectName("radioButton_monoaxiales")
        self.radioButton_polyaxiales = QtWidgets.QRadioButton(self.frame_gauche1)
        self.radioButton_polyaxiales.setGeometry(QtCore.QRect(30, 60, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_polyaxiales.setFont(font)
        self.radioButton_polyaxiales.setObjectName("radioButton_polyaxiales")
        self.frame_droite1 = QtWidgets.QFrame(Frame)
        self.frame_droite1.setEnabled(False)
        self.frame_droite1.setGeometry(QtCore.QRect(320, 110, 291, 181))
        self.frame_droite1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_droite1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_droite1.setObjectName("frame_droite1")
        self.radioButton_plaque_2 = QtWidgets.QRadioButton(self.frame_droite1)
        self.radioButton_plaque_2.setGeometry(QtCore.QRect(10, 60, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_plaque_2.setFont(font)
        self.radioButton_plaque_2.setObjectName("radioButton_plaque_2")
        self.radioButton_aucune2 = QtWidgets.QRadioButton(self.frame_droite1)
        self.radioButton_aucune2.setGeometry(QtCore.QRect(10, 100, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_aucune2.setFont(font)
        self.radioButton_aucune2.setObjectName("radioButton_aucune2")
        self.label_fixation = QtWidgets.QLabel(self.frame_droite1)
        self.label_fixation.setEnabled(False)
        self.label_fixation.setGeometry(QtCore.QRect(250, 10, 2, 2))
        self.label_fixation.setText("")
        self.label_fixation.setObjectName("label_fixation")
        self.frame_gauche2 = QtWidgets.QFrame(Frame)
        self.frame_gauche2.setEnabled(False)
        self.frame_gauche2.setGeometry(QtCore.QRect(20, 310, 291, 231))
        self.frame_gauche2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_gauche2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_gauche2.setObjectName("frame_gauche2")
        self.radioButton_aucuneGreffe = QtWidgets.QRadioButton(self.frame_gauche2)
        self.radioButton_aucuneGreffe.setGeometry(QtCore.QRect(10, 190, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_aucuneGreffe.setFont(font)
        self.radioButton_aucuneGreffe.setObjectName("radioButton_aucuneGreffe")
        self.radioButton_1plif = QtWidgets.QRadioButton(self.frame_gauche2)
        self.radioButton_1plif.setGeometry(QtCore.QRect(10, 70, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_1plif.setFont(font)
        self.radioButton_1plif.setObjectName("radioButton_1plif")
        self.radioButton_os = QtWidgets.QRadioButton(self.frame_gauche2)
        self.radioButton_os.setGeometry(QtCore.QRect(10, 150, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_os.setFont(font)
        self.radioButton_os.setObjectName("radioButton_os")
        self.radioButton_2plif = QtWidgets.QRadioButton(self.frame_gauche2)
        self.radioButton_2plif.setGeometry(QtCore.QRect(10, 30, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2plif.setFont(font)
        self.radioButton_2plif.setObjectName("radioButton_2plif")
        self.radioButton_tlif = QtWidgets.QRadioButton(self.frame_gauche2)
        self.radioButton_tlif.setGeometry(QtCore.QRect(10, 110, 231, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_tlif.setFont(font)
        self.radioButton_tlif.setObjectName("radioButton_tlif")
        self.frame_droite2 = QtWidgets.QFrame(Frame)
        self.frame_droite2.setEnabled(False)
        self.frame_droite2.setGeometry(QtCore.QRect(320, 310, 291, 231))
        self.frame_droite2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_droite2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_droite2.setObjectName("frame_droite2")
        self.radioButton_os2 = QtWidgets.QRadioButton(self.frame_droite2)
        self.radioButton_os2.setGeometry(QtCore.QRect(10, 140, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_os2.setFont(font)
        self.radioButton_os2.setObjectName("radioButton_os2")
        self.radioButton_aucuneGreffe2 = QtWidgets.QRadioButton(self.frame_droite2)
        self.radioButton_aucuneGreffe2.setGeometry(QtCore.QRect(10, 180, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_aucuneGreffe2.setFont(font)
        self.radioButton_aucuneGreffe2.setObjectName("radioButton_aucuneGreffe2")
        self.radioButton_intersomatique = QtWidgets.QRadioButton(self.frame_droite2)
        self.radioButton_intersomatique.setGeometry(QtCore.QRect(10, 60, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_intersomatique.setFont(font)
        self.radioButton_intersomatique.setObjectName("radioButton_intersomatique")
        self.radioButton_corporectomie_2 = QtWidgets.QRadioButton(self.frame_droite2)
        self.radioButton_corporectomie_2.setGeometry(QtCore.QRect(10, 100, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_corporectomie_2.setFont(font)
        self.radioButton_corporectomie_2.setObjectName("radioButton_corporectomie_2")
        self.label_greffe = QtWidgets.QLabel(self.frame_droite2)
        self.label_greffe.setEnabled(False)
        self.label_greffe.setGeometry(QtCore.QRect(260, 0, 2, 2))
        self.label_greffe.setText("")
        self.label_greffe.setObjectName("label_greffe")
        self.line_3 = QtWidgets.QFrame(Frame)
        self.line_3.setGeometry(QtCore.QRect(20, 290, 601, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(20, 100, 601, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_4 = QtWidgets.QFrame(Frame)
        self.line_4.setGeometry(QtCore.QRect(20, 540, 601, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtWidgets.QFrame(Frame)
        self.line_2.setGeometry(QtCore.QRect(305, 160, 20, 121))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_5 = QtWidgets.QFrame(Frame)
        self.line_5.setGeometry(QtCore.QRect(305, 360, 20, 181))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(180, 310, 261, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(210, 130, 211, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.frame_gauche2.raise_()
        self.frame_droite2.raise_()
        self.frame_gauche1.raise_()
        self.frame_droite1.raise_()
        self.frame_haut.raise_()
        self.frame_bas.raise_()
        self.line_3.raise_()
        self.line.raise_()
        self.line_4.raise_()
        self.line_2.raise_()
        self.line_5.raise_()
        self.label_5.raise_()
        self.label_4.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_retour.setText(_translate("Frame", "Retour"))
        self.pushButton_annuler.setText(_translate("Frame", "Annuler"))
        self.radioButton_anterieure.setText(_translate("Frame", "Voie antérieure"))
        self.radioButton_posterieure.setText(_translate("Frame", "Voie postérieure"))
        self.pushButton_suivant.setText(_translate("Frame", "Suivant"))
        self.label_2.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Fixation</p></body></html>"))
        self.label_3.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Greffe</p></body></html>"))
        self.radioButton_plaque.setText(_translate("Frame", "Plaque"))
        self.radioButton_aucune.setText(_translate("Frame", "Aucune"))
        self.radioButton_monoaxiales.setText(_translate("Frame", "Vis pédiculaires monoaxiales"))
        self.radioButton_polyaxiales.setText(_translate("Frame", "Vis pédiculaires polyaxiales"))
        self.radioButton_plaque_2.setText(_translate("Frame", "Plaque"))
        self.radioButton_aucune2.setText(_translate("Frame", "Aucune"))
        self.radioButton_aucuneGreffe.setText(_translate("Frame", "Aucune"))
        self.radioButton_1plif.setText(_translate("Frame", "1 cage intersomatique PLIF"))
        self.radioButton_os.setText(_translate("Frame", "Os seulement"))
        self.radioButton_2plif.setText(_translate("Frame", "2 cages intersomatiques PLIF"))
        self.radioButton_tlif.setText(_translate("Frame", "1 cage intersomatique TLIF"))
        self.radioButton_os2.setText(_translate("Frame", "Os seulement"))
        self.radioButton_aucuneGreffe2.setText(_translate("Frame", "Aucune"))
        self.radioButton_intersomatique.setText(_translate("Frame", "Cage intersomatique"))
        self.radioButton_corporectomie_2.setText(_translate("Frame", "Cage de corporectomie"))
        self.label_5.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Greffe</p></body></html>"))
        self.label_4.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Fixation</p></body></html>"))


class MainWindow_FormArthrodese(QtWidgets.QWidget, Ui_Frame_Arthrodese):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)



        # valeur des radiobuttons
        self.radioButton_anterieure.toggled.connect(self.radiobtnFrame_Haut_anterieur)
        self.radioButton_posterieure.toggled.connect(self.radiobtnFrame_Haut_posterieur)

        self.radioButton_monoaxiales.toggled.connect(self.radiobtn_monoaxiales)
        self.radioButton_polyaxiales.toggled.connect(self.radiobtn_polyaxiales)
        self.radioButton_aucune.toggled.connect(self.radiobtn_fixationAucune)

        self.radioButton_plaque_2.toggled.connect(self.radiobtn_plaque)
        self.radioButton_aucune2.toggled.connect(self.radiobtn_fixationAucunes2)

        self.radioButton_aucuneGreffe.toggled.connect(self.radiobtn_greffeAucune)
        self.radioButton_1plif.toggled.connect(self.radiobtn_1PLIF)
        self.radioButton_2plif.toggled.connect(self.radiobtn_2PLIF)
        self.radioButton_tlif.toggled.connect(self.radiobtn_TLIF)
        self.radioButton_os.toggled.connect(self.radiobtn_OsSeulement)

        self.radioButton_intersomatique.toggled.connect(self.radiobtn_intersomatique)
        self.radioButton_corporectomie_2.toggled.connect(self.radiobtn_corporectomie)
        self.radioButton_os2.toggled.connect(self.radiobtn_OsSeulement2)
        self.radioButton_aucuneGreffe2.toggled.connect(self.radiobtn_greffeAucune2)

        # controlleur pour les boutons
        self.pushButton_retour.clicked.connect(self.retourEtapePrecedente)
        self.pushButton_annuler.clicked.connect(self.annulerCreationDP)
        self.pushButton_suivant.clicked.connect(self.suivant) #Ne change pas d'interface mais récupère uniquement les valeurs pour lineedit de creationDP

    def retourEtapePrecedente(self):
        global validerArthrodese, annulerArthrodese
        validerArthrodese = False
        annulerArthrodese = False
        self.switch_window1.emit()

    def annulerCreationDP(self):
        global validerArthrodese, annulerArthrodese
        validerArthrodese = False
        annulerArthrodese = True
        self.switch_window2.emit()

    def radiobtnFrame_Haut_anterieur(self):
        global glb_arthrodese_posterieur, glb_arthrodese_anterieur
        global glb_arthro_postAnt
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_arthrodese_posterieur = False
            glb_arthrodese_anterieur = True
            self.frame_gauche1.setEnabled(False)
            self.frame_gauche2.setEnabled(False)
            self.frame_droite1.setEnabled(True)
            self.frame_droite2.setEnabled(False)
            self.radioButton_polyaxiales.setChecked(False)
            self.radioButton_monoaxiales.setChecked(False)
            self.radioButton_aucune.setChecked(False)
            self.radioButton_1plif.setChecked(False)
            self.radioButton_2plif.setChecked(False)
            self.radioButton_tlif.setChecked(False)
            self.radioButton_os.setChecked(False)
            self.radioButton_aucuneGreffe.setChecked(False)
            glb_arthro_postAnt = "Arthrodèse par voie antérieure"

    def radiobtnFrame_Haut_posterieur(self):
        global glb_arthrodese_posterieur, glb_arthrodese_anterieur
        global glb_arthro_postAnt
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_arthrodese_posterieur = True
            glb_arthrodese_anterieur = False
            self.frame_gauche1.setEnabled(True)
            self.frame_gauche2.setEnabled(False)
            self.frame_droite1.setEnabled(False)
            self.frame_droite2.setEnabled(False)
            self.radioButton_plaque_2.setChecked(False)
            self.radioButton_aucune2.setChecked(False)
            self.radioButton_intersomatique.setChecked(False)
            self.radioButton_corporectomie_2.setChecked(False)
            self.radioButton_os2.setChecked(False)
            self.radioButton_aucuneGreffe2.setChecked(False)
            glb_arthro_postAnt = "Arthrodèse par voie postérieure"

    def radiobtn_polyaxiales(self):
        global glb_arthrodese_polyaxiales, glb_arthrodese_monoaxiales, glb_arthrodese_fixationAucune
        global glb_arthro_fixation
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_arthrodese_polyaxiales = True
            glb_arthrodese_monoaxiales = False
            glb_arthrodese_fixationAucune = False
            self.frame_gauche2.setEnabled(True)
            glb_arthro_fixation = "par vis pédiculaires polyaxiales "

    def radiobtn_monoaxiales(self):
        global glb_arthrodese_polyaxiales, glb_arthrodese_monoaxiales, glb_arthrodese_fixationAucune
        self.radiobutton = self.sender()
        global glb_arthro_fixation
        if self.radiobutton.isChecked():
            glb_arthrodese_polyaxiales = False
            glb_arthrodese_monoaxiales = True
            glb_arthrodese_fixationAucune = False
            self.frame_gauche2.setEnabled(True)
            glb_arthro_fixation = "par vis pédiculaires monoaxiales "


    def radiobtn_fixationAucune(self):
        global glb_arthrodese_polyaxiales, glb_arthrodese_monoaxiales, glb_arthrodese_fixationAucune
        self.radiobutton = self.sender()
        global glb_arthro_fixation
        if self.radiobutton.isChecked():
            glb_arthrodese_polyaxiales = False
            glb_arthrodese_monoaxiales = False
            glb_arthrodese_fixationAucune = True
            self.frame_gauche2.setEnabled(True)
            glb_arthro_fixation = ""


    def radiobtn_plaque(self):
        global glb_arthrodese_plaque, glb_arthrodese_fixationAucune2
        self.radiobutton = self.sender()
        global glb_arthro_fixation
        if self.radiobutton.isChecked():
            glb_arthrodese_plaque = True
            glb_arthrodese_fixationAucune2 = False
            self.frame_droite2.setEnabled(True)
            glb_arthro_fixation = "avec plaque "

    def radiobtn_fixationAucunes2(self):
        global glb_arthrodese_plaque, glb_arthrodese_fixationAucune2
        self.radiobutton = self.sender()
        global glb_arthro_fixation
        if self.radiobutton.isChecked():
            glb_arthrodese_plaque = False
            glb_arthrodese_fixationAucune2 = True
            self.frame_droite2.setEnabled(True)
            glb_arthro_fixation = ""

    def radiobtn_2PLIF(self):
        global glb_arthrodese_2PLIF, glb_arthrodese_PLIF, glb_arthrodese_TLIF, glb_arthrodese_OsSeulement, glb_arthrodese_greffeAucune
        global glb_arthro_greffe
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_arthrodese_2PLIF = True
            glb_arthrodese_PLIF = False
            glb_arthrodese_TLIF = False
            glb_arthrodese_OsSeulement = False
            glb_arthrodese_greffeAucune = False
            self.pushButton_suivant.setEnabled(True)
            glb_arthro_greffe = "2 cages intersomatiques PLIF"

    def radiobtn_1PLIF(self):
        global glb_arthrodese_2PLIF, glb_arthrodese_PLIF, glb_arthrodese_TLIF, glb_arthrodese_OsSeulement, glb_arthrodese_greffeAucune
        global glb_arthro_greffe
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_arthrodese_2PLIF = False
            glb_arthrodese_PLIF = True
            glb_arthrodese_TLIF = False
            glb_arthrodese_OsSeulement = False
            glb_arthrodese_greffeAucune = False
            self.pushButton_suivant.setEnabled(True)
            glb_arthro_greffe = "1 cage intersomatique PLIF"

    def radiobtn_TLIF(self):
        global glb_arthrodese_2PLIF, glb_arthrodese_PLIF, glb_arthrodese_TLIF, glb_arthrodese_OsSeulement, glb_arthrodese_greffeAucune
        global glb_arthro_greffe
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_arthrodese_2PLIF = False
            glb_arthrodese_PLIF = False
            glb_arthrodese_TLIF = True
            glb_arthrodese_OsSeulement = False
            glb_arthrodese_greffeAucune = False
            self.pushButton_suivant.setEnabled(True)
            glb_arthro_greffe = "1 cage intersomatique TLIF"

    def radiobtn_OsSeulement(self):
        global glb_arthrodese_2PLIF, glb_arthrodese_PLIF, glb_arthrodese_TLIF, glb_arthrodese_OsSeulement, glb_arthrodese_greffeAucune
        global glb_arthro_greffe
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_arthrodese_2PLIF = False
            glb_arthrodese_PLIF = False
            glb_arthrodese_TLIF = False
            glb_arthrodese_OsSeulement = True
            glb_arthrodese_greffeAucune = False
            self.pushButton_suivant.setEnabled(True)
            glb_arthro_greffe = "Os seulement"

    def radiobtn_greffeAucune(self):
        global glb_arthrodese_2PLIF, glb_arthrodese_PLIF, glb_arthrodese_TLIF, glb_arthrodese_OsSeulement, glb_arthrodese_greffeAucune
        global glb_arthro_greffe
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_arthrodese_2PLIF = False
            glb_arthrodese_PLIF = False
            glb_arthrodese_TLIF = False
            glb_arthrodese_OsSeulement = False
            glb_arthrodese_greffeAucune = True
            self.pushButton_suivant.setEnabled(True)
            glb_arthro_greffe = ""

    def radiobtn_intersomatique(self):
        global glb_arthrodese_intersomatique, glb_arthrodese_corporectomie, glb_arthrodese_OsSeulement2, glb_arthrodese_greffeAucune2
        global glb_arthro_greffe
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_arthrodese_intersomatique = True
            glb_arthrodese_corporectomie = False
            glb_arthrodese_OsSeulement2 = False
            glb_arthrodese_greffeAucune2 = False
            self.pushButton_suivant.setEnabled(True)
            glb_arthro_greffe = "cage intersomatique"

    def radiobtn_corporectomie(self):
        global glb_arthrodese_intersomatique, glb_arthrodese_corporectomie, glb_arthrodese_OsSeulement2, glb_arthrodese_greffeAucune2
        global glb_arthro_greffe
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_arthrodese_intersomatique = False
            glb_arthrodese_corporectomie = True
            glb_arthrodese_OsSeulement2 = False
            glb_arthrodese_greffeAucune2 = False
            self.pushButton_suivant.setEnabled(True)
            glb_arthro_greffe = "cage de corporectomie"

    def radiobtn_OsSeulement2(self):
        global glb_arthrodese_intersomatique, glb_arthrodese_corporectomie, glb_arthrodese_OsSeulement2, glb_arthrodese_greffeAucune2
        global glb_arthro_greffe
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_arthrodese_intersomatique = False
            glb_arthrodese_corporectomie = False
            glb_arthrodese_OsSeulement2 = True
            glb_arthrodese_greffeAucune2 = False
            self.pushButton_suivant.setEnabled(True)
            glb_arthro_greffe = "Os seulement"

    def radiobtn_greffeAucune2(self):
        global glb_arthrodese_intersomatique, glb_arthrodese_corporectomie, glb_arthrodese_OsSeulement2, glb_arthrodese_greffeAucune2
        global glb_arthro_greffe
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_arthrodese_intersomatique = False
            glb_arthrodese_corporectomie = False
            glb_arthrodese_OsSeulement2 = False
            glb_arthrodese_greffeAucune2 = True
            self.pushButton_suivant.setEnabled(True)
            glb_arthro_greffe = ""


    def suivant(self):
        global validerArthrodese, annulerArthrodese
        global glb_arthrodese_posterieur, glb_arthrodese_anterieur
        global glb_arthrodese_polyaxiales, glb_arthrodese_monoaxiales, glb_arthrodese_fixationAucune
        global glb_arthrodese_plaque, glb_arthrodese_fixationAucune2
        global glb_arthrodese_2PLIF, glb_arthrodese_PLIF, glb_arthrodese_TLIF, glb_arthrodese_OsSeulement, glb_arthrodese_greffeAucune
        global glb_arthrodese_intersomatique, glb_arthrodese_corporectomie, glb_arthrodese_OsSeulement2, glb_arthrodese_greffeAucune2

        glb_arthrodese_posterieur = False
        glb_arthrodese_anterieur = False
        glb_arthrodese_polyaxiales = False
        glb_arthrodese_monoaxiales = False
        glb_arthrodese_plaque = False
        glb_arthrodese_fixationAucune = False
        glb_arthrodese_fixationAucune2 = False
        glb_arthrodese_2PLIF = False
        glb_arthrodese_PLIF = False
        glb_arthrodese_TLIF = False
        glb_arthrodese_OsSeulement = False
        glb_arthrodese_greffeAucune = False
        glb_arthrodese_intersomatique = False
        glb_arthrodese_corporectomie = False
        glb_arthrodese_OsSeulement2 = False
        glb_arthrodese_greffeAucune2 = False

        validerArthrodese = True
        annulerArthrodese = False
        self.switch_window3.emit() #faute de mieux