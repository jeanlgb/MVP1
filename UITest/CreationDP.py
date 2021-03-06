from PyQt5.QtCore import QDate

import UITest as UITest
from PyQt5 import QtCore, QtGui, QtWidgets
from Utilisateur import *
from PyQt5.QtWidgets import QCalendarWidget, QLineEdit

# variables globales appelées dans controller_test
patient_nom = ("NOM")
patient_prenom = ("PRENOM")
patient_numMagic = ("NUMERO MAGIC")
patient_dateIntervention = ("")
patient_jour = ("1")
patient_mois = ("Janvier")
patient_annee = ("2000")
patient_anneeControlleur = int(2000)
patient_dateNaissance = ("21/04/1997")
valeur_cb_cervicale_radiculaire = False
valeur_cb_medullaire = False
valeur_cb_thoraco_lombaire = False
valeur_cb_autre = False
signal_eval = False
nomPathologieCR = "CR"

glb_textEdit_intervention = ""
glb_textEditNomIntervention = ""


class Ui_Frame_CreationDP(object):
    # Interface générée automatiquement via qtdesigner ==> def setupUi et def retranslateUI
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setEnabled(True)
        Frame.setFixedSize(900, 800)
        self.label_nom = QtWidgets.QLabel(Frame)
        self.label_nom.setGeometry(QtCore.QRect(130, 140, 141, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_nom.setFont(font)
        self.label_nom.setObjectName("label_nom")
        self.lineEdit_nom = QtWidgets.QLineEdit(Frame)
        self.lineEdit_nom.setGeometry(QtCore.QRect(270, 140, 271, 20))
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.lineEdit_prenom = QtWidgets.QLineEdit(Frame)
        self.lineEdit_prenom.setGeometry(QtCore.QRect(270, 195, 271, 20))
        self.lineEdit_prenom.setObjectName("lineEdit_prenom")
        self.comboBox_jour = QtWidgets.QComboBox(Frame)
        self.comboBox_jour.setGeometry(QtCore.QRect(270, 245, 51, 22))
        self.comboBox_jour.setMaxCount(31)
        self.comboBox_jour.setObjectName("comboBox_jour")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_jour.addItem("")
        self.comboBox_mois = QtWidgets.QComboBox(Frame)
        self.comboBox_mois.setGeometry(QtCore.QRect(350, 245, 81, 22))
        self.comboBox_mois.setObjectName("comboBox_mois")
        self.comboBox_mois.addItem("")
        self.comboBox_mois.addItem("")
        self.comboBox_mois.addItem("")
        self.comboBox_mois.addItem("")
        self.comboBox_mois.addItem("")
        self.comboBox_mois.addItem("")
        self.comboBox_mois.addItem("")
        self.comboBox_mois.addItem("")
        self.comboBox_mois.addItem("")
        self.comboBox_mois.addItem("")
        self.comboBox_mois.addItem("")
        self.comboBox_mois.addItem("")
        self.spinBox_annee = QtWidgets.QSpinBox(Frame)
        self.spinBox_annee.setGeometry(QtCore.QRect(460, 245, 81, 22))
        self.spinBox_annee.setMinimum(1900)
        self.spinBox_annee.setMaximum(2050)
        self.spinBox_annee.setProperty("value", 2000)
        self.spinBox_annee.setObjectName("spinBox_annee")
        self.lineEdit_numeroMagic = QtWidgets.QLineEdit(Frame)
        self.lineEdit_numeroMagic.setGeometry(QtCore.QRect(270, 295, 271, 20))
        self.lineEdit_numeroMagic.setObjectName("lineEdit_numeroMagic")
        self.checkBox_cervicalRadiculaire = QtWidgets.QCheckBox(Frame)
        self.checkBox_cervicalRadiculaire.setGeometry(QtCore.QRect(270, 340, 145, 20))
        self.checkBox_cervicalRadiculaire.setObjectName("checkBox_cervicalRadiculaire")
        self.checkBox_thoracoLombaire = QtWidgets.QCheckBox(Frame)
        self.checkBox_thoracoLombaire.setGeometry(QtCore.QRect(500, 340, 141, 20))
        self.checkBox_thoracoLombaire.setObjectName("checkBox_thoracoLombaire")
        self.checkBox_medullaire = QtWidgets.QCheckBox(Frame)
        self.checkBox_medullaire.setGeometry(QtCore.QRect(270, 370, 131, 20))
        self.checkBox_medullaire.setObjectName("checkBox_medullaire")
        self.checkBox_autre = QtWidgets.QCheckBox(Frame)
        self.checkBox_autre.setGeometry(QtCore.QRect(500, 370, 141, 20))
        self.checkBox_autre.setObjectName("checkBox_autre")
        self.textEdit_interventionNonModifiable = QtWidgets.QTextEdit(Frame)
        self.pushButton_ok = QtWidgets.QPushButton(Frame)
        self.pushButton_ok.setEnabled(False)
        self.pushButton_ok.setGeometry(QtCore.QRect(690, 350, 51, 23))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.textEdit_interventionNonModifiable.setGeometry(QtCore.QRect(270, 420, 271, 21))
        self.textEdit_interventionNonModifiable.setObjectName("textEdit_interventionNonModifiable")
        self.lineEdit_interventionModifiable = QtWidgets.QLineEdit(Frame)
        self.lineEdit_interventionModifiable.setGeometry(QtCore.QRect(270, 460, 271, 21))
        self.lineEdit_interventionModifiable.setObjectName("lineEdit_interventionModifiable")
        self.calendarWidget = QtWidgets.QCalendarWidget(Frame)
        self.calendarWidget.setFixedSize(400, 250)
        self.calendarWidget.setGeometry(QtCore.QRect(270, 510, 400, 200))
        self.calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.calendarWidget.setObjectName("calendarWidget")
        self.calendarWidget.setGridVisible(True)
        self.lineEdit_dateIntervention = QtWidgets.QLineEdit(Frame)
        self.lineEdit_dateIntervention.setGeometry(QtCore.QRect(710, 510, 141, 21))
        self.lineEdit_dateIntervention.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.lineEdit_dateIntervention.setObjectName("lineEdit_dateIntervention")
        self.pushButton_evaluation = QtWidgets.QPushButton(Frame)
        self.pushButton_evaluation.setGeometry(QtCore.QRect(700, 670, 80, 30))
        self.pushButton_evaluation.setObjectName("pushButton_evaluation")
        self.pushButton_annuler = QtWidgets.QPushButton(Frame)
        self.pushButton_annuler.setGeometry(QtCore.QRect(50, 40, 61, 30))
        self.pushButton_annuler.setObjectName("pushButton_annuler")
        self.label_nomIntervention = QtWidgets.QLabel(Frame)
        self.label_nomIntervention.setGeometry(QtCore.QRect(20, 410, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_nomIntervention.setFont(font)
        self.label_nomIntervention.setObjectName("label_nomIntervention")
        self.label_commentaire = QtWidgets.QLabel(Frame)
        self.label_commentaire.setGeometry(QtCore.QRect(20, 460, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_commentaire.setFont(font)
        self.label_commentaire.setObjectName("label_commentaire")
        self.label_prenom = QtWidgets.QLabel(Frame)
        self.label_prenom.setGeometry(QtCore.QRect(94, 190, 181, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_prenom.setFont(font)
        self.label_prenom.setObjectName("label_prenom")
        self.label_titre = QtWidgets.QLabel(Frame)
        self.label_titre.setGeometry(QtCore.QRect(10, 40, 651, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_titre.setFont(font)
        self.label_titre.setObjectName("label_titre")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(10, 530, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setObjectName("label")
        self.label_dateDeNaissance = QtWidgets.QLabel(Frame)
        self.label_dateDeNaissance.setGeometry(QtCore.QRect(10, 240, 261, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_dateDeNaissance.setFont(font)
        self.label_dateDeNaissance.setObjectName("label_dateDeNaissance")
        self.label_pathologie = QtWidgets.QLabel(Frame)
        self.label_pathologie.setGeometry(QtCore.QRect(90, 340, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_pathologie.setFont(font)
        self.label_pathologie.setObjectName("label_pathologie")
        self.label_dateIntervention = QtWidgets.QLabel(Frame)
        self.label_dateIntervention.setGeometry(QtCore.QRect(20, 500, 261, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_dateIntervention.setFont(font)
        self.label_dateIntervention.setObjectName("label_dateIntervention")
        self.label_numeroMagic = QtWidgets.QLabel(Frame)
        self.label_numeroMagic.setGeometry(QtCore.QRect(10, 290, 261, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_numeroMagic.setFont(font)
        self.label_numeroMagic.setObjectName("label_numeroMagic")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(330, 245, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(440, 245, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_recuperationDateDeNaissance = QtWidgets.QLabel(Frame)
        self.label_recuperationDateDeNaissance.setEnabled(False)
        self.label_recuperationDateDeNaissance.setGeometry(QtCore.QRect(550, 250, 4, 4))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_recuperationDateDeNaissance.setFont(font)
        self.label_recuperationDateDeNaissance.setText("")
        self.label_recuperationDateDeNaissance.setObjectName("label_recuperationDateDeNaissance")
        self.label_recuperationPathologie = QtWidgets.QLabel(Frame)
        self.label_recuperationPathologie.setEnabled(False)
        self.label_recuperationPathologie.setGeometry(QtCore.QRect(120, 370, 2, 2))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_recuperationPathologie.setFont(font)
        self.label_recuperationPathologie.setText("")
        self.label_recuperationPathologie.setObjectName("label_recuperationPathologie")

        self.label_titre.raise_()
        self.label_nom.raise_()
        self.lineEdit_prenom.raise_()
        self.label_nomIntervention.raise_()
        self.label_commentaire.raise_()
        self.pushButton_evaluation.raise_()
        self.label_prenom.raise_()
        self.lineEdit_numeroMagic.raise_()
        self.lineEdit_nom.raise_()
        self.label.raise_()
        self.label_dateDeNaissance.raise_()
        self.label_pathologie.raise_()
        self.label_dateIntervention.raise_()
        self.label_numeroMagic.raise_()
        self.calendarWidget.raise_()
        self.lineEdit_dateIntervention.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.comboBox_jour.raise_()
        self.comboBox_mois.raise_()
        self.spinBox_annee.raise_()
        self.label_recuperationDateDeNaissance.raise_()
        self.pushButton_ok.raise_()
        self.label_recuperationPathologie.raise_()
        self.textEdit_interventionNonModifiable.raise_()
        self.pushButton_annuler.raise_()
        self.checkBox_autre.raise_()
        self.checkBox_medullaire.raise_()
        self.checkBox_cervicalRadiculaire.raise_()
        self.checkBox_thoracoLombaire.raise_()
        self.lineEdit_interventionModifiable.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_nom.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Nom :</p></body></html>"))
        self.label_nomIntervention.setText(
            _translate("Frame", "<html><head/><body><p align=\"center\">Nom de l\'intervention :</p></body></html>"))
        self.label_commentaire.setText(
            _translate("Frame", "<html><head/><body><p align=\"center\">Commentaire :</p></body></html>"))
        self.pushButton_evaluation.setText(_translate("Frame", "Evaluation"))
        self.label_prenom.setText(
            _translate("Frame", "<html><head/><body><p align=\"center\">Prénom :</p></body></html>"))
        self.label_titre.setText(_translate("Frame",
                                            "<html><head/><body><p align=\"center\">Création d\'un dossier patient</p></body></html>"))
        self.label.setText(_translate("Frame",
                                      "<html><head/><body><p align=\"center\">* Doit être obligatirement renseigné</p></body></html>"))
        self.label_dateDeNaissance.setText(
            _translate("Frame", "<html><head/><body><p align=\"center\">Date de naissance :</p></body></html>"))
        self.label_pathologie.setText(
            _translate("Frame", "<html><head/><body><p align=\"center\">Pathologie* :</p></body></html>"))
        self.label_dateIntervention.setText(
            _translate("Frame", "<html><head/><body><p align=\"center\">Date de l\'intervention* :</p></body></html>"))
        self.label_numeroMagic.setText(
            _translate("Frame", "<html><head/><body><p align=\"center\">Numéro MagicMed :</p></body></html>"))
        self.label_2.setText(_translate("Frame", "/"))
        self.label_3.setText(_translate("Frame", "/"))
        self.comboBox_jour.setItemText(0, _translate("Frame", "1"))
        self.comboBox_jour.setItemText(1, _translate("Frame", "2"))
        self.comboBox_jour.setItemText(2, _translate("Frame", "3"))
        self.comboBox_jour.setItemText(3, _translate("Frame", "4"))
        self.comboBox_jour.setItemText(4, _translate("Frame", "5"))
        self.comboBox_jour.setItemText(5, _translate("Frame", "6"))
        self.comboBox_jour.setItemText(6, _translate("Frame", "7"))
        self.comboBox_jour.setItemText(7, _translate("Frame", "8"))
        self.comboBox_jour.setItemText(8, _translate("Frame", "9"))
        self.comboBox_jour.setItemText(9, _translate("Frame", "10"))
        self.comboBox_jour.setItemText(10, _translate("Frame", "11"))
        self.comboBox_jour.setItemText(11, _translate("Frame", "12"))
        self.comboBox_jour.setItemText(12, _translate("Frame", "13"))
        self.comboBox_jour.setItemText(13, _translate("Frame", "14"))
        self.comboBox_jour.setItemText(14, _translate("Frame", "15"))
        self.comboBox_jour.setItemText(15, _translate("Frame", "16"))
        self.comboBox_jour.setItemText(16, _translate("Frame", "17"))
        self.comboBox_jour.setItemText(17, _translate("Frame", "18"))
        self.comboBox_jour.setItemText(18, _translate("Frame", "19"))
        self.comboBox_jour.setItemText(19, _translate("Frame", "20"))
        self.comboBox_jour.setItemText(20, _translate("Frame", "21"))
        self.comboBox_jour.setItemText(21, _translate("Frame", "22"))
        self.comboBox_jour.setItemText(22, _translate("Frame", "23"))
        self.comboBox_jour.setItemText(23, _translate("Frame", "24"))
        self.comboBox_jour.setItemText(24, _translate("Frame", "25"))
        self.comboBox_jour.setItemText(25, _translate("Frame", "26"))
        self.comboBox_jour.setItemText(26, _translate("Frame", "27"))
        self.comboBox_jour.setItemText(27, _translate("Frame", "28"))
        self.comboBox_jour.setItemText(28, _translate("Frame", "29"))
        self.comboBox_jour.setItemText(29, _translate("Frame", "30"))
        self.comboBox_jour.setItemText(30, _translate("Frame", "31"))
        self.comboBox_mois.setItemText(0, _translate("Frame", "Janvier"))
        self.comboBox_mois.setItemText(1, _translate("Frame", "Février"))
        self.comboBox_mois.setItemText(2, _translate("Frame", "Mars"))
        self.comboBox_mois.setItemText(3, _translate("Frame", "Avril"))
        self.comboBox_mois.setItemText(4, _translate("Frame", "Mai"))
        self.comboBox_mois.setItemText(5, _translate("Frame", "Juin"))
        self.comboBox_mois.setItemText(6, _translate("Frame", "Juillet"))
        self.comboBox_mois.setItemText(7, _translate("Frame", "Août"))
        self.comboBox_mois.setItemText(8, _translate("Frame", "Septembre"))
        self.comboBox_mois.setItemText(9, _translate("Frame", "Octobre"))
        self.comboBox_mois.setItemText(10, _translate("Frame", "Novembre"))
        self.comboBox_mois.setItemText(11, _translate("Frame", "Décembre"))
        self.spinBox_annee.setToolTip(_translate("Frame", "<html><head/><body><p>fhj</p></body></html>"))
        self.pushButton_ok.setText(_translate("Frame", "ok"))
        self.textEdit_interventionNonModifiable.setHtml(_translate("Frame",
                                                                   "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                   "p, li { white-space: pre-wrap; }\n"
                                                                   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                   "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_annuler.setText(_translate("Frame", "Retour"))
        self.checkBox_autre.setText(_translate("Frame", "Autre"))
        self.checkBox_medullaire.setText(_translate("Frame", "Médullaire"))
        self.checkBox_cervicalRadiculaire.setText(_translate("Frame", "Cervicale Radiculaire"))
        self.checkBox_thoracoLombaire.setText(_translate("Frame", "Thoraco-lombaire"))


# class à créer
class MainWindow_CreationDP(QtWidgets.QWidget, Ui_Frame_CreationDP):

    # Pour CréationDP, Variables qui permettent de switcher entre les interfaces pour chaque bouton.
    # Les switch sont utilisés également dans la classe Controller_Test
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)


        # controlleur pour les boutons
        self.pushButton_evaluation.clicked.connect(self.evaluation)
        self.calendarWidget.clicked[QDate].connect(self.showDate)
        self.pushButton_ok.clicked.connect(self.etape2)
        self.pushButton_annuler.clicked.connect(self.annuler)

        # Date de naissance
        self.jour = self.comboBox_jour.activated[str].connect(self.showDateNaissance)
        self.mois = self.comboBox_mois.activated[str].connect(self.showDateNaissance)
        self.annee = self.spinBox_annee.valueChanged.connect(self.showDateNaissance)

        # récupération des valeurs des checkbox
        self.checkBox_cervicalRadiculaire.stateChanged.connect(self.checkBoxChangeAction_cervicale)
        self.checkBox_medullaire.stateChanged.connect(self.checkBoxChangeAction_medullaire)
        self.checkBox_thoracoLombaire.stateChanged.connect(self.checkBoxChangeAction_lombaire)
        self.checkBox_autre.stateChanged.connect(self.checkBoxChangeAction_autre)

        # Qcalendar date intervention
        self.date_Intervention = self.calendarWidget.selectedDate()
        self.lineEdit_dateIntervention.setText(self.date_Intervention.toString("dd/MM/yyyy"))

        # récupération du nom de l'intervention
        self.glb_textEditNomIntervention = self.lineEdit_interventionModifiable.text()

    # les actions de chaque bouton
    # Methode qui permet d'aller dans l'interface Evaluation
    def evaluation(self):
        global patient_nom
        global patient_prenom
        global patient_numMagic
        global signal_eval
        global glb_textEditNomIntervention

        self.nom = self.lineEdit_nom.text()  # récupérer le texte dans le champ de texte
        self.prenom = self.lineEdit_prenom.text()  # récupérer le texte dans le champ de texte
        self.numMagic = self.lineEdit_numeroMagic.text()
        self.glb_textEditNomIntervention = self.lineEdit_interventionModifiable.text()

        patient_nom = self.nom
        patient_prenom = self.prenom
        patient_numMagic = self.numMagic
        glb_textEditNomIntervention = self.glb_textEditNomIntervention

        signal_eval = True
        self.switch_window1.emit()

    # Methode qui permet de choisir la date à partir du Qcalendar
    def showDate(self, date_Intervention):
        global patient_dateIntervention

        self.dateDeIntervention = self.lineEdit_dateIntervention.setText(date_Intervention.toString("dd/MM/yyyy"))
        self.dateRecuperation = self.lineEdit_dateIntervention.text()
        patient_dateIntervention = self.dateRecuperation

    # Methode qui permet de rentrer la date de naissance
    def showDateNaissance(self):
        global patient_dateNaissance, patient_jour, patient_mois, patient_annee, patient_annee, patient_anneeControlleur

        self.jour = self.comboBox_jour.currentText()
        self.mois = self.comboBox_mois.currentText()
        self.annee = self.spinBox_annee.value()

        patient_jour = self.jour
        patient_mois = self.mois
        patient_annee = str(self.annee)
        patient_anneeControlleur = self.annee

        self.label_recuperationDateDeNaissance.setText(self.jour + ' / ' + self.mois + ' / ' + str(self.annee))
        self.naissance = self.label_recuperationDateDeNaissance.text()
        patient_dateNaissance = self.naissance

    # Methode liée à la checkbox cervicale
    def checkBoxChangeAction_cervicale(self, state):
        global valeur_cb_cervicale_radiculaire
        global valeur_cb_medullaire
        global valeur_cb_thoraco_lombaire
        global valeur_cb_autre
        global nomPathologieCR
        global glb_textEdit_intervention

        if (state == QtCore.Qt.Checked):
            self.pushButton_ok.setEnabled(True)
            valeur_cb_cervicale_radiculaire = True
            valeur_cb_medullaire = False
            valeur_cb_thoraco_lombaire = False
            valeur_cb_autre = False
            glb_textEdit_intervention = "Cervicale Radiculaire"
            self.textEdit_interventionNonModifiable.setText(glb_textEdit_intervention)
        else:
            self.textEdit_interventionNonModifiable.setText("")

    # Methode liée à la checkbox medullaire
    def checkBoxChangeAction_medullaire(self, state):
        global valeur_cb_cervicale_radiculaire
        global valeur_cb_medullaire
        global valeur_cb_thoraco_lombaire
        global valeur_cb_autre
        global glb_textEdit_intervention

        if (state == QtCore.Qt.Checked):
            self.pushButton_ok.setEnabled(True)
            valeur_cb_medullaire = True
            valeur_cb_cervicale_radiculaire = False
            valeur_cb_thoraco_lombaire = False
            valeur_cb_autre = False
            glb_textEdit_intervention = "Médullaire"
            self.textEdit_interventionNonModifiable.setText(glb_textEdit_intervention)
        else:
            self.textEdit_interventionNonModifiable.setText("")

    # Methode liée à la checkbox lombaire
    def checkBoxChangeAction_lombaire(self, state):
        global valeur_cb_cervicale_radiculaire
        global valeur_cb_medullaire
        global valeur_cb_thoraco_lombaire
        global valeur_cb_autre
        global glb_textEdit_intervention

        if (state == QtCore.Qt.Checked):
            self.pushButton_ok.setEnabled(True)
            valeur_cb_thoraco_lombaire = True
            valeur_cb_medullaire = False
            valeur_cb_cervicale_radiculaire = False
            valeur_cb_autre = False
            glb_textEdit_intervention = "Thoraco-Lombaire"
            self.textEdit_interventionNonModifiable.setText(glb_textEdit_intervention)
        else:
            self.textEdit_interventionNonModifiable.setText("")

    # Methode liée à la checkbox autre
    def checkBoxChangeAction_autre(self, state):
        global valeur_cb_cervicale_radiculaire
        global valeur_cb_medullaire
        global valeur_cb_thoraco_lombaire
        global valeur_cb_autre
        global glb_textEdit_intervention

        if (state == QtCore.Qt.Checked):
            self.pushButton_ok.setEnabled(True)
            valeur_cb_autre = True
            valeur_cb_thoraco_lombaire = False
            valeur_cb_medullaire = False
            valeur_cb_cervicale_radiculaire = False
            glb_textEdit_intervention = "Pathologie de type Autre"
            self.textEdit_interventionNonModifiable.setText(glb_textEdit_intervention)
        else:
            self.textEdit_interventionNonModifiable.setText("")

    # Methode qui permet d'aller dans l'interface Etape 2
    def etape2(self):
        global patient_nom, patient_prenom, patient_dateIntervention, patient_numMagic, glb_textEditNomIntervention
        global patient_dateNaissance, patient_jour, patient_mois, patient_annee, patient_annee

        patient_nom = self.lineEdit_nom.text()
        patient_prenom = self.lineEdit_prenom.text()
        patient_numMagic = self.lineEdit_numeroMagic.text()
        glb_textEditNomIntervention = self.lineEdit_interventionModifiable.text()
        patient_dateIntervention = self.lineEdit_dateIntervention.text()
        patient_jour = self.comboBox_jour.currentText()
        patient_mois = self.comboBox_mois.currentText()
        patient_annee = self.comboBox_jour.currentText()
        self.switch_window2.emit()

    # Methode qui permet d'aller dans l'interface précédente (accueil)
    def annuler(self):
        global patient_dateNaissance, patient_jour, patient_mois, patient_annee, patient_annee, patient_anneeControlleur, patient_dateIntervention
        global valeur_cb_cervicale_radiculaire, valeur_cb_medullaire, valeur_cb_thoraco_lombaire, valeur_cb_autre
        patient_jour = ("1")
        patient_mois = ("Janvier")
        patient_annee = ("2000")
        patient_anneeControlleur = int(2000)
        patient_dateNaissance = ("21/04/1997")
        patient_dateIntervention = ("")
        valeur_cb_cervicale_radiculaire = False
        valeur_cb_medullaire = False
        valeur_cb_thoraco_lombaire = False
        valeur_cb_autre = False

        self.switch_window3.emit()
