import os
import random
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QCheckBox
from PyQt5.QtCore import Qt
import time

class Ui_Frame_Evaluation(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(638, 620)
        self.checkBox_oswestry = QtWidgets.QCheckBox(Frame)
        self.checkBox_oswestry.setGeometry(QtCore.QRect(259, 420, 171, 25))
        self.checkBox_oswestry.setObjectName("checkBox_oswestry")
        self.label_identite = QtWidgets.QLabel(Frame)
        self.label_identite.setGeometry(QtCore.QRect(0, 120, 151, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_identite.setFont(font)
        self.label_identite.setObjectName("label_identite")
        self.lineEdit_identite = QtWidgets.QLineEdit(Frame)
        self.lineEdit_identite.setGeometry(QtCore.QRect(150, 125, 271, 20))
        self.lineEdit_identite.setObjectName("lineEdit_identite")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(90, 330, 161, 20))
        self.label.setObjectName("label")
        self.checkBox_glassman = QtWidgets.QCheckBox(Frame)
        self.checkBox_glassman.setGeometry(QtCore.QRect(259, 390, 171, 25))
        self.checkBox_glassman.setObjectName("checkBox_glassman")
        self.label_typeEvaluation = QtWidgets.QLabel(Frame)
        self.label_typeEvaluation.setGeometry(QtCore.QRect(0, 390, 271, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_typeEvaluation.setFont(font)
        self.label_typeEvaluation.setObjectName("label_typeEvaluation")
        self.pushButton_demarrer = QtWidgets.QPushButton(Frame)
        self.pushButton_demarrer.setGeometry(QtCore.QRect(260, 510, 80, 30))
        self.pushButton_demarrer.setObjectName("pushButton_demarrer")
        self.lineEdit_calculPost = QtWidgets.QLineEdit(Frame)
        self.lineEdit_calculPost.setEnabled(False)
        self.lineEdit_calculPost.setGeometry(QtCore.QRect(260, 325, 50, 30))
        self.lineEdit_calculPost.setObjectName("lineEdit_calculPost")
        self.lineEdit_numeroMagic_2 = QtWidgets.QLineEdit(Frame)
        self.lineEdit_numeroMagic_2.setGeometry(QtCore.QRect(430, 125, 160, 20))
        self.lineEdit_numeroMagic_2.setObjectName("lineEdit_numeroMagic_2")
        self.lineEdit_dateIntervention = QtWidgets.QLineEdit(Frame)
        self.lineEdit_dateIntervention.setGeometry(QtCore.QRect(260, 185, 162, 20))
        self.lineEdit_dateIntervention.setObjectName("dateEdit_dateIntervention")
        self.checkBox_ndi = QtWidgets.QCheckBox(Frame)
        self.checkBox_ndi.setGeometry(QtCore.QRect(440, 420, 171, 25))
        self.checkBox_ndi.setObjectName("checkBox_ndi")
        self.radioButton_postOp = QtWidgets.QRadioButton(Frame)
        self.radioButton_postOp.setGeometry(QtCore.QRect(260, 280, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_postOp.setFont(font)
        self.radioButton_postOp.setObjectName("radioButton_postOp")
        self.label_tempsEvaluation = QtWidgets.QLabel(Frame)
        self.label_tempsEvaluation.setGeometry(QtCore.QRect(-1, 240, 261, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_tempsEvaluation.setFont(font)
        self.label_tempsEvaluation.setObjectName("label_tempsEvaluation")
        self.label_dateIntervention = QtWidgets.QLabel(Frame)
        self.label_dateIntervention.setGeometry(QtCore.QRect(0, 180, 261, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_dateIntervention.setFont(font)
        self.label_dateIntervention.setObjectName("label_dateIntervention")
        self.label_titre = QtWidgets.QLabel(Frame)
        self.label_titre.setGeometry(QtCore.QRect(10, 10, 601, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_titre.setFont(font)
        self.label_titre.setObjectName("label_titre")
        self.checkBox_evaCervical = QtWidgets.QCheckBox(Frame)
        self.checkBox_evaCervical.setGeometry(QtCore.QRect(440, 390, 171, 25))
        self.checkBox_evaCervical.setObjectName("checkBox_evaCervical")
        self.radioButton_preOp = QtWidgets.QRadioButton(Frame)
        self.radioButton_preOp.setGeometry(QtCore.QRect(260, 240, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_preOp.setFont(font)
        self.radioButton_preOp.setObjectName("radioButton_preOp")
        self.checkBox_mjoa = QtWidgets.QCheckBox(Frame)
        self.checkBox_mjoa.setGeometry(QtCore.QRect(440, 450, 171, 25))
        self.checkBox_mjoa.setObjectName("checkBox_mjoa")
        self.checkBox_evaLombaire = QtWidgets.QCheckBox(Frame)
        self.checkBox_evaLombaire.setGeometry(QtCore.QRect(260, 450, 171, 25))
        self.checkBox_evaLombaire.setObjectName("checkBox_evaLombaire")
        self.label_titre.raise_()
        self.label_typeEvaluation.raise_()
        self.checkBox_oswestry.raise_()
        self.label_identite.raise_()
        self.lineEdit_identite.raise_()
        self.label.raise_()
        self.checkBox_glassman.raise_()
        self.pushButton_demarrer.raise_()
        self.lineEdit_calculPost.raise_()
        self.lineEdit_numeroMagic_2.raise_()
        self.lineEdit_dateIntervention.raise_()
        self.checkBox_ndi.raise_()
        self.radioButton_postOp.raise_()
        self.label_tempsEvaluation.raise_()
        self.label_dateIntervention.raise_()
        self.checkBox_evaCervical.raise_()
        self.radioButton_preOp.raise_()
        self.checkBox_mjoa.raise_()
        self.checkBox_evaLombaire.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)


    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.checkBox_oswestry.setText(_translate("Frame", "Score d’Oswestry"))
        self.label_identite.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Identité :</p></body></html>"))
        self.label.setText(_translate("Frame", "Calcul post-opération :"))
        self.checkBox_glassman.setText(_translate("Frame", "Score de Glassman"))
        self.label_typeEvaluation.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Type de l\'évaluation :</p></body></html>"))
        self.pushButton_demarrer.setText(_translate("Frame", "Démarrer"))
        self.checkBox_ndi.setText(_translate("Frame", "Score NDI"))
        self.radioButton_postOp.setText(_translate("Frame", "Post-opératoire"))
        self.label_tempsEvaluation.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Temps de l\'évaluation :</p></body></html>"))
        self.label_dateIntervention.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Date de l\'intervention :</p></body></html>"))
        self.label_titre.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Type d\'évaluation</p></body></html>"))
        self.checkBox_evaCervical.setText(_translate("Frame", "Score EVA cervical"))
        self.radioButton_preOp.setText(_translate("Frame", "Pré-opératoire"))
        self.checkBox_mjoa.setText(_translate("Frame", "Score mJOA"))
        self.checkBox_evaLombaire.setText(_translate("Frame", "Score EVA lombaire"))

        # self.lineEdit_identite.setText(_translate("Frame", self.nom + " " + self.prenom))


class MainWindow_Evaluation(QtWidgets.QWidget, Ui_Frame_Evaluation):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):

        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)


        # récupération des valeurs des checkbox
        self.checkBox_glassman.stateChanged.connect(self.checkBoxChangeAction_glassman)
        self.state_glassman = "false"
        self.checkBox_evaCervical.stateChanged.connect(self.checkBoxChangeAction_EVAC)
        self.state_EVAC = "false"
        self.checkBox_evaLombaire.stateChanged.connect(self.checkBoxChangeAction_EVAL)
        self.state_EVAL = "false"
        self.checkBox_ndi.stateChanged.connect(self.checkBoxChangeAction_NDI)
        self.state_ndi = "false"
        self.checkBox_mjoa.stateChanged.connect(self.checkBoxChangeAction_MJOA)
        self.state_mjoa = "false"
        self.checkBox_oswestry.stateChanged.connect(self.checkBoxChangeAction_Oswestry)
        self.state_oswestry = "false"



        self.pushButton_demarrer.clicked.connect(self.popup)
        self.pushButton_demarrer.clicked.connect(self.transfert)


    def checkBoxChangeAction_glassman (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
            self.state_glassman = "true"
        else:
            print ("unchecked")
            self.state_glassman = "false"

    def checkBoxChangeAction_EVAC (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
            self.state_EVAC = "true"
        else:
            print ("unchecked")
            self.state_EVAC = "false"

    def checkBoxChangeAction_EVAL (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
            self.state_EVAL = "true"
        else:
            print ("unchecked")
            self.state_EVAL = "false"

    def checkBoxChangeAction_NDI (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
            self.state_ndi = "true"
        else:
            print ("unchecked")
            self.state_ndi = "false"

    def checkBoxChangeAction_MJOA (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
            self.state_mjoa = "true"
        else:
            print ("unchecked")
            self.state_mjoa = "false"

    def checkBoxChangeAction_Oswestry (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
            self.state_oswestry = "true"
        else:
            print ("unchecked")
            self.state_oswestry = "false"


    def transfert(self):
        self.identite = self.lineEdit_identite.text()
        self.numMagic = self.lineEdit_numeroMagic_2.text()
        dictionnaire_données = dict()
        dictionnaire_données = {'Nom et Prénom': self.identite, 'scoreGlassman': self.state_glassman, 'scoreEVAC': self.state_EVAC,
                                'scoreEVAL': self.state_EVAL, 'scoreNDI': self.state_ndi, 'scoreMJOA': self.state_mjoa , 'scoreOswestry': self.state_oswestry }
        f = open('C:/Users/Public/Ecrire/Donneestransferees.txt', 'w')
        f.write(str(dictionnaire_données.get('Nom et Prénom')) + '\n' + str(
            dictionnaire_données.get('scoreGlassman')) + '\n' + str(dictionnaire_données.get('scoreEVAC')) + '\n' + str(
            dictionnaire_données.get('scoreEVAL')) + '\n' + str(dictionnaire_données.get('scoreNDI')) + '\n' + str(
            dictionnaire_données.get('scoreMJOA')) + '\n' + str(dictionnaire_données.get('scoreOswestry')))
        f.close()
        os.system("C:/Users/Jean-Loup/Desktop/PFE/adb/adb push C:/Users/Public/Ecrire/Donneestransferees.txt sdcard/Documents/Donneestransferees.txt")

        if os.path.getsize("C:/Users/Public/Ecrire/FichierDeTransfert.txt") == 0:
            print("Vide")  # Récupération du fichier texte
        else:
            print("Rempli")
        self.switch_window.emit()

    def popup (self):
        # start = time.time()  # Début du timer
        # while time.time() - start < 5:  # Attendre 5 sec. Pour attendre 20 minutes, remplacer par 1200
        #     print("Temps pas écoulé")
        #
        # print("Temps écoulé")

        msg = QMessageBox()
        msg.setWindowTitle("Attention")
        msg.setText("Les données n'ont pas encore été récupées")
        x = msg.exec_()
