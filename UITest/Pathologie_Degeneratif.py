# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pathologie_Degeneratif.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame_Degeneratif(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(662, 503)
        self.pushButton_valider = QtWidgets.QPushButton(Frame)
        self.pushButton_valider.setGeometry(QtCore.QRect(420, 410, 130, 30))
        self.pushButton_valider.setObjectName("pushButton_valider")
        self.pushButton_annuler = QtWidgets.QPushButton(Frame)
        self.pushButton_annuler.setGeometry(QtCore.QRect(550, 30, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_annuler.setFont(font)
        self.pushButton_annuler.setObjectName("pushButton_annuler")
        self.pushButton_ajouterIntervention = QtWidgets.QPushButton(Frame)
        self.pushButton_ajouterIntervention.setGeometry(QtCore.QRect(100, 410, 130, 30))
        self.pushButton_ajouterIntervention.setObjectName("pushButton_ajouterIntervention")
        self.pushButton_retour = QtWidgets.QPushButton(Frame)
        self.pushButton_retour.setGeometry(QtCore.QRect(30, 30, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_retour.setFont(font)
        self.pushButton_retour.setObjectName("pushButton_retour")
        self.toolBox_etape3 = QtWidgets.QToolBox(Frame)
        self.toolBox_etape3.setGeometry(QtCore.QRect(20, 90, 611, 281))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toolBox_etape3.setFont(font)
        self.toolBox_etape3.setObjectName("toolBox_etape3")
        self.page_finalite = QtWidgets.QWidget()
        self.page_finalite.setGeometry(QtCore.QRect(0, 0, 611, 146))
        self.page_finalite.setObjectName("page_finalite")
        self.checkBox_radiculaire = QtWidgets.QCheckBox(self.page_finalite)
        self.checkBox_radiculaire.setGeometry(QtCore.QRect(50, 20, 301, 30))
        self.checkBox_radiculaire.setChecked(True)
        self.checkBox_radiculaire.setTristate(False)
        self.checkBox_radiculaire.setObjectName("checkBox_radiculaire")
        self.checkBox_medullaire = QtWidgets.QCheckBox(self.page_finalite)
        self.checkBox_medullaire.setGeometry(QtCore.QRect(360, 20, 241, 30))
        self.checkBox_medullaire.setObjectName("checkBox_medullaire")
        self.checkBox_radicoMedullaire = QtWidgets.QCheckBox(self.page_finalite)
        self.checkBox_radicoMedullaire.setGeometry(QtCore.QRect(50, 60, 301, 30))
        self.checkBox_radicoMedullaire.setObjectName("checkBox_radicoMedullaire")
        self.checkBox_non = QtWidgets.QCheckBox(self.page_finalite)
        self.checkBox_non.setGeometry(QtCore.QRect(360, 60, 201, 30))
        self.checkBox_non.setObjectName("checkBox_non")
        self.toolBox_etape3.addItem(self.page_finalite, "")
        self.page_niveau = QtWidgets.QWidget()
        self.page_niveau.setGeometry(QtCore.QRect(0, 0, 611, 146))
        self.page_niveau.setObjectName("page_niveau")
        self.label_niveau = QtWidgets.QLabel(self.page_niveau)
        self.label_niveau.setGeometry(QtCore.QRect(130, 30, 491, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_niveau.setFont(font)
        self.label_niveau.setObjectName("label_niveau")
        self.label_niveauCalcul = QtWidgets.QLabel(self.page_niveau)
        self.label_niveauCalcul.setGeometry(QtCore.QRect(130, 90, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_niveauCalcul.setFont(font)
        self.label_niveauCalcul.setObjectName("label_niveauCalcul")
        self.lineEdit = QtWidgets.QLineEdit(self.page_niveau)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(240, 90, 60, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox_nombre1 = QtWidgets.QSpinBox(self.page_niveau)
        self.spinBox_nombre1.setGeometry(QtCore.QRect(320, 30, 51, 21))
        self.spinBox_nombre1.setMinimum(1)
        self.spinBox_nombre1.setMaximum(32)
        self.spinBox_nombre1.setObjectName("spinBox_nombre1")
        self.spinBox_nombre2 = QtWidgets.QSpinBox(self.page_niveau)
        self.spinBox_nombre2.setGeometry(QtCore.QRect(390, 30, 51, 21))
        self.spinBox_nombre2.setMinimum(2)
        self.spinBox_nombre2.setMaximum(33)
        self.spinBox_nombre2.setObjectName("spinBox_nombre2")
        self.toolBox_etape3.addItem(self.page_niveau, "")
        self.page_recalibrage = QtWidgets.QWidget()
        self.page_recalibrage.setGeometry(QtCore.QRect(0, 0, 611, 146))
        self.page_recalibrage.setObjectName("page_recalibrage")
        self.frame_recalibrage = QtWidgets.QFrame(self.page_recalibrage)
        self.frame_recalibrage.setGeometry(QtCore.QRect(10, 0, 591, 141))
        self.frame_recalibrage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_recalibrage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_recalibrage.setObjectName("frame_recalibrage")
        self.radioButton_herniePure = QtWidgets.QRadioButton(self.frame_recalibrage)
        self.radioButton_herniePure.setGeometry(QtCore.QRect(220, 30, 281, 30))
        self.radioButton_herniePure.setChecked(True)
        self.radioButton_herniePure.setObjectName("radioButton_herniePure")
        self.radioButton_recalibrageOui = QtWidgets.QRadioButton(self.frame_recalibrage)
        self.radioButton_recalibrageOui.setGeometry(QtCore.QRect(90, 30, 71, 30))
        self.radioButton_recalibrageOui.setObjectName("radioButton_recalibrageOui")
        self.pushButton_recalibrageSuivant = QtWidgets.QPushButton(self.frame_recalibrage)
        self.pushButton_recalibrageSuivant.setGeometry(QtCore.QRect(380, 80, 61, 30))
        self.pushButton_recalibrageSuivant.setObjectName("pushButton_recalibrageSuivant")
        self.radioButton_recalibrageNon = QtWidgets.QRadioButton(self.frame_recalibrage)
        self.radioButton_recalibrageNon.setGeometry(QtCore.QRect(90, 80, 121, 30))
        self.radioButton_recalibrageNon.setObjectName("radioButton_recalibrageNon")
        self.toolBox_etape3.addItem(self.page_recalibrage, "")
        self.page_cote = QtWidgets.QWidget()
        self.page_cote.setGeometry(QtCore.QRect(0, 0, 611, 146))
        self.page_cote.setObjectName("page_cote")
        self.frame_cote = QtWidgets.QFrame(self.page_cote)
        self.frame_cote.setGeometry(QtCore.QRect(10, 10, 591, 131))
        self.frame_cote.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_cote.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_cote.setObjectName("frame_cote")
        self.radioButton_bilateral = QtWidgets.QRadioButton(self.frame_cote)
        self.radioButton_bilateral.setGeometry(QtCore.QRect(180, 70, 261, 30))
        self.radioButton_bilateral.setObjectName("radioButton_bilateral")
        self.radioButton_gauche = QtWidgets.QRadioButton(self.frame_cote)
        self.radioButton_gauche.setGeometry(QtCore.QRect(300, 20, 141, 30))
        self.radioButton_gauche.setObjectName("radioButton_gauche")
        self.radioButton_Droit = QtWidgets.QRadioButton(self.frame_cote)
        self.radioButton_Droit.setEnabled(True)
        self.radioButton_Droit.setGeometry(QtCore.QRect(180, 20, 141, 30))
        self.radioButton_Droit.setObjectName("radioButton_Droit")
        self.label_bilateral = QtWidgets.QLabel(self.frame_cote)
        self.label_bilateral.setGeometry(QtCore.QRect(50, 70, 121, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_bilateral.setFont(font)
        self.label_bilateral.setObjectName("label_bilateral")
        self.label_unilateral = QtWidgets.QLabel(self.frame_cote)
        self.label_unilateral.setGeometry(QtCore.QRect(50, 20, 121, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_unilateral.setFont(font)
        self.label_unilateral.setObjectName("label_unilateral")
        self.toolBox_etape3.addItem(self.page_cote, "")
        self.page_arthrodese = QtWidgets.QWidget()
        self.page_arthrodese.setGeometry(QtCore.QRect(0, 0, 611, 146))
        self.page_arthrodese.setObjectName("page_arthrodese")
        self.frame_arthrodese = QtWidgets.QFrame(self.page_arthrodese)
        self.frame_arthrodese.setGeometry(QtCore.QRect(10, 10, 591, 111))
        self.frame_arthrodese.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_arthrodese.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_arthrodese.setObjectName("frame_arthrodese")
        self.pushButton_arthrodeseSuivant = QtWidgets.QPushButton(self.frame_arthrodese)
        self.pushButton_arthrodeseSuivant.setGeometry(QtCore.QRect(420, 70, 61, 30))
        self.pushButton_arthrodeseSuivant.setObjectName("pushButton_arthrodeseSuivant")
        self.radioButton_arthrodeseOui = QtWidgets.QRadioButton(self.frame_arthrodese)
        self.radioButton_arthrodeseOui.setGeometry(QtCore.QRect(90, 20, 101, 30))
        self.radioButton_arthrodeseOui.setObjectName("radioButton_arthrodeseOui")
        self.radioButton_arthrodeseNon = QtWidgets.QRadioButton(self.frame_arthrodese)
        self.radioButton_arthrodeseNon.setGeometry(QtCore.QRect(90, 70, 121, 30))
        self.radioButton_arthrodeseNon.setChecked(True)
        self.radioButton_arthrodeseNon.setObjectName("radioButton_arthrodeseNon")
        self.toolBox_etape3.addItem(self.page_arthrodese, "")

        self.retranslateUi(Frame)
        self.toolBox_etape3.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_valider.setText(_translate("Frame", "Valider"))
        self.pushButton_annuler.setText(_translate("Frame", "Annuler"))
        self.pushButton_ajouterIntervention.setText(_translate("Frame", "Ajouter intervention"))
        self.pushButton_retour.setText(_translate("Frame", "Retour"))
        self.checkBox_radiculaire.setText(_translate("Frame", "Décompression radiculaire"))
        self.checkBox_medullaire.setText(_translate("Frame", "Décompression médullaire"))
        self.checkBox_radicoMedullaire.setText(_translate("Frame", "Décompression radico-médullaire"))
        self.checkBox_non.setText(_translate("Frame", "Non"))
        self.toolBox_etape3.setItemText(self.toolBox_etape3.indexOf(self.page_finalite), _translate("Frame", "Finalité neurologique"))
        self.label_niveau.setText(_translate("Frame", "Intervention de la vertèbre           à             ."))
        self.label_niveauCalcul.setText(_translate("Frame", "Espace vertèbre : "))
        self.toolBox_etape3.setItemText(self.toolBox_etape3.indexOf(self.page_niveau), _translate("Frame", "Niveau(x)"))
        self.radioButton_herniePure.setText(_translate("Frame", "Hernie discale pure"))
        self.radioButton_recalibrageOui.setText(_translate("Frame", "Oui"))
        self.pushButton_recalibrageSuivant.setText(_translate("Frame", "Suivant"))
        self.radioButton_recalibrageNon.setText(_translate("Frame", "Non"))
        self.toolBox_etape3.setItemText(self.toolBox_etape3.indexOf(self.page_recalibrage), _translate("Frame", "Recalibrage"))
        self.radioButton_bilateral.setText(_translate("Frame", "Bilatéral"))
        self.radioButton_gauche.setText(_translate("Frame", "Gauche"))
        self.radioButton_Droit.setText(_translate("Frame", "Droit"))
        self.label_bilateral.setText(_translate("Frame", "Bilatéral :"))
        self.label_unilateral.setText(_translate("Frame", "Unilatéral :"))
        self.toolBox_etape3.setItemText(self.toolBox_etape3.indexOf(self.page_cote), _translate("Frame", "Côté"))
        self.pushButton_arthrodeseSuivant.setText(_translate("Frame", "Suivant"))
        self.radioButton_arthrodeseOui.setText(_translate("Frame", "Oui"))
        self.radioButton_arthrodeseNon.setText(_translate("Frame", "Non"))
        self.toolBox_etape3.setItemText(self.toolBox_etape3.indexOf(self.page_arthrodese), _translate("Frame", "Arthrodèse"))


class MainWindow_Degeneratif(QtWidgets.QWidget, Ui_Frame_Degeneratif):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()
    switch_window5 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        # récupération des valeurs des checkbox
        self.checkBox_radiculaire.stateChanged.connect(self.checkBoxChangeAction_radiculaire)
        self.checkBox_radicoMedullaire.stateChanged.connect(self.checkBoxChangeAction_radicoMedullaire)
        self.checkBox_medullaire.stateChanged.connect(self.checkBoxChangeAction_medullaire)
        self.checkBox_non.stateChanged.connect(self.checkBoxChangeAction_non)

        # # récupération nombre de vertèbres
        # self.nombre1 = self.spinBox_nombre1.valueChanged.connect(self.countVertebres)
        # self.nombre2 = self.spinBox_nombre2.valueChanged.connect(self.countVertebres)


        # controlleur pour les boutons
        self.pushButton_retour.clicked.connect(self.retourEtape2)
        self.pushButton_annuler.clicked.connect(self.annulerCreationDP)
        self.pushButton_recalibrageSuivant.clicked.connect(self.suivantRecalibrage)
        self.pushButton_arthrodeseSuivant.clicked.connect(self.suivantArthrodese)
        self.pushButton_ajouterIntervention.clicked.connect(self.ajouterIntervention)
        self.pushButton_valider.clicked.connect(self.valider) #Ne change pas d'interface mais récupère uniquement les valeurs pour lineedit de creationDP

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

    def retourEtape2(self):
        self.switch_window1.emit()

    def annulerCreationDP(self):
        self.switch_window2.emit()

    # def countVertebres(self):
    #     self.nombre1 = self.spinBox_nombre1.value()
    #     self.nombre2 = self.spinBox_nombre2.value()
    #     self.lineEdit.setText(self.nombre1)

    def suivantRecalibrage(self):
        self.switch_window3.emit()

    def suivantArthrodese(self):
        self.switch_window4.emit()

    def ajouterIntervention(self):
        self.switch_window5.emit()

    def valider(self):
        self.switch_window6.emit() #faute de mieux