
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame_Etape2(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(532, 207)
        self.pushButton_oncologie = QtWidgets.QPushButton(Frame)
        self.pushButton_oncologie.setGeometry(QtCore.QRect(365, 130, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_oncologie.setFont(font)
        self.pushButton_oncologie.setObjectName("pushButton_3")
        self.pushButton_traumatologique = QtWidgets.QPushButton(Frame)
        self.pushButton_traumatologique.setGeometry(QtCore.QRect(190, 130, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_traumatologique.setFont(font)
        self.pushButton_traumatologique.setObjectName("pushButton_2")
        self.pushButton_degeneratif = QtWidgets.QPushButton(Frame)
        self.pushButton_degeneratif.setGeometry(QtCore.QRect(15, 130, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_degeneratif.setFont(font)
        self.pushButton_degeneratif.setObjectName("pushButton")
        self.pushButton_retour = QtWidgets.QPushButton(Frame)
        self.pushButton_retour.setGeometry(QtCore.QRect(20, 20, 61, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_retour.setFont(font)
        self.pushButton_retour.setObjectName("pushButton_retour")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.pushButton_oncologie.setText(_translate("Frame", "Oncologique"))
        self.pushButton_traumatologique.setText(_translate("Frame", "Traumatologique"))
        self.pushButton_degeneratif.setText(_translate("Frame", "Dégénératif"))
        self.pushButton_retour.setText(_translate("Frame", "Retour"))


class MainWindow_Etape2(QtWidgets.QWidget, Ui_Frame_Etape2):
    switch_window1 = QtCore.pyqtSignal()
    switch_window2 = QtCore.pyqtSignal()
    switch_window3 = QtCore.pyqtSignal()
    switch_window4 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        # controlleur pour les boutons
        self.pushButton_degeneratif.clicked.connect(self.degeneratif)
        self.pushButton_traumatologique.clicked.connect(self.traumato)
        self.pushButton_oncologie.clicked.connect(self.oncologie)
        self.pushButton_retour.clicked.connect(self.retour)

    def degeneratif(self):
        self.switch_window1.emit()

    def traumato(self):
        self.switch_window2.emit()

    def oncologie(self):
        self.switch_window3.emit()

    def retour(self):
        self.switch_window4.emit()