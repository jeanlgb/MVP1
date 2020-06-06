
from PyQt5 import QtCore, QtGui, QtWidgets

# variables globales appelées dans controller_test
signal_degeneratif = False
signal_traumatologique = False
signal_oncologie = False

signal_cervicale = False
signal_dorsale = False
signal_lombaire = False
signal_sacro = False

glb_nom_contexte = ""

class Ui_Frame_Etape2(object):
    # Interface générée automatiquement via qtdesigner ==> def setupUi et def retranslateUI
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.setFixedSize(532, 266)
        self.pushButton_oncologie = QtWidgets.QPushButton(Frame)
        self.pushButton_oncologie.setEnabled(False)
        self.pushButton_oncologie.setGeometry(QtCore.QRect(360, 190, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_oncologie.setFont(font)
        self.pushButton_oncologie.setObjectName("pushButton_3")
        self.pushButton_traumatologique = QtWidgets.QPushButton(Frame)
        self.pushButton_traumatologique.setEnabled(False)
        self.pushButton_traumatologique.setGeometry(QtCore.QRect(185, 190, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_traumatologique.setFont(font)
        self.pushButton_traumatologique.setObjectName("pushButton_2")
        self.pushButton_degeneratif = QtWidgets.QPushButton(Frame)
        self.pushButton_degeneratif.setEnabled(False)
        self.pushButton_degeneratif.setGeometry(QtCore.QRect(10, 190, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_degeneratif.setFont(font)
        self.pushButton_degeneratif.setObjectName("pushButton")
        self.pushButton_retour = QtWidgets.QPushButton(Frame)
        self.pushButton_retour.setGeometry(QtCore.QRect(20, 20, 61, 30))
        self.pushButton_retour.setObjectName("pushButton_retour")
        self.frame_bas = QtWidgets.QFrame(Frame)
        self.frame_bas.setGeometry(QtCore.QRect(0, 160, 521, 91))
        self.frame_bas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bas.setObjectName("frame_bas")
        self.frame_haut = QtWidgets.QFrame(Frame)
        self.frame_haut.setGeometry(QtCore.QRect(0, 60, 521, 91))
        self.frame_haut.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_haut.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_haut.setObjectName("frame_haut")
        self.label = QtWidgets.QLabel(self.frame_haut)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkBox_cervicale = QtWidgets.QCheckBox(self.frame_haut)
        self.checkBox_cervicale.setGeometry(QtCore.QRect(20, 50, 91, 17))
        self.checkBox_cervicale.setObjectName("checkBox_cervicale")
        self.checkBox_dorsale = QtWidgets.QCheckBox(self.frame_haut)
        self.checkBox_dorsale.setGeometry(QtCore.QRect(120, 50, 91, 17))
        self.checkBox_dorsale.setObjectName("checkBox_dorsale")
        self.checkBox_lombaire = QtWidgets.QCheckBox(self.frame_haut)
        self.checkBox_lombaire.setGeometry(QtCore.QRect(220, 50, 91, 17))
        self.checkBox_lombaire.setObjectName("checkBox_lombaire")
        self.checkBox_sacro = QtWidgets.QCheckBox(self.frame_haut)
        self.checkBox_sacro.setGeometry(QtCore.QRect(320, 50, 141, 17))
        self.checkBox_sacro.setObjectName("checkBox_sacro")
        self.frame_haut.raise_()
        self.frame_bas.raise_()
        self.pushButton_oncologie.raise_()
        self.pushButton_traumatologique.raise_()
        self.pushButton_degeneratif.raise_()
        self.pushButton_retour.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_oncologie.setText(_translate("Frame", "Oncologique"))
        self.pushButton_traumatologique.setText(_translate("Frame", "Traumatologique"))
        self.pushButton_degeneratif.setText(_translate("Frame", "Dégénératif"))
        self.pushButton_retour.setText(_translate("Frame", "Retour"))
        self.label.setText(_translate("Frame", "Zone de la pathologie : "))
        self.checkBox_cervicale.setText(_translate("Frame", "Cervicale"))
        self.checkBox_dorsale.setText(_translate("Frame", "Dorsale"))
        self.checkBox_lombaire.setText(_translate("Frame", "Lombaire"))
        self.checkBox_sacro.setText(_translate("Frame", "Sacro-coccygienne"))

# class à créer
class MainWindow_Etape2(QtWidgets.QWidget, Ui_Frame_Etape2):

    # Pour Pathologie Etape2, Variables qui permettent de switcher entre les interfaces pour chaque bouton.
    # Les switch sont utilisés également dans la classe Controller_Test
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        global signal_cervicale, signal_lombaire, signal_dorsale, signal_sacro
        signal_cervicale = False
        signal_lombaire = False
        signal_dorsale = False
        signal_sacro = False

        # controlleur pour les boutons
        self.pushButton_degeneratif.clicked.connect(self.degeneratif)
        self.pushButton_traumatologique.clicked.connect(self.traumato)
        self.pushButton_oncologie.clicked.connect(self.oncologie)
        self.pushButton_retour.clicked.connect(self.retour)

        # récupération des valeurs des checkbox
        self.checkBox_cervicale.stateChanged.connect(self.checkBoxChangeAction_cervicale)
        self.checkBox_dorsale.stateChanged.connect(self.checkBoxChangeAction_dorsale)
        self.checkBox_lombaire.stateChanged.connect(self.checkBoxChangeAction_lombaire)
        self.checkBox_sacro.stateChanged.connect(self.checkBoxChangeAction_sacro)

    def checkBoxChangeAction_cervicale(self, state):
        global signal_cervicale
        if ( state == QtCore.Qt.Checked):
            signal_cervicale = True
            self.pushButton_degeneratif.setEnabled(True)
            self.pushButton_traumatologique.setEnabled(True)
            self.pushButton_oncologie.setEnabled(True)
            print("2")
        else:
            signal_cervicale = False
            print("unchecked")

    def checkBoxChangeAction_dorsale(self, state):
        global signal_dorsale
        if ( state == QtCore.Qt.Checked):
            signal_dorsale = True
            self.pushButton_degeneratif.setEnabled(True)
            self.pushButton_traumatologique.setEnabled(True)
            self.pushButton_oncologie.setEnabled(True)
        else:
            signal_dorsale = False
            print ("unchecked")

    def checkBoxChangeAction_lombaire(self, state):
        global signal_lombaire
        if ( state == QtCore.Qt.Checked):
            signal_lombaire = True
            self.pushButton_degeneratif.setEnabled(True)
            self.pushButton_traumatologique.setEnabled(True)
            self.pushButton_oncologie.setEnabled(True)
        else:
            signal_lombaire = False
            print ("unchecked")

    def checkBoxChangeAction_sacro(self, state):
        global signal_sacro
        if ( state == QtCore.Qt.Checked):
            signal_sacro = True
            self.pushButton_degeneratif.setEnabled(True)
            self.pushButton_traumatologique.setEnabled(True)
            self.pushButton_oncologie.setEnabled(True)
        else:
            signal_sacro = False
            print ("unchecked")

    def degeneratif(self):
        global signal_degeneratif
        global signal_traumatologique
        global signal_oncologie
        global glb_nom_contexte

        signal_degeneratif = True
        signal_traumatologique = False
        signal_oncologie = False
        glb_nom_contexte = "Dégénératif"

        self.switch_window1.emit()

    def traumato(self):
        global signal_degeneratif
        global signal_traumatologique
        global signal_oncologie
        global glb_nom_contexte

        signal_degeneratif = False
        signal_traumatologique = True
        print(signal_traumatologique)
        signal_oncologie = False
        glb_nom_contexte = "Traumatologique"

        self.switch_window2.emit()

    def oncologie(self):
        global signal_degeneratif
        global signal_traumatologique
        global signal_oncologie
        global glb_nom_contexte

        signal_degeneratif = False
        signal_traumatologique = False
        signal_oncologie = True
        glb_nom_contexte = "Oncologie"

        self.switch_window3.emit()

    def retour(self):
        self.switch_window4.emit()