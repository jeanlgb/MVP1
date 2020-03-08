from PyQt5 import QtCore, QtGui, QtWidgets
import sys


from UITest.Accueil_Medecin import MainWindow_Acceuil
from UITest.CreationDP import MainWindow_CreationDP
from UITest.CreationDP import *
from UITest.Evaluation import MainWindow_Evaluation
from UITest.Accueil_Secretaire import MainWindow_Acceuil_Secretaire
from UITest.Connexion import Login
from UITest.Pathologie_Etape2 import MainWindow_Etape2
from UITest.Pathologie_Degeneratif import MainWindow_Degeneratif
from UITest.Pathologie_Oncologie import MainWindow_Oncologie
from UITest.Pathologie_Traumatologique import MainWindow_Traumatologie
from UITest.Traumatologique_Niveaux import MainWindow_Niveau
from UITest.Traumatologique_Niveaux import *
from UITest.Formulaire_Arthrodese import MainWindow_FormArthrodese
from UITest.Formulaire_Recalibrage import MainWindow_FormRecalibrage

class Controller_Test:

    def __init__(self):
        pass

    def show_Connexion(self):
        self.med = MainWindow_Acceuil()
        self.sec = MainWindow_Acceuil_Secretaire()
        self.co = Login()

        self.co.switch_window1.connect(self.show_Medecin)
        self.co.switch_window2.connect(self.show_Secretaire)

        self.med.hide()
        self.sec.hide()
        self.co.show()

    def show_Medecin(self):
        self.med = MainWindow_Acceuil()
        self.co = Login()
        self.windowCreationDP = MainWindow_CreationDP()
        self.windowEvaluation = MainWindow_Evaluation()

        self.med.switch_window1.connect(self.show_CreationDP)
        # self.med.switch_window2.connect(self.show_)
        self.med.switch_window5.connect(self.show_Connexion)

        self.windowEvaluation.hide()
        self.windowCreationDP.hide()
        self.co.hide()
        self.med.show()

    def show_Secretaire(self):
        self.co = Login()
        self.sec = MainWindow_Acceuil_Secretaire()
        self.windowCreationDP = MainWindow_CreationDP()
        self.windowEvaluation = MainWindow_Evaluation()

        self.sec.switch_window1.connect(self.show_CreationDP)
        # self.sec.switch_window2.connect(self.show_)
        self.sec.switch_window3.connect(self.show_Connexion)

        self.windowEvaluation.hide()
        self.co.hide()
        self.windowCreationDP.hide()
        self.sec.show()


    def show_CreationDP(self):
        self.signal_med = UITest.Connexion.signal_medecin
        self.signal_sec = UITest.Connexion.signal_secretaire

        self.sec = MainWindow_Acceuil_Secretaire()
        self.med = MainWindow_Acceuil()
        self.etape2 = MainWindow_Etape2()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowOncologique = MainWindow_Oncologie()
        self.windowTraumato = MainWindow_Traumatologie()
        self.windowCreationDP = MainWindow_CreationDP()

        #actions de chaque bouton en fct du window
        self.windowCreationDP.switch_window1.connect(self.show_Evaluation)
        self.windowCreationDP.switch_window2.connect(self.show_Etape2)

        if self.signal_med == True:
            self.windowCreationDP.switch_window3.connect(self.show_Medecin)
        elif self.signal_sec == True:
            self.windowCreationDP.switch_window3.connect(self.show_Secretaire)

        self.med.hide()
        self.sec.hide()
        self.etape2.hide()
        self.windowDegeneratif.hide()
        self.windowOncologique.hide()
        self.windowTraumato.hide()

        self.windowCreationDP.show()

    def show_Evaluation(self):
        self.nom = UITest.CreationDP.patient_nom
        self.prenom = UITest.CreationDP.patient_prenom
        self.numMagic = UITest.CreationDP.patient_numMagic
        self.dateDeIntervention = UITest.CreationDP.patient_dateIntervention
        self.dateDeNaissance = UITest.CreationDP.patient_dateNaissance

        self.windowEvaluation = MainWindow_Evaluation()
        self.windowCreationDP = MainWindow_CreationDP()
        self.med = MainWindow_Acceuil()

        self.windowEvaluation.switch_window.connect(self.show_Medecin)
        self.windowEvaluation.switch_window2.connect(self.show_CreationDP)

        self.windowEvaluation.lineEdit_identite.setText(self.nom + ' ' + self.prenom)
        self.windowEvaluation.lineEdit_numeroMagic_2.setText(self.numMagic)
        self.windowEvaluation.lineEdit_dateIntervention.setText(self.dateDeIntervention)
        self.windowEvaluation.label_recuperationDateDeNaissance.setText(self.dateDeNaissance)


        self.windowCreationDP.hide()
        self.med.hide()
        self.windowEvaluation.show()

    def show_Etape2(self):
        self.windowCreationDP = MainWindow_CreationDP()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowOncologique = MainWindow_Oncologie()
        self.windowTraumato = MainWindow_Traumatologie()
        self.etape2 = MainWindow_Etape2()

        #actions de chaque bouton en fct du window
        self.etape2.switch_window1.connect(self.show_Degeneratif)
        self.etape2.switch_window2.connect(self.show_Traumatologique)
        self.etape2.switch_window3.connect(self.show_Oncologique)

        self.etape2.switch_window4.connect(self.show_CreationDP)

        self.windowDegeneratif.hide()
        self.windowOncologique.hide()
        self.windowTraumato.hide()
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

    def show_Traumatologique(self):
        self.windowCreationDP = MainWindow_CreationDP()
        self.etape2 = MainWindow_Etape2()
        self.windowRecalibrage = MainWindow_FormRecalibrage()
        self.windowArthrodese = MainWindow_FormArthrodese()
        self.windowNiveau = MainWindow_Niveau()
        self.windowTraumato = MainWindow_Traumatologie()

        self.nbVertebre = UITest.Traumatologique_Niveaux.compteur_recuperation
        self.windowTraumato.lineEdit_nombreVertebre.setText(self.nbVertebre)

        # actions de chaque bouton en fct du window
        self.windowTraumato.switch_window1.connect(self.show_Etape2)
        self.windowTraumato.switch_window2.connect(self.show_CreationDP)
        self.windowTraumato.switch_window3.connect(self.show_Niveau)
        self.windowTraumato.switch_window4.connect(self.show_Recalibrage)
        self.windowTraumato.switch_window5.connect(self.show_Arthrodese)
        self.windowTraumato.switch_window6.connect(self.show_Niveau)
        self.windowTraumato.switch_window7.connect(self.show_Etape2)
        self.windowTraumato.switch_window8.connect(self.show_CreationDP)

        self.etape2.hide()
        self.windowRecalibrage.hide()
        self.windowArthrodese.hide()
        self.windowNiveau.hide()

        self.windowTraumato.show()

    def show_Niveau(self):
        self.windowTraumato = MainWindow_Traumatologie()
        self.windowNiveau = MainWindow_Niveau()

        # actions de chaque bouton en fct du window
        self.windowNiveau.switch_window1.connect(self.show_Traumatologique)
        self.windowNiveau.switch_window2.connect(self.show_Traumatologique)

        self.windowNiveau.show()

    def show_Recalibrage(self):
        self.windowCreationDP = MainWindow_CreationDP()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowOncologique = MainWindow_Oncologie()
        self.windowTraumato = MainWindow_Traumatologie()
        self.windowRecalibrage = MainWindow_FormRecalibrage()

        # actions de chaque bouton en fct du window
        self.windowRecalibrage.switch_window1.connect(self.show_Degeneratif)
        self.windowRecalibrage.switch_window2.connect(self.show_CreationDP)
        self.windowRecalibrage.switch_window3.connect(self.show_Degeneratif)

        self.windowRecalibrage.show()

    def show_Arthrodese(self):
        self.windowCreationDP = MainWindow_CreationDP()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowOncologique = MainWindow_Oncologie()
        self.windowTraumato = MainWindow_Traumatologie()
        self.windowArthrodese = MainWindow_FormArthrodese()

        # actions de chaque bouton en fct du window
        self.windowArthrodese.switch_window1.connect(self.show_Degeneratif)
        self.windowArthrodese.switch_window2.connect(self.show_CreationDP)
        self.windowArthrodese.switch_window3.connect(self.show_Degeneratif)

        self.windowArthrodese.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller_INPEC2 = Controller_Test()
    controller_INPEC2.show_Connexion()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()