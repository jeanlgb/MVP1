from PyQt5 import QtCore, QtGui, QtWidgets
import sys


from UITest.Accueil_Medecin import MainWindow_Acceuil
from UITest.CreationDP import MainWindow_CreationDP
from UITest.Evaluation import MainWindow_Evaluation
from UITest.Accueil_Secretaire import MainWindow_Acceuil_Secretaire
from UITest.Connexion import Login
from UITest.CreationDP import *

class Controller_Test:

    def __init__(self):
        pass

    def show_Connexion(self):
        self.co = Login()
        self.co.switch_window1.connect(self.show_Medecin)
        self.co.switch_window2.connect(self.show_Secretaire)
        self.co.show()

    def show_Medecin(self):
        self.med = MainWindow_Acceuil()
        self.med.switch_window1.connect(self.show_CreationDP)
        # self.med.switch_window2.connect(self.show_)
        self.co.hide()
        self.med.show()

    def show_Secretaire(self):
        self.co = Login()
        self.sec = MainWindow_Acceuil_Secretaire()
        self.sec.switch_window1.connect(self.show_CreationDP)
        # self.sec.switch_window2.connect(self.show_)
        self.co.hide()
        self.sec.show()


    def show_CreationDP(self):
        self.sec = MainWindow_Acceuil_Secretaire()
        self.med = MainWindow_Acceuil()
        self.windowCreationDP = MainWindow_CreationDP()

        #actions de chaque bouton en fct du window
        self.windowCreationDP.switch_window.connect(self.show_Evaluation)
        self.med.hide()
        self.sec.hide()
        self.windowCreationDP.show()

    def show_Evaluation(self):
        self.nom = UITest.CreationDP.patient_nom
        self.prenom = UITest.CreationDP.patient_prenom
        self.numMagic = UITest.CreationDP.patient_numMagic
        self.dateDeIntervention = UITest.CreationDP.patient_dateIntervention

        self.windowEvaluation = MainWindow_Evaluation()
        self.windowCreationDP = MainWindow_CreationDP()

        self.windowEvaluation.switch_window.connect(self.show_Medecin)

        self.windowEvaluation.lineEdit_identite.setText(self.nom + ' ' + self.prenom)
        self.windowEvaluation.lineEdit_numeroMagic_2.setText(self.numMagic)
        self.windowEvaluation.lineEdit_dateIntervention.setText(self.dateDeIntervention)


        self.windowCreationDP.hide()
        self.windowEvaluation.show()



def main():
    app = QtWidgets.QApplication(sys.argv)
    controller_INPEC2 = Controller_Test()
    controller_INPEC2.show_CreationDP()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()