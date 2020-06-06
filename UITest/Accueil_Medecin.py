# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accueil_Medecin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# variables globales appelées dans controller_test
signal_med_selectionDP = False
signal_med_creationDP = False

class Ui_Frame_Medecin(object):
    # Interface générée automatiquement via qtdesigner ==> def setupUi et def retranslateUI
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


# class à créer
class MainWindow_Acceuil(QtWidgets.QWidget, Ui_Frame_Medecin):

    # Pour accueil Médecin Variables qui permettent de switcher entre les interfaces pour chaque bouton.
    # Les switch sont utilisés également dans la classe Controller_Test
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
        self.pushButton_selectionnerDP.clicked.connect(self.selectionnerDP)
        self.pushButton_deconnexion.clicked.connect(self.deconnexion)


    #les actions de chaque bouton
    # Methode qui permet d'aller dans l'interface CréationDP
    def tablette_et_creationDP(self):
        global signal_med_creationDP, signal_med_selectionDP
        signal_med_creationDP = True
        signal_med_selectionDP = False
        self.switch_window1.emit()

    # Methode qui permet d'aller dans l'interface SélectionnerDP
    def selectionnerDP(self):
        global signal_med_creationDP, signal_med_selectionDP
        signal_med_creationDP = False
        signal_med_selectionDP = True
        self.switch_window2.emit()

    # Methode qui permet de se déconnecter
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
