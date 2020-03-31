
from PyQt5 import QtCore, QtGui, QtWidgets

glb_onco_FN_radiculaire = True
glb_onco_FN_radicoMedullaire = False
glb_onco_FN_medullaire = False
glb_onco_FN_non = False
glb_onco_topo_epidurale = True
glb_onco_topo_osseuse = False
glb_onco_topo_intraDurale = False
glb_onco_topo_intraMedullaire = False
glb_onco_topo_enSablier = False
glb_onco_topo_autre = False
glb_onco_origine_radiculaire = True
glb_onco_origine_meningee = False
glb_onco_origine_osseuse = False
glb_onco_origine_secondaire =  False
glb_onco_origine_medullaire = False
glb_onco_origine_autre = False
onco_vertebre1 = int(1)
onco_vertebre2 =int(2)

onco_recalibrage_oui = False
onco_recalibrage_hernie = True
onco_recalibrage_non = False
glb_onco_cote_gauche = False
glb_onco_cote_droit = False
glb_onco_cote_bilateral = False
onco_arthrodese_oui = False
onco_arthrodese_non = True

glb_label_FN = "Décompression radiculaire"
glb_label_topo = ""
glb_label_origine = ""
glb_label_Niveau = "Intervention entre les vertèbres: 1 et 2"
glb_label_recalibrage = "Hernie Discale Pure"
glb_label_cote = ""
glb_label_arthrodese = "Non"
glb_label_patho = ""

glb_lbl_topo_epi = "Topographie épidurale, "
glb_lbl_topo_ID = ""
glb_lbl_topo_IM = ""
glb_lbl_topo_sablier = ""
glb_lbl_topo_oss = ""
glb_lbl_topo_autre = ""

glb_lbl_origine_radi = "Origine radiculaire, "
glb_lbl_origine_menin = ""
glb_lbl_origine_oss = ""
glb_lbl_origine_sec = ""
glb_lbl_origine_medu = ""
glb_lbl_origine_autre = ""

validerOnco = False

