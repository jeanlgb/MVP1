from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


from Utilisateur import *
import keyboard
signal_medecin = True
signal_secretaire = True

class Ui_Frame_Connexion(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(626, 545)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_logo = QtWidgets.QLabel(Frame)
        self.label_logo.setEnabled(True)
        self.label_logo.setGeometry(QtCore.QRect(0, 90, 621, 151))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.label_logo.setFont(font)
        self.label_logo.setObjectName("label_logo")
        self.label_utilisateur = QtWidgets.QLabel(Frame)
        self.label_utilisateur.setGeometry(QtCore.QRect(110, 285, 161, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_utilisateur.setFont(font)
        self.label_utilisateur.setObjectName("label_utilisateur")
        self.lineEdit_utilisateur = QtWidgets.QLineEdit(Frame)
        self.lineEdit_utilisateur.setGeometry(QtCore.QRect(280, 290, 170, 20))
        self.lineEdit_utilisateur.setObjectName("lineEdit_utilisateur")
        self.label_mdp = QtWidgets.QLabel(Frame)
        self.label_mdp.setGeometry(QtCore.QRect(90, 335, 181, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_mdp.setFont(font)
        self.label_mdp.setObjectName("label_mdp")
        self.lineEdit_mdp = QtWidgets.QLineEdit(Frame)
        self.lineEdit_mdp.setGeometry(QtCore.QRect(280, 340, 170, 20))
        self.lineEdit_mdp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_mdp.setObjectName("lineEdit_mdp")
        self.pushButton_connexion = QtWidgets.QPushButton(Frame)
        self.pushButton_connexion.setGeometry(QtCore.QRect(480, 400, 75, 30))
        self.pushButton_connexion.setObjectName("pushButton_connexion")
        self.pushButton_mdpOublie = QtWidgets.QPushButton(Frame)
        self.pushButton_mdpOublie.setEnabled(False)
        self.pushButton_mdpOublie.setGeometry(QtCore.QRect(310, 370, 101, 16))
        self.pushButton_mdpOublie.setMaximumSize(QtCore.QSize(101, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_mdpOublie.setFont(font)
        self.pushButton_mdpOublie.setObjectName("pushButton_mdpOublie")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_logo.setText(_translate("Frame", "<html><head/><body><p align=\"center\">IN PEC</p></body></html>"))
        self.label_utilisateur.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Utilisateur :</p></body></html>"))
        self.label_mdp.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Mot de passe :</p></body></html>"))
        self.pushButton_connexion.setText(_translate("Frame", "Connexion"))
        self.pushButton_mdpOublie.setText(_translate("Frame", "Mot de passe oublié ?"))


class Login(QtWidgets.QWidget, Ui_Frame_Connexion):

    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)

        self.pushButton_connexion.clicked.connect(self.seConnecter)

    def keyPressEvent(self, QKeyEvent):
        self.seConnecter()

    def seConnecter(self):
        global signal_secretaire
        global signal_medecin

        self.nom = self.lineEdit_utilisateur.text()
        self.mdp = self.lineEdit_mdp.text()
        self.medecin = QtWidgets.QMainWindow()
        self.secretaire = QtWidgets.QMainWindow()
        for i in listeUtilisateurs:
           if self.nom == Utilisateur.get_nom(i) and self.mdp == Utilisateur.get_mdp(i) and Utilisateur.get_type(
                   i) == 'Medecin':
               signal_medecin = True
               signal_secretaire = False


               self.switch_window1.emit()

           if self.nom == Utilisateur.get_nom(i) and self.mdp == Utilisateur.get_mdp(i) and Utilisateur.get_type(
                   i) == 'Secretaire':
                signal_medecin = False
                signal_secretaire = True

                self.switch_window2.emit()

