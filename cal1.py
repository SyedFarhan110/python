import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        layout = QVBoxLayout()

        self.result = QLineEdit()
        self.result.setReadOnly(True)
        layout.addWidget(self.result)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        for button in buttons:
            button_object = QPushButton(button)
            button_object.clicked.connect(self.button_clicked)
            layout.addWidget(button_object)

        self.setLayout(layout)

    def button_clicked(self):
        button = self.sender()
        if button.text() == "=":
            result = eval(self.result.text())
            self.result.setText(str(result))
        elif button.text() == "C":
            self.result.setText("")
        else:
            text = self.result.text() + button.text()
            self.result.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())
