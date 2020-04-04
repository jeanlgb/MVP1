from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from datetime import datetime


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
from UITest.Pathologie_Traumatologique import  *
from UITest.Traumatologique_Niveaux import MainWindow_Niveau
from UITest.Traumatologique_Niveaux import *
from UITest.Formulaire_Arthrodese import MainWindow_FormArthrodese
from UITest.Formulaire_Recalibrage import MainWindow_FormRecalibrage
from UITest.Formulaire_Recalibrage import *
from UITest.SelectionDP import MainWindow_SelectionnerDP
from UITest.SelectionDP import *
from UITest.SelectionDP_suite import MainWindow_SelectionnerDP_suite
from UITest.SelectionDP_suite import *
from Connexion_BD import *

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

controlleur_topo_epidurale = False
controlleur_topo_osseuse = False
controlleur_topo_intraDurale = False
controlleur_topo_intraMedullaire = False
controlleur_topo_enSablier = False
controlleur_topo_autre = False
controlleur_origine_radiculaire = False
controlleur_origine_meningee = False
controlleur_origine_osseuse = False
controlleur_origine_secondaire = False
controlleur_origine_medullaire = False
controlleur_origine_autre = False

controlleur_percutanee = False
controlleur_foyer = False
controlleur_percutanee2 = False
controlleur_foyer2 = False
controlleur_corpo_vertebro = False
controlleur_corpo_cypho = False
controlleur_corpo_non = False
controlleur_osteo_mono = False
controlleur_osteo_poly = False
controlleur_osteo_non = False

ctr_glb_label_topo = ""
ctr_glb_label_origine = ""
ctr_glb_label_corpo = ""
ctr_glb_label_osteo = ""
ctr_glb_label_modalite = ""
ctl_glb_label_patho = ""
ctl_glb_label_FN = ""
ctl_glb_label_niveau = ""
ctl_glb_label_reca = ""
ctl_glb_label_cote = ""
ctl_glb_label_arthro = ""
ctl_glb_textEdit_intervention = ""

ctr_signal_contexte = ""

ctr_reca_postAnt = ""
ctr_reca_infos = ""
ctr_reca_hernie = ""
ctr_arthro_postAnt = ""
ctr_arthro_fixation = ""
ctr_arthro_greffe = ""
concatenation_recalibrage = ""
concatenation_arthrodese = ""
concatenation_traumato_niveau = ""

controlleur_postOp = False
controlleur_preOp = False

control_med_creaDP = False
control_med_selecDP = False
control_sec_creaDP = False
control_sec_selecDP = False

valider = False
validerTraumato = False
validerOnco = False
validerRecalibrage = False
validerArthrodese = False
validerNiveaux = False


ctr_niveaux_CDLS = ""
ctr_niveaux_zoneC = ""
ctr_niveaux_zoneD = ""
ctr_niveaux_zoneL = ""
ctr_niveaux_zoneS = ""

ctr_nomIntervention_commentaire = ""
ctr_nomIntervention_nonModifiable = ""

arthro_postAnt2 = ""
arthro_greffe2 = ""
arthro_fixation2 = ""
reca_postAnt2 = ""
reca_infos2 = ""
reca_hernie2 = ""

