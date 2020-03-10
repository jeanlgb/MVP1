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

controlleur_nom = ""
controlleur_prenom = ""
controlleur_numMagic = ""
controlleur_dateDeIntervention = ""
controlleur_dateNaissance = ""
controlleur_jour = ""
controlleur_mois = ""
controlleur_annee = ""
controlleur_cbox_cervicaleRadiculaire = ""
controlleur_cbox_medullaire = ""
controlleur_cbox_thoracoLombaire = ""
controlleur_cbox_autre = ""

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
        global controlleur_nom, controlleur_prenom, controlleur_numMagic, controlleur_dateDeIntervention, controlleur_jour, controlleur_mois, controlleur_annee
        global controlleur_cbox_cervicaleRadiculaire, controlleur_cbox_medullaire, controlleur_cbox_thoracoLombaire, controlleur_cbox_autre

        controlleur_nom = ""
        controlleur_prenom = ""
        controlleur_numMagic = ""
        controlleur_dateDeIntervention = ""

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
        global controlleur_nom, controlleur_prenom, controlleur_numMagic, controlleur_dateDeIntervention, controlleur_jour, controlleur_mois, controlleur_annee
        global controlleur_cbox_cervicaleRadiculaire, controlleur_cbox_medullaire, controlleur_cbox_thoracoLombaire, controlleur_cbox_autre

        controlleur_jour = UITest.CreationDP.patient_jour
        controlleur_mois = UITest.CreationDP.patient_mois
        controlleur_annee = UITest.CreationDP.patient_anneeControlleur
        controlleur_cbox_cervicaleRadiculaire = UITest.CreationDP.valeur_cb_cervicale_radiculaire
        controlleur_cbox_medullaire = UITest.CreationDP.valeur_cb_medullaire
        controlleur_cbox_thoracoLombaire = UITest.CreationDP.valeur_cb_thoraco_lombaire
        controlleur_cbox_autre = UITest.CreationDP.valeur_cb_autre

        self.signal_med = UITest.Connexion.signal_medecin
        self.signal_sec = UITest.Connexion.signal_secretaire

        self.windowEvaluation = MainWindow_Evaluation()
        self.sec = MainWindow_Acceuil_Secretaire()
        self.med = MainWindow_Acceuil()
        self.etape2 = MainWindow_Etape2()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowOncologique = MainWindow_Oncologie()
        self.windowTraumato = MainWindow_Traumatologie()
        self.windowArthrodese = MainWindow_FormArthrodese()
        self.windowRecalibrage = MainWindow_FormRecalibrage()
        self.windowCreationDP = MainWindow_CreationDP()

        #actions de chaque bouton en fct du window
        self.windowCreationDP.switch_window1.connect(self.show_Evaluation)
        self.windowCreationDP.switch_window2.connect(self.show_Etape2)

        self.windowCreationDP.lineEdit_nom.setText(controlleur_nom)
        self.windowCreationDP.lineEdit_prenom.setText(controlleur_prenom)
        self.windowCreationDP.lineEdit_dateIntervention.setText(controlleur_dateDeIntervention)
        self.windowCreationDP.lineEdit_numeroMagic.setText(controlleur_numMagic)
        self.windowCreationDP.comboBox_jour.setCurrentText(controlleur_jour)
        self.windowCreationDP.comboBox_mois.setCurrentText(controlleur_mois)
        self.windowCreationDP.spinBox_annee.setValue(controlleur_annee)
        self.windowCreationDP.checkBox_cervicalRadiculaire.setChecked(controlleur_cbox_cervicaleRadiculaire)
        self.windowCreationDP.checkBox_medullaire.setChecked(controlleur_cbox_medullaire)
        self.windowCreationDP.checkBox_thoracoLombaire.setChecked(controlleur_cbox_thoracoLombaire)
        self.windowCreationDP.checkBox_autre.setChecked(controlleur_cbox_autre)


        if self.signal_med == True:
            self.windowCreationDP.switch_window3.connect(self.show_Medecin)
        elif self.signal_sec == True:
            self.windowCreationDP.switch_window3.connect(self.show_Secretaire)

        self.med.hide()
        self.sec.hide()
        self.etape2.hide()
        self.windowEvaluation.hide()
        self.windowArthrodese.hide()
        self.windowRecalibrage.hide()
        self.windowDegeneratif.hide()
        self.windowOncologique.hide()
        self.windowTraumato.hide()

        self.windowCreationDP.show()

    def show_Evaluation(self):
        global controlleur_nom, controlleur_prenom, controlleur_numMagic, controlleur_dateDeIntervention, controlleur_dateNaissance
        global controlleur_cbox_cervicaleRadiculaire, controlleur_cbox_medullaire, controlleur_cbox_thoracoLombaire, controlleur_cbox_autre


        controlleur_nom = UITest.CreationDP.patient_nom
        controlleur_prenom = UITest.CreationDP.patient_prenom
        controlleur_dateNaissance = UITest.CreationDP.patient_dateNaissance
        controlleur_numMagic = UITest.CreationDP.patient_numMagic
        controlleur_dateDeIntervention = UITest.CreationDP.patient_dateIntervention
        controlleur_cbox_cervicaleRadiculaire = UITest.CreationDP.valeur_cb_cervicale_radiculaire
        controlleur_cbox_medullaire = UITest.CreationDP.valeur_cb_medullaire
        controlleur_cbox_thoracoLombaire = UITest.CreationDP.valeur_cb_thoraco_lombaire
        controlleur_cbox_autre = UITest.CreationDP.valeur_cb_autre

        self.windowEvaluation = MainWindow_Evaluation()
        self.windowCreationDP = MainWindow_CreationDP()
        self.med = MainWindow_Acceuil()

        self.windowEvaluation.switch_window.connect(self.show_Medecin)
        self.windowEvaluation.switch_window2.connect(self.show_CreationDP)

        self.windowEvaluation.lineEdit_identite.setText(controlleur_nom + ' ' + controlleur_prenom)
        self.windowEvaluation.lineEdit_numeroMagic_2.setText(controlleur_numMagic)
        self.windowEvaluation.lineEdit_dateIntervention.setText(controlleur_dateDeIntervention)
        self.windowEvaluation.label_recuperationDateDeNaissance.setText(controlleur_dateNaissance)

        # coche automatiquement les checkbox des scores
        if controlleur_cbox_cervicaleRadiculaire == True:
            self.windowEvaluation.checkBox_ndi.setChecked(True)
            self.windowEvaluation.checkBox_evaCervical.setChecked(True)
            self.windowEvaluation.checkBox_glassman.setChecked(True)


        elif controlleur_cbox_medullaire == True:
            self.windowEvaluation.checkBox_oswestry.setChecked(True)


        elif controlleur_cbox_thoracoLombaire == True:
            self.windowEvaluation.checkBox_mjoa.setChecked(True)
            self.windowEvaluation.checkBox_glassman.setChecked(True)
            self.windowEvaluation.checkBox_evaLombaire.setChecked(True)



        elif controlleur_cbox_autre == True:
            self.windowEvaluation.checkBox_oswestry.setChecked(False)
            self.windowEvaluation.checkBox_evaLombaire.setChecked(False)
            self.windowEvaluation.checkBox_glassman.setChecked(False)
            self.windowEvaluation.checkBox_mjoa.setChecked(False)
            self.windowEvaluation.checkBox_evaCervical.setChecked(False)
            self.windowEvaluation.checkBox_ndi.setChecked(False)


        self.windowCreationDP.hide()
        self.med.hide()
        self.windowEvaluation.show()

    def show_Etape2(self):
        global controlleur_nom, controlleur_prenom, controlleur_numMagic, controlleur_dateDeIntervention, controlleur_jour, controlleur_mois, controlleur_annee
        controlleur_nom = UITest.CreationDP.patient_nom
        controlleur_prenom = UITest.CreationDP.patient_prenom
        controlleur_jour = UITest.CreationDP.patient_jour
        controlleur_mois = UITest.CreationDP.patient_mois
        controlleur_annee = UITest.CreationDP.patient_anneeControlleur
        controlleur_numMagic = UITest.CreationDP.patient_numMagic
        controlleur_dateDeIntervention = UITest.CreationDP.patient_dateIntervention

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
        self.signal_degene = UITest.Pathologie_Etape2.signal_degeneratif
        self.signal_trauma = UITest.Pathologie_Etape2.signal_traumatologique
        self.signal_onco = UITest.Pathologie_Etape2.signal_oncologie


        self.windowCreationDP = MainWindow_CreationDP()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowOncologique = MainWindow_Oncologie()
        self.windowTraumato = MainWindow_Traumatologie()
        self.windowRecalibrage = MainWindow_FormRecalibrage()

        if self.signal_degene == True:
            self.windowRecalibrage.switch_window1.connect(self.show_Degeneratif)
            self.windowRecalibrage.switch_window3.connect(self.show_Degeneratif)

        elif self.signal_trauma == True:
            self.windowRecalibrage.switch_window1.connect(self.show_Traumatologique)
            self.windowRecalibrage.switch_window3.connect(self.show_Traumatologique)

        elif self.signal_onco == True:
            self.windowRecalibrage.switch_window1.connect(self.show_Oncologique)
            self.windowRecalibrage.switch_window3.connect(self.show_Oncologique)

        # actions de chaque bouton en fct du window
        self.windowRecalibrage.switch_window1.connect(self.show_Degeneratif)
        self.windowRecalibrage.switch_window2.connect(self.show_CreationDP)


        self.windowRecalibrage.show()

    def show_Arthrodese(self):
        self.signal_degene = UITest.Pathologie_Etape2.signal_degeneratif
        self.signal_trauma = UITest.Pathologie_Etape2.signal_traumatologique
        self.signal_onco = UITest.Pathologie_Etape2.signal_oncologie

        self.windowCreationDP = MainWindow_CreationDP()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowOncologique = MainWindow_Oncologie()
        self.windowTraumato = MainWindow_Traumatologie()
        self.windowArthrodese = MainWindow_FormArthrodese()

        if self.signal_degene == True:
            self.windowArthrodese.switch_window1.connect(self.show_Degeneratif)
            self.windowArthrodese.switch_window3.connect(self.show_Degeneratif)

        elif self.signal_trauma == True:
            self.windowArthrodese.switch_window1.connect(self.show_Traumatologique)
            self.windowArthrodese.switch_window3.connect(self.show_Traumatologique)

        elif self.signal_onco == True:
            self.windowArthrodese.switch_window1.connect(self.show_Oncologique)
            self.windowArthrodese.switch_window3.connect(self.show_Oncologique)

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