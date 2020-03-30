

from PyQt5 import QtCore, QtGui, QtWidgets

glb_traumato_FN_radiculaire = True
glb_traumato_FN_radicoMedullaire = False
glb_traumato_FN_medullaire = False
glb_traumato_FN_non = False
glb_traumato_modalite_percutanee = True
glb_traumato_modalite_foyer = False
glb_traumato_modalite_percutanee2 = True
glb_traumato_modalite_foyer2 = False
traumato_vertebre1 = int(1)
traumato_vertebre2 =int(2)
glb_traumato_corpo_vertebro = True
glb_traumato_corpo_cypho = False
glb_traumato_corpo_non = False
glb_traumato_osteo_mono = False
glb_traumato_osteo_poly = False
glb_traumato_osteo_non = True

traumato_recalibrage_oui = False
traumato_recalibrage_hernie = True
traumato_recalibrage_non = False
glb_traumato_cote_gauche = False
glb_traumato_cote_droit = False
glb_traumato_cote_bilateral = False
traumato_arthrodese_oui = False
traumato_arthrodese_non = True

glb_label_FN = "Décompression radiculaire"
glb_label_modalite = "Modalité percutanée"
glb_label_percutanee_niveau = ""
glb_label_corpo = " Geste Corporéal : Vertébroplastie"
glb_label_osteo = "Ostéosynthèse : Non"
glb_label_Niveau = "Intervention entre les vertèbres: 1 et 2"
glb_label_recalibrage = "Hernie Discale Pure"
glb_label_cote = ""
glb_label_arthrodese = "Non"
glb_label_patho = ""

validerTraumato = False


