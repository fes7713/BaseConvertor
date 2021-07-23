from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QSize, QTimer, QTime, Qt, pyqtSignal, QDate


def is_base(num, base):
    try:
        int(num, base)
        return True
    except ValueError:
        return False

def oct2dec(oct):
    nLen = len(str(oct))
    nIncrement = nLen - 1
    octList = list(str(oct))
    result = 0
    for i in range(0, nLen):
        result += (int(octList[i]) * (8 ** nIncrement))
        nIncrement -= 1
    result = result
    return result

def hex2dec(hex):
    nLen = len(str(hex))
    nIncrement = nLen - 1
    hexList = list(hex)
    result = 0
    for i in range(0, nLen):
        if hexList[i] == "A":
            hexList[i] = 10
        elif hexList[i] == "B":
            hexList[i] = 11
        elif hexList[i] == "C":
            hexList[i] = 12
        elif hexList[i] == "D":
            hexList[i] = 13
        elif hexList[i] == "E":
            hexList[i] = 14
        elif hexList[i] == "F":
            hexList[i] = 15
    hexList2 = hexList
    for i in range(0, nLen):
        result += (int(hexList2[i]) * (16 ** nIncrement))
        nIncrement -= 1
    result = result
    return result

def bin2dec(bin):
    nLen = len(str(bin))
    nTotalPower = 2 ** (nLen - 1)
    binList = list(str(bin))
    result = 0
    for i in range(0, nLen):
        result += (int(binList[i]) * nTotalPower)
        nTotalPower //= 2
        if binList[nLen - 1] == 0:
            break
    result = result
    return result

class Ui_Form(QtWidgets.QWidget):
    def __init__(self, Form):
        super().__init__()
        Form.setObjectName("Form")

        # Remove window tlttle bar
        # Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Set main background to transparent
        # Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        Form.resize(487, 599)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.ResetButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.ResetButton.setFont(font)
        self.ResetButton.setObjectName("ResetButton")
        self.verticalLayout.addWidget(self.ResetButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 20, 5, 20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BinaryLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BinaryLabel.setFont(font)
        self.BinaryLabel.setObjectName("BinaryLabel")
        self.horizontalLayout.addWidget(self.BinaryLabel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem2)
        self.binaryAnswer = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.binaryAnswer.sizePolicy().hasHeightForWidth())
        self.binaryAnswer.setSizePolicy(sizePolicy)
        self.binaryAnswer.setMinimumSize(QtCore.QSize(100, 50))
        self.binaryAnswer.setObjectName("binaryAnswer")
        self.horizontalLayout.addWidget(self.binaryAnswer)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 20, 5, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.DecimalLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.DecimalLabel.setFont(font)
        self.DecimalLabel.setObjectName("DecimalLabel")
        self.horizontalLayout_2.addWidget(self.DecimalLabel)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.DecimalInOut = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DecimalInOut.sizePolicy().hasHeightForWidth())
        self.DecimalInOut.setSizePolicy(sizePolicy)
        self.DecimalInOut.setMinimumSize(QtCore.QSize(100, 50))
        self.DecimalInOut.setObjectName("DecimalInOut")
        self.horizontalLayout_2.addWidget(self.DecimalInOut)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 20, 5, 20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.HexaDecimalLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.HexaDecimalLabel.setFont(font)
        self.HexaDecimalLabel.setObjectName("HexaDecimalLabel")
        self.horizontalLayout_3.addWidget(self.HexaDecimalLabel)
        self.HexadecimalInOut = QtWidgets.QLineEdit(Form)
        self.HexadecimalInOut.setMinimumSize(QtCore.QSize(100, 50))
        self.HexadecimalInOut.setObjectName("HexadecimalInOut")
        self.horizontalLayout_3.addWidget(self.HexadecimalInOut)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 20, 5, 20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.CustomBase = QtWidgets.QComboBox(Form)
        self.CustomBase.setMinimumSize(QtCore.QSize(50, 50))
        self.CustomBase.setObjectName("CustomBase")
        self.horizontalLayout_4.addWidget(self.CustomBase)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.CustomBaseOutput = QtWidgets.QLCDNumber(Form)
        self.CustomBaseOutput.setMinimumSize(QtCore.QSize(100, 50))
        self.CustomBaseOutput.setObjectName("CustomBaseOutput")
        self.horizontalLayout_4.addWidget(self.CustomBaseOutput)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.binaryAnswer.setFont(font)
        self.DecimalInOut.setFont(font)
        self.HexadecimalInOut.setFont(font)

        self.binaryAnswer.textEdited.connect(lambda text: self.update_answer(text, self.binaryAnswer))
        self.DecimalInOut.textEdited.connect(lambda text: self.update_answer(text, self.DecimalInOut))
        self.HexadecimalInOut.textEdited.connect(lambda text: self.update_answer(text, self.HexadecimalInOut))

        self.ResetButton.clicked.connect(self.clearTextBox)


        self.ResetButton.setIcon(QIcon("arrow_up.png"))
        # self.addHourButton.setIcon(QIcon("arrow_up.png"))
        # self.addHourButton.setIconSize(QSize(80, 80))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ResetButton.setText(_translate("Form", "Reset"))
        self.BinaryLabel.setText(_translate("Form", "Binary     "))
        self.DecimalLabel.setText(_translate("Form", "Decimal   "))
        self.HexaDecimalLabel.setText(_translate("Form", "HexaDecimal"))

    def clearTextBox(self):
        self.binaryAnswer.clear()
        self.DecimalInOut.clear()
        self.HexadecimalInOut.clear()

    def update_answer(self, text, obj):
        if obj is self.binaryAnswer:
            if is_base(text, 2):
                # self.DecimalInOut.setText(str(int(text, 2)))
                # self.HexadecimalInOut.setText(hex((int(text, 2)))[2:])
                self.DecimalInOut.setText(str(bin2dec(text)))
                self.HexadecimalInOut.setText(hex(bin2dec(text))[2:])
            else:
                self.DecimalInOut.setText("Error")
                self.HexadecimalInOut.setText("Error")
        elif obj == self.DecimalInOut:
            if is_base(text, 10):
                self.binaryAnswer.setText(bin(int(text))[2:])
                self.HexadecimalInOut.setText(hex(int(text))[2:])
            else:
                self.binaryAnswer.setText("Error")
                self.HexadecimalInOut.setText("Error")
        elif obj == self.HexadecimalInOut:
            if is_base(text, 16):
                self.binaryAnswer.setText(bin(hex2dec(text))[2:])
                self.DecimalInOut.setText(str(hex2dec(text)))
            else:
                self.binaryAnswer.setText("Error")
                self.DecimalInOut.setText("Error")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form(Form)
    Form.show()
    sys.exit(app.exec_())
