from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Connexion_BD import *

from UITest.Accueil_Medecin import MainWindow_Acceuil
from UITest.CreationDP import MainWindow_CreationDP
from UITest.CreationDP import *
from UITest.Evaluation import MainWindow_Evaluation
from UITest.Evaluation import *
from UITest.Accueil_Secretaire import MainWindow_Acceuil_Secretaire
from UITest.Connexion import Login
from UITest.Pathologie_Etape2 import MainWindow_Etape2
from UITest.Pathologie_Degeneratif import MainWindow_Degeneratif
from UITest.Pathologie_Degeneratif import *
from UITest.Pathologie_Oncologie import MainWindow_Oncologie
from UITest.Pathologie_Traumatologique import MainWindow_Traumatologie
from UITest.Traumatologique_Niveaux import MainWindow_Niveau
from UITest.Traumatologique_Niveaux import *
from UITest.Formulaire_Arthrodese import MainWindow_FormArthrodese
from UITest.Formulaire_Recalibrage import MainWindow_FormRecalibrage
from UITest.Formulaire_Recalibrage import *

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
controlleur_cursor = ""

controlleur_zoneCervicale = False
controlleur_zoneDorsale = False
controlleur_zoneLombaire = False
controlleur_zoneSacro = False

controlleur_FN_radiculaire = False
controlleur_FN_radicoMedullaire = False
controlleur_FN_medullaire = False
controlleur_FN_non = False
controlleur_vertebre1 = int(1)
controlleur_vertebre2 = int(2)
controlleur_recalibrage_oui = False
controlleur_recalibrage_hernie = False
controlleur_recalibrage_non = False
controlleur_cote_droit = False
controlleur_cote_gauche = False
controlleur_cote_bilateral = False
controlleur_arthrodese_oui = False
controlleur_arthrodese_non = False
creerPat = False
BD = Connexion_DB()


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
        global BD
        global creerPat

        controlleur_nom = ""
        controlleur_prenom = ""
        controlleur_numMagic = ""
        controlleur_dateDeIntervention = ""

        self.med = MainWindow_Acceuil()
        self.co = Login()
        self.windowCreationDP = MainWindow_CreationDP()
        self.windowEvaluation = MainWindow_Evaluation()




        BD = Connexion_DB()
        BD.connexion_DB()

        if creerPat == True:
            controlleur_nom = UITest.CreationDP.patient_nom
            controlleur_prenom = UITest.CreationDP.patient_prenom
            controlleur_dateNaissance = UITest.CreationDP.patient_dateNaissance
            controlleur_numMagic = UITest.CreationDP.patient_numMagic
            BD.creation_patient(controlleur_numMagic, controlleur_nom, controlleur_prenom, 'X')
            creerPat = False
            controlleur_nom = ""
            controlleur_prenom = ""
            controlleur_numMagic = ""
            controlleur_dateDeIntervention = ""


        self.med.switch_window1.connect(self.show_CreationDP)
        # self.med.switch_window2.connect(self.show_)
        self.med.switch_window5.connect(self.show_Connexion)


        self.windowEvaluation.hide()
        self.windowCreationDP.hide()
        self.co.hide()
        self.med.show()

    def show_Secretaire(self):
        global controlleur_nom, controlleur_prenom, controlleur_numMagic, controlleur_dateDeIntervention, controlleur_jour, controlleur_mois, controlleur_annee
        global controlleur_cbox_cervicaleRadiculaire, controlleur_cbox_medullaire, controlleur_cbox_thoracoLombaire, controlleur_cbox_autre
        global BD
        global creerPat

        controlleur_nom = ""
        controlleur_prenom = ""
        controlleur_numMagic = ""
        controlleur_dateDeIntervention = ""


        self.co = Login()
        self.sec = MainWindow_Acceuil_Secretaire()
        self.windowCreationDP = MainWindow_CreationDP()
        self.windowEvaluation = MainWindow_Evaluation()

        self.BD = Connexion_DB()
        self.BD.connexion_DB()

        if creerPat == True:
            controlleur_nom = UITest.CreationDP.patient_nom
            controlleur_prenom = UITest.CreationDP.patient_prenom
            controlleur_dateNaissance = UITest.CreationDP.patient_dateNaissance
            controlleur_numMagic = UITest.CreationDP.patient_numMagic
            BD.creation_patient(controlleur_numMagic, controlleur_nom, controlleur_prenom, 'X')
            creerPat = False
            controlleur_nom = ""
            controlleur_prenom = ""
            controlleur_numMagic = ""
            controlleur_dateDeIntervention = ""

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
        global res
        global creerPat

        

        controlleur_cursor = ""
        self.signal_med = UITest.Connexion.signal_medecin
        self.signal_sec = UITest.Connexion.signal_secretaire
        self.signal_eval = UITest.CreationDP.signal_eval

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

        # controlleur_cursor = Connexion_DB.cursor
        #
        # self.BD = Connexion_DB
        #
        res = ""
        with open("C:/Users/Public/InPec/DonneestransfereesAndroid.txt", "r") as f:
            for line in f.readlines():
                # Traiter la ligne et ainsi de suite ...
                res = line.strip()

        BD.ajouter_score_oswestry(res)


        self.windowEvaluation.switch_window2.connect(self.show_CreationDP)

        self.windowEvaluation.lineEdit_identite.setText(controlleur_nom + ' ' + controlleur_prenom)
        self.windowEvaluation.lineEdit_numeroMagic_2.setText(controlleur_numMagic)
        self.windowEvaluation.lineEdit_dateIntervention.setText(controlleur_dateDeIntervention)
        self.windowEvaluation.label_recuperationDateDeNaissance.setText(controlleur_dateNaissance)

        if self.signal_med == True:

            if self.windowEvaluation.switch_window.connect(self.show_Medecin):
                creerPat = True

        elif self.signal_sec == True:
            if self.windowEvaluation.switch_window.connect(self.show_Secretaire):
                creerPat = True

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
        global controlleur_zoneCervicale, controlleur_zoneDorsale, controlleur_zoneLombaire, controlleur_zoneSacro
        global controlleur_FN_radicoMedullaire, controlleur_FN_radiculaire, controlleur_FN_medullaire, controlleur_FN_non
        global controlleur_vertebre1, controlleur_vertebre2
        global controlleur_recalibrage_hernie, controlleur_recalibrage_non, controlleur_recalibrage_oui
        global controlleur_cote_bilateral, controlleur_cote_droit, controlleur_cote_gauche
        global controlleur_arthrodese_non, controlleur_arthrodese_oui

        controlleur_zoneCervicale = UITest.Pathologie_Etape2.signal_cervicale
        controlleur_zoneDorsale = UITest.Pathologie_Etape2.signal_dorsale
        controlleur_zoneLombaire = UITest.Pathologie_Etape2.signal_lombaire
        controlleur_zoneSacro = UITest.Pathologie_Etape2.signal_sacro

        controlleur_FN_radicoMedullaire = UITest.Pathologie_Degeneratif.glb_dege_FN_radicoMedullaire
        controlleur_FN_radiculaire = UITest.Pathologie_Degeneratif.glb_dege_FN_radiculaire
        controlleur_FN_medullaire = UITest.Pathologie_Degeneratif.glb_dege_FN_medullaire
        controlleur_FN_non = UITest.Pathologie_Degeneratif.glb_dege_FN_non
        controlleur_vertebre1 = UITest.Pathologie_Degeneratif.dege_vertebre1
        controlleur_vertebre2 = UITest.Pathologie_Degeneratif.dege_vertebre2
        controlleur_recalibrage_hernie = UITest.Pathologie_Degeneratif.dege_recalibrage_hernie
        controlleur_recalibrage_non = UITest.Pathologie_Degeneratif.dege_recalibrage_non
        controlleur_recalibrage_oui = UITest.Pathologie_Degeneratif.dege_recalibrage_oui

        controlleur_cote_bilateral = UITest.Pathologie_Degeneratif.glb_dege_cote_bilateral
        controlleur_cote_gauche = UITest.Pathologie_Degeneratif.glb_dege_cote_gauche
        controlleur_cote_droit = UITest.Pathologie_Degeneratif.glb_dege_cote_droit
        controlleur_arthrodese_non = UITest.Pathologie_Degeneratif.dege_arthrodese_non
        controlleur_arthrodese_oui = UITest.Pathologie_Degeneratif.dege_arthrodese_oui

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

        self.windowDegeneratif.spinBox_nombre1.setValue(controlleur_vertebre1)
        self.windowDegeneratif.spinBox_nombre2.setValue(controlleur_vertebre2)
        self.windowDegeneratif.radioButton_medullaire.setChecked(controlleur_FN_medullaire)
        self.windowDegeneratif.radioButton_radicoMedullaire.setChecked(controlleur_FN_radicoMedullaire)
        self.windowDegeneratif.radioButton_non.setChecked(controlleur_FN_non)
        self.windowDegeneratif.radioButton_radiculaire.setChecked(controlleur_FN_radiculaire)
        self.windowDegeneratif.radioButton_recalibrageNon.setChecked(controlleur_recalibrage_non)
        self.windowDegeneratif.radioButton_recalibrageOui.setChecked(controlleur_recalibrage_oui)
        self.windowDegeneratif.radioButton_herniePure.setChecked(controlleur_recalibrage_hernie)
        self.windowDegeneratif.radioButton_Droit.setChecked(controlleur_cote_droit)
        self.windowDegeneratif.radioButton_gauche.setChecked(controlleur_cote_gauche)
        self.windowDegeneratif.radioButton_bilateral.setChecked(controlleur_cote_bilateral)
        self.windowDegeneratif.radioButton_arthrodeseOui.setChecked(controlleur_arthrodese_oui)
        self.windowDegeneratif.radioButton_recalibrageNon.setChecked(controlleur_arthrodese_non)

        if (controlleur_zoneCervicale == True):
            self.windowDegeneratif.label_patho.setText("Cervicale")
        if (controlleur_zoneDorsale == True):
            self.windowDegeneratif.label_patho.setText("Dorsale")
        if (controlleur_zoneLombaire == True):
            self.windowDegeneratif.label_patho.setText("Lombaire")
        if (controlleur_zoneSacro == True):
            self.windowDegeneratif.label_patho.setText("Sacro-coccygienne")

        if (controlleur_zoneCervicale == True and controlleur_zoneDorsale == True):
            self.windowDegeneratif.label_patho.setText("Cervicale + Dorsale")
        if (controlleur_zoneDorsale == True and controlleur_zoneLombaire == True):
            self.windowDegeneratif.label_patho.setText("Dorsale + Lombaire")
        if (controlleur_zoneLombaire == True and controlleur_zoneSacro == True):
            self.windowDegeneratif.label_patho.setText("Lombaire + Sacro-coccygienne")

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
        global controlleur_vertebre1, controlleur_vertebre2

        self.signal_degene = UITest.Pathologie_Etape2.signal_degeneratif
        self.signal_trauma = UITest.Pathologie_Etape2.signal_traumatologique
        self.signal_onco = UITest.Pathologie_Etape2.signal_oncologie
        controlleur_vertebre1 = UITest.Pathologie_Degeneratif.dege_vertebre1
        controlleur_vertebre2 = UITest.Pathologie_Degeneratif.dege_vertebre2

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
        global controlleur_vertebre1, controlleur_vertebre2

        self.signal_degene = UITest.Pathologie_Etape2.signal_degeneratif
        self.signal_trauma = UITest.Pathologie_Etape2.signal_traumatologique
        self.signal_onco = UITest.Pathologie_Etape2.signal_oncologie
        controlleur_vertebre1 = UITest.Pathologie_Degeneratif.dege_vertebre1
        controlleur_vertebre2 = UITest.Pathologie_Degeneratif.dege_vertebre2

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