class Ui_Frame_Oncologie(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(840, 893)
        self.gridLayout = QtWidgets.QGridLayout(Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_retour = QtWidgets.QPushButton(Frame)
        self.pushButton_retour.setObjectName("pushButton_retour")
        self.gridLayout.addWidget(self.pushButton_retour, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_titre = QtWidgets.QLabel(Frame)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_titre.setFont(font)
        self.label_titre.setObjectName("label_titre")
        self.gridLayout.addWidget(self.label_titre, 0, 1, 1, 2)
        self.pushButton_annuler = QtWidgets.QPushButton(Frame)
        self.pushButton_annuler.setObjectName("pushButton_annuler")
        self.gridLayout.addWidget(self.pushButton_annuler, 0, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.groupBox_finaliteNeurologique = QtWidgets.QGroupBox(Frame)
        self.groupBox_finaliteNeurologique.setObjectName("groupBox_finaliteNeurologique")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_finaliteNeurologique)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.radioButton_radiculaire = QtWidgets.QRadioButton(self.groupBox_finaliteNeurologique)
        self.radioButton_radiculaire.setGeometry(QtCore.QRect(10, 33, 361, 17))
        self.radioButton_radiculaire.setChecked(True)
        self.radioButton_radiculaire.setObjectName("radioButton_radiculaire")
        self.gridLayout_2.addWidget(self.radioButton_radiculaire, 0, 0, 1, 1)
        self.radioButton_radicoMedullaire = QtWidgets.QRadioButton(self.groupBox_finaliteNeurologique)
        self.radioButton_radicoMedullaire.setGeometry(QtCore.QRect(10, 66, 371, 17))
        self.radioButton_radicoMedullaire.setObjectName("radioButton_radicoMedullaire")
        self.gridLayout_2.addWidget(self.radioButton_radicoMedullaire, 1, 0, 1, 1)
        self.radioButton_non = QtWidgets.QRadioButton(self.groupBox_finaliteNeurologique)
        self.radioButton_non.setGeometry(QtCore.QRect(493, 66, 311, 17))
        self.radioButton_non.setObjectName("radioButton_non")
        self.gridLayout_2.addWidget(self.radioButton_non, 1, 1, 1, 1)
        self.radioButton_medullaire = QtWidgets.QRadioButton(self.groupBox_finaliteNeurologique)
        self.radioButton_medullaire.setGeometry(QtCore.QRect(493, 33, 311, 17))
        self.radioButton_medullaire.setObjectName("radioButton_medullaire")
        self.gridLayout_2.addWidget(self.radioButton_medullaire, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_finaliteNeurologique, 1, 0, 1, 4)
        self.line = QtWidgets.QFrame(Frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 4)
        self.groupBox_topographie = QtWidgets.QGroupBox(Frame)
        self.groupBox_topographie.setObjectName("groupBox_topographie")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_topographie)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_epidurale = QtWidgets.QCheckBox(self.groupBox_topographie)
        self.checkBox_epidurale.setGeometry(QtCore.QRect(10, 33, 201, 17))
        self.checkBox_epidurale.setChecked(True)
        self.checkBox_epidurale.setTristate(False)
        self.checkBox_epidurale.setObjectName("checkBox_epidurale")
        self.gridLayout_3.addWidget(self.checkBox_epidurale, 0, 0, 1, 1)
        self.checkBox_intraDurale = QtWidgets.QCheckBox(self.groupBox_topographie)
        self.checkBox_intraDurale.setGeometry(QtCore.QRect(332, 33, 221, 17))
        self.checkBox_intraDurale.setObjectName("checkBox_intraDurale")
        self.gridLayout_3.addWidget(self.checkBox_intraDurale, 0, 1, 1, 1)
        self.checkBox_enSablier = QtWidgets.QCheckBox(self.groupBox_topographie)
        self.checkBox_enSablier.setGeometry(QtCore.QRect(654, 33, 211, 17))
        self.checkBox_enSablier.setObjectName("checkBox_enSablier")
        self.gridLayout_3.addWidget(self.checkBox_enSablier, 0, 2, 1, 1)
        self.checkBox_osseuseTopographie = QtWidgets.QCheckBox(self.groupBox_topographie)
        self.checkBox_osseuseTopographie.setGeometry(QtCore.QRect(10, 66, 221, 17))
        self.checkBox_osseuseTopographie.setObjectName("checkBox_osseuseTopographie")
        self.gridLayout_3.addWidget(self.checkBox_osseuseTopographie, 1, 0, 1, 1)
        self.checkBox_intraMedullaire = QtWidgets.QCheckBox(self.groupBox_topographie)
        self.checkBox_intraMedullaire.setGeometry(QtCore.QRect(332, 66, 261, 17))
        self.checkBox_intraMedullaire.setObjectName("checkBox_intraMedullaire")
        self.gridLayout_3.addWidget(self.checkBox_intraMedullaire, 1, 1, 1, 1)
        self.checkBox_autreTopographie = QtWidgets.QCheckBox(self.groupBox_topographie)
        self.checkBox_autreTopographie.setGeometry(QtCore.QRect(654, 66, 211, 17))
        self.checkBox_autreTopographie.setObjectName("checkBox_autreTopographie")
        self.label_topo_massacre = QtWidgets.QLabel(self.groupBox_topographie)
        self.label_topo_massacre.setGeometry(QtCore.QRect(940, 20, 2, 2))
        self.label_topo_massacre.setText("")
        self.label_topo_massacre.setObjectName("label_topo_massacre")
        self.gridLayout_3.addWidget(self.checkBox_autreTopographie, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_topographie, 3, 0, 1, 4)
        self.line_2 = QtWidgets.QFrame(Frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 4, 0, 1, 4)
        self.groupBox_origine = QtWidgets.QGroupBox(Frame)
        self.groupBox_origine.setObjectName("groupBox_origine")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_origine)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox_origineRadiculaire = QtWidgets.QCheckBox(self.groupBox_origine)
        self.checkBox_origineRadiculaire.setGeometry(QtCore.QRect(10, 33, 231, 17))
        self.checkBox_origineRadiculaire.setChecked(True)
        self.checkBox_origineRadiculaire.setTristate(False)
        self.checkBox_origineRadiculaire.setObjectName("checkBox_origineRadiculaire")
        self.gridLayout_4.addWidget(self.checkBox_origineRadiculaire, 0, 0, 1, 1)
        self.checkBox_origineOsseuse = QtWidgets.QCheckBox(self.groupBox_origine)
        self.checkBox_origineOsseuse.setGeometry(QtCore.QRect(332, 33, 231, 17))
        self.checkBox_origineOsseuse.setObjectName("checkBox_origineOsseuse")
        self.gridLayout_4.addWidget(self.checkBox_origineOsseuse, 0, 1, 1, 1)
        self.checkBox_origineMedullaire = QtWidgets.QCheckBox(self.groupBox_origine)
        self.checkBox_origineMedullaire.setGeometry(QtCore.QRect(654, 33, 241, 17))
        self.checkBox_origineMedullaire.setObjectName("checkBox_origineMedullaire")
        self.gridLayout_4.addWidget(self.checkBox_origineMedullaire, 0, 2, 1, 1)
        self.checkBox_meningee = QtWidgets.QCheckBox(self.groupBox_origine)
        self.checkBox_meningee.setGeometry(QtCore.QRect(10, 66, 201, 17))
        self.checkBox_meningee.setObjectName("checkBox_meningee")
        self.gridLayout_4.addWidget(self.checkBox_meningee, 1, 0, 1, 1)
        self.checkBox_secondaire = QtWidgets.QCheckBox(self.groupBox_origine)
        self.checkBox_secondaire.setGeometry(QtCore.QRect(332, 66, 211, 17))
        self.checkBox_secondaire.setObjectName("checkBox_secondaire")
        self.gridLayout_4.addWidget(self.checkBox_secondaire, 1, 1, 1, 1)
        self.checkBox_origineAutre = QtWidgets.QCheckBox(self.groupBox_origine)
        self.checkBox_origineAutre.setGeometry(QtCore.QRect(654, 66, 241, 17))
        self.checkBox_origineAutre.setObjectName("checkBox_origineAutre")
        self.label_origine_massacre = QtWidgets.QLabel(self.groupBox_origine)
        self.label_origine_massacre.setEnabled(False)
        self.label_origine_massacre.setGeometry(QtCore.QRect(940, 20, 2, 2))
        self.label_origine_massacre.setText("")
        self.label_origine_massacre.setObjectName("label_origine_massacre")
        self.gridLayout_4.addWidget(self.checkBox_origineAutre, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.groupBox_origine, 5, 0, 1, 4)
        self.line_3 = QtWidgets.QFrame(Frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 6, 0, 1, 4)
        self.groupBox_Niveau = QtWidgets.QGroupBox(Frame)
        self.groupBox_Niveau.setObjectName("groupBox_Niveau")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_Niveau)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(330, 40, 60, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_niveau = QtWidgets.QLabel(self.groupBox_Niveau)
        self.label_niveau.setGeometry(QtCore.QRect(210, 10, 491, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_niveau.setFont(font)
        self.label_niveau.setObjectName("label_niveau")
        self.label_niveauCalcul = QtWidgets.QLabel(self.groupBox_Niveau)
        self.label_niveauCalcul.setGeometry(QtCore.QRect(220, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_niveauCalcul.setFont(font)
        self.label_niveauCalcul.setObjectName("label_niveauCalcul")
        self.spinBox_nombre1 = QtWidgets.QSpinBox(self.groupBox_Niveau)
        self.spinBox_nombre1.setGeometry(QtCore.QRect(400, 10, 51, 21))
        self.spinBox_nombre1.setMinimum(1)
        self.spinBox_nombre1.setMaximum(32)
        self.spinBox_nombre1.setObjectName("spinBox_nombre1")
        self.spinBox_nombre2 = QtWidgets.QSpinBox(self.groupBox_Niveau)
        self.spinBox_nombre2.setGeometry(QtCore.QRect(470, 10, 51, 21))
        self.spinBox_nombre2.setMinimum(2)
        self.spinBox_nombre2.setMaximum(33)
        self.spinBox_nombre2.setObjectName("spinBox_nombre2")
        self.label_patho = QtWidgets.QLabel(self.groupBox_Niveau)
        self.label_patho.setEnabled(False)
        self.label_patho.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_patho.setText("")
        self.label_patho.setObjectName("label_patho")
        self.label_nivea_massacre = QtWidgets.QLabel(self.groupBox_Niveau)
        self.label_nivea_massacre.setEnabled(False)
        self.label_nivea_massacre.setGeometry(QtCore.QRect(20, 70, 2, 2))
        self.label_nivea_massacre.setText("")
        self.label_nivea_massacre.setObjectName("label_nivea_massacre")
        self.gridLayout.addWidget(self.groupBox_Niveau, 7, 0, 1, 4)
        self.line_4 = QtWidgets.QFrame(Frame)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 8, 0, 1, 4)
        self.groupBox_recalibrage = QtWidgets.QGroupBox(Frame)
        self.groupBox_recalibrage.setObjectName("groupBox_recalibrage")
        self.pushButton_recalibrageSuivant = QtWidgets.QPushButton(self.groupBox_recalibrage)
        self.pushButton_recalibrageSuivant.setGeometry(QtCore.QRect(520, 40, 61, 30))
        self.pushButton_recalibrageSuivant.setObjectName("pushButton_recalibrageSuivant")
        self.radioButton_herniePure = QtWidgets.QRadioButton(self.groupBox_recalibrage)
        self.radioButton_herniePure.setGeometry(QtCore.QRect(230, 20, 281, 30))
        self.radioButton_herniePure.setChecked(True)
        self.radioButton_herniePure.setObjectName("radioButton_herniePure")
        self.radioButton_recalibrageNon = QtWidgets.QRadioButton(self.groupBox_recalibrage)
        self.radioButton_recalibrageNon.setGeometry(QtCore.QRect(100, 40, 121, 30))
        self.radioButton_recalibrageNon.setObjectName("radioButton_recalibrageNon")
        self.radioButton_recalibrageOui = QtWidgets.QRadioButton(self.groupBox_recalibrage)
        self.radioButton_recalibrageOui.setGeometry(QtCore.QRect(100, 20, 71, 30))
        self.radioButton_recalibrageOui.setObjectName("radioButton_recalibrageOui")
        self.label_reca_massacre = QtWidgets.QLabel(self.groupBox_recalibrage)
        self.label_reca_massacre.setGeometry(QtCore.QRect(10, 80, 2, 2))
        self.label_reca_massacre.setText("")
        self.label_reca_massacre.setObjectName("label_reca_massacre")
        self.gridLayout.addWidget(self.groupBox_recalibrage, 9, 0, 1, 4)
        self.line_5 = QtWidgets.QFrame(Frame)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout.addWidget(self.line_5, 10, 0, 1, 4)
        self.groupBox_cote = QtWidgets.QGroupBox(Frame)
        self.groupBox_cote.setEnabled(True)
        self.groupBox_cote.setObjectName("groupBox_cote")
        self.label_bilateral = QtWidgets.QLabel(self.groupBox_cote)
        self.label_bilateral.setGeometry(QtCore.QRect(100, 40, 121, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_bilateral.setFont(font)
        self.label_bilateral.setObjectName("label_bilateral")
        self.label_unilateral = QtWidgets.QLabel(self.groupBox_cote)
        self.label_unilateral.setGeometry(QtCore.QRect(100, 10, 121, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_unilateral.setFont(font)
        self.label_unilateral.setObjectName("label_unilateral")
        self.radioButton_bilateral = QtWidgets.QRadioButton(self.groupBox_cote)
        self.radioButton_bilateral.setGeometry(QtCore.QRect(230, 40, 261, 30))
        self.radioButton_bilateral.setObjectName("radioButton_bilateral")
        self.radioButton_gauche = QtWidgets.QRadioButton(self.groupBox_cote)
        self.radioButton_gauche.setGeometry(QtCore.QRect(400, 10, 141, 30))
        self.radioButton_gauche.setObjectName("radioButton_gauche")
        self.radioButton_Droit = QtWidgets.QRadioButton(self.groupBox_cote)
        self.radioButton_Droit.setEnabled(True)
        self.radioButton_Droit.setGeometry(QtCore.QRect(230, 10, 141, 30))
        self.radioButton_Droit.setObjectName("radioButton_Droit")
        self.label_cote_massacre = QtWidgets.QLabel(self.groupBox_cote)
        self.label_cote_massacre.setEnabled(False)
        self.label_cote_massacre.setGeometry(QtCore.QRect(10, 80, 2, 2))
        self.label_cote_massacre.setText("")
        self.label_cote_massacre.setObjectName("label_cote_massacre")
        self.gridLayout.addWidget(self.groupBox_cote, 11, 0, 1, 4)
        self.line_6 = QtWidgets.QFrame(Frame)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout.addWidget(self.line_6, 12, 0, 1, 4)
        self.groupBox_arthrodese = QtWidgets.QGroupBox(Frame)
        self.groupBox_arthrodese.setObjectName("groupBox_arthrodese")
        self.radioButton_arthrodeseNon = QtWidgets.QRadioButton(self.groupBox_arthrodese)
        self.radioButton_arthrodeseNon.setGeometry(QtCore.QRect(100, 50, 121, 30))
        self.radioButton_arthrodeseNon.setChecked(True)
        self.radioButton_arthrodeseNon.setObjectName("radioButton_arthrodeseNon")
        self.radioButton_arthrodeseOui = QtWidgets.QRadioButton(self.groupBox_arthrodese)
        self.radioButton_arthrodeseOui.setGeometry(QtCore.QRect(100, 20, 101, 30))
        self.radioButton_arthrodeseOui.setObjectName("radioButton_arthrodeseOui")
        self.pushButton_arthrodeseSuivant = QtWidgets.QPushButton(self.groupBox_arthrodese)
        self.pushButton_arthrodeseSuivant.setEnabled(False)
        self.pushButton_arthrodeseSuivant.setGeometry(QtCore.QRect(530, 40, 61, 30))
        self.pushButton_arthrodeseSuivant.setObjectName("pushButton_arthrodeseSuivant")
        self.label_arthro_massacre = QtWidgets.QLabel(self.groupBox_arthrodese)
        self.label_arthro_massacre.setEnabled(False)
        self.label_arthro_massacre.setGeometry(QtCore.QRect(20, 80, 2, 2))
        self.label_arthro_massacre.setText("")
        self.label_arthro_massacre.setObjectName("label_arthro_massacre")
        self.gridLayout.addWidget(self.groupBox_arthrodese, 13, 0, 1, 4)
        self.pushButton_ajouterIntervention = QtWidgets.QPushButton(Frame)
        self.pushButton_ajouterIntervention.setObjectName("pushButton_ajouterIntervention")
        self.gridLayout.addWidget(self.pushButton_ajouterIntervention, 14, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.pushButton_valider = QtWidgets.QPushButton(Frame)
        self.pushButton_valider.setObjectName("pushButton_valider")
        self.gridLayout.addWidget(self.pushButton_valider, 14, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_titre.raise_()
        self.groupBox_cote.raise_()
        self.groupBox_arthrodese.raise_()
        self.groupBox_recalibrage.raise_()
        self.groupBox_finaliteNeurologique.raise_()
        self.pushButton_valider.raise_()
        self.pushButton_annuler.raise_()
        self.pushButton_ajouterIntervention.raise_()
        self.pushButton_retour.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.groupBox_topographie.raise_()
        self.groupBox_origine.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.groupBox_Niveau.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_retour.setText(_translate("Frame", "Retour"))
        self.label_titre.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Pathologie Oncologie</span></p></body></html>"))
        self.pushButton_annuler.setText(_translate("Frame", "Annuler"))
        self.groupBox_finaliteNeurologique.setTitle(_translate("Frame", "1 - Finalité neurologique"))
        self.radioButton_radiculaire.setText(_translate("Frame", "Décompression radiculaire"))
        self.radioButton_radicoMedullaire.setText(_translate("Frame", "Décompression radico-médullaire"))
        self.radioButton_non.setText(_translate("Frame", "Non"))
        self.radioButton_medullaire.setText(_translate("Frame", "Décompression médullaire"))
        self.groupBox_topographie.setTitle(_translate("Frame", "2 - Topographie"))
        self.checkBox_epidurale.setText(_translate("Frame", "Epidurale"))
        self.checkBox_intraDurale.setText(_translate("Frame", "Intra-durale"))
        self.checkBox_enSablier.setText(_translate("Frame", "En sablier"))
        self.checkBox_osseuseTopographie.setText(_translate("Frame", "Osseuse"))
        self.checkBox_intraMedullaire.setText(_translate("Frame", "Intra-médullaire"))
        self.checkBox_autreTopographie.setText(_translate("Frame", "Autre"))
        self.groupBox_origine.setTitle(_translate("Frame", "3 - Origine"))
        self.checkBox_origineRadiculaire.setText(_translate("Frame", "Radiculaire"))
        self.checkBox_origineOsseuse.setText(_translate("Frame", "Osseuse"))
        self.checkBox_origineMedullaire.setText(_translate("Frame", "Médullaire"))
        self.checkBox_meningee.setText(_translate("Frame", "Méningée"))
        self.checkBox_secondaire.setText(_translate("Frame", "Secondaire"))
        self.checkBox_origineAutre.setText(_translate("Frame", "Autre"))
        self.groupBox_Niveau.setTitle(_translate("Frame", "4 - Niveau(x)"))
        self.label_niveau.setText(_translate("Frame", "Intervention de la vertèbre           à             ."))
        self.label_niveauCalcul.setText(_translate("Frame", "Espace vertèbre : "))
        self.groupBox_recalibrage.setTitle(_translate("Frame", "5 - Recalibrage"))
        self.pushButton_recalibrageSuivant.setText(_translate("Frame", "Suivant"))
        self.radioButton_herniePure.setText(_translate("Frame", "Hernie discale pure"))
        self.radioButton_recalibrageNon.setText(_translate("Frame", "Non"))
        self.radioButton_recalibrageOui.setText(_translate("Frame", "Oui"))
        self.groupBox_cote.setTitle(_translate("Frame", "6 - Côté"))
        self.label_bilateral.setText(_translate("Frame", "Bilatéral :"))
        self.label_unilateral.setText(_translate("Frame", "Unilatéral :"))
        self.radioButton_bilateral.setText(_translate("Frame", "Bilatéral"))
        self.radioButton_gauche.setText(_translate("Frame", "Gauche"))
        self.radioButton_Droit.setText(_translate("Frame", "Droit"))
        self.groupBox_arthrodese.setTitle(_translate("Frame", "7 - Arthrodèse"))
        self.radioButton_arthrodeseNon.setText(_translate("Frame", "Non"))
        self.radioButton_arthrodeseOui.setText(_translate("Frame", "Oui"))
        self.pushButton_arthrodeseSuivant.setText(_translate("Frame", "Suivant"))
        self.pushButton_ajouterIntervention.setText(_translate("Frame", "Ajouter intervention"))
        self.pushButton_valider.setText(_translate("Frame", "Valider"))


class MainWindow_Oncologie(QtWidgets.QWidget, Ui_Frame_Oncologie):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()
    switch_window6 = QtCore.pyqtSignal()

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

        self.checkBox_epidurale.stateChanged.connect(self.checkBoxChangeAction_epidurale)
        self.checkBox_osseuseTopographie.stateChanged.connect(self.checkBoxChangeAction_topographieOsseuse)
        self.checkBox_intraDurale.stateChanged.connect(self.checkBoxChangeAction_intraDurale)
        self.checkBox_intraMedullaire.stateChanged.connect(self.checkBoxChangeAction_intraMedullaire)
        self.checkBox_enSablier.stateChanged.connect(self.checkBoxChangeAction_sablier)
        self.checkBox_autreTopographie.stateChanged.connect(self.checkBoxChangeAction_topographieAutre)

        self.checkBox_origineRadiculaire.stateChanged.connect(self.checkBoxChangeAction_origineRadiculaire)
        self.checkBox_meningee.stateChanged.connect(self.checkBoxChangeAction_meningee)
        self.checkBox_origineOsseuse.stateChanged.connect(self.checkBoxChangeAction_origineOsseuse)
        self.checkBox_secondaire.stateChanged.connect(self.checkBoxChangeAction_secondaire)
        self.checkBox_origineMedullaire.stateChanged.connect(self.checkBoxChangeAction_origineMedullaire)
        self.checkBox_origineAutre.stateChanged.connect(self.checkBoxChangeAction_origineAutre)

        # récupération nombre de vertèbres
        self.nombre1 = self.spinBox_nombre1.valueChanged.connect(self.countVertebres)
        self.nombre2 = self.spinBox_nombre2.valueChanged.connect(self.countVertebres)

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
        self.pushButton_recalibrageSuivant.clicked.connect(self.suivantRecalibrage)
        self.pushButton_arthrodeseSuivant.clicked.connect(self.suivantArthrodese)
        self.pushButton_ajouterIntervention.clicked.connect(self.ajouterIntervention)
        self.pushButton_valider.clicked.connect(self.valider) #Ne change pas d'interface mais récupère uniquement les valeurs pour lineedit de creationDP

    def radiobtn_FN_radiculaire(self):
        global glb_onco_FN_medullaire, glb_onco_FN_non, glb_onco_FN_radicoMedullaire, glb_onco_FN_radiculaire
        global glb_label_FN
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_onco_FN_radiculaire = True
            glb_onco_FN_radicoMedullaire = False
            glb_onco_FN_medullaire = False
            glb_onco_FN_non = False
            glb_label_FN = "Décompression radiculaire"

    def radiobtn_FN_radicoMedullaire(self):
        global glb_onco_FN_medullaire, glb_onco_FN_non, glb_onco_FN_radicoMedullaire, glb_onco_FN_radiculaire
        global glb_label_FN
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_onco_FN_radiculaire = False
            glb_onco_FN_radicoMedullaire = True
            glb_onco_FN_medullaire = False
            glb_onco_FN_non = False
            glb_label_FN = "Décompression radico-médullaire"

    def radiobtn_FN_medullaire(self):
        global glb_onco_FN_medullaire, glb_onco_FN_non, glb_onco_FN_radicoMedullaire, glb_onco_FN_radiculaire
        global glb_label_FN
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_onco_FN_radiculaire = False
            glb_onco_FN_radicoMedullaire = False
            glb_onco_FN_medullaire = True
            glb_onco_FN_non = False
            glb_label_FN = "Décompression médullaire"

    def radiobtn_FN_non(self):
        global glb_onco_FN_medullaire, glb_onco_FN_non, glb_onco_FN_radicoMedullaire, glb_onco_FN_radiculaire
        global glb_label_FN
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_onco_FN_radiculaire = False
            glb_onco_FN_radicoMedullaire = False
            glb_onco_FN_medullaire = False
            glb_onco_FN_non = True
            glb_label_FN = "Sans finalité neurologique"

    def checkBoxChangeAction_epidurale (self, state):
        global glb_onco_topo_epidurale, glb_lbl_topo_epi
        if ( state == QtCore.Qt.Checked):
            glb_onco_topo_epidurale = True
            glb_lbl_topo_epi = "Topographie épidurale, "
        else:
            glb_lbl_topo_epi = ""
            glb_onco_topo_epidurale = False


    def checkBoxChangeAction_topographieOsseuse (self, state):
        global glb_onco_topo_osseuse, glb_lbl_topo_oss
        if ( state == QtCore.Qt.Checked):
            glb_onco_topo_osseuse = True
            glb_lbl_topo_oss = "Topographie osseuse, "
        else:
            glb_lbl_topo_oss = ""
            glb_onco_topo_osseuse = False

    def checkBoxChangeAction_intraDurale (self, state):
        global glb_onco_topo_intraDurale, glb_lbl_topo_ID
        if (state == QtCore.Qt.Checked):
            glb_onco_topo_intraDurale = True
            glb_lbl_topo_ID = "Topographie intra-durale, "
        else:
            glb_lbl_topo_ID = ""
            glb_onco_topo_intraDurale = False

    def checkBoxChangeAction_intraMedullaire (self, state):
        global glb_onco_topo_intraMedullaire, glb_lbl_topo_IM
        if (state == QtCore.Qt.Checked):
            glb_onco_topo_intraMedullaire = True
            glb_lbl_topo_IM = "Topographie intra-médullaire, "
        else:
            glb_lbl_topo_IM = ""
            glb_onco_topo_intraMedullaire = False

    def checkBoxChangeAction_sablier (self, state):
        global glb_onco_topo_enSablier, glb_lbl_topo_sablier
        if (state == QtCore.Qt.Checked):
            glb_onco_topo_enSablier = True
            glb_lbl_topo_sablier = "Topographie en sablier, "
        else:
            glb_lbl_topo_sablier = ""
            glb_onco_topo_enSablier = False

    def checkBoxChangeAction_topographieAutre (self, state):
        global glb_onco_topo_autre, glb_lbl_topo_autre
        if (state == QtCore.Qt.Checked):
            glb_onco_topo_autre = True
            glb_lbl_topo_autre = "Topographie autre, "
        else:
            glb_lbl_topo_autre = ""
            glb_onco_topo_autre = False


    def checkBoxChangeAction_origineRadiculaire(self, state):
        global glb_onco_origine_radiculaire, glb_lbl_origine_radi
        if (state == QtCore.Qt.Checked):
            glb_onco_origine_radiculaire = True
            glb_lbl_origine_radi = "Origine radiculaire, "
        else:
            glb_lbl_origine_radi = ""
            glb_onco_origine_radiculaire = False

    def checkBoxChangeAction_meningee(self, state):
        global glb_onco_origine_meningee, glb_lbl_origine_menin
        if (state == QtCore.Qt.Checked):
            glb_onco_origine_meningee = True
            glb_lbl_origine_menin = "Origine méningée, "
        else:
            glb_lbl_origine_menin = ""
            glb_onco_origine_meningee = False

    def checkBoxChangeAction_origineOsseuse(self, state):
        global glb_onco_origine_osseuse, glb_lbl_origine_oss
        if (state == QtCore.Qt.Checked):
            glb_onco_origine_osseuse = True
            glb_lbl_origine_oss = "Origine osseuse, "
        else:
            glb_lbl_origine_oss = ""
            glb_onco_origine_osseuse = False

    def checkBoxChangeAction_secondaire(self, state):
        global glb_onco_origine_secondaire, glb_lbl_origine_sec
        if (state == QtCore.Qt.Checked):
            glb_onco_origine_secondaire = True
            glb_lbl_origine_sec = "Origine secondaire, "
        else:
            glb_lbl_origine_sec = ""
            glb_onco_origine_secondaire = False

    def checkBoxChangeAction_origineMedullaire(self, state):
        global glb_onco_origine_medullaire, glb_lbl_origine_medu
        if (state == QtCore.Qt.Checked):
            glb_onco_origine_medullaire = True
            glb_lbl_origine_medu = "Origine médullaire, "
        else:
            glb_lbl_origine_medu = ""
            glb_onco_origine_medullaire = False

    def checkBoxChangeAction_origineAutre(self, state):
        global glb_onco_origine_autre, glb_lbl_origine_autre
        if (state == QtCore.Qt.Checked):
            glb_onco_origine_autre = True
            glb_lbl_origine_autre = "Origine autre, "
        else:
            glb_lbl_origine_autre = ""
            glb_onco_origine_autre = False

    def retourEtape2(self):
        global glb_onco_origine_radiculaire, glb_onco_origine_meningee, glb_onco_origine_osseuse, glb_onco_origine_secondaire, glb_onco_origine_medullaire, glb_onco_origine_autre
        global glb_onco_topo_epidurale, glb_onco_topo_osseuse, glb_onco_topo_intraDurale, glb_onco_topo_intraMedullaire, glb_onco_topo_enSablier, glb_onco_topo_autre
        global glb_onco_FN_medullaire, glb_onco_FN_non, glb_onco_FN_radicoMedullaire, glb_onco_FN_radiculaire, onco_vertebre1, onco_vertebre2
        global onco_recalibrage_oui, onco_recalibrage_hernie, onco_recalibrage_non, onco_arthrodese_non, onco_arthrodese_oui
        global glb_onco_cote_bilateral, glb_onco_cote_droit, glb_onco_cote_gauche

        glb_onco_FN_radiculaire = True
        glb_onco_FN_radicoMedullaire = False
        glb_onco_FN_medullaire = False
        glb_onco_FN_non = False
        glb_onco_topo_epidurale = True
        glb_onco_topo_osseuse = False
        glb_onco_topo_intraDurale = False
        glb_onco_topo_intraMedullaire = False
        glb_onco_topo_enSablier = False
        glb_onco_topo_autre = False
        glb_onco_origine_radiculaire = True
        glb_onco_origine_meningee = False
        glb_onco_origine_osseuse = False
        glb_onco_origine_secondaire = False
        glb_onco_origine_medullaire = False
        glb_onco_origine_autre = False
        onco_vertebre1 = int(1)
        onco_vertebre2 = int(2)

        onco_recalibrage_oui = False
        onco_recalibrage_hernie = True
        onco_recalibrage_non = False
        glb_onco_cote_gauche = False
        glb_onco_cote_droit = False
        glb_onco_cote_bilateral = False
        onco_arthrodese_oui = False
        onco_arthrodese_non = True

        self.switch_window1.emit()

    def annulerCreationDP(self):
        global glb_onco_origine_radiculaire, glb_onco_origine_meningee, glb_onco_origine_osseuse, glb_onco_origine_secondaire, glb_onco_origine_medullaire, glb_onco_origine_autre
        global glb_onco_topo_epidurale, glb_onco_topo_osseuse, glb_onco_topo_intraDurale, glb_onco_topo_intraMedullaire, glb_onco_topo_enSablier, glb_onco_topo_autre
        global glb_onco_FN_medullaire, glb_onco_FN_non, glb_onco_FN_radicoMedullaire, glb_onco_FN_radiculaire, onco_vertebre1, onco_vertebre2
        global onco_recalibrage_oui, onco_recalibrage_hernie, onco_recalibrage_non, onco_arthrodese_non, onco_arthrodese_oui
        global glb_onco_cote_bilateral, glb_onco_cote_droit, glb_onco_cote_gauche

        glb_onco_FN_radiculaire = True
        glb_onco_FN_radicoMedullaire = False
        glb_onco_FN_medullaire = False
        glb_onco_FN_non = False
        glb_onco_topo_epidurale = True
        glb_onco_topo_osseuse = False
        glb_onco_topo_intraDurale = False
        glb_onco_topo_intraMedullaire = False
        glb_onco_topo_enSablier = False
        glb_onco_topo_autre = False
        glb_onco_origine_radiculaire = True
        glb_onco_origine_meningee = False
        glb_onco_origine_osseuse = False
        glb_onco_origine_secondaire = False
        glb_onco_origine_medullaire = False
        glb_onco_origine_autre = False
        onco_vertebre1 = int(1)
        onco_vertebre2 = int(2)

        onco_recalibrage_oui = False
        onco_recalibrage_hernie = True
        onco_recalibrage_non = False
        glb_onco_cote_gauche = False
        glb_onco_cote_droit = False
        glb_onco_cote_bilateral = False
        onco_arthrodese_oui = False
        onco_arthrodese_non = True

        self.switch_window2.emit()

    def countVertebres(self):
        global onco_vertebre1, onco_vertebre2
        global glb_label_Niveau

        onco_vertebre1 = self.spinBox_nombre1.value()
        onco_vertebre2 = self.spinBox_nombre2.value()

        glb_label_Niveau = "intervention entre les vertèbres : " + str(onco_vertebre1) + " et " + str(onco_vertebre2)
        self.soustraction = int(onco_vertebre2) + int(-onco_vertebre1)
        self.lineEdit.setText(str(self.soustraction))

    def radiobtnRecalibrage_oui(self):
        global onco_recalibrage_oui, onco_recalibrage_hernie, onco_recalibrage_non
        global glb_label_recalibrage
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            onco_recalibrage_oui = True
            onco_recalibrage_hernie = False
            onco_recalibrage_non = False
            self.pushButton_recalibrageSuivant.setEnabled(True)
            self.groupBox_cote.setEnabled(True)
            glb_label_recalibrage = "Oui"

    def radiobtnRecalibrage_hernie(self):
        global onco_recalibrage_oui, onco_recalibrage_hernie, onco_recalibrage_non
        global glb_label_recalibrage
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            onco_recalibrage_oui = False
            onco_recalibrage_hernie = True
            onco_recalibrage_non = False
            self.pushButton_recalibrageSuivant.setEnabled(True)
            self.groupBox_cote.setEnabled(True)
            glb_label_recalibrage = "Hernie Discale Pure"

    def radiobtnRecalibrage_non(self):
        global onco_recalibrage_oui, onco_recalibrage_hernie, onco_recalibrage_non
        global glb_label_recalibrage
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            onco_recalibrage_oui = False
            onco_recalibrage_hernie = False
            onco_recalibrage_non = True
            self.pushButton_recalibrageSuivant.setEnabled(False)
            self.groupBox_cote.setEnabled(False)
            glb_label_recalibrage = "Non"

    def suivantRecalibrage(self):
        self.switch_window3.emit()

    def radiobtnCote_bilateral(self):
        global glb_onco_cote_bilateral, glb_onco_cote_droit, glb_onco_cote_gauche
        global glb_label_cote
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_onco_cote_droit = False
            glb_onco_cote_gauche = False
            glb_onco_cote_bilateral = True
            glb_label_cote = "en bilatéral"

    def radiobtnCote_droit(self):
        global glb_onco_cote_bilateral, glb_onco_cote_droit, glb_onco_cote_gauche
        global glb_label_cote
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_onco_cote_droit = True
            glb_onco_cote_gauche = False
            glb_onco_cote_bilateral = False
            glb_label_cote = "sur le côté droit"

    def radiobtnCote_gauche(self):
        global glb_onco_cote_bilateral, glb_onco_cote_droit, glb_onco_cote_gauche
        global glb_label_cote
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            glb_onco_cote_droit = False
            glb_onco_cote_gauche = True
            glb_onco_cote_bilateral = False
            glb_label_cote = "sur le côté gauche"

    def radiobtnArthrodese_non(self):
        global glb_label_arthrodese
        global onco_arthrodese_non, onco_arthrodese_oui
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            onco_arthrodese_non = True
            onco_arthrodese_oui = False
            self.pushButton_arthrodeseSuivant.setEnabled(False)
            glb_label_arthrodese = "Non"

    def radiobtnArthrodese_oui(self):
        global glb_label_arthrodese
        global onco_arthrodese_non, onco_arthrodese_oui
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            onco_arthrodese_oui = True
            onco_arthrodese_non = False
            print("8")
            self.pushButton_arthrodeseSuivant.setEnabled(True)
            glb_label_arthrodese = "Oui"

    def suivantArthrodese(self):
        self.switch_window4.emit()


    def ajouterIntervention(self):
        global onco_vertebre1, onco_vertebre2
        global glb_onco_cote_bilateral, glb_onco_cote_droit, glb_onco_cote_gauche
        global validerOnco, glb_label_Niveau, glb_label_cote
        global glb_lbl_topo_epi, glb_lbl_topo_ID, glb_lbl_topo_IM, glb_lbl_topo_sablier, glb_lbl_topo_oss, glb_lbl_topo_autre, glb_label_topo
        global glb_lbl_origine_radi, glb_lbl_origine_menin, glb_lbl_origine_oss, glb_lbl_origine_sec, glb_lbl_origine_medu, glb_lbl_origine_autre, glb_label_origine

        glb_label_topo = glb_lbl_topo_epi + glb_lbl_topo_ID + glb_lbl_topo_IM + glb_lbl_topo_sablier + glb_lbl_topo_oss + glb_lbl_topo_autre
        glb_label_origine = glb_lbl_origine_radi + glb_lbl_origine_menin + glb_lbl_origine_oss + glb_lbl_origine_sec + glb_lbl_origine_medu + glb_lbl_origine_autre

        onco_vertebre1 = int(1)
        onco_vertebre2 = int(2)
        glb_onco_cote_gauche = False
        glb_onco_cote_droit = False
        glb_onco_cote_bilateral = False
        validerOnco = True

        self.switch_window5.emit()

        self.radioButton_radiculaire.setChecked(True)
        self.checkBox_epidurale.setChecked(True)
        self.checkBox_osseuseTopographie.setChecked(False)
        self.checkBox_intraDurale.setChecked(False)
        self.checkBox_intraMedullaire.setChecked(False)
        self.checkBox_enSablier.setChecked(False)
        self.checkBox_autreTopographie.setChecked(False)
        self.checkBox_origineRadiculaire.setChecked(True)
        self.checkBox_meningee.setChecked(False)
        self.checkBox_origineOsseuse.setChecked(False)
        self.checkBox_secondaire.setChecked(False)
        self.checkBox_origineMedullaire.setChecked(False)
        self.checkBox_origineAutre.setChecked(False)
        glb_label_Niveau = "Intervention entre les vertèbres: 1 et 2"
        self.radioButton_herniePure.setChecked(True)
        glb_label_cote = ""
        self.radioButton_arthrodeseNon.setChecked(True)

    def valider(self):
        global onco_vertebre1, onco_vertebre2
        global glb_onco_cote_bilateral, glb_onco_cote_droit, glb_onco_cote_gauche
        global validerOnco, glb_label_Niveau, glb_label_cote
        global glb_lbl_topo_epi, glb_lbl_topo_ID, glb_lbl_topo_IM, glb_lbl_topo_sablier, glb_lbl_topo_oss, glb_lbl_topo_autre, glb_label_topo
        global glb_lbl_origine_radi, glb_lbl_origine_menin, glb_lbl_origine_oss, glb_lbl_origine_sec, glb_lbl_origine_medu, glb_lbl_origine_autre, glb_label_origine

        glb_label_topo = glb_lbl_topo_epi + glb_lbl_topo_ID + glb_lbl_topo_IM + glb_lbl_topo_sablier + glb_lbl_topo_oss + glb_lbl_topo_autre
        glb_label_origine = glb_lbl_origine_radi + glb_lbl_origine_menin + glb_lbl_origine_oss + glb_lbl_origine_sec + glb_lbl_origine_medu + glb_lbl_origine_autre



        onco_vertebre1 = int(1)
        onco_vertebre2 = int(2)
        glb_onco_cote_gauche = False
        glb_onco_cote_droit = False
        glb_onco_cote_bilateral = False
        validerOnco = True
        
        self.switch_window6.emit() #faute de mieux

        self.radioButton_radiculaire.setChecked(True)
        self.checkBox_epidurale.setChecked(True)
        self.checkBox_osseuseTopographie.setChecked(False)
        self.checkBox_intraDurale.setChecked(False)
        self.checkBox_intraMedullaire.setChecked(False)
        self.checkBox_enSablier.setChecked(False)
        self.checkBox_autreTopographie.setChecked(False)
        self.checkBox_origineRadiculaire.setChecked(True)
        self.checkBox_meningee.setChecked(False)
        self.checkBox_origineOsseuse.setChecked(False)
        self.checkBox_secondaire.setChecked(False)
        self.checkBox_origineMedullaire.setChecked(False)
        self.checkBox_origineAutre.setChecked(False)
        glb_label_Niveau = "Intervention entre les vertèbres: 1 et 2"
        self.radioButton_herniePure.setChecked(True)
        glb_label_cote = ""
        self.radioButton_arthrodeseNon.setChecked(True)