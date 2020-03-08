

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame_Traumatologique(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(840, 681)
        self.pushButton_valider = QtWidgets.QPushButton(Frame)
        self.pushButton_valider.setGeometry(QtCore.QRect(560, 610, 130, 30))
        self.pushButton_valider.setObjectName("pushButton_valider")
        self.pushButton_annuler = QtWidgets.QPushButton(Frame)
        self.pushButton_annuler.setGeometry(QtCore.QRect(710, 10, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_annuler.setFont(font)
        self.pushButton_annuler.setObjectName("pushButton_annuler")
        self.pushButton_ajouterIntervention = QtWidgets.QPushButton(Frame)
        self.pushButton_ajouterIntervention.setGeometry(QtCore.QRect(340, 610, 130, 30))
        self.pushButton_ajouterIntervention.setObjectName("pushButton_ajouterIntervention")
        self.pushButton_retour = QtWidgets.QPushButton(Frame)
        self.pushButton_retour.setGeometry(QtCore.QRect(30, 10, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_retour.setFont(font)
        self.pushButton_retour.setObjectName("pushButton_retour")
        self.groupBox_finaliteNeurologique = QtWidgets.QGroupBox(Frame)
        self.groupBox_finaliteNeurologique.setGeometry(QtCore.QRect(30, 50, 751, 91))
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
        self.groupBox_Modalite = QtWidgets.QGroupBox(Frame)
        self.groupBox_Modalite.setGeometry(QtCore.QRect(30, 160, 751, 91))
        self.groupBox_Modalite.setObjectName("groupBox_Modalite")
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
        self.groupBox_recalibrage = QtWidgets.QGroupBox(Frame)
        self.groupBox_recalibrage.setEnabled(False)
        self.groupBox_recalibrage.setGeometry(QtCore.QRect(410, 380, 371, 91))
        self.groupBox_recalibrage.setObjectName("groupBox_recalibrage")
        self.pushButton_recalibrageSuivant = QtWidgets.QPushButton(self.groupBox_recalibrage)
        self.pushButton_recalibrageSuivant.setGeometry(QtCore.QRect(20, 30, 61, 30))
        self.pushButton_recalibrageSuivant.setObjectName("pushButton_recalibrageSuivant")
        self.textEdit_resultatRecalibrage = QtWidgets.QTextEdit(self.groupBox_recalibrage)
        self.textEdit_resultatRecalibrage.setEnabled(False)
        self.textEdit_resultatRecalibrage.setGeometry(QtCore.QRect(100, 30, 241, 31))
        self.textEdit_resultatRecalibrage.setObjectName("textEdit_resultatRecalibrage")
        self.groupBox_arthrodese = QtWidgets.QGroupBox(Frame)
        self.groupBox_arthrodese.setEnabled(False)
        self.groupBox_arthrodese.setGeometry(QtCore.QRect(410, 490, 371, 91))
        self.groupBox_arthrodese.setObjectName("groupBox_arthrodese")
        self.pushButton_arthrodeseSuivant = QtWidgets.QPushButton(self.groupBox_arthrodese)
        self.pushButton_arthrodeseSuivant.setGeometry(QtCore.QRect(20, 30, 61, 30))
        self.pushButton_arthrodeseSuivant.setObjectName("pushButton_arthrodeseSuivant")
        self.textEdit_resultatArthrodese = QtWidgets.QTextEdit(self.groupBox_arthrodese)
        self.textEdit_resultatArthrodese.setEnabled(False)
        self.textEdit_resultatArthrodese.setGeometry(QtCore.QRect(100, 30, 241, 31))
        self.textEdit_resultatArthrodese.setObjectName("textEdit_resultatArthrodese")
        self.line = QtWidgets.QFrame(Frame)
        self.line.setGeometry(QtCore.QRect(30, 140, 751, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Frame)
        self.line_2.setGeometry(QtCore.QRect(30, 250, 751, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Frame)
        self.line_3.setGeometry(QtCore.QRect(30, 360, 751, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Frame)
        self.line_4.setGeometry(QtCore.QRect(30, 470, 751, 20))
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
        self.line_6.setGeometry(QtCore.QRect(390, 380, 21, 91))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Frame)
        self.line_7.setGeometry(QtCore.QRect(390, 490, 21, 91))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.groupBox_gesteCorpo = QtWidgets.QGroupBox(Frame)
        self.groupBox_gesteCorpo.setGeometry(QtCore.QRect(30, 380, 361, 91))
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
        self.groupBox_osteosynthese = QtWidgets.QGroupBox(Frame)
        self.groupBox_osteosynthese.setGeometry(QtCore.QRect(30, 490, 361, 91))
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
        self.pushButton_ajouterNiveau = QtWidgets.QPushButton(Frame)
        self.pushButton_ajouterNiveau.setGeometry(QtCore.QRect(120, 610, 130, 30))
        self.pushButton_ajouterNiveau.setObjectName("pushButton_ajouterNiveau")
        self.groupBox_Niveau = QtWidgets.QGroupBox(Frame)
        self.groupBox_Niveau.setGeometry(QtCore.QRect(30, 270, 751, 91))
        self.groupBox_Niveau.setObjectName("groupBox_Niveau")
        self.lineEdit_nombreVertebre = QtWidgets.QLineEdit(self.groupBox_Niveau)
        self.lineEdit_nombreVertebre.setEnabled(False)
        self.lineEdit_nombreVertebre.setGeometry(QtCore.QRect(600, 50, 60, 20))
        self.lineEdit_nombreVertebre.setObjectName("lineEdit_nombreVertebre")
        self.label_nombreVertebre = QtWidgets.QLabel(self.groupBox_Niveau)
        self.label_nombreVertebre.setGeometry(QtCore.QRect(560, 20, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_nombreVertebre.setFont(font)
        self.label_nombreVertebre.setObjectName("label_nombreVertebre")
        self.line_8 = QtWidgets.QFrame(self.groupBox_Niveau)
        self.line_8.setGeometry(QtCore.QRect(530, 10, 21, 71))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.pushButton_niveauSuivant = QtWidgets.QPushButton(self.groupBox_Niveau)
        self.pushButton_niveauSuivant.setGeometry(QtCore.QRect(400, 30, 61, 30))
        self.pushButton_niveauSuivant.setObjectName("pushButton_niveauSuivant")
        self.label = QtWidgets.QLabel(self.groupBox_Niveau)
        self.label.setGeometry(QtCore.QRect(40, 30, 241, 31))
        self.label.setObjectName("label")
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
        self.pushButton_ajouterNiveau.raise_()
        self.groupBox_Niveau.raise_()

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
        self.groupBox_arthrodese.setTitle(_translate("Frame", "4bis - Arthrodèse"))
        self.pushButton_arthrodeseSuivant.setText(_translate("Frame", "Suivant"))
        self.label_titre.setText(_translate("Frame", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Pathologie Traumatologique</span></p></body></html>"))
        self.groupBox_gesteCorpo.setTitle(_translate("Frame", "4 - Geste Corporéal"))
        self.checkBox_vertebroplastie.setText(_translate("Frame", "Vertébroplastie"))
        self.checkBox_cyphoplastie.setText(_translate("Frame", "Cyphoplastie"))
        self.checkBox_corporealNon.setText(_translate("Frame", "Non"))
        self.groupBox_osteosynthese.setTitle(_translate("Frame", "5 - Ostéosynthèse"))
        self.checkBox_visMonoaxiales.setText(_translate("Frame", "Vis monoaxiales"))
        self.checkBox_visPolyaxiales.setText(_translate("Frame", "Vis polyaxiales"))
        self.checkBox_osteosyntheseNon.setText(_translate("Frame", "Non"))
        self.pushButton_ajouterNiveau.setText(_translate("Frame", "Ajouter Niveau"))
        self.groupBox_Niveau.setTitle(_translate("Frame", "3 - Niveau(x)"))
        self.label_nombreVertebre.setText(_translate("Frame", "Nombre de vertèbres :"))
        self.pushButton_niveauSuivant.setText(_translate("Frame", "Suivant"))
        self.label.setText(_translate("Frame", "Veuillez choisir les vertèbres considérées : "))


class MainWindow_Traumatologie(QtWidgets.QWidget, Ui_Frame_Traumatologique):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()
    switch_window6 = QtCore.pyqtSignal()
    switch_window7 = QtCore.pyqtSignal()
    switch_window8 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        # récupération des valeurs des checkbox
        self.checkBox_radiculaire.stateChanged.connect(self.checkBoxChangeAction_radiculaire)
        self.checkBox_radicoMedullaire.stateChanged.connect(self.checkBoxChangeAction_radicoMedullaire)
        self.checkBox_medullaire.stateChanged.connect(self.checkBoxChangeAction_medullaire)
        self.checkBox_non.stateChanged.connect(self.checkBoxChangeAction_non)

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

        # controlleur pour les boutons
        self.pushButton_retour.clicked.connect(self.retourEtape2)
        self.pushButton_annuler.clicked.connect(self.annulerCreationDP)
        self.pushButton_niveauSuivant.clicked.connect(self.suivantNiveau)
        self.pushButton_recalibrageSuivant.clicked.connect(self.suivantRecalibrage)
        self.pushButton_arthrodeseSuivant.clicked.connect(self.suivantArthrodese)
        self.pushButton_ajouterNiveau.clicked.connect(self.ajouterNiveau)
        self.pushButton_ajouterIntervention.clicked.connect(self.ajouterIntervention)
        self.pushButton_valider.clicked.connect(self.valider)

    def checkBoxChangeAction_radiculaire (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
        else:
            print ("unchecked")

    def checkBoxChangeAction_radicoMedullaire (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
        else:
            print ("unchecked")

    def checkBoxChangeAction_medullaire (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
        else:
            print ("unchecked")

    def checkBoxChangeAction_non (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
        else:
            print ("unchecked")

    def checkBoxChangeAction_vertebroplastie (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
        else:
            print ("unchecked")

    def checkBoxChangeAction_cyphoplastie (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
        else:
            print ("unchecked")

    def checkBoxChangeAction_corporealNon (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
        else:
            print ("unchecked")

    def checkBoxChangeAction_monoaxiales (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
        else:
            print ("unchecked")

    def checkBoxChangeAction_polyaxiales (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
        else:
            print ("unchecked")

    def checkBoxChangeAction_osteosyntheseNon (self, state):
        if ( state == QtCore.Qt.Checked):
            print("checked")
        else:
            print ("unchecked")


    def retourEtape2(self):
        self.switch_window1.emit()

    def annulerCreationDP(self):
        self.switch_window2.emit()

    def radiobtnModalite(self):
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            self.spinBox_nombre1.setEnabled(False)
            self.spinBox_nombre2.setEnabled(False)
            self.groupBox_recalibrage.setEnabled(False)
            self.groupBox_arthrodese.setEnabled(False)
            self.groupBox_Niveau.setEnabled(True)
            self.groupBox_gesteCorpo.setEnabled(True)
            self.groupBox_osteosynthese.setEnabled(True)

    def radiobtnModalite_ouvert(self):
        self.radiobutton = self.sender()
        if self.radiobutton.isChecked():
            self.spinBox_nombre1.setEnabled(True)
            self.spinBox_nombre2.setEnabled(True)
            self.groupBox_recalibrage.setEnabled(True)
            self.groupBox_arthrodese.setEnabled(True)
            self.groupBox_Niveau.setEnabled(False)
            self.groupBox_gesteCorpo.setEnabled(False)
            self.groupBox_osteosynthese.setEnabled(False)

    def countVertebres(self):
        self.nombre1 = self.spinBox_nombre1.value()
        self.nombre2 = self.spinBox_nombre2.value()
        print(type(self.nombre2))
        self.soustraction = int(self.nombre2) + int(-self.nombre1)
        print(self.soustraction)
        self.lineEdit.setText(str(self.soustraction))

    def suivantNiveau(self):
        self.switch_window3.emit()

    def suivantRecalibrage(self):
        self.switch_window4.emit()

    def suivantArthrodese(self):
        self.switch_window5.emit()

    def ajouterNiveau(self):
        self.switch_window6.emit()

    def ajouterIntervention(self):
        self.switch_window7.emit()

    def valider(self):
        self.switch_window8.emit() #faute de mieux
