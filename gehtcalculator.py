"""GehtCalculator Ver 1.1"""

import userinterface as ui
from utilities import calculatorEngine
from PyQt5 import QtWidgets, Qt


class MainWindow(QtWidgets.QMainWindow):
    def linkButtons(self, buttons: tuple):
        self.buttons = buttons

    def keyPressEvent(self, event):
        if event.key() == Qt.Qt.Key_0:
            self.buttons[0].setFocus()
            self.buttons[0].click()
        elif event.key() == Qt.Qt.Key_1:
            self.buttons[1].setFocus()
            self.buttons[1].click()
        elif event.key() == Qt.Qt.Key_2:
            self.buttons[2].setFocus()
            self.buttons[2].click()
        elif event.key() == Qt.Qt.Key_3:
            self.buttons[3].setFocus()
            self.buttons[3].click()
        elif event.key() == Qt.Qt.Key_4:
            self.buttons[4].setFocus()
            self.buttons[4].click()
        elif event.key() == Qt.Qt.Key_5:
            self.buttons[5].setFocus()
            self.buttons[5].click()
        elif event.key() == Qt.Qt.Key_6:
            self.buttons[6].setFocus()
            self.buttons[6].click()
        elif event.key() == Qt.Qt.Key_7:
            self.buttons[7].setFocus()
            self.buttons[7].click()
        elif event.key() == Qt.Qt.Key_8:
            self.buttons[8].setFocus()
            self.buttons[8].click()
        elif event.key() == Qt.Qt.Key_9:
            self.buttons[9].setFocus()
            self.buttons[9].click()
        elif event.key() == Qt.Qt.Key_Plus:
            self.buttons[10].setFocus()
            self.buttons[10].click()
        elif event.key() == Qt.Qt.Key_Minus:
            self.buttons[11].setFocus()
            self.buttons[11].click()
        elif event.key() == Qt.Qt.Key_Slash:
            self.buttons[12].setFocus()
            self.buttons[12].click()
        elif event.key() == Qt.Qt.Key_Asterisk:
            self.buttons[13].setFocus()
            self.buttons[13].click()
        elif event.key() == Qt.Qt.Key_Return:
            self.buttons[14].setFocus()
            self.buttons[14].click()
        elif event.key() == Qt.Qt.Key_Backspace:
            self.buttons[15].setFocus()
            self.buttons[15].click()
        else:
            pass


