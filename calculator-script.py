import sys
import PyQt5.Qt
from PyQt5 import *
from PyQt5 import QtWidgets, uic
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QFile

postfixNotationModule = __import__("postfix-notation")


class CalculatorUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(CalculatorUI, self).__init__()
        uic.loadUi('CalculatorUI.ui', self)
        self.initUI()

    def initUI(self):
        self.initializeDigitButtons()
        self.initializeArithmeticalActionsButtons()
        self.initializeBracketButtons()
        self.initializeTrigonometricButtons()
        self.initializeBinHexOctButtons()
        self.initializeBHOButtons()
        self.initializeHexLettersButtons()
        self.clearLastSymbolButton = self.findChild(QtWidgets.QPushButton, 'clearLastSymbolButton')
        self.clearLastSymbolButton.clicked.connect(self.clearLastSymbol)
        self.clearAllTextButton = self.findChild(QtWidgets.QPushButton, 'clearAllTextButton')
        self.clearAllTextButton.clicked.connect(self.clearAllText)
        self.expressionTextBox = self.findChild(QtWidgets.QTextEdit, 'expressionTextBox')
        self.calculateExpressionButton = self.findChild(QtWidgets.QPushButton, 'calculateExpressionButton')
        self.calculateExpressionButton.clicked.connect(self.calculateExpressionButtonClicked)
        self.resultTextBox = self.findChild(QtWidgets.QTextEdit, 'resultTextBox')
        self.show()

    def initializeDigitButtons(self):
        self.button1digit = self.findChild(QtWidgets.QPushButton, 'Button1Digit')
        self.button1digit.clicked.connect(self.digitButtonPressed)
        self.button2digit = self.findChild(QtWidgets.QPushButton, 'Button2Digit')
        self.button2digit.clicked.connect(self.digitButtonPressed)
        self.button3digit = self.findChild(QtWidgets.QPushButton, 'Button3Digit')
        self.button3digit.clicked.connect(self.digitButtonPressed)
        self.button4digit = self.findChild(QtWidgets.QPushButton, 'Button4Digit')
        self.button4digit.clicked.connect(self.digitButtonPressed)
        self.button5digit = self.findChild(QtWidgets.QPushButton, 'Button5Digit')
        self.button5digit.clicked.connect(self.digitButtonPressed)
        self.button6digit = self.findChild(QtWidgets.QPushButton, 'Button6Digit')
        self.button6digit.clicked.connect(self.digitButtonPressed)
        self.button7digit = self.findChild(QtWidgets.QPushButton, 'Button7Digit')
        self.button7digit.clicked.connect(self.digitButtonPressed)
        self.button8digit = self.findChild(QtWidgets.QPushButton, 'Button8Digit')
        self.button8digit.clicked.connect(self.digitButtonPressed)
        self.button9digit = self.findChild(QtWidgets.QPushButton, 'Button9Digit')
        self.button9digit.clicked.connect(self.digitButtonPressed)
        self.button0digit = self.findChild(QtWidgets.QPushButton, 'Button0Digit')
        self.button0digit.clicked.connect(self.digitButtonPressed)
        self.dotButton = self.findChild(QtWidgets.QPushButton, 'dotButton')
        self.dotButton.clicked.connect(self.dotButtonPressed)

    def initializeArithmeticalActionsButtons(self):
        self.plusButton = self.findChild(QtWidgets.QPushButton, 'plusButton')
        self.plusButton.clicked.connect(self.arithmeticalActionButtonPressed)
        self.subtractButton = self.findChild(QtWidgets.QPushButton, 'subtractButton')
        self.subtractButton.clicked.connect(self.arithmeticalActionButtonPressed)
        self.multiplyButton = self.findChild(QtWidgets.QPushButton, 'multiplyButton')
        self.multiplyButton.clicked.connect(self.arithmeticalActionButtonPressed)
        self.divideButton = self.findChild(QtWidgets.QPushButton, 'divideButton')
        self.divideButton.clicked.connect(self.arithmeticalActionButtonPressed)

    def initializeBracketButtons(self):
        self.leftBracketButton = self.findChild(QtWidgets.QPushButton, 'leftBracketButton')
        self.leftBracketButton.clicked.connect(self.bracketButtonPressed)
        self.rightBracketButton = self.findChild(QtWidgets.QPushButton, 'rightBracketButton')
        self.rightBracketButton.clicked.connect(self.bracketButtonPressed)

    def initializeTrigonometricButtons(self):
        self.sinButton = self.findChild(QtWidgets.QPushButton, 'sinButton')
        self.sinButton.clicked.connect(self.trigonometricalAndBinHexOctButtonPressed)
        self.cosButton = self.findChild(QtWidgets.QPushButton, 'cosButton')
        self.cosButton.clicked.connect(self.trigonometricalAndBinHexOctButtonPressed)
        self.tgButton = self.findChild(QtWidgets.QPushButton, 'tgButton')
        self.tgButton.clicked.connect(self.trigonometricalAndBinHexOctButtonPressed)
        self.ctgButton = self.findChild(QtWidgets.QPushButton, 'ctgButton')
        self.ctgButton.clicked.connect(self.trigonometricalAndBinHexOctButtonPressed)

    def initializeBinHexOctButtons(self):
        self.binButton = self.findChild(QtWidgets.QPushButton, 'binButton')
        self.binButton.clicked.connect(self.trigonometricalAndBinHexOctButtonPressed)
        self.hexButton = self.findChild(QtWidgets.QPushButton, 'hexButton')
        self.hexButton.clicked.connect(self.trigonometricalAndBinHexOctButtonPressed)
        self.octButton = self.findChild(QtWidgets.QPushButton, 'octButton')
        self.octButton.clicked.connect(self.trigonometricalAndBinHexOctButtonPressed)

    def initializeBHOButtons(self):
        self.bButton = self.findChild(QtWidgets.QPushButton, 'bButton')
        self.bButton.clicked.connect(self.BHOButtonPressed)
        self.hButton = self.findChild(QtWidgets.QPushButton, 'hButton')
        self.hButton.clicked.connect(self.BHOButtonPressed)
        self.oButton = self.findChild(QtWidgets.QPushButton, 'oButton')
        self.oButton.clicked.connect(self.BHOButtonPressed)

    def initializeHexLettersButtons(self):
        self.aHexButton = self.findChild(QtWidgets.QPushButton, 'aHexButton')
        self.aHexButton.clicked.connect(self.hexLetterButtonPressed)
        self.bHexButton = self.findChild(QtWidgets.QPushButton, 'bHexButton')
        self.bHexButton.clicked.connect(self.hexLetterButtonPressed)
        self.cHexButton = self.findChild(QtWidgets.QPushButton, 'cHexButton')
        self.cHexButton.clicked.connect(self.hexLetterButtonPressed)
        self.dHexButton = self.findChild(QtWidgets.QPushButton, 'dHexButton')
        self.dHexButton.clicked.connect(self.hexLetterButtonPressed)
        self.eHexButton = self.findChild(QtWidgets.QPushButton, 'eHexButton')
        self.eHexButton.clicked.connect(self.hexLetterButtonPressed)
        self.fHexButton = self.findChild(QtWidgets.QPushButton, 'fHexButton')
        self.fHexButton.clicked.connect(self.hexLetterButtonPressed)

    def digitButtonPressed(self):
        sender = self.sender()
        text = str(self.expressionTextBox.toPlainText())
        if len(text) != 0:
            if text[len(text) - 1] == "0" and (text[len(text) - 2] == "+" or text[len(text) - 2] == "-" or text[len(text) - 2] == "*" or text[len(text) - 2] == "/" or text[len(text) - 2] == "("):
                return
            if text[len(text) - 1] == ")":
                return
            symbolIndex = len(text) - 1
            while symbolIndex != -1:
                if str.isdigit(text[symbolIndex]):
                    symbolIndex -= 1
                elif text[symbolIndex] == 'b' and (sender.text() != '0' and sender.text() != '1'):
                    return
                elif text[symbolIndex] == 'o' and (sender.text() == '8' or sender.text() == '9'):
                    return
                else:
                    self.expressionTextBox.setText(text + sender.text())
                    break

        self.expressionTextBox.setText(text + sender.text())

    def arithmeticalActionButtonPressed(self):
        sender = self.sender()
        text = str(self.expressionTextBox.toPlainText())
        if sender.text() != '-' and len(text) == 0:
            return
        if len(text) != 0:
            if text[len(text) - 1] == '-' or text[len(text) - 1] == '+' or text[len(text) - 1] == '*' or text[len(text) - 1] == '/':
                return
            if text[len(text) - 1] == 'b' or text[len(text) - 1] == 'h' or text[len(text) - 1] == 'o':
                return
            if text[len(text) - 1] == '(' and sender.text() != '-':
                return
        self.expressionTextBox.setText(text + sender.text())

    def clearLastSymbol(self):
        if len(str(self.expressionTextBox.toPlainText())) == 0:
            return
        self.expressionTextBox.setText(str(self.expressionTextBox.toPlainText())[:-1])

    def clearAllText(self):
        if len(str(self.expressionTextBox.toPlainText())) == 0:
            return
        self.expressionTextBox.setText("")

    def bracketButtonPressed(self):
        sender = self.sender()
        currentExpressionText = str(self.expressionTextBox.toPlainText())
        if len(currentExpressionText) != 0:
            if sender.text() == ")":
                leftBracketCount = currentExpressionText.count('(')
                rightBracketCount = currentExpressionText.count(')')
                if leftBracketCount <= rightBracketCount:
                    return
            if (str.isdigit(currentExpressionText[len(currentExpressionText) - 1]) and sender.text() == "(") or currentExpressionText[len(currentExpressionText) - 1] == '.':
                return
            if currentExpressionText[len(currentExpressionText) - 1] == 'b' or currentExpressionText[len(currentExpressionText) - 1] == 'h' or currentExpressionText[len(currentExpressionText) - 1] == 'o':
                return
            if sender.text() == "(" and currentExpressionText[len(currentExpressionText) - 1] == ")":
                return
        self.expressionTextBox.setText(currentExpressionText + sender.text())

    def trigonometricalAndBinHexOctButtonPressed(self):
        sender = self.sender()
        currentExpressionText = str(self.expressionTextBox.toPlainText())
        if len(currentExpressionText) != 0:
            if currentExpressionText[len(currentExpressionText) - 1] == ")" or str.isdigit(currentExpressionText[len(currentExpressionText) - 1]) or currentExpressionText[len(currentExpressionText) - 1] == ".":
                return
            if currentExpressionText[len(currentExpressionText) - 1] == 'b' or currentExpressionText[len(currentExpressionText) - 1] == 'h' or currentExpressionText[len(currentExpressionText) - 1] == 'o':
                return
        self.expressionTextBox.setText(currentExpressionText + sender.text() + '(')

    def dotButtonPressed(self):
        sender = self.sender()
        currentExpressionText = str(self.expressionTextBox.toPlainText())
        if len(currentExpressionText) != 0:
            if not str.isdigit(currentExpressionText[len(currentExpressionText) - 1]):
                return
            symbolIndex = len(currentExpressionText) - 1
            while symbolIndex != -1:
                if str.isdigit(currentExpressionText[symbolIndex]):
                    symbolIndex -= 1
                elif currentExpressionText[symbolIndex] == 'h':
                    return
                elif currentExpressionText[symbolIndex] == 'b':
                    return
                elif currentExpressionText[symbolIndex] == 'o':
                    return
                else:
                    self.expressionTextBox.setText(currentExpressionText + sender.text())
                    break
        else:
            return
        self.expressionTextBox.setText(currentExpressionText + sender.text())

    def BHOButtonPressed(self):
        sender = self.sender()
        currentExpressionText = str(self.expressionTextBox.toPlainText())
        if len(currentExpressionText) != 0:
            if currentExpressionText[len(currentExpressionText) - 1] == '.' or currentExpressionText[len(currentExpressionText) - 1] == ')':
                return
            if str.isdigit(currentExpressionText[len(currentExpressionText) - 1]):
                return
            if currentExpressionText[len(currentExpressionText) - 1] == 'b' or currentExpressionText[len(currentExpressionText) - 1] == 'h' or currentExpressionText[len(currentExpressionText) - 1] == 'o':
                return
        self.expressionTextBox.setText(currentExpressionText + sender.text())

    def hexLetterButtonPressed(self):
        sender = self.sender()
        currentExpressionText = str(self.expressionTextBox.toPlainText())
        if len(currentExpressionText) != 0:
            if currentExpressionText[len(currentExpressionText) - 1] == '.' or currentExpressionText[len(currentExpressionText) - 1] == ')':
                return
            lastSymbolIndex = len(currentExpressionText) - 1
            while lastSymbolIndex != -1:
                if str.isdigit(currentExpressionText[lastSymbolIndex]) or currentExpressionText[lastSymbolIndex] == 'A' or currentExpressionText[lastSymbolIndex] == 'B' or currentExpressionText[lastSymbolIndex] == 'C' or currentExpressionText[lastSymbolIndex] == 'D' or currentExpressionText[lastSymbolIndex] == 'E' or currentExpressionText[lastSymbolIndex] == 'F':
                    lastSymbolIndex = lastSymbolIndex - 1
                elif currentExpressionText[lastSymbolIndex] != 'h':
                    return
                else:
                    self.expressionTextBox.setText(currentExpressionText + sender.text())
                    break

    def calculateExpressionButtonClicked(self):
        currentExpressionText = str(self.expressionTextBox.toPlainText())
        if len(currentExpressionText) < 3:
            return
        leftBracketCount = currentExpressionText.count('(')
        rightBracketCount = currentExpressionText.count(')')
        if leftBracketCount != rightBracketCount:
            self.resultTextBox.setText('Недостатня кількість закриваючих дужок')
            return
        if currentExpressionText[len(currentExpressionText) - 1] == 'h' or currentExpressionText[len(currentExpressionText) - 1] == 'b' or currentExpressionText[len(currentExpressionText) - 1] == 'o':
            self.resultTextBox.setText('Заповніть числа з систем числення')
            return
        if currentExpressionText[len(currentExpressionText) - 1] == '+' or currentExpressionText[len(currentExpressionText) - 1] == '-' or currentExpressionText[len(currentExpressionText) - 1] == '/' or currentExpressionText[len(currentExpressionText) - 1] == '*':
            self.resultTextBox.setText('Завершіть вираз')
            return
        for i in range(len(currentExpressionText)):
            if currentExpressionText[i] == '/':
                if i + 2 >= (len(currentExpressionText) - 1):
                    if currentExpressionText[i + 1] == '0':
                        self.resultTextBox.setText('Ділення на 0 заборонене')
                        return
                elif currentExpressionText[i + 1] == '0' and currentExpressionText[i + 2] != '.':
                    self.resultTextBox.setText('Ділення на 0 заборонене')
                    return
            if i + 1 <= len(currentExpressionText) - 1:
                if ((currentExpressionText[i] == 'b' and currentExpressionText[i + 1] != 'i') or (currentExpressionText[i] == 'o' and currentExpressionText[i + 1] != 'c')) and not str.isdigit(currentExpressionText[i + 1]):
                    self.resultTextBox.setText('Заповніть числа з систем числення')
                    return
                elif (currentExpressionText[i] == 'h' and currentExpressionText[i + 1] != 'e') and (not str.isdigit(currentExpressionText[i + 1]) and currentExpressionText[i + 1] != 'A' and currentExpressionText[i + 1] != 'B' and currentExpressionText[i + 1] != 'C' and currentExpressionText[i + 1] != 'D' and currentExpressionText[i + 1] != 'E' and currentExpressionText[i + 1] != 'F'):
                    self.resultTextBox.setText('Заповніть числа з систем числення')
                    return
        resultText = postfixNotationModule.setWholeExpression(currentExpressionText)
        self.resultTextBox.setText(str(resultText))


app = QApplication(sys.argv)
window = CalculatorUI()
app.exec_()


sys.exit(app.exec_())
