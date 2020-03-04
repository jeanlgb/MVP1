# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accueil_Secretaire.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame_Secretaire(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(677, 587)
        self.pushButton_creerDP = QtWidgets.QPushButton(Frame)
        self.pushButton_creerDP.setGeometry(QtCore.QRect(270, 230, 150, 30))
        self.pushButton_creerDP.setObjectName("pushButton_creerDP")
        self.pushButton_selectionnerDP = QtWidgets.QPushButton(Frame)
        self.pushButton_selectionnerDP.setGeometry(QtCore.QRect(270, 330, 150, 30))
        self.pushButton_selectionnerDP.setObjectName("pushButton_selectionnerDP")
        self.label_titre = QtWidgets.QLabel(Frame)
        self.label_titre.setGeometry(QtCore.QRect(30, 20, 161, 51))
        self.label_titre.setObjectName("label_titre")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_creerDP.setText(_translate("Frame", "Créer DP"))
        self.pushButton_selectionnerDP.setText(_translate("Frame", "Récupérer tablette"))
        self.label_titre.setText(_translate("Frame", "Accueil Secrétaire"))


class MainWindow_Acceuil_Secretaire(QtWidgets.QWidget, Ui_Frame_Secretaire):

    #creer les var pour chaque bouton
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()



    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        #controlleur pour les boutons
        self.pushButton_creerDP.clicked.connect(self.creation)
        self.pushButton_selectionnerDP.clicked.connect(self.tablette)


    #les actions de chaque bouton
    def creation(self):
        self.switch_window1.emit()

    def tablette(self):
        self.switch_window2.emit()