class MainInterface(ui.Ui_MainWindow):
    def __init__(self):
        self.screenText = "0,00"
        self.operation = []
        self.buttonReset = False

    def setupDialog(self):
        self.Dialog = QtWidgets.QMessageBox()
        self.Dialog.setWindowTitle("ERROR")
        self.Dialog.setText(
            "El resultado contiene demasiados dígitos y no se puede " +
            "mostrar"
        )

    def setupUi(self, MainWindow):
        self.setupDialog()
        self.MainWindow = MainWindow
        super().setupUi(self.MainWindow)
        self.button0.clicked.connect(self.buttonPress)
        self.button1.clicked.connect(self.buttonPress)
        self.button2.clicked.connect(self.buttonPress)
        self.button3.clicked.connect(self.buttonPress)
        self.button4.clicked.connect(self.buttonPress)
        self.button5.clicked.connect(self.buttonPress)
        self.button6.clicked.connect(self.buttonPress)
        self.button7.clicked.connect(self.buttonPress)
        self.button8.clicked.connect(self.buttonPress)
        self.button9.clicked.connect(self.buttonPress)
        self.buttonPlus.clicked.connect(self.operatorPress)
        self.buttonMinus.clicked.connect(self.operatorPress)
        self.buttonDivide.clicked.connect(self.operatorPress)
        self.buttonMultiply.clicked.connect(self.operatorPress)
        self.buttonEquals.clicked.connect(self.operatorPress)
        self.buttonDelete.clicked.connect(self.miscPress)
        self.buttonClear.clicked.connect(self.miscPress)
        self.buttonCE.clicked.connect(self.miscPress)
        self.MainWindow.linkButtons((
                self.button0,
                self.button1,
                self.button2,
                self.button3,
                self.button4,
                self.button5,
                self.button6,
                self.button7,
                self.button8,
                self.button9,
                self.buttonPlus, # 10
                self.buttonMinus, # 11
                self.buttonDivide, # 12
                self.buttonMultiply, # 13
                self.buttonEquals, # 14
                self.buttonDelete, # 15
            ))

    def buttonPress(self):
        if self.buttonReset is True:
            self.updateDisplay(distype="R")
            self.operationScreen.setText("")
            self.buttonReset = False
        if len(self.screenText) >= 18:
            pass
        elif self.button0.hasFocus():
            self.updateDisplay("0")
        elif self.button1.hasFocus():
            self.updateDisplay("1")
        elif self.button2.hasFocus():
            self.updateDisplay("2")
        elif self.button3.hasFocus():
            self.updateDisplay("3")
        elif self.button4.hasFocus():
            self.updateDisplay("4")
        elif self.button5.hasFocus():
            self.updateDisplay("5")
        elif self.button6.hasFocus():
            self.updateDisplay("6")
        elif self.button7.hasFocus():
            self.updateDisplay("7")
        elif self.button8.hasFocus():
            self.updateDisplay("8")
        elif self.button9.hasFocus():
            self.updateDisplay("9")

    def miscPress(self):
        if self.buttonDelete.hasFocus():
            if self.screenText == "0,00":
                pass
            elif self.buttonReset:
                self.buttonCE.setFocus()
                self.buttonCE.click()
            else:
                textList = list(self.screenText)
                self.screenText = ""
                textList.pop()
                if len(textList) <= 3:
                    textList.insert(0, "0")
                self.checkPuntuation(textList, checktype="C")
                if textList[0] == ".":
                    textList.remove(".")
                for item in textList:
                    self.screenText += item
                self.numberScreen.setText(self.screenText)
        elif self.buttonClear.hasFocus():
            self.updateDisplay(distype="R")
        elif self.buttonCE.hasFocus():
            self.operation.clear()
            self.operationScreen.setText("")
            self.updateDisplay(distype="R")

    def operatorPress(self):
        if self.buttonPlus.hasFocus() and self.screenText != "0,00":
            self.addOperator("+")
        elif self.buttonMinus.hasFocus() and self.screenText != "0,00":
            self.addOperator("-")
        elif self.buttonDivide.hasFocus() and self.screenText != "0,00":
            self.addOperator("/")
        elif self.buttonMultiply.hasFocus() and self.screenText != "0,00":
            self.addOperator("*")
        elif self.buttonReset is True or len(self.operation) < 2:
            pass
        elif self.buttonEquals.hasFocus() and self.screenText != "0,00":
            self.operation.append(self.screenText)
            for number in range(len(self.operation)):
                if self.operation[number] in ("+", "-","*","/"):
                    pass
                else:
                    self.operation[number] = self.checkPuntuation(
                        self.operation[number],
                        checktype="R"
                    )
            self.operationScreen.setText(
                self.operationScreen.text() + (self.screenText + " = ")
            )
            solver = calculatorEngine(self.operation)
            try:
                self.screenText = self.checkPuntuation(
                    str(solver.solveEquation()),
                    checktype="P"
                )
            except ValueError:
                self.buttonCE.setFocus()
                self.buttonCE.click()
                self.Dialog.setText("El resultado no se puede imprimir")
                self.Dialog.exec()
            if len(self.screenText) > 18:
                self.buttonCE.setFocus()
                self.buttonCE.click()
                self.Dialog.exec()
            else:
                self.operation.clear()
                self.numberScreen.setText(self.screenText)
                self.buttonReset = True
            

    def updateDisplay(self, value=None, distype="D"):
        if distype == "D":
            if value == "0" and self.screenText == "0,00":
                pass
            else:
                self.screenText = self.checkPuntuation(
                    self.screenText.lstrip("0") + value,
                    checktype="C"
                )
                self.numberScreen.setText(self.screenText)
        elif distype == "R":
            self.screenText = "0,00"
            self.numberScreen.setText(self.screenText)

    def addOperator(self, operator: str):
        self.operation.append(self.screenText)
        self.operation.append(operator)
        if self.buttonReset is True:
            self.operationScreen.setText(self.screenText + f" {operator} ")
            self.buttonReset = False
        else:
            self.operationScreen.setText(
                self.operationScreen.text() +
                (self.screenText + f" {operator} ")
            )
        self.updateDisplay(distype="R")

    def checkPuntuation(self, tocheck, *, checktype="C"):
        if type(tocheck) is str:
            checklist = list(tocheck)
            tocheck = ""
        else:
            checklist = tocheck
        if checktype == "C":
            checklist.remove(",")
            checklist.insert(-2, ",")
            repeat = checklist.count(".")
            for dotremove in range(repeat):
                checklist.remove(".")
            for dotplace in range(repeat):
                checklist.insert(-6 - (dotplace * 4), ".")
            if checklist.count(".") < 1 and len(checklist) == 7:
                checklist.insert(-6, ".")
            elif checklist.count(".") < 2 and len(checklist) == 11:
                checklist.insert(-10, ".")
            elif checklist.count(".") < 3 and len(checklist) == 15:
                checklist.insert(-14, ".")
        elif checktype == "R":
            for dotremove in range(checklist.count(".")):
                checklist.remove(".")
            checklist.remove(",")
            checklist.insert(-2, ".")
        elif checktype == "P":
            if checklist[-3] != ".":
                checklist.append("0")
            checklist.remove(".")
            checklist.insert(-2, ",")
            if len(checklist) > 6:
                checklist.insert(-6, ".")
            if len(checklist) > 10:
                checklist.insert(-10, ".")
            if len(checklist) > 14:
                checklist.insert(-14, ".")
        if type(tocheck) is str:
            for item in checklist:
                tocheck += item
            return tocheck



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    interface = MainInterface()
    interface.setupUi(window)
    window.show()
    sys.exit(app.exec_())
