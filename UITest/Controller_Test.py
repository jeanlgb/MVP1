from PyQt5 import QtCore, QtGui, QtWidgets
import sys


from UITest.Accueil_Medecin import MainWindow_Acceuil
from UITest.CreationDP import MainWindow_CreationDP
from UITest.Evaluation import MainWindow_Evaluation
from UITest.Accueil_Secretaire import MainWindow_Acceuil_Secretaire
from UITest.Connexion import Login
from UITest.CreationDP import *
from UITest.Pathologie_Etape2 import MainWindow_Etape2
from UITest.Pathologie_Degeneratif import MainWindow_Degeneratif
from UITest.Pathologie_Oncologie import MainWindow_Oncologie
from UITest.Formulaire_Arthrodese import MainWindow_FormArthrodese
from UITest.Formulaire_Recalibrage import MainWindow_FormRecalibrage

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
        self.etape2 = MainWindow_Etape2()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowCreationDP = MainWindow_CreationDP()

        #actions de chaque bouton en fct du window
        self.windowCreationDP.switch_window1.connect(self.show_Evaluation)
        self.windowCreationDP.switch_window2.connect(self.show_Etape2)

        self.med.hide()
        self.sec.hide()
        self.etape2.hide()

        self.windowDegeneratif.hide()
        self.windowOncologique.hide()
        self.windowCreationDP.show()

    def show_Evaluation(self):
        self.nom = UITest.CreationDP.patient_nom
        self.prenom = UITest.CreationDP.patient_prenom
        self.numMagic = UITest.CreationDP.patient_numMagic
        self.dateDeIntervention = UITest.CreationDP.patient_dateIntervention
        self.dateDeNaissance = UITest.CreationDP.patient_dateNaissance

        self.windowEvaluation = MainWindow_Evaluation()
        self.windowCreationDP = MainWindow_CreationDP()

        self.windowEvaluation.switch_window.connect(self.show_Medecin)

        self.windowEvaluation.lineEdit_identite.setText(self.nom + ' ' + self.prenom)
        self.windowEvaluation.lineEdit_numeroMagic_2.setText(self.numMagic)
        self.windowEvaluation.lineEdit_dateIntervention.setText(self.dateDeIntervention)
        self.windowEvaluation.label_recuperationDateDeNaissance.setText(self.dateDeNaissance)


        self.windowCreationDP.hide()
        self.windowEvaluation.show()

    def show_Etape2(self):
        self.windowCreationDP = MainWindow_CreationDP()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.etape2 = MainWindow_Etape2()

        #actions de chaque bouton en fct du window
        self.etape2.switch_window1.connect(self.show_Degeneratif)
        self.etape2.switch_window2.connect(self.show_Secretaire)
        self.etape2.switch_window3.connect(self.show_Oncologique)

        self.etape2.switch_window4.connect(self.show_CreationDP)

        self.windowDegeneratif.hide()
        self.windowOncologique.hide()
        self.etape2.show()

    def show_Degeneratif(self):
        self.windowCreationDP = MainWindow_CreationDP()
        self.etape2 = MainWindow_Etape2()
        self.windowRecalibrage = MainWindow_FormRecalibrage()
        self.windowArthrodese = MainWindow_FormArthrodese()
        self.windowDegeneratif = MainWindow_Degeneratif()

        # actions de chaque bouton en fct du window
        self.windowDegeneratif.switch_window1.connect(self.show_Etape2)
        self.windowDegeneratif.switch_window2.connect(self.show_CreationDP)
        self.windowDegeneratif.switch_window3.connect(self.show_Recalibrage)
        self.windowDegeneratif.switch_window4.connect(self.show_Arthrodese)
        self.windowDegeneratif.switch_window5.connect(self.show_Etape2)
        self.windowDegeneratif.switch_window6.connect(self.show_CreationDP)

        self.etape2.hide()
        self.windowRecalibrage.hide()
        self.windowArthrodese.hide()
        self.windowDegeneratif.show()

    def show_Oncologique(self):
        self.windowCreationDP = MainWindow_CreationDP()
        self.etape2 = MainWindow_Etape2()
        self.windowRecalibrage = MainWindow_FormRecalibrage()
        self.windowArthrodese = MainWindow_FormArthrodese()
        self.windowOncologique = MainWindow_Oncologie()

        # actions de chaque bouton en fct du window
        self.windowOncologique.switch_window1.connect(self.show_Etape2)
        self.windowOncologique.switch_window2.connect(self.show_CreationDP)
        self.windowOncologique.switch_window3.connect(self.show_Recalibrage)
        self.windowOncologique.switch_window4.connect(self.show_Arthrodese)
        self.windowOncologique.switch_window5.connect(self.show_Etape2)
        self.windowOncologique.switch_window6.connect(self.show_CreationDP)

        self.etape2.hide()
        self.windowRecalibrage.hide()
        self.windowArthrodese.hide()
        self.windowOncologique.show()

    def show_Recalibrage(self):
        self.windowCreationDP = MainWindow_CreationDP()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowRecalibrage = MainWindow_FormRecalibrage()

        # actions de chaque bouton en fct du window
        self.windowRecalibrage.switch_window1.connect(self.show_Degeneratif)
        self.windowRecalibrage.switch_window2.connect(self.show_CreationDP)
        self.windowRecalibrage.switch_window3.connect(self.show_Degeneratif)

        self.windowRecalibrage.show()

    def show_Arthrodese(self):
        self.windowCreationDP = MainWindow_CreationDP()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowArthrodese = MainWindow_FormArthrodese()

        # actions de chaque bouton en fct du window
        self.windowArthrodese.switch_window1.connect(self.show_Degeneratif)
        self.windowArthrodese.switch_window2.connect(self.show_CreationDP)
        self.windowArthrodese.switch_window3.connect(self.show_Degeneratif)

        self.windowArthrodese.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller_INPEC2 = Controller_Test()
    controller_INPEC2.show_Oncologique()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()