nom_intervention = ""

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
        global controlleur_postOp, controlleur_preOp, ctr_nomIntervention_commentaire, ctr_nomIntervention_nonModifiable, nom_intervention
        global control_med_creaDP, control_med_selecDP

        controlleur_nom = ""
        controlleur_prenom = ""
        controlleur_numMagic = ""
        controlleur_dateDeIntervention = ""
        ctr_nomIntervention_commentaire = ""
        nom_intervention = ""

        self.med = MainWindow_Acceuil()
        self.co = Login()
        self.windowSelectionnerDP = MainWindow_SelectionnerDP()
        self.windowCreationDP = MainWindow_CreationDP()
        self.windowEvaluation = MainWindow_Evaluation()
        self.vider = ""
        self.date_consultation = str(datetime.now())
        controlleur_postOp = UITest.Evaluation.glb_postOp
        controlleur_preOp = UITest.Evaluation.glb_preOp

        BD = Connexion_DB()
        BD.connexion_DB()

        if creerPat == True:
            controlleur_nom = UITest.CreationDP.patient_nom
            controlleur_prenom = UITest.CreationDP.patient_prenom
            controlleur_dateNaissance = UITest.CreationDP.patient_dateNaissance
            controlleur_dateDeIntervention = UITest.CreationDP.patient_dateIntervention
            ctr_nomIntervention_commentaire = UITest.CreationDP.glb_textEditNomIntervention
            controlleur_jour = UITest.CreationDP.patient_jour
            controlleur_mois = UITest.CreationDP.patient_mois
            controlleur_annee = UITest.CreationDP.patient_anneeControlleur
            controlleur_cbox_medullaire = UITest.CreationDP.valeur_cb_medullaire
            controlleur_cbox_cervicaleRadiculaire = UITest.CreationDP.valeur_cb_cervicale_radiculaire
            controlleur_cbox_thoracoLombaire = UITest.CreationDP.valeur_cb_thoraco_lombaire
            controlleur_cbox_autre = UITest.CreationDP.valeur_cb_autre

            if control_med_creaDP == True:
                BD.creation_patient(controlleur_numMagic, controlleur_nom, controlleur_prenom, 'X')
                controlleur_numMagic = UITest.CreationDP.patient_numMagic

            if control_med_selecDP == True:
                controlleur_numMagic = UITest.SelectionDP.patient_numMagic_existant

            if controlleur_postOp:
                BD.creation_consultation(controlleur_numMagic, ctr_nomIntervention_nonModifiable, ctr_nomIntervention_commentaire , self.date_consultation, "POST")

            if controlleur_preOp:
                BD.creation_consultation(controlleur_numMagic, ctr_nomIntervention_nonModifiable, ctr_nomIntervention_commentaire, self.date_consultation,  "PRE")

            liste = []
            with open("C:/Users/Public/InPec/DonneestransfereesAndroid.txt", "r") as f:
                for line in f.readlines():
                    # Traiter la ligne et ainsi de suite ...
                    ligne = line.strip()
                    liste.append(ligne)
                print(liste)

            if not liste:
                print("liste vide")

            else:

                if liste[0] != "X":
                    numeroM = liste[0]

                else:
                    numeroM = ""

                if liste[1] != "X":
                    glassman = liste[1]

                else:
                    glassman = ""

                if liste[2] != "X":
                    evacer = liste[2]

                else:
                    evacer = ""

                if liste[3] != "X":
                    evalom = liste[3]
                else:
                    evalom = ""
                if liste[4] != "X":
                    ndi = liste[4]
                else:
                    ndi = ""
                if liste[5] != "X":
                    mjoa = liste[5]
                else:
                    mjoa = ""
                if liste[6] != "X":
                    oswestry = liste[6]
                else:
                    oswestry = ""

                BD.ajouter_scores(numeroM, glassman, evacer, evalom, ndi, mjoa, oswestry)
                f = open('C:/Users/Public/InPec/DonneestransfereesAndroid.txt', 'w')
                f.write(self.vider)


            creerPat = False
            controlleur_nom = ""
            controlleur_prenom = ""
            controlleur_numMagic = ""
            ctr_nomIntervention_commentaire = ""
            controlleur_dateDeIntervention = ""
            UITest.CreationDP.patient_jour = ""
            UITest.CreationDP.patient_mois = ""
            UITest.CreationDP.patient_anneeControlleur = int(2000)
            UITest.CreationDP.valeur_cb_medullaire = False
            UITest.CreationDP.valeur_cb_cervicale_radiculaire = False
            UITest.CreationDP.valeur_cb_autre = False
            UITest.CreationDP.valeur_cb_thoraco_lombaire = False



        self.med.switch_window1.connect(self.show_CreationDP)
        self.med.switch_window2.connect(self.show_SelectionnerDP)

        self.med.switch_window5.connect(self.show_Connexion)


        self.windowEvaluation.hide()
        self.windowSelectionnerDP.hide()
        self.windowCreationDP.hide()
        self.co.hide()
        self.med.show()

    def show_Secretaire(self):
        global controlleur_nom, controlleur_prenom, controlleur_numMagic, controlleur_dateDeIntervention, controlleur_jour, controlleur_mois, controlleur_annee
        global controlleur_cbox_cervicaleRadiculaire, controlleur_cbox_medullaire, controlleur_cbox_thoracoLombaire, controlleur_cbox_autre
        global BD, controlleur_postOp, controlleur_preOp
        global creerPat, ctr_nomIntervention_commentaire, ctr_nomIntervention_nonModifiable, nom_intervention
        global control_sec_creaDP, control_sec_selecDP

        controlleur_nom = ""
        controlleur_prenom = ""
        controlleur_numMagic = ""
        ctr_nomIntervention_commentaire = ""
        controlleur_dateDeIntervention = ""
        nom_intervention = ""

        self.date_consultation = str(datetime.now())


        self.co = Login()
        self.sec = MainWindow_Acceuil_Secretaire()
        self.windowSelectionnerDP = MainWindow_SelectionnerDP()
        self.windowCreationDP = MainWindow_CreationDP()
        self.windowEvaluation = MainWindow_Evaluation()

        self.vider = ""
        controlleur_postOp = UITest.Evaluation.glb_postOp
        controlleur_preOp = UITest.Evaluation.glb_preOp

        BD = Connexion_DB()
        BD.connexion_DB()

        if creerPat == True:
            controlleur_nom = UITest.CreationDP.patient_nom
            controlleur_prenom = UITest.CreationDP.patient_prenom
            controlleur_dateNaissance = UITest.CreationDP.patient_dateNaissance
            controlleur_dateDeIntervention = UITest.CreationDP.patient_dateIntervention
            ctr_nomIntervention_commentaire = UITest.CreationDP.glb_textEditNomIntervention
            controlleur_jour = UITest.CreationDP.patient_jour
            controlleur_mois = UITest.CreationDP.patient_mois
            controlleur_annee = UITest.CreationDP.patient_anneeControlleur
            controlleur_cbox_medullaire = UITest.CreationDP.valeur_cb_medullaire
            controlleur_cbox_cervicaleRadiculaire = UITest.CreationDP.valeur_cb_cervicale_radiculaire
            controlleur_cbox_thoracoLombaire = UITest.CreationDP.valeur_cb_thoraco_lombaire
            controlleur_cbox_autre = UITest.CreationDP.valeur_cb_autre

            if control_sec_creaDP == True:
                controlleur_numMagic = UITest.CreationDP.patient_numMagic
                BD.creation_patient(controlleur_numMagic, controlleur_nom, controlleur_prenom, 'X')

            if control_sec_selecDP == True:
                controlleur_numMagic = UITest.SelectionDP.patient_numMagic_existant

            if controlleur_postOp:
                BD.creation_consultation(controlleur_numMagic, ctr_nomIntervention_nonModifiable, ctr_nomIntervention_commentaire, self.date_consultation, "POST")

            if controlleur_preOp:
                BD.creation_consultation(controlleur_numMagic, ctr_nomIntervention_nonModifiable, ctr_nomIntervention_commentaire, self.date_consultation, "PRE")


            liste = []
            with open("C:/Users/Public/InPec/DonneestransfereesAndroid.txt", "r") as f:
                for line in f.readlines():
                    # Traiter la ligne et ainsi de suite ...
                    ligne = line.strip()
                    liste.append(ligne)
                print(liste)

            if not liste:
                print("liste vide")

            else:

                if liste[0] != "X":
                    numeroM = liste[0]

                else:
                    numeroM = ""

                if liste[1] != "X":
                    glassman = liste[1]

                else:
                    glassman = ""

                if liste[2] != "X":
                    evacer = liste[2]

                else:
                    evacer = ""

                if liste[3] != "X":
                    evalom = liste[3]
                else:
                    evalom = ""
                if liste[4] != "X":
                    ndi = liste[4]
                else:
                    ndi = ""
                if liste[5] != "X":
                    mjoa = liste[5]
                else:
                    mjoa = ""
                if liste[6] != "X":
                    oswestry = liste[6]
                else:
                    oswestry = ""

                BD.ajouter_scores(numeroM, glassman, evacer, evalom, ndi, mjoa, oswestry)
                f = open('C:/Users/Public/InPec/DonneestransfereesAndroid.txt', 'w')
                f.write(self.vider)
            creerPat = False
            controlleur_nom = ""
            controlleur_prenom = ""
            controlleur_numMagic = ""
            ctr_nomIntervention_commentaire = ""
            controlleur_dateDeIntervention = ""
            UITest.CreationDP.patient_jour = ""
            UITest.CreationDP.patient_mois = ""
            UITest.CreationDP.patient_anneeControlleur = int(2000)
            UITest.CreationDP.valeur_cb_medullaire = False
            UITest.CreationDP.valeur_cb_cervicale_radiculaire = False
            UITest.CreationDP.valeur_cb_autre = False
            UITest.CreationDP.valeur_cb_thoraco_lombaire = False

        self.sec.switch_window1.connect(self.show_CreationDP)
        self.sec.switch_window2.connect(self.show_SelectionnerDP)
        self.sec.switch_window3.connect(self.show_Connexion)

        self.windowEvaluation.hide()
        self.co.hide()
        self.windowSelectionnerDP.hide()
        self.windowCreationDP.hide()
        self.sec.show()


    def show_CreationDP(self):
        global controlleur_nom, controlleur_prenom, controlleur_numMagic, controlleur_dateDeIntervention, controlleur_jour, controlleur_mois, controlleur_annee
        global controlleur_cbox_cervicaleRadiculaire, controlleur_cbox_medullaire, controlleur_cbox_thoracoLombaire, controlleur_cbox_autre
        global ctl_glb_label_patho, ctl_glb_label_FN, ctl_glb_label_niveau, ctl_glb_label_reca, ctl_glb_label_cote, ctl_glb_label_arthro, ctl_glb_textEdit_intervention, ctr_signal_contexte
        global ctr_glb_label_origine, ctr_glb_label_topo
        global ctr_glb_label_corpo, ctr_glb_label_osteo, ctr_glb_label_modalite
        global concatenation_arthrodese, concatenation_recalibrage, concatenation_traumato_niveau
        global BD, ctr_nomIntervention_commentaire, ctr_nomIntervention_nonModifiable
        global valider, validerOnco, validerTraumato
        global controlleur_percutanee2, controlleur_foyer2
        global arthro_greffe2, arthro_fixation2, arthro_postAnt2, reca_postAnt2, reca_infos2, reca_hernie2, nom_intervention

        controlleur_jour = UITest.CreationDP.patient_jour
        controlleur_mois = UITest.CreationDP.patient_mois
        controlleur_annee = UITest.CreationDP.patient_anneeControlleur
        controlleur_cbox_cervicaleRadiculaire = UITest.CreationDP.valeur_cb_cervicale_radiculaire
        controlleur_cbox_medullaire = UITest.CreationDP.valeur_cb_medullaire
        controlleur_cbox_thoracoLombaire = UITest.CreationDP.valeur_cb_thoraco_lombaire
        controlleur_cbox_autre = UITest.CreationDP.valeur_cb_autre

        valider = UITest.Pathologie_Degeneratif.valider
        validerTraumato = UITest.Pathologie_Traumatologique.validerTraumato
        validerOnco = UITest.Pathologie_Oncologie.validerOnco

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

        # actions de chaque bouton en fct du window
        self.windowCreationDP.switch_window1.connect(self.show_Evaluation)
        self.windowCreationDP.switch_window2.connect(self.show_Etape2)



        self.windowCreationDP.lineEdit_nom.setText(controlleur_nom)
        self.windowCreationDP.lineEdit_prenom.setText(controlleur_prenom)
        self.windowCreationDP.lineEdit_dateIntervention.setText(controlleur_dateDeIntervention)
        self.windowCreationDP.lineEdit_numeroMagic.setText(controlleur_numMagic)
        self.windowCreationDP.lineEdit_interventionModifiable.setText(ctr_nomIntervention_commentaire)
        self.windowCreationDP.comboBox_jour.setCurrentText(controlleur_jour)
        self.windowCreationDP.comboBox_mois.setCurrentText(controlleur_mois)
        self.windowCreationDP.spinBox_annee.setValue(controlleur_annee)
        self.windowCreationDP.checkBox_cervicalRadiculaire.setChecked(controlleur_cbox_cervicaleRadiculaire)
        self.windowCreationDP.checkBox_medullaire.setChecked(controlleur_cbox_medullaire)
        self.windowCreationDP.checkBox_thoracoLombaire.setChecked(controlleur_cbox_thoracoLombaire)
        self.windowCreationDP.checkBox_autre.setChecked(controlleur_cbox_autre)


        if valider == True:
            controlleur_numMagic = UITest.CreationDP.patient_numMagic
            ctl_glb_textEdit_intervention = UITest.CreationDP.glb_textEdit_intervention
            ctr_signal_contexte = UITest.Pathologie_Etape2.glb_nom_contexte
            ctl_glb_label_FN = UITest.Pathologie_Degeneratif.glb_label_FN
            ctl_glb_label_niveau = UITest.Pathologie_Degeneratif.glb_label_Niveau
            ctl_glb_label_reca = UITest.Pathologie_Degeneratif.glb_label_recalibrage
            ctl_glb_label_cote = UITest.Pathologie_Degeneratif.glb_label_cote
            ctl_glb_label_arthro = UITest.Pathologie_Degeneratif.glb_label_arthrodese
            ctr_nomIntervention_commentaire = UITest.CreationDP.glb_textEditNomIntervention

            BD.ajouter_pathologie_degeneratif("", controlleur_numMagic, ctl_glb_label_patho,
                                                  ctr_signal_contexte, ctl_glb_label_FN,
                                                  ctl_glb_label_niveau, ctl_glb_label_reca, ctl_glb_label_cote,
                                                  ctl_glb_label_arthro, ctr_nomIntervention_commentaire)

            nom_intervention = (ctl_glb_textEdit_intervention + " " + ctl_glb_label_patho + " " +
                                                                     ctr_signal_contexte + " " + ctl_glb_label_FN + " " +
                                                                     ctl_glb_label_niveau + " " + "Recalibrage: " + ctl_glb_label_reca + " " + concatenation_recalibrage + " " + ctl_glb_label_cote + " " +
                                                                     "Arthrodèse: " + ctl_glb_label_arthro + " " + concatenation_arthrodese)

            print(nom_intervention)
            ctr_nomIntervention_nonModifiable = nom_intervention
            self.windowCreationDP.textEdit_interventionNonModifiable.setText(nom_intervention)

            if validerRecalibrage == True:
                BD.ajouter_formuaire_recalibrage("", controlleur_numMagic, reca_postAnt2, reca_infos2,
                                                 reca_hernie2)
                UITest.Formulaire_Recalibrage.validerRecalibrage = False

            if validerArthrodese == True:
                BD.ajouter_formuaire_arthrodese("", controlleur_numMagic, arthro_postAnt2, arthro_fixation2,
                                                arthro_greffe2)
                UITest.Formulaire_Arthrodese.validerArthrodese = False

            ctl_glb_label_patho = ""
            ctl_glb_label_FN = ""
            ctr_signal_contexte = ""
            ctl_glb_textEdit_intervention = ""
            ctl_glb_label_niveau = ""
            ctl_glb_label_reca = ""
            ctl_glb_label_cote = ""
            ctl_glb_label_arthro = ""
            UITest.Pathologie_Degeneratif.valider = False


        elif validerOnco == True:
                controlleur_numMagic = UITest.CreationDP.patient_numMagic
                ctl_glb_textEdit_intervention = UITest.CreationDP.glb_textEdit_intervention
                ctr_signal_contexte = UITest.Pathologie_Etape2.glb_nom_contexte
                ctr_glb_label_origine = UITest.Pathologie_Oncologie.glb_label_origine
                ctr_glb_label_topo = UITest.Pathologie_Oncologie.glb_label_topo
                ctl_glb_label_FN = UITest.Pathologie_Oncologie.glb_label_FN
                ctl_glb_label_niveau = UITest.Pathologie_Oncologie.glb_label_Niveau
                ctl_glb_label_reca = UITest.Pathologie_Oncologie.glb_label_recalibrage
                ctl_glb_label_cote = UITest.Pathologie_Oncologie.glb_label_cote
                ctl_glb_label_arthro = UITest.Pathologie_Oncologie.glb_label_arthrodese
                ctr_nomIntervention_commentaire = UITest.CreationDP.glb_textEditNomIntervention

                BD.ajouter_pathologie_oncologie("", controlleur_numMagic, ctl_glb_label_patho,
                                                      ctr_signal_contexte, ctl_glb_label_FN, ctr_glb_label_topo, ctr_glb_label_origine,
                                                      ctl_glb_label_niveau, ctl_glb_label_reca, ctl_glb_label_cote,
                                                      ctl_glb_label_arthro, ctr_nomIntervention_commentaire)

                nom_intervention = (ctl_glb_textEdit_intervention + " " + ctl_glb_label_patho + " " +
                                    ctr_signal_contexte + " " + ctl_glb_label_FN + " " + ctr_glb_label_topo + " " + ctr_glb_label_origine + " " +
                                    ctl_glb_label_niveau + " " + "Recalibrage: " + ctl_glb_label_reca + " " + concatenation_recalibrage + " " + ctl_glb_label_cote + " " + "Arthrodèse: " +
                                    ctl_glb_label_arthro + " " + concatenation_arthrodese)
                print(nom_intervention)
                ctr_nomIntervention_nonModifiable = nom_intervention

                self.windowCreationDP.textEdit_interventionNonModifiable.setText(nom_intervention)

                if validerRecalibrage == True:
                    BD.ajouter_formuaire_recalibrage("", controlleur_numMagic, reca_postAnt2, reca_infos2,
                                                     reca_hernie2)
                    UITest.Formulaire_Recalibrage.validerRecalibrage = False

                if validerArthrodese == True:
                    BD.ajouter_formuaire_arthrodese("", controlleur_numMagic, arthro_postAnt2, arthro_fixation2,
                                                arthro_greffe2)
                    UITest.Formulaire_Arthrodese.validerArthrodese = False

                ctr_glb_label_origine = ""
                ctr_glb_label_topo = ""
                ctl_glb_label_patho = ""
                ctl_glb_label_FN = ""
                ctr_signal_contexte = ""
                ctl_glb_textEdit_intervention = ""
                ctl_glb_label_niveau = ""
                ctl_glb_label_reca = ""
                ctl_glb_label_cote = ""
                ctl_glb_label_arthro = ""
                UITest.Pathologie_Oncologie.validerOnco = False


        if validerTraumato == True:
                controlleur_percutanee2 = UITest.Pathologie_Traumatologique.glb_traumato_modalite_percutanee2
                controlleur_foyer2 = UITest.Pathologie_Traumatologique.glb_traumato_modalite_foyer2

                controlleur_numMagic = UITest.CreationDP.patient_numMagic
                ctl_glb_textEdit_intervention = UITest.CreationDP.glb_textEdit_intervention
                ctr_signal_contexte = UITest.Pathologie_Etape2.glb_nom_contexte
                ctr_glb_label_corpo = UITest.Pathologie_Traumatologique.glb_label_corpo
                ctr_glb_label_osteo = UITest.Pathologie_Traumatologique.glb_label_osteo
                ctr_glb_label_modalite = UITest.Pathologie_Traumatologique.glb_label_modalite
                ctl_glb_label_FN = UITest.Pathologie_Traumatologique.glb_label_FN
                ctl_glb_label_niveau = UITest.Pathologie_Traumatologique.glb_label_Niveau
                ctl_glb_label_reca = UITest.Pathologie_Traumatologique.glb_label_recalibrage
                ctl_glb_label_cote = UITest.Pathologie_Traumatologique.glb_label_cote
                ctl_glb_label_arthro = UITest.Pathologie_Traumatologique.glb_label_arthrodese
                ctr_nomIntervention_commentaire = UITest.CreationDP.glb_textEditNomIntervention
                ctr_niveaux_zoneC = UITest.Traumatologique_Niveaux.glb_zoneC
                ctr_niveaux_CDLS = UITest.Traumatologique_Niveaux.glb_zoneCDLS
                ctr_niveaux_zoneL = UITest.Traumatologique_Niveaux.glb_zoneL
                ctr_niveaux_zoneS = UITest.Traumatologique_Niveaux.glb_zoneS
                ctr_niveaux_zoneD = UITest.Traumatologique_Niveaux.glb_zoneD


                if (controlleur_percutanee2 == True):
                    BD.ajouter_pathologie_traumatologique("", controlleur_numMagic, ctl_glb_label_patho,
                                                      ctr_signal_contexte, ctl_glb_label_FN, ctr_glb_label_modalite, ctr_glb_label_corpo, ctr_glb_label_osteo,
                                                      "", "", "", "", ctr_nomIntervention_commentaire)

                    BD.ajouter_traumato_niveaux("", controlleur_numMagic, ctr_niveaux_CDLS, ctr_niveaux_zoneC,
                                                ctr_niveaux_zoneD, ctr_niveaux_zoneL, ctr_niveaux_zoneS)

                    nom_intervention = (ctl_glb_textEdit_intervention + " " + ctl_glb_label_patho + " " +
                                    ctr_signal_contexte + " " + ctl_glb_label_FN + " " + ctr_glb_label_modalite + " " + concatenation_traumato_niveau + " " + ctr_glb_label_corpo + " " + ctr_glb_label_osteo)

                    print(nom_intervention)

                    self.windowCreationDP.textEdit_interventionNonModifiable.setText(nom_intervention)
                    ctr_nomIntervention_nonModifiable = nom_intervention

                    concatenation_traumato_niveau = ""
                    controlleur_percutanee2 = False


                if (controlleur_foyer2 == True):
                    BD.ajouter_pathologie_traumatologique("", controlleur_numMagic, ctl_glb_label_patho,
                                                          ctr_signal_contexte, ctl_glb_label_FN, ctr_glb_label_modalite,
                                                          "", "",
                                                          ctl_glb_label_niveau, ctl_glb_label_reca, ctl_glb_label_cote,
                                                          ctl_glb_label_arthro, ctr_nomIntervention_commentaire)

                    nom_intervention = (ctl_glb_textEdit_intervention + " " + ctl_glb_label_patho + " " +
                                          ctr_signal_contexte + " " + ctl_glb_label_FN + " " + ctr_glb_label_modalite + " " +
                                          ctl_glb_label_niveau + " " + "Recalibrage: " + ctl_glb_label_reca + " " + concatenation_recalibrage + " " + ctl_glb_label_cote + " " + "Arthrodèse: " +
                                          ctl_glb_label_arthro + " " + concatenation_arthrodese)

                    print(nom_intervention)
                    ctr_nomIntervention_nonModifiable = nom_intervention

                    self.windowCreationDP.textEdit_interventionNonModifiable.setText(nom_intervention)
                    controlleur_foyer2 = False

                if validerRecalibrage == True:
                    BD.ajouter_formuaire_recalibrage("", controlleur_numMagic, reca_postAnt2, reca_infos2,
                                                     reca_hernie2)
                    UITest.Formulaire_Recalibrage.validerRecalibrage = False

                if validerArthrodese == True:
                    BD.ajouter_formuaire_arthrodese("", controlleur_numMagic, arthro_postAnt2, arthro_fixation2,
                                                arthro_greffe2)
                    UITest.Formulaire_Arthrodese.validerArthrodese = False

                ctr_glb_label_corpo = ""
                ctr_glb_label_osteo = ""
                ctr_glb_label_modalite = ""
                ctl_glb_label_patho = ""
                ctl_glb_label_FN = ""
                ctr_signal_contexte = ""
                ctl_glb_textEdit_intervention = ""
                ctl_glb_label_niveau = ""
                ctl_glb_label_reca = ""
                ctl_glb_label_cote = ""
                ctl_glb_label_arthro = ""
                UITest.Traumatologique_Niveaux.compteur_recuperation = ""
                validerTraumato = False
                UITest.Pathologie_Traumatologique.validerTraumato = False


        self.windowCreationDP.textEdit_interventionNonModifiable.setText(nom_intervention)

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

    def show_SelectionnerDP(self):
        global controlleur_nom, controlleur_prenom, controlleur_numMagic

        self.signal_med = UITest.Connexion.signal_medecin
        self.signal_sec = UITest.Connexion.signal_secretaire
        self.windowsSelectionnerDP_suite = MainWindow_SelectionnerDP_suite()

        self.sec = MainWindow_Acceuil_Secretaire()
        self.med = MainWindow_Acceuil()
        self.windowSelectionnerDP = MainWindow_SelectionnerDP()

        # actions de chaque bouton en fct du window
        self.windowSelectionnerDP.switch_window1.connect(self.show_SelectionnerDP_suite)



        if self.signal_med == True:
            self.windowSelectionnerDP.switch_window2.connect(self.show_Medecin)
        elif self.signal_sec == True:
            self.windowSelectionnerDP.switch_window2.connect(self.show_Secretaire)

        self.med.hide()
        self.sec.hide()
        self.windowsSelectionnerDP_suite.hide()

        self.windowSelectionnerDP.show()

    def show_SelectionnerDP_suite(self):
        global controlleur_cbox_cervicaleRadiculaire, controlleur_cbox_medullaire, controlleur_cbox_thoracoLombaire, controlleur_cbox_autre, controlleur_dateDeIntervention
        global ctl_glb_label_patho, ctl_glb_label_FN, ctl_glb_label_niveau, ctl_glb_label_reca, ctl_glb_label_cote, ctl_glb_label_arthro, ctl_glb_textEdit_intervention, ctr_signal_contexte
        global ctr_glb_label_origine, ctr_glb_label_topo
        global concatenation_arthrodese, concatenation_recalibrage
        global BD
        global ctr_glb_label_corpo, ctr_glb_label_osteo, ctr_glb_label_modalite
        global concatenation_arthrodese, concatenation_recalibrage, concatenation_traumato_niveau
        global ctr_nomIntervention_commentaire, ctr_nomIntervention_nonModifiable
        global valider, validerOnco, validerTraumato
        global controlleur_percutanee2, controlleur_foyer2
        global arthro_greffe2, arthro_fixation2, arthro_postAnt2, reca_postAnt2, reca_infos2, reca_hernie2, nom_intervention
        global controlleur_numMagic


        controlleur_cbox_cervicaleRadiculaire = UITest.SelectionDP_suite.valeur_cb_cervicale_radiculaire
        controlleur_cbox_medullaire = UITest.SelectionDP_suite.valeur_cb_medullaire
        controlleur_cbox_thoracoLombaire = UITest.SelectionDP_suite.valeur_cb_thoraco_lombaire
        controlleur_cbox_autre = UITest.SelectionDP_suite.valeur_cb_autre

        self.windowEvaluation = MainWindow_Evaluation()
        self.etape2 = MainWindow_Etape2()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowOncologique = MainWindow_Oncologie()
        self.windowTraumato = MainWindow_Traumatologie()
        self.windowArthrodese = MainWindow_FormArthrodese()
        self.windowRecalibrage = MainWindow_FormRecalibrage()
        self.windowSelectionnerDP = MainWindow_SelectionnerDP()
        self.windowsSelectionnerDP_suite = MainWindow_SelectionnerDP_suite()

        self.windowsSelectionnerDP_suite.switch_window1.connect(self.show_Evaluation)
        self.windowsSelectionnerDP_suite.switch_window2.connect(self.show_Etape2)
        self.windowsSelectionnerDP_suite.switch_window3.connect(self.show_SelectionnerDP)

        self.patient_nom = UITest.SelectionDP.patient_nom_existant
        self.patient_prenom = UITest.SelectionDP.patient_prenom_existant
        controlleur_numMagic = UITest.SelectionDP.patient_numMagic_existant


        BD = Connexion_DB()
        BD.connexion_DB()
        self.identite = BD.selectionner_patient_num(controlleur_numMagic)


        self.windowsSelectionnerDP_suite.lineEdit_identite.setText(self.identite)
        self.windowsSelectionnerDP_suite.lineEdit_numeroMagic.setText(controlleur_numMagic)

        self.windowsSelectionnerDP_suite.checkBox_cervicalRadiculaire.setChecked(controlleur_cbox_cervicaleRadiculaire)
        self.windowsSelectionnerDP_suite.checkBox_medullaire.setChecked(controlleur_cbox_medullaire)
        self.windowsSelectionnerDP_suite.checkBox_thoracoLombaire.setChecked(controlleur_cbox_thoracoLombaire)
        self.windowsSelectionnerDP_suite.checkBox_autre.setChecked(controlleur_cbox_autre)
        self.windowsSelectionnerDP_suite.lineEdit_dateIntervention.setText(controlleur_dateDeIntervention)

        if valider == True:
            controlleur_numMagic = UITest.SelectionDP.patient_numMagic_existant
            ctl_glb_textEdit_intervention = UITest.SelectionDP_suite.glb_textEdit_intervention
            ctr_signal_contexte = UITest.Pathologie_Etape2.glb_nom_contexte
            ctl_glb_label_FN = UITest.Pathologie_Degeneratif.glb_label_FN
            ctl_glb_label_niveau = UITest.Pathologie_Degeneratif.glb_label_Niveau
            ctl_glb_label_reca = UITest.Pathologie_Degeneratif.glb_label_recalibrage
            ctl_glb_label_cote = UITest.Pathologie_Degeneratif.glb_label_cote
            ctl_glb_label_arthro = UITest.Pathologie_Degeneratif.glb_label_arthrodese
            ctr_nomIntervention_commentaire = UITest.SelectionDP_suite.glb_textEditNomIntervention

            BD.ajouter_pathologie_degeneratif("", controlleur_numMagic, ctl_glb_label_patho,
                                              ctr_signal_contexte, ctl_glb_label_FN,
                                              ctl_glb_label_niveau, ctl_glb_label_reca, ctl_glb_label_cote,
                                              ctl_glb_label_arthro, ctr_nomIntervention_commentaire)

            nom_intervention = (ctl_glb_textEdit_intervention + " " + ctl_glb_label_patho + " " +
                                ctr_signal_contexte + " " + ctl_glb_label_FN + " " +
                                ctl_glb_label_niveau + " " + "Recalibrage: " + ctl_glb_label_reca + " " + concatenation_recalibrage + " " + ctl_glb_label_cote + " " +
                                "Arthrodèse: " + ctl_glb_label_arthro + " " + concatenation_arthrodese)

            print(nom_intervention)
            ctr_nomIntervention_nonModifiable = nom_intervention
            self.windowsSelectionnerDP_suite.textEdit_interventionNonModifiable.setText(nom_intervention)

            if validerRecalibrage == True:
                BD.ajouter_formuaire_recalibrage("", controlleur_numMagic, reca_postAnt2, reca_infos2,
                                                 reca_hernie2)
                UITest.Formulaire_Recalibrage.validerRecalibrage = False

            if validerArthrodese == True:
                BD.ajouter_formuaire_arthrodese("", controlleur_numMagic, arthro_postAnt2, arthro_fixation2,
                                                arthro_greffe2)
                UITest.Formulaire_Arthrodese.validerArthrodese = False

            ctl_glb_label_patho = ""
            ctl_glb_label_FN = ""
            ctr_signal_contexte = ""
            ctl_glb_textEdit_intervention = ""
            ctl_glb_label_niveau = ""
            ctl_glb_label_reca = ""
            ctl_glb_label_cote = ""
            ctl_glb_label_arthro = ""
            UITest.Pathologie_Degeneratif.valider = False


        elif validerOnco == True:
            controlleur_numMagic = UITest.SelectionDP.patient_numMagic_existant
            ctl_glb_textEdit_intervention = UITest.SelectionDP_suite.glb_textEdit_intervention
            ctr_signal_contexte = UITest.Pathologie_Etape2.glb_nom_contexte
            ctr_glb_label_origine = UITest.Pathologie_Oncologie.glb_label_origine
            ctr_glb_label_topo = UITest.Pathologie_Oncologie.glb_label_topo
            ctl_glb_label_FN = UITest.Pathologie_Oncologie.glb_label_FN
            ctl_glb_label_niveau = UITest.Pathologie_Oncologie.glb_label_Niveau
            ctl_glb_label_reca = UITest.Pathologie_Oncologie.glb_label_recalibrage
            ctl_glb_label_cote = UITest.Pathologie_Oncologie.glb_label_cote
            ctl_glb_label_arthro = UITest.Pathologie_Oncologie.glb_label_arthrodese
            ctr_nomIntervention_commentaire = UITest.SelectionDP_suite.glb_textEditNomIntervention

            BD.ajouter_pathologie_oncologie("", controlleur_numMagic, ctl_glb_label_patho,
                                            ctr_signal_contexte, ctl_glb_label_FN, ctr_glb_label_topo,
                                            ctr_glb_label_origine,
                                            ctl_glb_label_niveau, ctl_glb_label_reca, ctl_glb_label_cote,
                                            ctl_glb_label_arthro, ctr_nomIntervention_commentaire)

            nom_intervention = (ctl_glb_textEdit_intervention + " " + ctl_glb_label_patho + " " +
                                ctr_signal_contexte + " " + ctl_glb_label_FN + " " + ctr_glb_label_topo + " " + ctr_glb_label_origine + " " +
                                ctl_glb_label_niveau + " " + "Recalibrage: " + ctl_glb_label_reca + " " + concatenation_recalibrage + " " + ctl_glb_label_cote + " " + "Arthrodèse: " +
                                ctl_glb_label_arthro + " " + concatenation_arthrodese)
            print(nom_intervention)
            ctr_nomIntervention_nonModifiable = nom_intervention

            self.windowsSelectionnerDP_suite.textEdit_interventionNonModifiable.setText(nom_intervention)

            if validerRecalibrage == True:
                BD.ajouter_formuaire_recalibrage("", controlleur_numMagic, reca_postAnt2, reca_infos2,
                                                 reca_hernie2)
                UITest.Formulaire_Recalibrage.validerRecalibrage = False

            if validerArthrodese == True:
                BD.ajouter_formuaire_arthrodese("", controlleur_numMagic, arthro_postAnt2, arthro_fixation2,
                                                arthro_greffe2)
                UITest.Formulaire_Arthrodese.validerArthrodese = False

            ctr_glb_label_origine = ""
            ctr_glb_label_topo = ""
            ctl_glb_label_patho = ""
            ctl_glb_label_FN = ""
            ctr_signal_contexte = ""
            ctl_glb_textEdit_intervention = ""
            ctl_glb_label_niveau = ""
            ctl_glb_label_reca = ""
            ctl_glb_label_cote = ""
            ctl_glb_label_arthro = ""
            UITest.Pathologie_Oncologie.validerOnco = False

        if validerTraumato == True:
            controlleur_percutanee2 = UITest.Pathologie_Traumatologique.glb_traumato_modalite_percutanee2
            controlleur_foyer2 = UITest.Pathologie_Traumatologique.glb_traumato_modalite_foyer2

            controlleur_numMagic = UITest.SelectionDP.patient_numMagic_existant
            ctl_glb_textEdit_intervention = UITest.SelectionDP_suite.glb_textEdit_intervention
            ctr_signal_contexte = UITest.Pathologie_Etape2.glb_nom_contexte
            ctr_glb_label_corpo = UITest.Pathologie_Traumatologique.glb_label_corpo
            ctr_glb_label_osteo = UITest.Pathologie_Traumatologique.glb_label_osteo
            ctr_glb_label_modalite = UITest.Pathologie_Traumatologique.glb_label_modalite
            ctl_glb_label_FN = UITest.Pathologie_Traumatologique.glb_label_FN
            ctl_glb_label_niveau = UITest.Pathologie_Traumatologique.glb_label_Niveau
            ctl_glb_label_reca = UITest.Pathologie_Traumatologique.glb_label_recalibrage
            ctl_glb_label_cote = UITest.Pathologie_Traumatologique.glb_label_cote
            ctl_glb_label_arthro = UITest.Pathologie_Traumatologique.glb_label_arthrodese
            ctr_nomIntervention_commentaire = UITest.SelectionDP_suite.glb_textEditNomIntervention
            ctr_niveaux_zoneC = UITest.Traumatologique_Niveaux.glb_zoneC
            ctr_niveaux_CDLS = UITest.Traumatologique_Niveaux.glb_zoneCDLS
            ctr_niveaux_zoneL = UITest.Traumatologique_Niveaux.glb_zoneL
            ctr_niveaux_zoneS = UITest.Traumatologique_Niveaux.glb_zoneS
            ctr_niveaux_zoneD = UITest.Traumatologique_Niveaux.glb_zoneD

            if (controlleur_percutanee2 == True):
                BD.ajouter_pathologie_traumatologique("", controlleur_numMagic, ctl_glb_label_patho,
                                                      ctr_signal_contexte, ctl_glb_label_FN, ctr_glb_label_modalite,
                                                      ctr_glb_label_corpo, ctr_glb_label_osteo,
                                                      "", "", "", "", ctr_nomIntervention_commentaire)

                BD.ajouter_traumato_niveaux("", controlleur_numMagic, ctr_niveaux_CDLS, ctr_niveaux_zoneC,
                                            ctr_niveaux_zoneD, ctr_niveaux_zoneL, ctr_niveaux_zoneS)

                nom_intervention = (ctl_glb_textEdit_intervention + " " + ctl_glb_label_patho + " " +
                                    ctr_signal_contexte + " " + ctl_glb_label_FN + " " + ctr_glb_label_modalite + " " + concatenation_traumato_niveau + " " + ctr_glb_label_corpo + " " + ctr_glb_label_osteo)

                print(nom_intervention)

                self.windowCreationDP.textEdit_interventionNonModifiable.setText(nom_intervention)
                ctr_nomIntervention_nonModifiable = nom_intervention

                concatenation_traumato_niveau = ""
                controlleur_percutanee2 = False

            if (controlleur_foyer2 == True):
                BD.ajouter_pathologie_traumatologique("", controlleur_numMagic, ctl_glb_label_patho,
                                                      ctr_signal_contexte, ctl_glb_label_FN, ctr_glb_label_modalite,
                                                      "", "",
                                                      ctl_glb_label_niveau, ctl_glb_label_reca, ctl_glb_label_cote,
                                                      ctl_glb_label_arthro, ctr_nomIntervention_commentaire)

                nom_intervention = (ctl_glb_textEdit_intervention + " " + ctl_glb_label_patho + " " +
                                    ctr_signal_contexte + " " + ctl_glb_label_FN + " " + ctr_glb_label_modalite + " " +
                                    ctl_glb_label_niveau + " " + "Recalibrage: " + ctl_glb_label_reca + " " + concatenation_recalibrage + " " + ctl_glb_label_cote + " " + "Arthrodèse: " +
                                    ctl_glb_label_arthro + " " + concatenation_arthrodese)

                print(nom_intervention)
                ctr_nomIntervention_nonModifiable = nom_intervention

                self.windowsSelectionnerDP_suite.textEdit_interventionNonModifiable.setText(nom_intervention)
                controlleur_foyer2 = False

            if validerRecalibrage == True:
                BD.ajouter_formuaire_recalibrage("", controlleur_numMagic, reca_postAnt2, reca_infos2,
                                                 reca_hernie2)
                UITest.Formulaire_Recalibrage.validerRecalibrage = False

            if validerArthrodese == True:
                BD.ajouter_formuaire_arthrodese("", controlleur_numMagic, arthro_postAnt2, arthro_fixation2,
                                                arthro_greffe2)
                UITest.Formulaire_Arthrodese.validerArthrodese = False

            ctr_glb_label_corpo = ""
            ctr_glb_label_osteo = ""
            ctr_glb_label_modalite = ""
            ctl_glb_label_patho = ""
            ctl_glb_label_FN = ""
            ctr_signal_contexte = ""
            ctl_glb_textEdit_intervention = ""
            ctl_glb_label_niveau = ""
            ctl_glb_label_reca = ""
            ctl_glb_label_cote = ""
            ctl_glb_label_arthro = ""
            UITest.Traumatologique_Niveaux.compteur_recuperation = ""
            validerTraumato = False
            UITest.Pathologie_Traumatologique.validerTraumato = False

        self.windowsSelectionnerDP_suite.textEdit_interventionNonModifiable.setText(nom_intervention)

        self.windowDegeneratif.hide()
        self.windowOncologique.hide()
        self.windowTraumato.hide()
        self.windowRecalibrage.hide()
        self.windowArthrodese.hide()
        self.windowEvaluation.hide()
        self.windowSelectionnerDP.hide()
        self.etape2.hide()


        self.windowsSelectionnerDP_suite.show()

    def show_Evaluation(self):
        global controlleur_nom, controlleur_prenom, controlleur_numMagic, controlleur_dateDeIntervention, controlleur_dateNaissance
        global controlleur_cbox_cervicaleRadiculaire, controlleur_cbox_medullaire, controlleur_cbox_thoracoLombaire, controlleur_cbox_autre
        global res
        global creerPat
        global controlleur_postOp, controlleur_preOp
        global control_med_creaDP, control_med_selecDP, control_sec_creaDP, control_sec_selecDP, ctr_nomIntervention_commentaire


        controlleur_cursor = ""
        self.signal_med = UITest.Connexion.signal_medecin
        self.signal_sec = UITest.Connexion.signal_secretaire
        self.signal_eval = UITest.CreationDP.signal_eval

        control_med_creaDP = UITest.Accueil_Medecin.signal_med_creationDP
        control_med_selecDP = UITest.Accueil_Medecin.signal_med_selectionDP
        control_sec_creaDP = UITest.Accueil_Secretaire.signal_sec_creationDP
        control_sec_selecDP = UITest.Accueil_Secretaire.signal_sec_selectionDP


        controlleur_postOp = UITest.Evaluation.glb_postOp
        controlleur_preOp = UITest.Evaluation.glb_preOp

        self.windowEvaluation = MainWindow_Evaluation()
        self.windowCreationDP = MainWindow_CreationDP()
        self.med = MainWindow_Acceuil()
        self.windowsSelectionnerDP_suite = MainWindow_SelectionnerDP_suite()


        if self.signal_med == True:
            if self.windowEvaluation.switch_window.connect(self.show_Medecin):
                creerPat = True

        elif self.signal_sec == True:
            if self.windowEvaluation.switch_window.connect(self.show_Secretaire):
                creerPat = True

        if control_med_creaDP == True:
            self.windowEvaluation.switch_window2.connect(self.show_CreationDP)
            controlleur_nom = UITest.CreationDP.patient_nom
            controlleur_prenom = UITest.CreationDP.patient_prenom
            controlleur_dateNaissance = UITest.CreationDP.patient_dateNaissance
            controlleur_numMagic = UITest.CreationDP.patient_numMagic
            ctr_nomIntervention_commentaire = UITest.CreationDP.glb_textEditNomIntervention
            controlleur_dateDeIntervention = UITest.CreationDP.patient_dateIntervention
            controlleur_cbox_cervicaleRadiculaire = UITest.CreationDP.valeur_cb_cervicale_radiculaire
            controlleur_cbox_medullaire = UITest.CreationDP.valeur_cb_medullaire
            controlleur_cbox_thoracoLombaire = UITest.CreationDP.valeur_cb_thoraco_lombaire
            controlleur_cbox_autre = UITest.CreationDP.valeur_cb_autre
        elif control_med_selecDP   == True:
            self.windowEvaluation.switch_window2.connect(self.show_SelectionnerDP_suite)
            controlleur_nom = UITest.SelectionDP.patient_nom_existant
            controlleur_prenom = UITest.SelectionDP.patient_prenom_existant
            controlleur_dateNaissance = UITest.SelectionDP_suite.patient_dateNaissance
            controlleur_numMagic = UITest.SelectionDP.patient_numMagic_existant
            ctr_nomIntervention_commentaire = UITest.SelectionDP_suite.glb_textEditNomIntervention
            controlleur_dateDeIntervention = UITest.SelectionDP_suite.patient_dateIntervention
            controlleur_cbox_cervicaleRadiculaire = UITest.SelectionDP_suite.valeur_cb_cervicale_radiculaire
            controlleur_cbox_medullaire = UITest.SelectionDP_suite.valeur_cb_medullaire
            controlleur_cbox_thoracoLombaire = UITest.SelectionDP_suite.valeur_cb_thoraco_lombaire
            controlleur_cbox_autre = UITest.SelectionDP_suite.valeur_cb_autre
        elif control_sec_creaDP   == True:
            self.windowEvaluation.switch_window2.connect(self.show_CreationDP)
            controlleur_nom = UITest.CreationDP.patient_nom
            controlleur_prenom = UITest.CreationDP.patient_prenom
            controlleur_dateNaissance = UITest.CreationDP.patient_dateNaissance
            controlleur_numMagic = UITest.CreationDP.patient_numMagic
            ctr_nomIntervention_commentaire = UITest.CreationDP.glb_textEditNomIntervention
            controlleur_dateDeIntervention = UITest.CreationDP.patient_dateIntervention
            controlleur_cbox_cervicaleRadiculaire = UITest.CreationDP.valeur_cb_cervicale_radiculaire
            controlleur_cbox_medullaire = UITest.CreationDP.valeur_cb_medullaire
            controlleur_cbox_thoracoLombaire = UITest.CreationDP.valeur_cb_thoraco_lombaire
            controlleur_cbox_autre = UITest.CreationDP.valeur_cb_autre
        elif control_sec_selecDP   == True:
            self.windowEvaluation.switch_window2.connect(self.show_SelectionnerDP_suite)
            controlleur_nom = UITest.SelectionDP.patient_nom_existant
            controlleur_prenom = UITest.SelectionDP.patient_prenom_existant
            controlleur_dateNaissance = UITest.SelectionDP_suite.patient_dateNaissance
            controlleur_numMagic = UITest.SelectionDP.patient_numMagic_existant
            ctr_nomIntervention_commentaire = UITest.SelectionDP_suite.glb_textEditNomIntervention
            controlleur_dateDeIntervention = UITest.SelectionDP_suite.patient_dateIntervention
            controlleur_cbox_cervicaleRadiculaire = UITest.SelectionDP_suite.valeur_cb_cervicale_radiculaire
            controlleur_cbox_medullaire = UITest.SelectionDP_suite.valeur_cb_medullaire
            controlleur_cbox_thoracoLombaire = UITest.SelectionDP_suite.valeur_cb_thoraco_lombaire
            controlleur_cbox_autre = UITest.SelectionDP_suite.valeur_cb_autre

        self.windowEvaluation.lineEdit_identite.setText(controlleur_nom + ' ' + controlleur_prenom)
        self.windowEvaluation.lineEdit_numeroMagic_2.setText(controlleur_numMagic)
        self.windowEvaluation.lineEdit_dateIntervention.setText(controlleur_dateDeIntervention)
        self.windowEvaluation.label_recuperationDateDeNaissance.setText(controlleur_dateNaissance)

        # coche automatiquement les checkbox des scores
        if controlleur_cbox_cervicaleRadiculaire == True:
            self.windowEvaluation.checkBox_ndi.setChecked(True)
            self.windowEvaluation.checkBox_evaCervical.setChecked(True)
            self.windowEvaluation.checkBox_oswestry.setChecked(True)
            controlleur_cbox_cervicaleRadiculaire = "Cervicale Radiculaire"

        elif controlleur_cbox_medullaire == True:
            self.windowEvaluation.checkBox_mjoa.setChecked(True)
            self.windowEvaluation.checkBox_evaLombaire.setChecked(True)
            controlleur_cbox_medullaire = "Médullaire"

        elif controlleur_cbox_thoracoLombaire == True:
            self.windowEvaluation.checkBox_mjoa.setChecked(True)
            self.windowEvaluation.checkBox_oswestry.setChecked(True)
            self.windowEvaluation.checkBox_evaLombaire.setChecked(True)
            controlleur_cbox_thoracoLombaire = "Thoraco Lombaire"


        elif controlleur_cbox_autre == True:
            self.windowEvaluation.checkBox_oswestry.setChecked(False)
            self.windowEvaluation.checkBox_evaLombaire.setChecked(False)
            self.windowEvaluation.checkBox_glassman.setChecked(False)
            self.windowEvaluation.checkBox_mjoa.setChecked(False)
            self.windowEvaluation.checkBox_evaCervical.setChecked(False)
            self.windowEvaluation.checkBox_ndi.setChecked(False)
            controlleur_cbox_autre = "Pathologie type Autre"

        self.windowCreationDP.hide()
        self.med.hide()
        self.windowsSelectionnerDP_suite.hide()
        self.windowEvaluation.show()

    def show_Etape2(self):
        global controlleur_nom, controlleur_prenom, controlleur_numMagic, controlleur_dateDeIntervention, controlleur_jour, controlleur_mois, controlleur_annee
        global ctl_glb_label_patho, ctl_glb_label_FN, ctl_glb_label_niveau, ctl_glb_label_reca, ctl_glb_label_cote, ctl_glb_label_arthro, ctl_glb_textEdit_intervention, ctr_signal_contexte
        global BD
        global control_med_creaDP, control_med_selecDP, control_sec_creaDP, control_sec_selecDP, ctr_nomIntervention_commentaire
        global ctr_glb_label_origine, ctr_glb_label_topo
        global ctr_glb_label_corpo, ctr_glb_label_osteo, ctr_glb_label_modalite
        global concatenation_arthrodese, concatenation_recalibrage, concatenation_traumato_niveau
        global ctr_nomIntervention_commentaire, ctr_nomIntervention_nonModifiable
        global valider, validerOnco, validerTraumato
        global controlleur_percutanee2, controlleur_foyer2
        global arthro_greffe2, arthro_fixation2, arthro_postAnt2, reca_postAnt2, reca_infos2, reca_hernie2, nom_intervention

        valider = UITest.Pathologie_Degeneratif.valider
        validerTraumato = UITest.Pathologie_Traumatologique.validerTraumato
        validerOnco = UITest.Pathologie_Oncologie.validerOnco

        controlleur_nom = UITest.CreationDP.patient_nom
        controlleur_prenom = UITest.CreationDP.patient_prenom
        controlleur_jour = UITest.CreationDP.patient_jour
        controlleur_mois = UITest.CreationDP.patient_mois
        controlleur_annee = UITest.CreationDP.patient_anneeControlleur
        controlleur_numMagic = UITest.CreationDP.patient_numMagic
        ctr_nomIntervention_commentaire = UITest.CreationDP.glb_textEditNomIntervention
        controlleur_dateDeIntervention = UITest.CreationDP.patient_dateIntervention

        self.windowCreationDP = MainWindow_CreationDP()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowOncologique = MainWindow_Oncologie()
        self.windowTraumato = MainWindow_Traumatologie()
        self.etape2 = MainWindow_Etape2()
        self.windowsSelectionnerDP_suite = MainWindow_SelectionnerDP_suite()

        control_med_creaDP = UITest.Accueil_Medecin.signal_med_creationDP
        control_med_selecDP = UITest.Accueil_Medecin.signal_med_selectionDP
        control_sec_creaDP = UITest.Accueil_Secretaire.signal_sec_creationDP
        control_sec_selecDP = UITest.Accueil_Secretaire.signal_sec_selectionDP


        #actions de chaque bouton en fct du window
        self.etape2.switch_window1.connect(self.show_Degeneratif)
        self.etape2.switch_window2.connect(self.show_Traumatologique)
        self.etape2.switch_window3.connect(self.show_Oncologique)

        if control_med_creaDP == True:
            self.etape2.switch_window4.connect(self.show_CreationDP)
        elif control_med_selecDP == True:
            self.etape2.switch_window4.connect(self.show_SelectionnerDP_suite)
        elif control_sec_creaDP == True:
            self.etape2.switch_window4.connect(self.show_CreationDP)
        elif control_sec_selecDP == True:
            self.etape2.switch_window4.connect(self.show_SelectionnerDP_suite)

        if valider == True:
            controlleur_numMagic = UITest.CreationDP.patient_numMagic
            ctl_glb_textEdit_intervention = UITest.CreationDP.glb_textEdit_intervention
            ctr_signal_contexte = UITest.Pathologie_Etape2.glb_nom_contexte
            ctl_glb_label_FN = UITest.Pathologie_Degeneratif.glb_label_FN
            ctl_glb_label_niveau = UITest.Pathologie_Degeneratif.glb_label_Niveau
            ctl_glb_label_reca = UITest.Pathologie_Degeneratif.glb_label_recalibrage
            ctl_glb_label_cote = UITest.Pathologie_Degeneratif.glb_label_cote
            ctl_glb_label_arthro = UITest.Pathologie_Degeneratif.glb_label_arthrodese
            ctr_nomIntervention_commentaire = UITest.CreationDP.glb_textEditNomIntervention

            BD.ajouter_pathologie_degeneratif("", controlleur_numMagic, ctl_glb_label_patho,
                                                  ctr_signal_contexte, ctl_glb_label_FN,
                                                  ctl_glb_label_niveau, ctl_glb_label_reca, ctl_glb_label_cote,
                                                  ctl_glb_label_arthro, ctr_nomIntervention_commentaire)

            nom_intervention = (ctl_glb_textEdit_intervention + " " + ctl_glb_label_patho + " " +
                                                                     ctr_signal_contexte + " " + ctl_glb_label_FN + " " +
                                                                     ctl_glb_label_niveau + " " + "Recalibrage: " + ctl_glb_label_reca + " " + concatenation_recalibrage + " " + ctl_glb_label_cote + " " +
                                                                     "Arthrodèse: " + ctl_glb_label_arthro + " " + concatenation_arthrodese)

            print(nom_intervention)
            ctr_nomIntervention_nonModifiable = nom_intervention
            self.windowCreationDP.textEdit_interventionNonModifiable.setText(nom_intervention)

            if validerRecalibrage == True:
                BD.ajouter_formuaire_recalibrage("", controlleur_numMagic, reca_postAnt2, reca_infos2,
                                                 reca_hernie2)
                UITest.Formulaire_Recalibrage.validerRecalibrage = False

            if validerArthrodese == True:
                BD.ajouter_formuaire_arthrodese("", controlleur_numMagic, arthro_postAnt2, arthro_fixation2,
                                                arthro_greffe2)
                UITest.Formulaire_Arthrodese.validerArthrodese = False

            ctl_glb_label_patho = ""
            ctl_glb_label_FN = ""
            ctr_signal_contexte = ""
            ctl_glb_textEdit_intervention = ""
            ctl_glb_label_niveau = ""
            ctl_glb_label_reca = ""
            ctl_glb_label_cote = ""
            ctl_glb_label_arthro = ""
            UITest.Pathologie_Degeneratif.valider = False


        elif validerOnco == True:
                controlleur_numMagic = UITest.CreationDP.patient_numMagic
                ctl_glb_textEdit_intervention = UITest.CreationDP.glb_textEdit_intervention
                ctr_signal_contexte = UITest.Pathologie_Etape2.glb_nom_contexte
                ctr_glb_label_origine = UITest.Pathologie_Oncologie.glb_label_origine
                ctr_glb_label_topo = UITest.Pathologie_Oncologie.glb_label_topo
                ctl_glb_label_FN = UITest.Pathologie_Oncologie.glb_label_FN
                ctl_glb_label_niveau = UITest.Pathologie_Oncologie.glb_label_Niveau
                ctl_glb_label_reca = UITest.Pathologie_Oncologie.glb_label_recalibrage
                ctl_glb_label_cote = UITest.Pathologie_Oncologie.glb_label_cote
                ctl_glb_label_arthro = UITest.Pathologie_Oncologie.glb_label_arthrodese
                ctr_nomIntervention_commentaire = UITest.CreationDP.glb_textEditNomIntervention

                BD.ajouter_pathologie_oncologie("", controlleur_numMagic, ctl_glb_label_patho,
                                                      ctr_signal_contexte, ctl_glb_label_FN, ctr_glb_label_topo, ctr_glb_label_origine,
                                                      ctl_glb_label_niveau, ctl_glb_label_reca, ctl_glb_label_cote,
                                                      ctl_glb_label_arthro, ctr_nomIntervention_commentaire)

                nom_intervention = (ctl_glb_textEdit_intervention + " " + ctl_glb_label_patho + " " +
                                    ctr_signal_contexte + " " + ctl_glb_label_FN + " " + ctr_glb_label_topo + " " + ctr_glb_label_origine + " " +
                                    ctl_glb_label_niveau + " " + "Recalibrage: " + ctl_glb_label_reca + " " + concatenation_recalibrage + " " + ctl_glb_label_cote + " " + "Arthrodèse: " +
                                    ctl_glb_label_arthro + " " + concatenation_arthrodese)
                print(nom_intervention)
                ctr_nomIntervention_nonModifiable = nom_intervention

                self.windowCreationDP.textEdit_interventionNonModifiable.setText(nom_intervention)

                if validerRecalibrage == True:
                    BD.ajouter_formuaire_recalibrage("", controlleur_numMagic, reca_postAnt2, reca_infos2,
                                                     reca_hernie2)
                    UITest.Formulaire_Recalibrage.validerRecalibrage = False

                if validerArthrodese == True:
                    BD.ajouter_formuaire_arthrodese("", controlleur_numMagic, arthro_postAnt2, arthro_fixation2,
                                                arthro_greffe2)
                    UITest.Formulaire_Arthrodese.validerArthrodese = False

                ctr_glb_label_origine = ""
                ctr_glb_label_topo = ""
                ctl_glb_label_patho = ""
                ctl_glb_label_FN = ""
                ctr_signal_contexte = ""
                ctl_glb_textEdit_intervention = ""
                ctl_glb_label_niveau = ""
                ctl_glb_label_reca = ""
                ctl_glb_label_cote = ""
                ctl_glb_label_arthro = ""
                UITest.Pathologie_Oncologie.validerOnco = False


        if validerTraumato == True:
                controlleur_percutanee2 = UITest.Pathologie_Traumatologique.glb_traumato_modalite_percutanee2
                controlleur_foyer2 = UITest.Pathologie_Traumatologique.glb_traumato_modalite_foyer2

                controlleur_numMagic = UITest.CreationDP.patient_numMagic
                ctl_glb_textEdit_intervention = UITest.CreationDP.glb_textEdit_intervention
                ctr_signal_contexte = UITest.Pathologie_Etape2.glb_nom_contexte
                ctr_glb_label_corpo = UITest.Pathologie_Traumatologique.glb_label_corpo
                ctr_glb_label_osteo = UITest.Pathologie_Traumatologique.glb_label_osteo
                ctr_glb_label_modalite = UITest.Pathologie_Traumatologique.glb_label_modalite
                ctl_glb_label_FN = UITest.Pathologie_Traumatologique.glb_label_FN
                ctl_glb_label_niveau = UITest.Pathologie_Traumatologique.glb_label_Niveau
                ctl_glb_label_reca = UITest.Pathologie_Traumatologique.glb_label_recalibrage
                ctl_glb_label_cote = UITest.Pathologie_Traumatologique.glb_label_cote
                ctl_glb_label_arthro = UITest.Pathologie_Traumatologique.glb_label_arthrodese
                ctr_nomIntervention_commentaire = UITest.CreationDP.glb_textEditNomIntervention
                ctr_niveaux_zoneC = UITest.Traumatologique_Niveaux.glb_zoneC
                ctr_niveaux_CDLS = UITest.Traumatologique_Niveaux.glb_zoneCDLS
                ctr_niveaux_zoneL = UITest.Traumatologique_Niveaux.glb_zoneL
                ctr_niveaux_zoneS = UITest.Traumatologique_Niveaux.glb_zoneS
                ctr_niveaux_zoneD = UITest.Traumatologique_Niveaux.glb_zoneD


                if (controlleur_percutanee2 == True):
                    BD.ajouter_pathologie_traumatologique("", controlleur_numMagic, ctl_glb_label_patho,
                                                      ctr_signal_contexte, ctl_glb_label_FN, ctr_glb_label_modalite, ctr_glb_label_corpo, ctr_glb_label_osteo,
                                                      "", "", "", "", ctr_nomIntervention_commentaire)

                    BD.ajouter_traumato_niveaux("", controlleur_numMagic, ctr_niveaux_CDLS, ctr_niveaux_zoneC,
                                                ctr_niveaux_zoneD, ctr_niveaux_zoneL, ctr_niveaux_zoneS)

                    nom_intervention = (ctl_glb_textEdit_intervention + " " + ctl_glb_label_patho + " " +
                                    ctr_signal_contexte + " " + ctl_glb_label_FN + " " + ctr_glb_label_modalite + " " + concatenation_traumato_niveau + " " + ctr_glb_label_corpo + " " + ctr_glb_label_osteo)

                    print(nom_intervention)

                    self.windowCreationDP.textEdit_interventionNonModifiable.setText(nom_intervention)
                    ctr_nomIntervention_nonModifiable = nom_intervention

                    concatenation_traumato_niveau = ""
                    controlleur_percutanee2 = False


                if (controlleur_foyer2 == True):
                    BD.ajouter_pathologie_traumatologique("", controlleur_numMagic, ctl_glb_label_patho,
                                                          ctr_signal_contexte, ctl_glb_label_FN, ctr_glb_label_modalite,
                                                          "", "",
                                                          ctl_glb_label_niveau, ctl_glb_label_reca, ctl_glb_label_cote,
                                                          ctl_glb_label_arthro, ctr_nomIntervention_commentaire)

                    nom_intervention = (ctl_glb_textEdit_intervention + " " + ctl_glb_label_patho + " " +
                                          ctr_signal_contexte + " " + ctl_glb_label_FN + " " + ctr_glb_label_modalite + " " +
                                          ctl_glb_label_niveau + " " + "Recalibrage: " + ctl_glb_label_reca + " " + concatenation_recalibrage + " " + ctl_glb_label_cote + " " + "Arthrodèse: " +
                                          ctl_glb_label_arthro + " " + concatenation_arthrodese)

                    print(nom_intervention)
                    ctr_nomIntervention_nonModifiable = nom_intervention

                    self.windowCreationDP.textEdit_interventionNonModifiable.setText(nom_intervention)
                    controlleur_foyer2 = False

                if validerRecalibrage == True:
                    BD.ajouter_formuaire_recalibrage("", controlleur_numMagic, reca_postAnt2, reca_infos2,
                                                     reca_hernie2)
                    UITest.Formulaire_Recalibrage.validerRecalibrage = False

                if validerArthrodese == True:
                    BD.ajouter_formuaire_arthrodese("", controlleur_numMagic, arthro_postAnt2, arthro_fixation2,
                                                arthro_greffe2)
                    UITest.Formulaire_Arthrodese.validerArthrodese = False

                ctr_glb_label_corpo = ""
                ctr_glb_label_osteo = ""
                ctr_glb_label_modalite = ""
                ctl_glb_label_patho = ""
                ctl_glb_label_FN = ""
                ctr_signal_contexte = ""
                ctl_glb_textEdit_intervention = ""
                ctl_glb_label_niveau = ""
                ctl_glb_label_reca = ""
                ctl_glb_label_cote = ""
                ctl_glb_label_arthro = ""
                UITest.Traumatologique_Niveaux.compteur_recuperation = ""
                validerTraumato = False
                UITest.Pathologie_Traumatologique.validerTraumato = False

        self.windowDegeneratif.hide()
        self.windowOncologique.hide()
        self.windowTraumato.hide()
        self.windowsSelectionnerDP_suite.hide()
        self.etape2.show()

    def show_Degeneratif(self):
        global controlleur_zoneCervicale, controlleur_zoneDorsale, controlleur_zoneLombaire, controlleur_zoneSacro
        global controlleur_FN_radicoMedullaire, controlleur_FN_radiculaire, controlleur_FN_medullaire, controlleur_FN_non
        global controlleur_vertebre1, controlleur_vertebre2
        global controlleur_recalibrage_hernie, controlleur_recalibrage_non, controlleur_recalibrage_oui
        global controlleur_cote_bilateral, controlleur_cote_droit, controlleur_cote_gauche
        global controlleur_arthrodese_non, controlleur_arthrodese_oui
        global ctl_glb_label_patho
        global validerRecalibrage, validerArthrodese, concatenation_arthrodese, concatenation_recalibrage
        global ctr_reca_postAnt,  ctr_reca_infos, ctr_reca_hernie, ctr_arthro_postAnt, ctr_arthro_greffe, ctr_arthro_fixation, BD
        global control_med_creaDP, control_med_selecDP, control_sec_creaDP, control_sec_selecDP, arthro_postAnt2, arthro_greffe2, arthro_fixation2, reca_postAnt2, reca_infos2, reca_hernie2


        controlleur_zoneCervicale = UITest.Pathologie_Etape2.signal_cervicale
        controlleur_zoneDorsale = UITest.Pathologie_Etape2.signal_dorsale
        controlleur_zoneLombaire = UITest.Pathologie_Etape2.signal_lombaire
        controlleur_zoneSacro = UITest.Pathologie_Etape2.signal_sacro

        control_med_creaDP = UITest.Accueil_Medecin.signal_med_creationDP
        control_med_selecDP = UITest.Accueil_Medecin.signal_med_selectionDP
        control_sec_creaDP = UITest.Accueil_Secretaire.signal_sec_creationDP
        control_sec_selecDP = UITest.Accueil_Secretaire.signal_sec_selectionDP

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

        validerArthrodese = UITest.Formulaire_Arthrodese.validerArthrodese
        validerRecalibrage = UITest.Formulaire_Recalibrage.validerRecalibrage

        self.windowCreationDP = MainWindow_CreationDP()
        self.etape2 = MainWindow_Etape2()
        self.windowRecalibrage = MainWindow_FormRecalibrage()
        self.windowArthrodese = MainWindow_FormArthrodese()
        self.windowDegeneratif = MainWindow_Degeneratif()
        self.windowsSelectionnerDP_suite = MainWindow_SelectionnerDP_suite()


        # actions de chaque bouton en fct du window
        self.windowDegeneratif.switch_window1.connect(self.show_Etape2)
        self.windowDegeneratif.switch_window3.connect(self.show_Recalibrage)
        self.windowDegeneratif.switch_window4.connect(self.show_Arthrodese)
        self.windowDegeneratif.switch_window5.connect(self.show_Etape2)

        if control_med_creaDP == True:
            self.windowDegeneratif.switch_window2.connect(self.show_CreationDP)
            self.windowDegeneratif.switch_window6.connect(self.show_CreationDP)
        elif control_med_selecDP == True:
            self.windowDegeneratif.switch_window2.connect(self.show_SelectionnerDP_suite)
            self.windowDegeneratif.switch_window6.connect(self.show_SelectionnerDP_suite)
        elif control_sec_creaDP == True:
            self.windowDegeneratif.switch_window2.connect(self.show_CreationDP)
            self.windowDegeneratif.switch_window6.connect(self.show_CreationDP)
        elif control_sec_selecDP == True:
            self.windowDegeneratif.switch_window2.connect(self.show_SelectionnerDP_suite)
            self.windowDegeneratif.switch_window6.connect(self.show_SelectionnerDP_suite)


        if (controlleur_zoneCervicale == True):
            ctl_glb_label_patho = "zone Cervicale"
            self.windowDegeneratif.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneDorsale == True):
            ctl_glb_label_patho = "zone Dorsale"
            self.windowDegeneratif.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneLombaire == True):
            ctl_glb_label_patho = "zone Lombaire"
            self.windowDegeneratif.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneSacro == True):
            ctl_glb_label_patho = "zone Sacro-coccygienne"
            self.windowDegeneratif.label_patho.setText(ctl_glb_label_patho)

        if (controlleur_zoneCervicale == True and controlleur_zoneDorsale == True):
            ctl_glb_label_patho = "zones Cervicale et Dorsale"
            self.windowDegeneratif.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneDorsale == True and controlleur_zoneLombaire == True):
            ctl_glb_label_patho = "zones Dorsale et Lombaire"
            self.windowDegeneratif.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneLombaire == True and controlleur_zoneSacro == True):
            ctl_glb_label_patho = "zones Lombaire et Sacro-coccygienne"
            self.windowDegeneratif.label_patho.setText(ctl_glb_label_patho)

        self.windowDegeneratif.label_patho.setText(ctl_glb_label_patho)
        ctl_glb_label_patho = self.windowDegeneratif.label_patho.text()

        concatenation_arthrodese = " "
        concatenation_recalibrage = " "

        if validerRecalibrage == True:
            ctr_reca_postAnt = UITest.Formulaire_Recalibrage.glb_reca_postAnt
            ctr_reca_hernie = UITest.Formulaire_Recalibrage.glb_reca_hernie_associer
            ctr_reca_infos = UITest.Formulaire_Recalibrage.glb_reca_infos

            reca_postAnt2 = ctr_reca_postAnt
            reca_infos2 = ctr_reca_infos
            reca_hernie2 = ctr_reca_hernie

            concatenation_recalibrage = ctr_reca_postAnt + " " + ctr_reca_infos + " " + ctr_reca_hernie

            ctr_reca_postAnt = ""
            ctr_reca_hernie = ""
            ctr_reca_infos = ""
            UITest.Formulaire_Recalibrage.validerRecalibrage = False

        if validerArthrodese == True:
            ctr_arthro_postAnt = UITest.Formulaire_Arthrodese.glb_arthro_postAnt
            ctr_arthro_fixation = UITest.Formulaire_Arthrodese.glb_arthro_fixation
            ctr_arthro_greffe = UITest.Formulaire_Arthrodese.glb_arthro_greffe

            arthro_postAnt2 = ctr_arthro_postAnt
            arthro_fixation2 = ctr_arthro_fixation
            arthro_greffe2 = ctr_arthro_greffe

            concatenation_arthrodese = ctr_arthro_postAnt + " " + ctr_arthro_fixation + " " + ctr_arthro_greffe

            ctr_arthro_postAnt = ""
            ctr_arthro_fixation = ""
            ctr_arthro_greffe = ""
            UITest.Formulaire_Arthrodese.validerArthrodese = False


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
        self.windowDegeneratif.radioButton_arthrodeseNon.setChecked(controlleur_arthrodese_non)

        self.etape2.hide()
        self.windowRecalibrage.hide()
        self.windowArthrodese.hide()
        self.windowsSelectionnerDP_suite.hide()

        self.windowDegeneratif.show()

    def show_Oncologique(self):
        global controlleur_zoneCervicale, controlleur_zoneDorsale, controlleur_zoneLombaire, controlleur_zoneSacro
        global controlleur_FN_radicoMedullaire, controlleur_FN_radiculaire, controlleur_FN_medullaire, controlleur_FN_non
        global controlleur_vertebre1, controlleur_vertebre2
        global controlleur_recalibrage_hernie, controlleur_recalibrage_non, controlleur_recalibrage_oui
        global controlleur_cote_bilateral, controlleur_cote_droit, controlleur_cote_gauche
        global controlleur_topo_epidurale, controlleur_topo_osseuse, controlleur_topo_intraDurale, controlleur_topo_intraMedullaire, controlleur_topo_enSablier, controlleur_topo_autre
        global controlleur_origine_radiculaire, controlleur_origine_meningee, controlleur_origine_osseuse, controlleur_origine_secondaire, controlleur_origine_medullaire, controlleur_origine_autre
        global controlleur_arthrodese_non, controlleur_arthrodese_oui
        global ctl_glb_label_patho
        global validerRecalibrage, validerArthrodese, concatenation_arthrodese, concatenation_recalibrage
        global ctr_reca_postAnt, ctr_reca_infos, ctr_reca_hernie, ctr_arthro_postAnt, ctr_arthro_greffe, ctr_arthro_fixation, BD
        global control_med_creaDP, control_med_selecDP, control_sec_creaDP, control_sec_selecDP, arthro_postAnt2, arthro_greffe2, arthro_fixation2, reca_postAnt2, reca_infos2, reca_hernie2

        BD = Connexion_DB()
        BD.connexion_DB()

        controlleur_zoneCervicale = UITest.Pathologie_Etape2.signal_cervicale
        controlleur_zoneDorsale = UITest.Pathologie_Etape2.signal_dorsale
        controlleur_zoneLombaire = UITest.Pathologie_Etape2.signal_lombaire
        controlleur_zoneSacro = UITest.Pathologie_Etape2.signal_sacro

        controlleur_FN_radicoMedullaire = UITest.Pathologie_Oncologie.glb_onco_FN_radicoMedullaire
        controlleur_FN_radiculaire = UITest.Pathologie_Oncologie.glb_onco_FN_radiculaire
        controlleur_FN_medullaire = UITest.Pathologie_Oncologie.glb_onco_FN_medullaire
        controlleur_FN_non = UITest.Pathologie_Oncologie.glb_onco_FN_non
        controlleur_vertebre1 = UITest.Pathologie_Oncologie.onco_vertebre1
        controlleur_vertebre2 = UITest.Pathologie_Oncologie.onco_vertebre2
        controlleur_recalibrage_hernie = UITest.Pathologie_Oncologie.onco_recalibrage_hernie
        controlleur_recalibrage_non = UITest.Pathologie_Oncologie.onco_recalibrage_non
        controlleur_recalibrage_oui = UITest.Pathologie_Oncologie.onco_recalibrage_oui

        control_med_creaDP = UITest.Accueil_Medecin.signal_med_creationDP
        control_med_selecDP = UITest.Accueil_Medecin.signal_med_selectionDP
        control_sec_creaDP = UITest.Accueil_Secretaire.signal_sec_creationDP
        control_sec_selecDP = UITest.Accueil_Secretaire.signal_sec_selectionDP

        controlleur_cote_bilateral = UITest.Pathologie_Oncologie.glb_onco_cote_bilateral
        controlleur_cote_gauche = UITest.Pathologie_Oncologie.glb_onco_cote_gauche
        controlleur_cote_droit = UITest.Pathologie_Oncologie.glb_onco_cote_droit
        controlleur_arthrodese_non = UITest.Pathologie_Oncologie.onco_arthrodese_non
        controlleur_arthrodese_oui = UITest.Pathologie_Oncologie.onco_arthrodese_oui

        controlleur_origine_autre = UITest.Pathologie_Oncologie.glb_onco_origine_autre
        controlleur_origine_radiculaire = UITest.Pathologie_Oncologie.glb_onco_origine_radiculaire
        controlleur_origine_meningee = UITest.Pathologie_Oncologie.glb_onco_origine_meningee
        controlleur_origine_osseuse = UITest.Pathologie_Oncologie.glb_onco_origine_osseuse
        controlleur_origine_secondaire = UITest.Pathologie_Oncologie.glb_onco_origine_secondaire
        controlleur_origine_medullaire = UITest.Pathologie_Oncologie.glb_onco_origine_medullaire

        controlleur_topo_autre = UITest.Pathologie_Oncologie.glb_onco_topo_autre
        controlleur_topo_epidurale = UITest.Pathologie_Oncologie.glb_onco_topo_epidurale
        controlleur_topo_intraMedullaire = UITest.Pathologie_Oncologie.glb_onco_topo_intraMedullaire
        controlleur_topo_intraDurale = UITest.Pathologie_Oncologie.glb_onco_topo_intraDurale
        controlleur_topo_enSablier = UITest.Pathologie_Oncologie.glb_onco_topo_enSablier
        controlleur_topo_osseuse = UITest.Pathologie_Oncologie.glb_onco_topo_osseuse

        validerArthrodese = UITest.Formulaire_Arthrodese.validerArthrodese
        validerRecalibrage = UITest.Formulaire_Recalibrage.validerRecalibrage

        self.windowCreationDP = MainWindow_CreationDP()
        self.etape2 = MainWindow_Etape2()
        self.windowRecalibrage = MainWindow_FormRecalibrage()
        self.windowArthrodese = MainWindow_FormArthrodese()
        self.windowOncologique = MainWindow_Oncologie()
        self.windowsSelectionnerDP_suite = MainWindow_SelectionnerDP_suite()


        # actions de chaque bouton en fct du window
        self.windowOncologique.switch_window1.connect(self.show_Etape2)
        self.windowOncologique.switch_window2.connect(self.show_CreationDP)
        self.windowOncologique.switch_window3.connect(self.show_Recalibrage)
        self.windowOncologique.switch_window4.connect(self.show_Arthrodese)
        self.windowOncologique.switch_window5.connect(self.show_Etape2)


        if control_med_creaDP == True:
            self.windowOncologique.switch_window2.connect(self.show_CreationDP)
            self.windowOncologique.switch_window6.connect(self.show_CreationDP)
        elif control_med_selecDP == True:
            self.windowOncologique.switch_window2.connect(self.show_SelectionnerDP_suite)
            self.windowOncologique.switch_window6.connect(self.show_SelectionnerDP_suite)
        elif control_sec_creaDP == True:
            self.windowOncologique.switch_window2.connect(self.show_CreationDP)
            self.windowOncologique.switch_window6.connect(self.show_CreationDP)
        elif control_sec_selecDP == True:
            self.windowOncologique.switch_window2.connect(self.show_SelectionnerDP_suite)
            self.windowOncologique.switch_window6.connect(self.show_SelectionnerDP_suite)

        if (controlleur_zoneCervicale == True):
            ctl_glb_label_patho = "zone Cervicale"
            self.windowOncologique.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneDorsale == True):
            ctl_glb_label_patho = "zone Dorsale"
            self.windowOncologique.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneLombaire == True):
            ctl_glb_label_patho = "zone Lombaire"
            self.windowOncologique.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneSacro == True):
            ctl_glb_label_patho = "zone Sacro-coccygienne"
            self.windowOncologique.label_patho.setText(ctl_glb_label_patho)

        if (controlleur_zoneCervicale == True and controlleur_zoneDorsale == True):
            ctl_glb_label_patho = "zones Cervicale et Dorsale"
            self.windowOncologique.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneDorsale == True and controlleur_zoneLombaire == True):
            ctl_glb_label_patho = "zones Dorsale et Lombaire"
            self.windowOncologique.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneLombaire == True and controlleur_zoneSacro == True):
            ctl_glb_label_patho = "zones Lombaire et Sacro-coccygienne"
            self.windowOncologique.label_patho.setText(ctl_glb_label_patho)

        self.windowOncologique.label_patho.setText(ctl_glb_label_patho)
        ctl_glb_label_patho = self.windowOncologique.label_patho.text()

        concatenation_arthrodese = " "
        concatenation_recalibrage = " "
        if validerRecalibrage == True:
            ctr_reca_postAnt = UITest.Formulaire_Recalibrage.glb_reca_postAnt
            ctr_reca_hernie = UITest.Formulaire_Recalibrage.glb_reca_hernie_associer
            ctr_reca_infos = UITest.Formulaire_Recalibrage.glb_reca_infos

            reca_postAnt2 = ctr_reca_postAnt
            reca_infos2 = ctr_reca_infos
            reca_hernie2 = ctr_reca_hernie

            concatenation_recalibrage = ctr_reca_postAnt + " " + ctr_reca_infos + " " + ctr_reca_hernie

            ctr_reca_postAnt = ""
            ctr_reca_hernie = ""
            ctr_reca_infos = ""
            UITest.Formulaire_Recalibrage.validerRecalibrage = False

        if validerArthrodese == True:
            ctr_arthro_postAnt = UITest.Formulaire_Arthrodese.glb_arthro_postAnt
            ctr_arthro_fixation = UITest.Formulaire_Arthrodese.glb_arthro_fixation
            ctr_arthro_greffe = UITest.Formulaire_Arthrodese.glb_arthro_greffe

            arthro_postAnt2 = ctr_arthro_postAnt
            arthro_fixation2 = ctr_arthro_fixation
            arthro_greffe2 = ctr_arthro_greffe

            concatenation_arthrodese = ctr_arthro_postAnt + " " + ctr_arthro_fixation + " " + ctr_arthro_greffe


            ctr_arthro_postAnt = ""
            ctr_arthro_fixation = ""
            ctr_arthro_greffe = ""
            UITest.Formulaire_Arthrodese.validerArthrodese = False

        self.windowOncologique.spinBox_nombre1.setValue(controlleur_vertebre1)
        self.windowOncologique.spinBox_nombre2.setValue(controlleur_vertebre2)
        self.windowOncologique.radioButton_medullaire.setChecked(controlleur_FN_medullaire)
        self.windowOncologique.radioButton_radicoMedullaire.setChecked(controlleur_FN_radicoMedullaire)
        self.windowOncologique.radioButton_non.setChecked(controlleur_FN_non)
        self.windowOncologique.radioButton_radiculaire.setChecked(controlleur_FN_radiculaire)
        self.windowOncologique.radioButton_recalibrageNon.setChecked(controlleur_recalibrage_non)
        self.windowOncologique.radioButton_recalibrageOui.setChecked(controlleur_recalibrage_oui)
        self.windowOncologique.radioButton_herniePure.setChecked(controlleur_recalibrage_hernie)
        self.windowOncologique.radioButton_Droit.setChecked(controlleur_cote_droit)
        self.windowOncologique.radioButton_gauche.setChecked(controlleur_cote_gauche)
        self.windowOncologique.radioButton_bilateral.setChecked(controlleur_cote_bilateral)
        self.windowOncologique.radioButton_arthrodeseOui.setChecked(controlleur_arthrodese_oui)
        self.windowOncologique.radioButton_arthrodeseNon.setChecked(controlleur_arthrodese_non)
        self.windowOncologique.checkBox_enSablier.setChecked(controlleur_topo_enSablier)
        self.windowOncologique.checkBox_epidurale.setChecked(controlleur_topo_epidurale)
        self.windowOncologique.checkBox_osseuseTopographie.setChecked(controlleur_topo_osseuse)
        self.windowOncologique.checkBox_intraMedullaire.setChecked(controlleur_topo_intraMedullaire)
        self.windowOncologique.checkBox_intraDurale.setChecked(controlleur_topo_intraDurale)
        self.windowOncologique.checkBox_autreTopographie.setChecked(controlleur_topo_autre)
        self.windowOncologique.checkBox_origineRadiculaire.setChecked(controlleur_origine_radiculaire)
        self.windowOncologique.checkBox_meningee.setChecked(controlleur_origine_meningee)
        self.windowOncologique.checkBox_origineOsseuse.setChecked(controlleur_origine_osseuse)
        self.windowOncologique.checkBox_secondaire.setChecked(controlleur_origine_secondaire)
        self.windowOncologique.checkBox_origineMedullaire.setChecked(controlleur_origine_medullaire)
        self.windowOncologique.checkBox_origineAutre.setChecked(controlleur_origine_autre)

        self.etape2.hide()
        self.windowRecalibrage.hide()
        self.windowArthrodese.hide()
        self.windowsSelectionnerDP_suite.hide()

        self.windowOncologique.show()

    def show_Traumatologique(self):
        global controlleur_zoneCervicale, controlleur_zoneDorsale, controlleur_zoneLombaire, controlleur_zoneSacro
        global controlleur_FN_radicoMedullaire, controlleur_FN_radiculaire, controlleur_FN_medullaire, controlleur_FN_non
        global controlleur_vertebre1, controlleur_vertebre2
        global controlleur_recalibrage_hernie, controlleur_recalibrage_non, controlleur_recalibrage_oui
        global controlleur_cote_bilateral, controlleur_cote_droit, controlleur_cote_gauche

        global controlleur_percutanee , controlleur_foyer , controlleur_corpo_vertebro , controlleur_corpo_cypho , controlleur_corpo_non , controlleur_osteo_mono, controlleur_osteo_poly ,controlleur_osteo_non
        global controlleur_arthrodese_non, controlleur_arthrodese_oui
        global ctl_glb_label_patho
        global validerRecalibrage, validerArthrodese, concatenation_arthrodese, concatenation_recalibrage, validerNiveaux, concatenation_traumato_niveau
        global ctr_reca_postAnt, ctr_reca_infos, ctr_reca_hernie, ctr_arthro_postAnt, ctr_arthro_greffe, ctr_arthro_fixation, BD
        global control_med_creaDP, control_med_selecDP, control_sec_creaDP, control_sec_selecDP
        global ctr_niveaux_zoneC, ctr_niveaux_CDLS, ctr_niveaux_zoneD, ctr_niveaux_zoneL, ctr_niveaux_zoneS, arthro_postAnt2, arthro_greffe2, arthro_fixation2, reca_postAnt2, reca_infos2, reca_hernie2

        BD = Connexion_DB()
        BD.connexion_DB()

        controlleur_zoneCervicale = UITest.Pathologie_Etape2.signal_cervicale
        controlleur_zoneDorsale = UITest.Pathologie_Etape2.signal_dorsale
        controlleur_zoneLombaire = UITest.Pathologie_Etape2.signal_lombaire
        controlleur_zoneSacro = UITest.Pathologie_Etape2.signal_sacro

        self.windowCreationDP = MainWindow_CreationDP()
        self.etape2 = MainWindow_Etape2()
        self.windowRecalibrage = MainWindow_FormRecalibrage()
        self.windowArthrodese = MainWindow_FormArthrodese()
        self.windowNiveau = MainWindow_Niveau()
        self.windowsSelectionnerDP_suite = MainWindow_SelectionnerDP_suite()
        self.windowTraumato = MainWindow_Traumatologie()

        controlleur_FN_radicoMedullaire = UITest.Pathologie_Traumatologique.glb_traumato_FN_radicoMedullaire
        controlleur_FN_radiculaire = UITest.Pathologie_Traumatologique.glb_traumato_FN_radiculaire
        controlleur_FN_medullaire = UITest.Pathologie_Traumatologique.glb_traumato_FN_medullaire
        controlleur_FN_non = UITest.Pathologie_Traumatologique.glb_traumato_FN_non
        controlleur_vertebre1 = UITest.Pathologie_Traumatologique.traumato_vertebre1
        controlleur_vertebre2 = UITest.Pathologie_Traumatologique.traumato_vertebre2
        controlleur_recalibrage_hernie = UITest.Pathologie_Traumatologique.traumato_recalibrage_hernie
        controlleur_recalibrage_non = UITest.Pathologie_Traumatologique.traumato_recalibrage_non
        controlleur_recalibrage_oui = UITest.Pathologie_Traumatologique.traumato_recalibrage_oui

        control_med_creaDP = UITest.Accueil_Medecin.signal_med_creationDP
        control_med_selecDP = UITest.Accueil_Medecin.signal_med_selectionDP
        control_sec_creaDP = UITest.Accueil_Secretaire.signal_sec_creationDP
        control_sec_selecDP = UITest.Accueil_Secretaire.signal_sec_selectionDP

        controlleur_cote_bilateral = UITest.Pathologie_Traumatologique.glb_traumato_cote_bilateral
        controlleur_cote_gauche = UITest.Pathologie_Traumatologique.glb_traumato_cote_gauche
        controlleur_cote_droit = UITest.Pathologie_Traumatologique.glb_traumato_cote_droit
        controlleur_arthrodese_non = UITest.Pathologie_Traumatologique.traumato_arthrodese_non
        controlleur_arthrodese_oui = UITest.Pathologie_Traumatologique.traumato_arthrodese_oui

        controlleur_percutanee = UITest.Pathologie_Traumatologique.glb_traumato_modalite_percutanee
        controlleur_foyer = UITest.Pathologie_Traumatologique.glb_traumato_modalite_foyer
        controlleur_corpo_vertebro = UITest.Pathologie_Traumatologique.glb_traumato_corpo_vertebro
        controlleur_corpo_cypho = UITest.Pathologie_Traumatologique.glb_traumato_corpo_cypho
        controlleur_corpo_non = UITest.Pathologie_Traumatologique.glb_traumato_corpo_non
        controlleur_osteo_mono = UITest.Pathologie_Traumatologique.glb_traumato_osteo_mono
        controlleur_osteo_poly = UITest.Pathologie_Traumatologique.glb_traumato_osteo_poly
        controlleur_osteo_non = UITest.Pathologie_Traumatologique.glb_traumato_osteo_non

        validerArthrodese = UITest.Formulaire_Arthrodese.validerArthrodese
        validerRecalibrage = UITest.Formulaire_Recalibrage.validerRecalibrage
        validerNiveaux = UITest.Traumatologique_Niveaux.validerNiveaux

        self.nbVertebre = UITest.Traumatologique_Niveaux.compteur_recuperation
        self.windowTraumato.lineEdit_nombreVertebre.setText(self.nbVertebre)

        # actions de chaque bouton en fct du window
        self.windowTraumato.switch_window1.connect(self.show_Etape2)
        self.windowTraumato.switch_window2.connect(self.show_CreationDP)
        self.windowTraumato.switch_window3.connect(self.show_Niveau)
        self.windowTraumato.switch_window4.connect(self.show_Recalibrage)
        self.windowTraumato.switch_window5.connect(self.show_Arthrodese)
        self.windowTraumato.switch_window7.connect(self.show_Etape2)


        if control_med_creaDP == True:
            self.windowTraumato.switch_window2.connect(self.show_CreationDP)
            self.windowTraumato.switch_window8.connect(self.show_CreationDP)
        elif control_med_selecDP == True:
            self.windowTraumato.switch_window2.connect(self.show_SelectionnerDP_suite)
            self.windowTraumato.switch_window8.connect(self.show_SelectionnerDP_suite)
        elif control_sec_creaDP == True:
            self.windowTraumato.switch_window2.connect(self.show_CreationDP)
            self.windowTraumato.switch_window8.connect(self.show_CreationDP)
        elif control_sec_selecDP == True:
            self.windowTraumato.switch_window2.connect(self.show_SelectionnerDP_suite)
            self.windowTraumato.switch_window8.connect(self.show_SelectionnerDP_suite)


        if (controlleur_zoneCervicale == True):
            ctl_glb_label_patho = "zone Cervicale"
            self.windowTraumato.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneDorsale == True):
            ctl_glb_label_patho = "zone Dorsale"
            self.windowTraumato.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneLombaire == True):
            ctl_glb_label_patho = "zone Lombaire"
            self.windowTraumato.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneSacro == True):
            ctl_glb_label_patho = "zone Sacro-coccygienne"
            self.windowTraumato.label_patho.setText(ctl_glb_label_patho)

        if (controlleur_zoneCervicale == True and controlleur_zoneDorsale == True):
            ctl_glb_label_patho = "zones Cervicale et Dorsale"
            self.windowTraumato.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneDorsale == True and controlleur_zoneLombaire == True):
            ctl_glb_label_patho = "zones Dorsale et Lombaire"
            self.windowTraumato.label_patho.setText(ctl_glb_label_patho)
        if (controlleur_zoneLombaire == True and controlleur_zoneSacro == True):
            ctl_glb_label_patho = "zones Lombaire et Sacro-coccygienne"
            self.windowTraumato.label_patho.setText(ctl_glb_label_patho)

        self.windowTraumato.label_patho.setText(ctl_glb_label_patho)
        ctl_glb_label_patho = self.windowTraumato.label_patho.text()


        concatenation_arthrodese = " "
        concatenation_recalibrage = " "
        concatenation_traumato_niveau = " "

        if validerRecalibrage == True:
            ctr_reca_postAnt = UITest.Formulaire_Recalibrage.glb_reca_postAnt
            ctr_reca_hernie = UITest.Formulaire_Recalibrage.glb_reca_hernie_associer
            ctr_reca_infos = UITest.Formulaire_Recalibrage.glb_reca_infos

            reca_postAnt2 = ctr_reca_postAnt
            reca_infos2 = ctr_reca_infos
            reca_hernie2 = ctr_reca_hernie

            concatenation_recalibrage = ctr_reca_postAnt + " " + ctr_reca_infos + " " + ctr_reca_hernie

            ctr_reca_postAnt = ""
            ctr_reca_hernie = ""
            ctr_reca_infos = ""
            UITest.Formulaire_Recalibrage.validerRecalibrage = False


        if validerArthrodese == True:
            ctr_arthro_postAnt = UITest.Formulaire_Arthrodese.glb_arthro_postAnt
            ctr_arthro_fixation = UITest.Formulaire_Arthrodese.glb_arthro_fixation
            ctr_arthro_greffe = UITest.Formulaire_Arthrodese.glb_arthro_greffe

            arthro_postAnt2 = ctr_arthro_postAnt
            arthro_fixation2 = ctr_arthro_fixation
            arthro_greffe2 = ctr_arthro_greffe

            concatenation_arthrodese = ctr_arthro_postAnt + " " + ctr_arthro_fixation + " " + ctr_arthro_greffe


            ctr_arthro_postAnt = ""
            ctr_arthro_fixation = ""
            ctr_arthro_greffe = ""
            UITest.Formulaire_Arthrodese.validerArthrodese = False

        ctr_niveaux_zoneC = UITest.Traumatologique_Niveaux.glb_zoneC
        ctr_niveaux_CDLS = UITest.Traumatologique_Niveaux.glb_zoneCDLS
        ctr_niveaux_zoneL = UITest.Traumatologique_Niveaux.glb_zoneL
        ctr_niveaux_zoneS = UITest.Traumatologique_Niveaux.glb_zoneS
        ctr_niveaux_zoneD = UITest.Traumatologique_Niveaux.glb_zoneD
        if validerNiveaux == True:

            concatenation_traumato_niveau = " "

            concatenation_traumato_niveau = ctr_niveaux_CDLS + " " + ctr_niveaux_zoneC + " " + ctr_niveaux_zoneD + " " + ctr_niveaux_zoneL + " " + ctr_niveaux_zoneS


            ctr_niveaux_zoneC = " "
            ctr_niveaux_CDLS = " "
            ctr_niveaux_zoneL = " "
            ctr_niveaux_zoneS = " "
            ctr_niveaux_zoneD = " "
            UITest.Traumatologique_Niveaux.validerNiveaux = False


        self.windowTraumato.spinBox_nombre1.setValue(controlleur_vertebre1)
        self.windowTraumato.spinBox_nombre2.setValue(controlleur_vertebre2)
        self.windowTraumato.radioButton_medullaire.setChecked(controlleur_FN_medullaire)
        self.windowTraumato.radioButton_radicoMedullaire.setChecked(controlleur_FN_radicoMedullaire)
        self.windowTraumato.radioButton_non.setChecked(controlleur_FN_non)
        self.windowTraumato.radioButton_radiculaire.setChecked(controlleur_FN_radiculaire)
        self.windowTraumato.radioButton_recalibrageNon.setChecked(controlleur_recalibrage_non)
        self.windowTraumato.radioButton_recalibrageOui.setChecked(controlleur_recalibrage_oui)
        self.windowTraumato.radioButton_herniePure.setChecked(controlleur_recalibrage_hernie)
        self.windowTraumato.radioButton_Droit.setChecked(controlleur_cote_droit)
        self.windowTraumato.radioButton_gauche.setChecked(controlleur_cote_gauche)
        self.windowTraumato.radioButton_bilateral.setChecked(controlleur_cote_bilateral)
        self.windowTraumato.radioButton_arthrodeseOui.setChecked(controlleur_arthrodese_oui)
        self.windowTraumato.radioButton_arthrodeseNon.setChecked(controlleur_arthrodese_non)

        self.windowTraumato.radioButton_percutanee.setChecked(controlleur_percutanee)
        self.windowTraumato.radioButton_foyerOuvert.setChecked(controlleur_foyer)
        self.windowTraumato.radiobutton_vertebroplastie.setChecked(controlleur_corpo_vertebro)
        self.windowTraumato.radiobutton_cyphoplastie.setChecked(controlleur_corpo_cypho)
        self.windowTraumato.radiobutton_corporealNon.setChecked(controlleur_corpo_non)
        self.windowTraumato.radiobutton_visMonoaxiales.setChecked(controlleur_osteo_mono)
        self.windowTraumato.radiobutton_visPolyaxiales.setChecked(controlleur_osteo_poly)
        self.windowTraumato.radiobutton_osteosyntheseNon.setChecked(controlleur_osteo_non)


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
        self.windowsSelectionnerDP_suite = MainWindow_SelectionnerDP_suite()
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
        self.windowsSelectionnerDP_suite = MainWindow_SelectionnerDP_suite()
        self.windowArthrodese = MainWindow_FormArthrodese()


        if self.signal_degene == True:
            self.windowArthrodese.switch_window1.connect(self.show_Degeneratif)
            self.windowArthrodese.switch_window3.connect(self.show_Degeneratif)

        elif self.signal_trauma == True:
            self.windowArthrodese.switch_window1.connect(self.show_Traumatologique)
            self.windowArthrodese.switch_window3.connect(self.show_Traumatologique)
                # validerArthrodese = True

        elif self.signal_onco == True:
            self.windowArthrodese.switch_window1.connect(self.show_Oncologique)
            self.windowArthrodese.switch_window3.connect(self.show_Oncologique)



        self.windowArthrodese.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller_INPEC2 = Controller_Test()
    controller_INPEC2.show_Connexion()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()