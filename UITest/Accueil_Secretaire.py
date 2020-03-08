# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accueil_Secretaire.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Frame_Secretaire(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(575, 471)
        self.pushButton_creerDP = QtWidgets.QPushButton(Frame)
        self.pushButton_creerDP.setGeometry(QtCore.QRect(130, 220, 281, 30))
        self.pushButton_creerDP.setObjectName("pushButton_creerDP")
        self.pushButton_selectionnerDP = QtWidgets.QPushButton(Frame)
        self.pushButton_selectionnerDP.setGeometry(QtCore.QRect(129, 310, 281, 30))
        self.pushButton_selectionnerDP.setObjectName("pushButton_selectionnerDP")
        self.label_titre = QtWidgets.QLabel(Frame)
        self.label_titre.setGeometry(QtCore.QRect(30, 20, 161, 51))
        self.label_titre.setObjectName("label_titre")
        self.pushButton_notification = QtWidgets.QPushButton(Frame)
        self.pushButton_notification.setGeometry(QtCore.QRect(90, 90, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_notification.setFont(font)
        self.pushButton_notification.setObjectName("pushButton_notification")
        self.pushButton_deconnexion = QtWidgets.QPushButton(Frame)
        self.pushButton_deconnexion.setGeometry(QtCore.QRect(360, 90, 121, 30))
        self.pushButton_deconnexion.setObjectName("pushButton_deconnexion")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_creerDP.setText(_translate("Frame", "Créer Dossier Patient"))
        self.label_titre.setText(_translate("Frame", "Accueil Secrétaire"))
        self.pushButton_notification.setText(_translate("Frame", "!"))
        self.pushButton_selectionnerDP.setText(_translate("Frame", "Sélectionner Dossier Patient déjà existant"))
        self.pushButton_deconnexion.setText(_translate("Frame", "Déconnexion"))


class MainWindow_Acceuil_Secretaire(QtWidgets.QWidget, Ui_Frame_Secretaire):

    #creer les var pour chaque bouton
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()



    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        #controlleur pour les boutons
        self.pushButton_creerDP.clicked.connect(self.creation)
        self.pushButton_notification.clicked.connect(self.tablette)
        self.pushButton_deconnexion.clicked.connect(self.deconnexion)


    #les actions de chaque bouton
    def creation(self):
        self.switch_window1.emit()

    def tablette(self):
        os.system(
            "C:/Users/Public/InPec/adb/adb pull sdcard/Documents/DonneestransfereesAndroid.txt C:/Users/Public/InPec/DonneestransfereesAndroid.txt")
        liste = []
        with open("C:/Users/Public/InPec/DonneestransfereesAndroid.txt", "r") as f:
            for line in f.readlines():
                # Traiter la ligne et ainsi de suite ...
                ligne = line.strip()
                liste.append(ligne)
            print(liste)

    def deconnexion(self):
        msg = QMessageBox()
        msg.setWindowTitle("Attention")
        msg.setText("Etes-vous sûr de vouloir vous déconnecter? ")
        x = msg.exec_()
        self.switch_window3.emit()