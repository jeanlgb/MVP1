# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SelectionnerDP.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(722, 501)
        self.label_numeroMagic = QtWidgets.QLabel(Frame)
        self.label_numeroMagic.setGeometry(QtCore.QRect(20, 190, 331, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_numeroMagic.setFont(font)
        self.label_numeroMagic.setObjectName("label_numeroMagic")
        self.pushButton_annuler = QtWidgets.QPushButton(Frame)
        self.pushButton_annuler.setGeometry(QtCore.QRect(35, 30, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_annuler.setFont(font)
        self.pushButton_annuler.setObjectName("pushButton_annuler")
        self.label_titre = QtWidgets.QLabel(Frame)
        self.label_titre.setGeometry(QtCore.QRect(50, 70, 611, 91))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_titre.setFont(font)
        self.label_titre.setObjectName("label_titre")
        self.lineEdit_numeroMagic = QtWidgets.QLineEdit(Frame)
        self.lineEdit_numeroMagic.setGeometry(QtCore.QRect(290, 190, 301, 20))
        self.lineEdit_numeroMagic.setObjectName("lineEdit_numeroMagic")
        self.lineEdit_nom = QtWidgets.QLineEdit(Frame)
        self.lineEdit_nom.setGeometry(QtCore.QRect(290, 240, 301, 20))
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.label_nom = QtWidgets.QLabel(Frame)
        self.label_nom.setGeometry(QtCore.QRect(190, 240, 101, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_nom.setFont(font)
        self.label_nom.setObjectName("label_nom")
        self.lineEdit_prenom = QtWidgets.QLineEdit(Frame)
        self.lineEdit_prenom.setGeometry(QtCore.QRect(290, 290, 301, 20))
        self.lineEdit_prenom.setObjectName("lineEdit_prenom")
        self.label_prenom = QtWidgets.QLabel(Frame)
        self.label_prenom.setGeometry(QtCore.QRect(160, 290, 131, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_prenom.setFont(font)
        self.label_prenom.setObjectName("label_prenom")
        self.pushButton_recherche = QtWidgets.QPushButton(Frame)
        self.pushButton_recherche.setGeometry(QtCore.QRect(300, 370, 80, 30))
        self.pushButton_recherche.setObjectName("pushButton_recherche")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_numeroMagic.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Numéro MagicMed :</p></body></html>"))
        self.pushButton_annuler.setText(_translate("Frame", "Annuler"))
        self.label_titre.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Sélectionner un dossier patient</p></body></html>"))
        self.label_nom.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Nom :</p></body></html>"))
        self.label_prenom.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Prénom :</p></body></html>"))
        self.pushButton_recherche.setText(_translate("Frame", "Suivant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
