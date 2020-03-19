# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accueil_Medecin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox



class Ui_Frame_Medecin(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(527, 545)
        self.pushButton_creerDP = QtWidgets.QPushButton(Frame)
        self.pushButton_creerDP.setGeometry(QtCore.QRect(89, 160, 321, 30))
        self.pushButton_creerDP.setObjectName("pushButton_creerDP")
        self.pushButton_selectionnerDP = QtWidgets.QPushButton(Frame)
        self.pushButton_selectionnerDP.setGeometry(QtCore.QRect(90, 220, 321, 30))
        self.pushButton_selectionnerDP.setObjectName("pushButton_selectionnerDP")
        self.pushButton_modifierVariables = QtWidgets.QPushButton(Frame)
        self.pushButton_modifierVariables.setGeometry(QtCore.QRect(90, 280, 321, 30))
        self.pushButton_modifierVariables.setObjectName("pushButton_modifierVariables")
        self.pushButton_excel = QtWidgets.QPushButton(Frame)
        self.pushButton_excel.setGeometry(QtCore.QRect(90, 340, 321, 30))
        self.pushButton_excel.setObjectName("pushButton_excel")
        self.pushButton_deconnexion = QtWidgets.QPushButton(Frame)
        self.pushButton_deconnexion.setGeometry(QtCore.QRect(350, 60, 150, 30))
        self.pushButton_deconnexion.setObjectName("pushButton_deconnexion")
        self.pushButton_notification = QtWidgets.QPushButton(Frame)
        self.pushButton_notification.setGeometry(QtCore.QRect(30, 60, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_notification.setFont(font)
        self.pushButton_notification.setObjectName("pushButton_notification")


        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_creerDP.setText(_translate("Frame", "Créer Dossier Patient"))
        self.pushButton_deconnexion.setText(_translate("Frame", "Déconnexion"))
        self.pushButton_notification.setText(_translate("Frame", "!"))
        self.pushButton_excel.setText(_translate("Frame", "Excel"))
        self.pushButton_selectionnerDP.setText(_translate("Frame", "Sélectionner Dossier Patient déjà existant"))
        self.pushButton_modifierVariables.setText(_translate("Frame", "Modifier Variables"))


class MainWindow_Acceuil(QtWidgets.QWidget, Ui_Frame_Medecin):

    #creer les var pour chaque bouton
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()




    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)


        #controlleur pour les boutons
        self.pushButton_creerDP.clicked.connect(self.tablette_et_creationDP)
        self.pushButton_deconnexion.clicked.connect(self.deconnexion)


    #les actions de chaque bouton
    def tablette_et_creationDP(self):
        # os.system("C:/Users/Public/InPec/adb/adb pull sdcard/Documents/DonneestransfereesAndroid.txt C:/Users/Public/InPec/DonneestransfereesAndroid.txt")
        # liste = []
        # with open("C:/Users/Public/InPec/DonneestransfereesAndroid.txt", "r") as f:
        #     for line in f.readlines():
        #         # Traiter la ligne et ainsi de suite ...
        #         ligne = line.strip()
        #         liste.append(ligne)
        #     print(liste)
        self.switch_window1.emit()

    def deconnexion(self):
        msg = QMessageBox()
        msg.setWindowTitle("Attention")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setText("Etes-vous sûr de vouloir vous déconnecter? ")
        msg.buttonClicked.connect(self.popup_clicked)
        x = msg.exec_()

    def popup_clicked(self):
        self.switch_window5.emit()
