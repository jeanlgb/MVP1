# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accueil_Medecin.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame_Medecin(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(573, 348)
        self.pushButton_creerDP = QtWidgets.QPushButton(Frame)
        self.pushButton_creerDP.setGeometry(QtCore.QRect(180, 160, 150, 30))
        self.pushButton_creerDP.setObjectName("pushButton_creerDP")
        self.pushButton_recuperer = QtWidgets.QPushButton(Frame)
        self.pushButton_recuperer.setGeometry(QtCore.QRect(180, 220, 150, 30))
        self.pushButton_recuperer.setObjectName("pushButton_recuperer")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_creerDP.setText(_translate("Frame", "Créer DP"))
        self.pushButton_recuperer.setText(_translate("Frame", "Récupérer tablette"))


class MainWindow_Acceuil(QtWidgets.QWidget, Ui_Frame_Medecin):

    #creer les var pour chaque bouton
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()



    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        #controlleur pour les boutons
        self.pushButton_creerDP.clicked.connect(self.creation)
        self.pushButton_recuperer.clicked.connect(self.tablette)


    #les actions de chaque bouton
    def creation(self):
        self.switch_window1.emit()

    def tablette(self):
        self.switch_window2.emit()