class Ui_Frame_Traumatologique(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(976, 681)
        self.pushButton_valider = QtWidgets.QPushButton(Frame)
        self.pushButton_valider.setGeometry(QtCore.QRect(690, 610, 130, 30))
        self.pushButton_valider.setObjectName("pushButton_valider")
        self.pushButton_annuler = QtWidgets.QPushButton(Frame)
        self.pushButton_annuler.setGeometry(QtCore.QRect(900, 10, 61, 30))
        self.pushButton_annuler.setObjectName("pushButton_annuler")
        self.pushButton_ajouterIntervention = QtWidgets.QPushButton(Frame)
        self.pushButton_ajouterIntervention.setGeometry(QtCore.QRect(180, 610, 130, 30))
        self.pushButton_ajouterIntervention.setObjectName("pushButton_ajouterIntervention")
        self.pushButton_retour = QtWidgets.QPushButton(Frame)
        self.pushButton_retour.setGeometry(QtCore.QRect(30, 10, 61, 30))
        self.pushButton_retour.setObjectName("pushButton_retour")
        self.groupBox_finaliteNeurologique = QtWidgets.QGroupBox(Frame)
        self.groupBox_finaliteNeurologique.setGeometry(QtCore.QRect(30, 50, 931, 91))
        self.groupBox_finaliteNeurologique.setObjectName("groupBox_finaliteNeurologique")
        self.radioButton_radicoMedullaire = QtWidgets.QRadioButton(self.groupBox_finaliteNeurologique)
        self.radioButton_radicoMedullaire.setGeometry(QtCore.QRect(50, 60, 301, 30))
        self.radioButton_radicoMedullaire.setObjectName("radioButton_radicoMedullaire")
        self.radioButton_non = QtWidgets.QRadioButton(self.groupBox_finaliteNeurologique)
        self.radioButton_non.setGeometry(QtCore.QRect(480, 60, 201, 30))
        self.radioButton_non.setObjectName("radioButton_non")
        self.radioButton_medullaire = QtWidgets.QRadioButton(self.groupBox_finaliteNeurologique)
        self.radioButton_medullaire.setGeometry(QtCore.QRect(480, 20, 241, 30))
        self.radioButton_medullaire.setObjectName("radioButton_medullaire")
        self.radioButton_radiculaire = QtWidgets.QRadioButton(self.groupBox_finaliteNeurologique)
        self.radioButton_radiculaire.setGeometry(QtCore.QRect(50, 20, 301, 30))
        self.radioButton_radiculaire.setChecked(True)
        self.radioButton_radiculaire.setObjectName("radioButton_radiculaire")
        self.label_FN = QtWidgets.QLabel(self.groupBox_finaliteNeurologique)
        self.label_FN.setEnabled(False)
        self.label_FN.setGeometry(QtCore.QRect(880, 30, 2, 2))
        self.label_FN.setText("")
        self.label_FN.setObjectName("label_FN")
        self.groupBox_Modalite = QtWidgets.QGroupBox(Frame)
        self.groupBox_Modalite.setGeometry(QtCore.QRect(30, 160, 931, 91))
        self.groupBox_Modalite.setObjectName("groupBox_Modalite")
        self.label_patho = QtWidgets.QLabel(self.groupBox_Modalite)
        self.label_patho.setEnabled(False)
        self.label_patho.setGeometry(QtCore.QRect(150, 10, 121, 16))
        self.label_patho.setText("")
        self.label_patho.setObjectName("label_patho")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_Modalite)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(400, 40, 60, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_niveau = QtWidgets.QLabel(self.groupBox_Modalite)
        self.label_niveau.setGeometry(QtCore.QRect(290, 10, 401, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_niveau.setFont(font)
        self.label_niveau.setObjectName("label_niveau")
        self.label_niveauCalcul = QtWidgets.QLabel(self.groupBox_Modalite)
        self.label_niveauCalcul.setGeometry(QtCore.QRect(290, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_niveauCalcul.setFont(font)
        self.label_niveauCalcul.setObjectName("label_niveauCalcul")
        self.spinBox_nombre1 = QtWidgets.QSpinBox(self.groupBox_Modalite)
        self.spinBox_nombre1.setEnabled(False)
        self.spinBox_nombre1.setGeometry(QtCore.QRect(480, 10, 51, 21))
        self.spinBox_nombre1.setMinimum(1)
        self.spinBox_nombre1.setMaximum(32)
        self.spinBox_nombre1.setObjectName("spinBox_nombre1")
        self.spinBox_nombre2 = QtWidgets.QSpinBox(self.groupBox_Modalite)
        self.spinBox_nombre2.setEnabled(False)
        self.spinBox_nombre2.setGeometry(QtCore.QRect(550, 10, 51, 21))
        self.spinBox_nombre2.setMinimum(2)
        self.spinBox_nombre2.setMaximum(33)
        self.spinBox_nombre2.setObjectName("spinBox_nombre2")
        self.radioButton_foyerOuvert = QtWidgets.QRadioButton(self.groupBox_Modalite)
        self.radioButton_foyerOuvert.setGeometry(QtCore.QRect(170, 30, 111, 30))
        self.radioButton_foyerOuvert.setObjectName("radioButton_foyerOuvert")
        self.radioButton_percutanee = QtWidgets.QRadioButton(self.groupBox_Modalite)
        self.radioButton_percutanee.setGeometry(QtCore.QRect(10, 30, 121, 30))
        self.radioButton_percutanee.setChecked(True)
        self.radioButton_percutanee.setObjectName("radioButton_percutanee")
        self.line_5 = QtWidgets.QFrame(self.groupBox_Modalite)
        self.line_5.setGeometry(QtCore.QRect(130, 10, 21, 71))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label__modalite_massacre = QtWidgets.QLabel(self.groupBox_Modalite)
        self.label__modalite_massacre.setEnabled(False)
        self.label__modalite_massacre.setGeometry(QtCore.QRect(820, 40, 2, 2))
        self.label__modalite_massacre.setText("")
        self.label__modalite_massacre.setObjectName("label__modalite_massacre")
        self.groupBox_recalibrage = QtWidgets.QGroupBox(Frame)
        self.groupBox_recalibrage.setEnabled(False)
        self.groupBox_recalibrage.setGeometry(QtCore.QRect(450, 270, 511, 91))
        self.groupBox_recalibrage.setObjectName("groupBox_recalibrage")
        self.pushButton_recalibrageSuivant = QtWidgets.QPushButton(self.groupBox_recalibrage)
        self.pushButton_recalibrageSuivant.setGeometry(QtCore.QRect(330, 50, 61, 30))
        self.pushButton_recalibrageSuivant.setObjectName("pushButton_recalibrageSuivant")
        self.radioButton_recalibrageNon = QtWidgets.QRadioButton(self.groupBox_recalibrage)
        self.radioButton_recalibrageNon.setGeometry(QtCore.QRect(10, 60, 121, 30))
        self.radioButton_recalibrageNon.setObjectName("radioButton_recalibrageNon")
        self.radioButton_recalibrageOui = QtWidgets.QRadioButton(self.groupBox_recalibrage)
        self.radioButton_recalibrageOui.setGeometry(QtCore.QRect(10, 20, 71, 30))
        self.radioButton_recalibrageOui.setObjectName("radioButton_recalibrageOui")
        self.radioButton_herniePure = QtWidgets.QRadioButton(self.groupBox_recalibrage)
        self.radioButton_herniePure.setGeometry(QtCore.QRect(140, 20, 141, 30))
        self.radioButton_herniePure.setChecked(True)
        self.radioButton_herniePure.setObjectName("radioButton_herniePure")
        self.label_reca_massacre = QtWidgets.QLabel(self.groupBox_recalibrage)
        self.label_reca_massacre.setEnabled(False)
        self.label_reca_massacre.setGeometry(QtCore.QRect(460, 20, 2, 2))
        self.label_reca_massacre.setText("")
        self.label_reca_massacre.setObjectName("label_reca_massacre")
        self.groupBox_arthrodese = QtWidgets.QGroupBox(Frame)
        self.groupBox_arthrodese.setEnabled(False)
        self.groupBox_arthrodese.setGeometry(QtCore.QRect(450, 490, 511, 91))
        self.groupBox_arthrodese.setObjectName("groupBox_arthrodese")
        self.pushButton_arthrodeseSuivant = QtWidgets.QPushButton(self.groupBox_arthrodese)
        self.pushButton_arthrodeseSuivant.setEnabled(False)
        self.pushButton_arthrodeseSuivant.setGeometry(QtCore.QRect(340, 50, 61, 30))
        self.pushButton_arthrodeseSuivant.setObjectName("pushButton_arthrodeseSuivant")
        self.radioButton_arthrodeseOui = QtWidgets.QRadioButton(self.groupBox_arthrodese)
        self.radioButton_arthrodeseOui.setGeometry(QtCore.QRect(20, 20, 101, 30))
        self.radioButton_arthrodeseOui.setObjectName("radioButton_arthrodeseOui")
        self.radioButton_arthrodeseNon = QtWidgets.QRadioButton(self.groupBox_arthrodese)
        self.radioButton_arthrodeseNon.setGeometry(QtCore.QRect(20, 50, 121, 30))
        self.radioButton_arthrodeseNon.setChecked(True)
        self.radioButton_arthrodeseNon.setObjectName("radioButton_arthrodeseNon")
        self.label_arthro_massacre = QtWidgets.QLabel(self.groupBox_arthrodese)
        self.label_arthro_massacre.setEnabled(False)
        self.label_arthro_massacre.setGeometry(QtCore.QRect(470, 20, 2, 2))
        self.label_arthro_massacre.setText("")
        self.label_arthro_massacre.setObjectName("label_arthro_massacre")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(30, 140, 931, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Frame)
        self.line_2.setGeometry(QtCore.QRect(30, 250, 931, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Frame)
        self.line_3.setGeometry(QtCore.QRect(30, 360, 931, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Frame)
        self.line_4.setGeometry(QtCore.QRect(30, 470, 931, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_titre = QtWidgets.QLabel(Frame)
        self.label_titre.setGeometry(QtCore.QRect(120, -10, 551, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_titre.setFont(font)
        self.label_titre.setObjectName("label_titre")
        self.line_6 = QtWidgets.QFrame(Frame)
        self.line_6.setGeometry(QtCore.QRect(430, 380, 21, 91))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Frame)
        self.line_7.setGeometry(QtCore.QRect(430, 490, 21, 91))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.groupBox_gesteCorpo = QtWidgets.QGroupBox(Frame)
        self.groupBox_gesteCorpo.setGeometry(QtCore.QRect(30, 380, 401, 91))
        self.groupBox_gesteCorpo.setObjectName("groupBox_gesteCorpo")
        self.checkBox_vertebroplastie = QtWidgets.QCheckBox(self.groupBox_gesteCorpo)
        self.checkBox_vertebroplastie.setGeometry(QtCore.QRect(20, 20, 151, 30))
        self.checkBox_vertebroplastie.setChecked(True)
        self.checkBox_vertebroplastie.setObjectName("checkBox_vertebroplastie")
        self.checkBox_cyphoplastie = QtWidgets.QCheckBox(self.groupBox_gesteCorpo)
        self.checkBox_cyphoplastie.setGeometry(QtCore.QRect(20, 50, 151, 30))
        self.checkBox_cyphoplastie.setObjectName("checkBox_cyphoplastie")
        self.checkBox_corporealNon = QtWidgets.QCheckBox(self.groupBox_gesteCorpo)
        self.checkBox_corporealNon.setGeometry(QtCore.QRect(190, 20, 121, 30))
        self.checkBox_corporealNon.setObjectName("checkBox_corporealNon")
        self.label_corpo = QtWidgets.QLabel(self.groupBox_gesteCorpo)
        self.label_corpo.setEnabled(False)
        self.label_corpo.setGeometry(QtCore.QRect(350, 70, 2, 2))
        self.label_corpo.setText("")
        self.label_corpo.setObjectName("label_corpo")
        self.groupBox_osteosynthese = QtWidgets.QGroupBox(Frame)
        self.groupBox_osteosynthese.setGeometry(QtCore.QRect(30, 490, 401, 91))
        self.groupBox_osteosynthese.setObjectName("groupBox_osteosynthese")
        self.checkBox_visMonoaxiales = QtWidgets.QCheckBox(self.groupBox_osteosynthese)
        self.checkBox_visMonoaxiales.setGeometry(QtCore.QRect(20, 20, 161, 30))
        self.checkBox_visMonoaxiales.setObjectName("checkBox_visMonoaxiales")
        self.checkBox_visPolyaxiales = QtWidgets.QCheckBox(self.groupBox_osteosynthese)
        self.checkBox_visPolyaxiales.setGeometry(QtCore.QRect(20, 50, 151, 30))
        self.checkBox_visPolyaxiales.setObjectName("checkBox_visPolyaxiales")
        self.checkBox_osteosyntheseNon = QtWidgets.QCheckBox(self.groupBox_osteosynthese)
        self.checkBox_osteosyntheseNon.setGeometry(QtCore.QRect(190, 20, 131, 30))
        self.checkBox_osteosyntheseNon.setChecked(True)
        self.checkBox_osteosyntheseNon.setObjectName("checkBox_osteosyntheseNon")
        self.label_osteo = QtWidgets.QLabel(self.groupBox_osteosynthese)
        self.label_osteo.setEnabled(False)
        self.label_osteo.setGeometry(QtCore.QRect(340, 60, 2, 2))
        self.label_osteo.setText("")
        self.label_osteo.setObjectName("label_osteo")
        self.groupBox_Niveau = QtWidgets.QGroupBox(Frame)
        self.groupBox_Niveau.setGeometry(QtCore.QRect(30, 270, 401, 91))
        self.groupBox_Niveau.setObjectName("groupBox_Niveau")
        self.lineEdit_nombreVertebre = QtWidgets.QLineEdit(self.groupBox_Niveau)
        self.lineEdit_nombreVertebre.setEnabled(False)
        self.lineEdit_nombreVertebre.setGeometry(QtCore.QRect(290, 50, 60, 20))
        self.lineEdit_nombreVertebre.setObjectName("lineEdit_nombreVertebre")
        self.label_nombreVertebre = QtWidgets.QLabel(self.groupBox_Niveau)
        self.label_nombreVertebre.setGeometry(QtCore.QRect(250, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_nombreVertebre.setFont(font)
        self.label_nombreVertebre.setObjectName("label_nombreVertebre")
        self.line_8 = QtWidgets.QFrame(self.groupBox_Niveau)
        self.line_8.setGeometry(QtCore.QRect(210, 30, 21, 21))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.pushButton_niveauSuivant = QtWidgets.QPushButton(self.groupBox_Niveau)
        self.pushButton_niveauSuivant.setGeometry(QtCore.QRect(80, 50, 61, 30))
        self.pushButton_niveauSuivant.setObjectName("pushButton_niveauSuivant")
        self.label = QtWidgets.QLabel(self.groupBox_Niveau)
        self.label.setGeometry(QtCore.QRect(10, 20, 211, 31))
        self.label.setObjectName("label")
        self.label_Niveau_massacre = QtWidgets.QLabel(self.groupBox_Niveau)
        self.label_Niveau_massacre.setEnabled(False)
        self.label_Niveau_massacre.setGeometry(QtCore.QRect(200, 70, 2, 2))
        self.label_Niveau_massacre.setText("")
        self.label_Niveau_massacre.setObjectName("label_Niveau_massacre")
        self.line_9 = QtWidgets.QFrame(Frame)
        self.line_9.setGeometry(QtCore.QRect(430, 270, 21, 91))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.groupBox_cote = QtWidgets.QGroupBox(Frame)
        self.groupBox_cote.setEnabled(False)
        self.groupBox_cote.setGeometry(QtCore.QRect(450, 380, 511, 91))
        self.groupBox_cote.setObjectName("groupBox")
        self.label_unilateral = QtWidgets.QLabel(self.groupBox_cote)
        self.label_unilateral.setGeometry(QtCore.QRect(20, 20, 121, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_unilateral.setFont(font)
        self.label_unilateral.setObjectName("label_unilateral")
        self.label_bilateral = QtWidgets.QLabel(self.groupBox_cote)
        self.label_bilateral.setGeometry(QtCore.QRect(20, 60, 121, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_bilateral.setFont(font)
        self.label_bilateral.setObjectName("label_bilateral")
        self.radioButton_bilateral = QtWidgets.QRadioButton(self.groupBox_cote)
        self.radioButton_bilateral.setGeometry(QtCore.QRect(150, 60, 261, 30))
        self.radioButton_bilateral.setObjectName("radioButton_bilateral")
        self.radioButton_Droit = QtWidgets.QRadioButton(self.groupBox_cote)
        self.radioButton_Droit.setEnabled(True)
        self.radioButton_Droit.setGeometry(QtCore.QRect(150, 20, 141, 30))
        self.radioButton_Droit.setObjectName("radioButton_Droit")
        self.radioButton_gauche = QtWidgets.QRadioButton(self.groupBox_cote)
        self.radioButton_gauche.setGeometry(QtCore.QRect(290, 20, 141, 30))
        self.radioButton_gauche.setObjectName("radioButton_gauche")
        self.label_cote_massacre = QtWidgets.QLabel(self.groupBox_cote)
        self.label_cote_massacre.setEnabled(False)
        self.label_cote_massacre.setGeometry(QtCore.QRect(480, 30, 2, 2))
        self.label_cote_massacre.setText("")
        self.label_cote_massacre.setObjectName("label_cote_massacre")
        self.label_titre.raise_()
        self.groupBox_arthrodese.raise_()
        self.groupBox_recalibrage.raise_()
        self.groupBox_Modalite.raise_()
        self.groupBox_finaliteNeurologique.raise_()
        self.pushButton_valider.raise_()
        self.pushButton_annuler.raise_()
        self.pushButton_ajouterIntervention.raise_()
        self.pushButton_retour.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.groupBox_gesteCorpo.raise_()
        self.groupBox_osteosynthese.raise_()
        self.groupBox_Niveau.raise_()
        self.line_9.raise_()
        self.groupBox_cote.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_valider.setText(_translate("Frame", "Valider"))
        self.pushButton_annuler.setText(_translate("Frame", "Annuler"))
        self.pushButton_ajouterIntervention.setText(_translate("Frame", "Ajouter intervention"))
        self.pushButton_retour.setText(_translate("Frame", "Retour"))
        self.groupBox_finaliteNeurologique.setTitle(_translate("Frame", "1 - Finalité neurologique"))
        self.radioButton_radicoMedullaire.setText(_translate("Frame", "Décompression radico-médullaire"))
        self.radioButton_non.setText(_translate("Frame", "Non"))
        self.radioButton_medullaire.setText(_translate("Frame", "Décompression médullaire"))
        self.radioButton_radiculaire.setText(_translate("Frame", "Décompression radiculaire"))
        self.groupBox_Modalite.setTitle(_translate("Frame", "2 - Modalité"))
        self.label_niveau.setText(_translate("Frame", "Intervention de la vertèbre           à             ."))
        self.label_niveauCalcul.setText(_translate("Frame", "Espace vertèbre : "))
        self.radioButton_foyerOuvert.setText(_translate("Frame", "Foyer ouvert"))
        self.radioButton_percutanee.setText(_translate("Frame", "Percutanée"))
        self.groupBox_recalibrage.setTitle(_translate("Frame", "3bis - Recalibrage"))
        self.pushButton_recalibrageSuivant.setText(_translate("Frame", "Suivant"))
        self.radioButton_recalibrageNon.setText(_translate("Frame", "Non"))
        self.radioButton_recalibrageOui.setText(_translate("Frame", "Oui"))
        self.radioButton_herniePure.setText(_translate("Frame", "Hernie discale pure"))
        self.groupBox_arthrodese.setTitle(_translate("Frame", "5bis - Arthrodèse"))
        self.pushButton_arthrodeseSuivant.setText(_translate("Frame", "Suivant"))
        self.radioButton_arthrodeseOui.setText(_translate("Frame", "Oui"))
        self.radioButton_arthrodeseNon.setText(_translate("Frame", "Non"))
        self.label_titre.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Pathologie Traumatologique</span></p></body></html>"))
        self.groupBox_gesteCorpo.setTitle(_translate("Frame", "4 - Geste Corporéal"))
        self.checkBox_vertebroplastie.setText(_translate("Frame", "Vertébroplastie"))
        self.checkBox_cyphoplastie.setText(_translate("Frame", "Cyphoplastie"))
        self.checkBox_corporealNon.setText(_translate("Frame", "Non"))
        self.groupBox_osteosynthese.setTitle(_translate("Frame", "5 - Ostéosynthèse"))
        self.checkBox_visMonoaxiales.setText(_translate("Frame", "Vis monoaxiales"))
        self.checkBox_visPolyaxiales.setText(_translate("Frame", "Vis polyaxiales"))
        self.checkBox_osteosyntheseNon.setText(_translate("Frame", "Non"))
        self.groupBox_Niveau.setTitle(_translate("Frame", "3 - Niveau(x)"))
        self.label_nombreVertebre.setText(_translate("Frame", "Nombre de vertèbres :"))
        self.pushButton_niveauSuivant.setText(_translate("Frame", "Suivant"))
        self.label.setText(_translate("Frame", "Veuillez choisir les vertèbres considérées : "))
        self.groupBox_cote.setTitle(_translate("Frame", "4bis - Côté"))
        self.label_unilateral.setText(_translate("Frame", "Unilatéral :"))
        self.label_bilateral.setText(_translate("Frame", "Bilatéral :"))
        self.radioButton_bilateral.setText(_translate("Frame", "Bilatéral"))
        self.radioButton_Droit.setText(_translate("Frame", "Droit"))
        self.radioButton_gauche.setText(_translate("Frame", "Gauche"))


class MainWindow_Traumatologie(QtWidgets.QWidget, Ui_Frame_Traumatologique):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()
    switch_window7 = QtCore.pyqtSignal()
    switch_window8 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        global glb_label_patho
        self.label_patho.setText(glb_label_patho)
        
        # valeur des radiobuttons finalité neuro
        self.radioButton_radiculaire.toggled.connect(self.radiobtn_FN_radiculaire)
        self.radioButton_radicoMedullaire.toggled.connect(self.radiobtn_FN_radicoMedullaire)
        self.radioButton_medullaire.toggled.connect(self.radiobtn_FN_medullaire)
        self.radioButton_non.toggled.connect(self.radiobtn_FN_non)
    

        self.checkBox_vertebroplastie.stateChanged.connect(self.checkBoxChangeAction_vertebroplastie)
        self.checkBox_cyphoplastie.stateChanged.connect(self.checkBoxChangeAction_cyphoplastie)
        self.checkBox_corporealNon.stateChanged.connect(self.checkBoxChangeAction_corporealNon)
        self.checkBox_visMonoaxiales.stateChanged.connect(self.checkBoxChangeAction_monoaxiales)
        self.checkBox_visPolyaxiales.stateChanged.connect(self.checkBoxChangeAction_polyaxiales)
        self.checkBox_osteosyntheseNon.stateChanged.connect(self.checkBoxChangeAction_osteosyntheseNon)

        # récupération nombre de vertèbres
        self.nombre1 = self.spinBox_nombre1.valueChanged.connect(self.countVertebres)
        self.nombre2 = self.spinBox_nombre2.valueChanged.connect(self.countVertebres)

        # valeur des radiobuttons modalité
        self.radioButton_percutanee.toggled.connect(self.radiobtnModalite)
        self.radioButton_foyerOuvert.toggled.connect(self.radiobtnModalite_ouvert)

        # valeur des radiobuttons recalibrage et arthrodèse
        self.radioButton_herniePure.toggled.connect(self.radiobtnRecalibrage_hernie)
        self.radioButton_recalibrageNon.toggled.connect(self.radiobtnRecalibrage_non)
        self.radioButton_recalibrageOui.toggled.connect(self.radiobtnRecalibrage_oui)
        self.radioButton_arthrodeseNon.toggled.connect(self.radiobtnArthrodese_non)
        self.radioButton_arthrodeseOui.toggled.connect(self.radiobtnArthrodese_oui)

        # valeur des radiobuttons côté
        self.radioButton_bilateral.toggled.connect(self.radiobtnCote_bilateral)
        self.radioButton_Droit.toggled.connect(self.radiobtnCote_droit)
        self.radioButton_gauche.toggled.connect(self.radiobtnCote_gauche)

        # controlleur pour les boutons
        self.pushButton_retour.clicked.connect(self.retourEtape2)
        self.pushButton_annuler.clicked.connect(self.annulerCreationDP)
        self.pushButton_niveauSuivant.clicked.connect(self.suivantNiveau)
        self.pushButton_recalibrageSuivant.clicked.connect(self.suivantRecalibrage)
        self.pushButton_arthrodeseSuivant.clicked.connect(self.suivantArthrodese)
        self.pushButton_ajouterIntervention.clicked.connect(self.ajouterIntervention)
        self.pushButton_valider.clicked.connect(self.valider)

    def radiobtn_FN_radiculaire(self):
        global glb_traumato_FN_medullaire, glb_traumato_FN_non, glb_traumato_FN_radicoMedullaire, glb_traumato_FN_radiculaire
        global glb_label_FN
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_traumato_FN_radiculaire = True
            glb_traumato_FN_radicoMedullaire = False
            glb_traumato_FN_medullaire = False
            glb_traumato_FN_non = False
            glb_label_FN = "Décompression radiculaire"

    def radiobtn_FN_radicoMedullaire(self):
        global glb_traumato_FN_medullaire, glb_traumato_FN_non, glb_traumato_FN_radicoMedullaire, glb_traumato_FN_radiculaire
        global glb_label_FN
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_traumato_FN_radiculaire = False
            glb_traumato_FN_radicoMedullaire = True
            glb_traumato_FN_medullaire = False
            glb_traumato_FN_non = False
            glb_label_FN = "Décompression radico-médullaire"

    def radiobtn_FN_medullaire(self):
        global glb_traumato_FN_medullaire, glb_traumato_FN_non, glb_traumato_FN_radicoMedullaire, glb_traumato_FN_radiculaire
        global glb_label_FN
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_traumato_FN_radiculaire = False
            glb_traumato_FN_radicoMedullaire = False
            glb_traumato_FN_medullaire = True
            glb_traumato_FN_non = False
            glb_label_FN = "Décompression médullaire"

    def radiobtn_FN_non(self):
        global glb_traumato_FN_medullaire, glb_traumato_FN_non, glb_traumato_FN_radicoMedullaire, glb_traumato_FN_radiculaire
        global glb_label_FN
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_traumato_FN_radiculaire = False
            glb_traumato_FN_radicoMedullaire = False
            glb_traumato_FN_medullaire = False
            glb_traumato_FN_non = True
            glb_label_FN = "Sans finalité neurologique"

    def checkBoxChangeAction_vertebroplastie (self, state):
        global glb_traumato_corpo_vertebro, glb_traumato_corpo_cypho, glb_traumato_corpo_non
        global glb_label_corpo
        if ( state == QtCore.Qt.Checked):
            glb_traumato_corpo_vertebro = True
            glb_traumato_corpo_cypho = False
            glb_traumato_corpo_non = False
            glb_label_corpo = "Geste corporéal : Vertébroplastie"

    def checkBoxChangeAction_cyphoplastie (self, state):
        global glb_traumato_corpo_vertebro, glb_traumato_corpo_cypho, glb_traumato_corpo_non
        global glb_label_corpo
        if ( state == QtCore.Qt.Checked):
            glb_traumato_corpo_vertebro = False
            glb_traumato_corpo_cypho = True
            glb_traumato_corpo_non = False
            glb_label_corpo = "Geste corporéal : Cyphoplastie"

    def checkBoxChangeAction_corporealNon (self, state):
        global glb_traumato_corpo_vertebro, glb_traumato_corpo_cypho, glb_traumato_corpo_non
        global glb_label_corpo
        if ( state == QtCore.Qt.Checked):
            glb_traumato_corpo_vertebro = False
            glb_traumato_corpo_cypho = False
            glb_traumato_corpo_non = True
            glb_label_corpo = "Geste corporéal : Non"

    def checkBoxChangeAction_monoaxiales (self, state):
        global glb_traumato_osteo_mono, glb_traumato_osteo_poly, glb_traumato_osteo_non
        global glb_label_osteo
        if ( state == QtCore.Qt.Checked):
            glb_traumato_osteo_mono = True
            glb_traumato_osteo_poly = False
            glb_traumato_osteo_non = False
            glb_label_osteo = "Ostéosynthèse : Vis monoaxiales"

    def checkBoxChangeAction_polyaxiales (self, state):
        global glb_traumato_osteo_mono, glb_traumato_osteo_poly, glb_traumato_osteo_non
        global glb_label_osteo
        if ( state == QtCore.Qt.Checked):
            glb_traumato_osteo_mono = False
            glb_traumato_osteo_poly = True
            glb_traumato_osteo_non = False
            glb_label_osteo = "Ostéosynthèse : Vis polyaxiales"

    def checkBoxChangeAction_osteosyntheseNon (self, state):
        global glb_traumato_osteo_mono, glb_traumato_osteo_poly, glb_traumato_osteo_non
        global glb_label_osteo
        if ( state == QtCore.Qt.Checked):
            glb_traumato_osteo_mono = False
            glb_traumato_osteo_poly = False
            glb_traumato_osteo_non = True
            glb_label_osteo = "Ostéosynthèse : Non"


    def retourEtape2(self):
        global glb_traumato_FN_radiculaire, glb_traumato_FN_radicoMedullaire, glb_traumato_FN_medullaire, glb_traumato_FN_non
        global glb_traumato_modalite_percutanee, glb_traumato_modalite_foyer, traumato_vertebre1, traumato_vertebre2
        global glb_traumato_corpo_vertebro, glb_traumato_corpo_cypho, glb_traumato_corpo_non, glb_traumato_osteo_mono, glb_traumato_osteo_poly, glb_traumato_osteo_non
        global traumato_recalibrage_oui, traumato_recalibrage_hernie, traumato_recalibrage_non, glb_traumato_cote_gauche, glb_traumato_cote_droit, glb_traumato_cote_bilateral, traumato_arthrodese_oui, traumato_arthrodese_non
        global validerTraumato

        glb_traumato_FN_radiculaire = True
        glb_traumato_FN_radicoMedullaire = False
        glb_traumato_FN_medullaire = False
        glb_traumato_FN_non = False
        glb_traumato_modalite_percutanee = True
        glb_traumato_modalite_foyer = False
        traumato_vertebre1 = int(1)
        traumato_vertebre2 = int(2)
        glb_traumato_corpo_vertebro = True
        glb_traumato_corpo_cypho = False
        glb_traumato_corpo_non = False
        glb_traumato_osteo_mono = False
        glb_traumato_osteo_poly = False
        glb_traumato_osteo_non = True

        traumato_recalibrage_oui = False
        traumato_recalibrage_hernie = True
        traumato_recalibrage_non = False
        glb_traumato_cote_gauche = False
        glb_traumato_cote_droit = False
        glb_traumato_cote_bilateral = False
        traumato_arthrodese_oui = False
        traumato_arthrodese_non = True

        validerTraumato = False

        self.switch_window1.emit()

    def annulerCreationDP(self):
        global glb_traumato_FN_radiculaire, glb_traumato_FN_radicoMedullaire, glb_traumato_FN_medullaire, glb_traumato_FN_non
        global glb_traumato_modalite_percutanee, glb_traumato_modalite_foyer, traumato_vertebre1, traumato_vertebre2
        global glb_traumato_corpo_vertebro, glb_traumato_corpo_cypho, glb_traumato_corpo_non, glb_traumato_osteo_mono, glb_traumato_osteo_poly, glb_traumato_osteo_non
        global traumato_recalibrage_oui, traumato_recalibrage_hernie, traumato_recalibrage_non, glb_traumato_cote_gauche, glb_traumato_cote_droit, glb_traumato_cote_bilateral, traumato_arthrodese_oui, traumato_arthrodese_non
        global validerTraumato

        glb_traumato_FN_radiculaire = True
        glb_traumato_FN_radicoMedullaire = False
        glb_traumato_FN_medullaire = False
        glb_traumato_FN_non = False
        glb_traumato_modalite_percutanee = True
        glb_traumato_modalite_foyer = False
        traumato_vertebre1 = int(1)
        traumato_vertebre2 = int(2)
        glb_traumato_corpo_vertebro = True
        glb_traumato_corpo_cypho = False
        glb_traumato_corpo_non = False
        glb_traumato_osteo_mono = False
        glb_traumato_osteo_poly = False
        glb_traumato_osteo_non = True

        traumato_recalibrage_oui = False
        traumato_recalibrage_hernie = True
        traumato_recalibrage_non = False
        glb_traumato_cote_gauche = False
        glb_traumato_cote_droit = False
        glb_traumato_cote_bilateral = False
        traumato_arthrodese_oui = False
        traumato_arthrodese_non = True

        validerTraumato = False

        self.switch_window2.emit()

    def radiobtnModalite(self):
        global glb_label_modalite, glb_traumato_modalite_foyer, glb_traumato_modalite_percutanee, glb_traumato_modalite_foyer2, glb_traumato_modalite_percutanee2
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_traumato_modalite_percutanee = True
            glb_traumato_modalite_foyer = False
            glb_traumato_modalite_percutanee2 = True
            glb_traumato_modalite_foyer2 = False
            self.spinBox_nombre1.setEnabled(False)
            self.spinBox_nombre2.setEnabled(False)
            self.groupBox_recalibrage.setEnabled(False)
            self.groupBox_cote.setEnabled(False)
            self.groupBox_arthrodese.setEnabled(False)
            self.groupBox_Niveau.setEnabled(True)
            self.groupBox_gesteCorpo.setEnabled(True)
            self.groupBox_osteosynthese.setEnabled(True)
            glb_label_modalite = "Modalité percutanée"

    def radiobtnModalite_ouvert(self):
        global glb_label_modalite, glb_traumato_modalite_foyer, glb_traumato_modalite_percutanee, glb_traumato_modalite_foyer2, glb_traumato_modalite_percutanee2
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_traumato_modalite_percutanee = False
            glb_traumato_modalite_foyer = True
            glb_traumato_modalite_percutanee2 = False
            glb_traumato_modalite_foyer2 = True
            self.spinBox_nombre1.setEnabled(True)
            self.spinBox_nombre2.setEnabled(True)
            self.groupBox_recalibrage.setEnabled(True)
            self.groupBox_cote.setEnabled(True)
            self.groupBox_arthrodese.setEnabled(True)
            self.groupBox_Niveau.setEnabled(False)
            self.groupBox_gesteCorpo.setEnabled(False)
            self.groupBox_osteosynthese.setEnabled(False)
            glb_label_modalite = "Modalité foyer ouvert"

    def countVertebres(self):
        global traumato_vertebre1, traumato_vertebre2
        global glb_label_Niveau

        traumato_vertebre1 = self.spinBox_nombre1.value()
        traumato_vertebre2 = self.spinBox_nombre2.value()

        glb_label_Niveau = "intervention entre les vertèbres : " + str(traumato_vertebre1) + " et " + str(traumato_vertebre2)
        self.soustraction = int(traumato_vertebre2) + int(-traumato_vertebre1)
        self.lineEdit.setText(str(self.soustraction))

    def suivantNiveau(self):
        self.switch_window3.emit()

    def radiobtnRecalibrage_oui(self):
        global traumato_recalibrage_oui, traumato_recalibrage_hernie, traumato_recalibrage_non
        global glb_label_recalibrage
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            traumato_recalibrage_oui = True
            traumato_recalibrage_hernie = False
            traumato_recalibrage_non = False
            self.pushButton_recalibrageSuivant.setEnabled(True)
            self.groupBox_cote.setEnabled(True)
            glb_label_recalibrage = "Oui"

    def radiobtnRecalibrage_hernie(self):
        global traumato_recalibrage_oui, traumato_recalibrage_hernie, traumato_recalibrage_non
        global glb_label_recalibrage
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            traumato_recalibrage_oui = False
            traumato_recalibrage_hernie = True
            traumato_recalibrage_non = False
            self.pushButton_recalibrageSuivant.setEnabled(True)
            self.groupBox_cote.setEnabled(True)
            glb_label_recalibrage = "Hernie Discale Pure"

    def radiobtnRecalibrage_non(self):
        global traumato_recalibrage_oui, traumato_recalibrage_hernie, traumato_recalibrage_non
        global glb_label_recalibrage
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            traumato_recalibrage_oui = False
            traumato_recalibrage_hernie = False
            traumato_recalibrage_non = True
            self.pushButton_recalibrageSuivant.setEnabled(False)
            self.groupBox_cote.setEnabled(False)
            glb_label_recalibrage = "Non"

    def suivantRecalibrage(self):
        self.switch_window4.emit()

    def radiobtnCote_bilateral(self):
        global glb_traumato_cote_bilateral, glb_traumato_cote_droit, glb_traumato_cote_gauche
        global glb_label_cote
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_traumato_cote_droit = False
            glb_traumato_cote_gauche = False
            glb_traumato_cote_bilateral = True
            glb_label_cote = "en bilatéral"

    def radiobtnCote_droit(self):
        global glb_traumato_cote_bilateral, glb_traumato_cote_droit, glb_traumato_cote_gauche
        global glb_label_cote
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_traumato_cote_droit = True
            glb_traumato_cote_gauche = False
            glb_traumato_cote_bilateral = False
            glb_label_cote = "sur le côté droit"

    def radiobtnCote_gauche(self):
        global glb_traumato_cote_bilateral, glb_traumato_cote_droit, glb_traumato_cote_gauche
        global glb_label_cote
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_traumato_cote_droit = False
            glb_traumato_cote_gauche = True
            glb_traumato_cote_bilateral = False
            glb_label_cote = "sur le côté gauche"

    def radiobtnArthrodese_non(self):
        global glb_label_arthrodese
        global traumato_arthrodese_non, traumato_arthrodese_oui
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            traumato_arthrodese_non = True
            traumato_arthrodese_oui = False
            self.pushButton_arthrodeseSuivant.setEnabled(False)
            glb_label_arthrodese = "Non"

    def radiobtnArthrodese_oui(self):
        global glb_label_arthrodese
        global traumato_arthrodese_non, traumato_arthrodese_oui
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            traumato_arthrodese_oui = True
            traumato_arthrodese_non = False
            print("8")
            self.pushButton_arthrodeseSuivant.setEnabled(True)
            glb_label_arthrodese = "Oui"

    def suivantArthrodese(self):
        self.switch_window5.emit()

    def ajouterIntervention(self):
        global glb_traumato_FN_radiculaire, glb_traumato_FN_radicoMedullaire, glb_traumato_FN_medullaire, glb_traumato_FN_non
        global glb_traumato_modalite_percutanee, glb_traumato_modalite_foyer, traumato_vertebre1, traumato_vertebre2
        global glb_traumato_corpo_vertebro, glb_traumato_corpo_cypho, glb_traumato_corpo_non, glb_traumato_osteo_mono, glb_traumato_osteo_poly, glb_traumato_osteo_non
        global traumato_recalibrage_oui, traumato_recalibrage_hernie, traumato_recalibrage_non, glb_traumato_cote_gauche, glb_traumato_cote_droit, glb_traumato_cote_bilateral, traumato_arthrodese_oui, traumato_arthrodese_non
        global validerTraumato

        glb_traumato_FN_radiculaire = True
        glb_traumato_FN_radicoMedullaire = False
        glb_traumato_FN_medullaire = False
        glb_traumato_FN_non = False
        glb_traumato_modalite_percutanee = True
        glb_traumato_modalite_foyer = False
        traumato_vertebre1 = int(1)
        traumato_vertebre2 = int(2)
        glb_traumato_corpo_vertebro = True
        glb_traumato_corpo_cypho = False
        glb_traumato_corpo_non = False
        glb_traumato_osteo_mono = False
        glb_traumato_osteo_poly = False
        glb_traumato_osteo_non = True

        traumato_recalibrage_oui = False
        traumato_recalibrage_hernie = True
        traumato_recalibrage_non = False
        glb_traumato_cote_gauche = False
        glb_traumato_cote_droit = False
        glb_traumato_cote_bilateral = False
        traumato_arthrodese_oui = False
        traumato_arthrodese_non = True

        validerTraumato = True

        self.switch_window7.emit()

    def valider(self):
        global glb_traumato_FN_radiculaire, glb_traumato_FN_radicoMedullaire, glb_traumato_FN_medullaire, glb_traumato_FN_non
        global glb_traumato_modalite_percutanee, glb_traumato_modalite_foyer, traumato_vertebre1, traumato_vertebre2, glb_traumato_modalite_percutanee2, glb_traumato_modalite_foyer2
        global glb_traumato_corpo_vertebro, glb_traumato_corpo_cypho, glb_traumato_corpo_non, glb_traumato_osteo_mono, glb_traumato_osteo_poly, glb_traumato_osteo_non
        global traumato_recalibrage_oui, traumato_recalibrage_hernie, traumato_recalibrage_non, glb_traumato_cote_gauche, glb_traumato_cote_droit, glb_traumato_cote_bilateral, traumato_arthrodese_oui, traumato_arthrodese_non
        global validerTraumato

        glb_traumato_FN_radiculaire = True
        glb_traumato_FN_radicoMedullaire = False
        glb_traumato_FN_medullaire = False
        glb_traumato_FN_non = False
        glb_traumato_modalite_percutanee = True
        glb_traumato_modalite_foyer = False
        traumato_vertebre1 = int(1)
        traumato_vertebre2 = int(2)
        glb_traumato_corpo_vertebro = True
        glb_traumato_corpo_cypho = False
        glb_traumato_corpo_non = False
        glb_traumato_osteo_mono = False
        glb_traumato_osteo_poly = False
        glb_traumato_osteo_non = True

        traumato_recalibrage_oui = False
        traumato_recalibrage_hernie = True
        traumato_recalibrage_non = False
        glb_traumato_cote_gauche = False
        glb_traumato_cote_droit = False
        glb_traumato_cote_bilateral = False
        traumato_arthrodese_oui = False
        traumato_arthrodese_non = True

        validerTraumato = True

        self.switch_window8.emit() #faute de mieux