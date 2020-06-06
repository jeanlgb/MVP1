
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate

# variables globales appelées dans controller_test
patient_dateNaissance = ("21/04/1997")
patient_dateIntervention = ("")
valeur_cb_cervicale_radiculaire = False
valeur_cb_medullaire = False
valeur_cb_thoraco_lombaire = False
valeur_cb_autre = False
signal_eval = False

identite_selectionDP = ""
glb_textEdit_intervention = ""
glb_textEditNomIntervention = ""

class Ui_Frame_SelectionnerDP_suite(object):
    # Interface générée automatiquement via qtdesigner ==> def setupUi et def retranslateUI
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setEnabled(True)
        Frame.resize(866, 862)
        self.label_nomIntervention = QtWidgets.QLabel(Frame)
        self.label_nomIntervention.setGeometry(QtCore.QRect(10, 280, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_nomIntervention.setFont(font)
        self.label_nomIntervention.setObjectName("label_nomIntervention")
        self.pushButton_evaluation = QtWidgets.QPushButton(Frame)
        self.pushButton_evaluation.setGeometry(QtCore.QRect(690, 750, 80, 30))
        self.pushButton_evaluation.setObjectName("pushButton_evaluation")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(0, 450, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label.setObjectName("label")
        self.label_pathologie = QtWidgets.QLabel(Frame)
        self.label_pathologie.setGeometry(QtCore.QRect(90, 180, 171, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_pathologie.setFont(font)
        self.label_pathologie.setObjectName("label_pathologie")
        self.label_dateIntervention = QtWidgets.QLabel(Frame)
        self.label_dateIntervention.setGeometry(QtCore.QRect(10, 420, 261, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_dateIntervention.setFont(font)
        self.label_dateIntervention.setObjectName("label_dateIntervention")
        self.calendarWidget = QtWidgets.QCalendarWidget(Frame)
        self.calendarWidget.setGeometry(QtCore.QRect(260, 430, 391, 291))
        self.calendarWidget.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.calendarWidget.setObjectName("calendarWidget")
        self.lineEdit_dateIntervention = QtWidgets.QLineEdit(Frame)
        self.lineEdit_dateIntervention.setGeometry(QtCore.QRect(660, 430, 141, 21))
        self.lineEdit_dateIntervention.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.France))
        self.lineEdit_dateIntervention.setObjectName("lineEdit_dateIntervention")
        self.label_recuperationDateDeNaissance = QtWidgets.QLabel(Frame)
        self.label_recuperationDateDeNaissance.setEnabled(False)
        self.label_recuperationDateDeNaissance.setGeometry(QtCore.QRect(550, 250, 4, 4))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_recuperationDateDeNaissance.setFont(font)
        self.label_recuperationDateDeNaissance.setText("")
        self.label_recuperationDateDeNaissance.setObjectName("label_recuperationDateDeNaissance")
        self.pushButton_ok = QtWidgets.QPushButton(Frame)
        self.pushButton_ok.setEnabled(False)
        self.pushButton_ok.setGeometry(QtCore.QRect(590, 190, 51, 23))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.label_recuperationPathologie = QtWidgets.QLabel(Frame)
        self.label_recuperationPathologie.setEnabled(False)
        self.label_recuperationPathologie.setGeometry(QtCore.QRect(120, 370, 2, 2))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_recuperationPathologie.setFont(font)
        self.label_recuperationPathologie.setText("")
        self.label_recuperationPathologie.setObjectName("label_recuperationPathologie")
        self.textEdit_interventionNonModifiable = QtWidgets.QTextEdit(Frame)
        self.textEdit_interventionNonModifiable.setGeometry(QtCore.QRect(260, 290, 271, 21))
        self.textEdit_interventionNonModifiable.setObjectName("textEdit_interventionNonModifiable")
        self.pushButton_annuler = QtWidgets.QPushButton(Frame)
        self.pushButton_annuler.setGeometry(QtCore.QRect(50, 40, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_annuler.setFont(font)
        self.pushButton_annuler.setObjectName("pushButton_annuler")
        self.checkBox_autre = QtWidgets.QCheckBox(Frame)
        self.checkBox_autre.setGeometry(QtCore.QRect(430, 210, 141, 20))
        self.checkBox_autre.setObjectName("checkBox_autre")
        self.checkBox_medullaire = QtWidgets.QCheckBox(Frame)
        self.checkBox_medullaire.setGeometry(QtCore.QRect(270, 210, 131, 20))
        self.checkBox_medullaire.setObjectName("checkBox_medullaire")
        self.checkBox_cervicalRadiculaire = QtWidgets.QCheckBox(Frame)
        self.checkBox_cervicalRadiculaire.setGeometry(QtCore.QRect(270, 180, 121, 20))
        self.checkBox_cervicalRadiculaire.setObjectName("checkBox_cervicalRadiculaire")
        self.checkBox_thoracoLombaire = QtWidgets.QCheckBox(Frame)
        self.checkBox_thoracoLombaire.setGeometry(QtCore.QRect(430, 180, 141, 20))
        self.checkBox_thoracoLombaire.setObjectName("checkBox_thoracoLombaire")
        self.textEdit_interventionModifiable = QtWidgets.QTextEdit(Frame)
        self.textEdit_interventionModifiable.setGeometry(QtCore.QRect(260, 330, 271, 21))
        self.textEdit_interventionModifiable.setObjectName("textEdit_interventionModifiable")
        self.label_identite = QtWidgets.QLabel(Frame)
        self.label_identite.setGeometry(QtCore.QRect(110, 110, 151, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_identite.setFont(font)
        self.label_identite.setObjectName("label_identite")
        self.label_recuperationDateDeNaissance_2 = QtWidgets.QLabel(Frame)
        self.label_recuperationDateDeNaissance_2.setEnabled(False)
        self.label_recuperationDateDeNaissance_2.setGeometry(QtCore.QRect(260, 140, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_recuperationDateDeNaissance_2.setFont(font)
        self.label_recuperationDateDeNaissance_2.setText("")
        self.label_recuperationDateDeNaissance_2.setObjectName("label_recuperationDateDeNaissance_2")
        self.lineEdit_identite = QtWidgets.QLineEdit(Frame)
        self.lineEdit_identite.setEnabled(False)
        self.lineEdit_identite.setGeometry(QtCore.QRect(260, 115, 271, 20))
        self.lineEdit_identite.setObjectName("lineEdit_identite")
        self.lineEdit_numeroMagic = QtWidgets.QLineEdit(Frame)
        self.lineEdit_numeroMagic.setEnabled(False)
        self.lineEdit_numeroMagic.setGeometry(QtCore.QRect(540, 115, 160, 20))
        self.lineEdit_numeroMagic.setObjectName("lineEdit_numeroMagic")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_nomIntervention.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Nom de l\'intervention :</p></body></html>"))
        self.pushButton_evaluation.setText(_translate("Frame", "Evaluation"))
        self.label.setText(_translate("Frame", "<html><head/><body><p align=\"center\">* Doit être obligatirement renseigné</p></body></html>"))
        self.label_pathologie.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Pathologie* :</p></body></html>"))
        self.label_dateIntervention.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Date de l\'intervention* :</p></body></html>"))
        self.pushButton_ok.setText(_translate("Frame", "ok"))
        self.textEdit_interventionNonModifiable.setHtml(_translate("Frame", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_annuler.setText(_translate("Frame", "Annuler"))
        self.checkBox_autre.setText(_translate("Frame", "Autre"))
        self.checkBox_medullaire.setText(_translate("Frame", "Médullaire"))
        self.checkBox_cervicalRadiculaire.setText(_translate("Frame", "Cervical Radiculaire"))
        self.checkBox_thoracoLombaire.setText(_translate("Frame", "Thoraco-lombaire"))
        self.label_identite.setText(_translate("Frame", "<html><head/><body><p align=\"center\">Identité :</p></body></html>"))

#class à créer
class MainWindow_SelectionnerDP_suite(QtWidgets.QWidget, Ui_Frame_SelectionnerDP_suite):

    # Pour SelectionDP_suite, Variables qui permettent de switcher entre les interfaces pour chaque bouton.
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


        # récupération des valeurs des checkbox
        self.checkBox_cervicalRadiculaire.stateChanged.connect(self.checkBoxChangeAction_cervicale)
        self.checkBox_medullaire.stateChanged.connect(self.checkBoxChangeAction_medullaire)
        self.checkBox_thoracoLombaire.stateChanged.connect(self.checkBoxChangeAction_lombaire)
        self.checkBox_autre.stateChanged.connect(self.checkBoxChangeAction_autre)


        # Qcalendar date intervention
        self.date_Intervention = self.calendarWidget.selectedDate()
        self.lineEdit_dateIntervention.setText(self.date_Intervention.toString("dd/MM/yyyy"))

        self.glb_textEditNomIntervention = self.textEdit_interventionModifiable.toPlainText()

    def evaluation(self):
        global signal_eval, glb_textEditNomIntervention
        global identite_selectionDP

        self.identite = self.lineEdit_identite.text()

        identite_selectionDP = self.identite
        signal_eval = True
        self.glb_textEditNomIntervention = self.textEdit_interventionModifiable
        glb_textEditNomIntervention = self.glb_textEditNomIntervention

        self.switch_window1.emit()

    def showDate(self, date_Intervention):
        global patient_dateIntervention

        self.dateDeIntervention = self.lineEdit_dateIntervention.setText(date_Intervention.toString("dd/MM/yyyy"))
        self.dateRecuperation = self.lineEdit_dateIntervention.text()
        patient_dateIntervention = self.dateRecuperation

    def checkBoxChangeAction_cervicale(self, state):
        global valeur_cb_cervicale_radiculaire
        global valeur_cb_medullaire
        global valeur_cb_thoraco_lombaire
        global valeur_cb_autre
        global nomPathologieCR
        global glb_textEdit_intervention

        if ( state == QtCore.Qt.Checked):
            self.pushButton_ok.setEnabled(True)
            valeur_cb_cervicale_radiculaire = True
            valeur_cb_medullaire = False
            valeur_cb_thoraco_lombaire = False
            valeur_cb_autre = False
            glb_textEdit_intervention = "Cervicale Radiculaire"
            self.textEdit_interventionNonModifiable.setText(glb_textEdit_intervention)
        else:
            self.textEdit_interventionNonModifiable.setText("")

    def checkBoxChangeAction_medullaire(self, state):
        global valeur_cb_cervicale_radiculaire
        global valeur_cb_medullaire
        global valeur_cb_thoraco_lombaire
        global valeur_cb_autre
        global glb_textEdit_intervention


        if ( state == QtCore.Qt.Checked):
            self.pushButton_ok.setEnabled(True)
            valeur_cb_medullaire = True
            valeur_cb_cervicale_radiculaire = False
            valeur_cb_thoraco_lombaire = False
            valeur_cb_autre = False
            glb_textEdit_intervention = "Médullaire"
            self.textEdit_interventionNonModifiable.setText(glb_textEdit_intervention)
        else:
            self.textEdit_interventionNonModifiable.setText("")

    def checkBoxChangeAction_lombaire(self, state):
        global valeur_cb_cervicale_radiculaire
        global valeur_cb_medullaire
        global valeur_cb_thoraco_lombaire
        global valeur_cb_autre
        global glb_textEdit_intervention


        if ( state == QtCore.Qt.Checked):
            self.pushButton_ok.setEnabled(True)
            valeur_cb_thoraco_lombaire = True
            valeur_cb_medullaire = False
            valeur_cb_cervicale_radiculaire = False
            valeur_cb_autre = False
            glb_textEdit_intervention = "Thoraco-Lombaire"
            self.textEdit_interventionNonModifiable.setText(glb_textEdit_intervention)
        else:
            self.textEdit_interventionNonModifiable.setText("")

    def checkBoxChangeAction_autre(self, state):
        global valeur_cb_cervicale_radiculaire
        global valeur_cb_medullaire
        global valeur_cb_thoraco_lombaire
        global valeur_cb_autre
        global glb_textEdit_intervention

        if ( state == QtCore.Qt.Checked):
            self.pushButton_ok.setEnabled(True)
            valeur_cb_autre = True
            valeur_cb_thoraco_lombaire = False
            valeur_cb_medullaire = False
            valeur_cb_cervicale_radiculaire = False
            glb_textEdit_intervention = "Pathologie de type Autre"
            self.textEdit_interventionNonModifiable.setText(glb_textEdit_intervention)
        else:
            self.textEdit_interventionNonModifiable.setText("")

    def etape2 (self):
        global patient_dateIntervention, glb_textEditNomIntervention
        patient_dateIntervention = self.lineEdit_dateIntervention.text()
        glb_textEditNomIntervention = self.textEdit_interventionModifiable.toPlainText()

        self.switch_window2.emit()

    def annuler(self):
        global patient_dateNaissance, patient_dateIntervention
        global valeur_cb_cervicale_radiculaire, valeur_cb_medullaire, valeur_cb_thoraco_lombaire, valeur_cb_autre
        patient_dateNaissance = ("21/04/1997")
        patient_dateIntervention = ("")
        valeur_cb_cervicale_radiculaire = False
        valeur_cb_medullaire = False
        valeur_cb_thoraco_lombaire = False
        valeur_cb_autre = False
        self.switch_window3.emit()