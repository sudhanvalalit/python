from MainWindow import Ui_MainWindow
from PyQt6 import QtWidgets
import sys


class CalcWindow(Ui_MainWindow, QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.equalButton.clicked.connect(self.calculation)
        self.cButton.clicked.connect(self.pressC)
        self.plusorminusButton.clicked.connect(self.change_sign)
        self.arrowButton.clicked.connect(self.remove_it)
        self.percentButton.clicked.connect(self.percent)
        self.zeroButton.clicked.connect(self.zero)
        self.oneButton.clicked.connect(self.one)
        self.twoButton.clicked.connect(self.two)
        self.threeButton.clicked.connect(self.three)
        self.fourButton.clicked.connect(self.four)
        self.fiveButton.clicked.connect(self.five)
        self.sixButton.clicked.connect(self.six)
        self.sevenButton.clicked.connect(self.seven)
        self.eightButton.clicked.connect(self.eight)
        self.nineButton.clicked.connect(self.nine)
        self.plusButton.clicked.connect(self.plus)
        self.minusButton.clicked.connect(self.subtract)
        self.divideButton.clicked.connect(self.divide)
        self.multiplyButton.clicked.connect(self.multiply)
        self.periodButton.clicked.connect(self.dot_it)

    def pressC(self):
        # if self.pressed == 'c':
        self.outputLabel.setText("0")

    def pressButton(self):
        screen = self.outputLabel.text()
        print(screen)
        if screen == "0" or screen == "NaN" or screen == "Incomplete":
            self.outputLabel.setText("0")
        self.outputLabel.setText(f'{screen}')

    #Numbers and symbols
    def zero(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + "0")

    def one(self):
        text = self.outputLabel.text()
        if text == "0":
            text = ""
        self.outputLabel.setText(text + "1")

    def two(self):
        text = self.outputLabel.text()
        if text == "0":
            text = ""
        self.outputLabel.setText(text + "2")

    def three(self):
        text = self.outputLabel.text()
        if text == "0":
            text = ""
        self.outputLabel.setText(text + "3")

    def four(self):
        text = self.outputLabel.text()
        if text == "0":
            text = ""
        self.outputLabel.setText(text + "4")

    def five(self):
        text = self.outputLabel.text()
        if text == "0":
            text = ""
        self.outputLabel.setText(text + "5")

    def six(self):
        text = self.outputLabel.text()
        if text == "0":
            text = ""
        self.outputLabel.setText(text + "6")

    def seven(self):
        text = self.outputLabel.text()
        if text == "0":
            text = ""
        self.outputLabel.setText(text + "7")

    def eight(self):
        text = self.outputLabel.text()
        if text == "0":
            text = ""
        self.outputLabel.setText(text + "8")

    def nine(self):
        text = self.outputLabel.text()
        if text == "0":
            text = ""
        self.outputLabel.setText(text + "9")

    def dot(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + ".")

    def plus(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + "+")

    def multiply(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + "*")

    def divide(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + "/")

    def subtract(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + "-")

    def percent(self):
        text = self.outputLabel.text()
        self.outputLabel.setText(text + "%")

    # Remove a symbol

    def remove_it(self):
        screen = self.outputLabel.text()
        print(len(screen))
        if len(screen) > 1:
            screen = screen[:-1]
        else:
            screen = "0"
        self.outputLabel.setText(f'{screen}')

    def calculation(self):
        screen = self.outputLabel.text()
        try:
            answer = eval(screen)
            self.outputLabel.setText(f"{answer}")
        except ZeroDivisionError:
            self.outputLabel.setText("NaN")
        except SyntaxError:
            self.outputLabel.setText("Incomplete")
        except NameError:
            self.pressC()

    # Change sign of the number
    def change_sign(self):
        screen = self.outputLabel.text()
        if "-" in screen:
            self.outputLabel.setText(f"{screen[1:]}")
            print(f"{screen[0]}")
        else:
            self.outputLabel.setText(f'-{screen}')

    # Add a decimal
    def check_symbol(self, s, arr):
        result = []
        for i in arr:
            if i in s:
                result.append(i)
        return result

    def dot_it(self):
        screen = self.outputLabel.text()
        if screen[-1] == ".":
            pass
        elif "." in screen:
            symbolList = ["+", "-", "/", "*"]
            result = self.check_symbol(screen, symbolList)
            if result is not []:
                for symbol in result:
                    num = screen.rindex(symbol)
                    if "." not in screen[num-1:]:
                        self.outputLabel.setText(f'{screen}.')
        else:
            self.outputLabel.setText(f'{screen}.')


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = CalcWindow()
    ui.show()
    sys.exit(app.exec())
