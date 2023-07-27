import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QFrame
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setWindowTitle('Math 1.0.0')
        self.setGeometry(100, 100, 350, 150)

        # Set the window color
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('#171717'))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Button, QColor('#171717'))
        palette.setColor(QPalette.ButtonText, Qt.white)
        self.setPalette(palette)

        # Create the tab widget
        self.tab_widget = QTabWidget(self)
        self.tab_widget.setTabPosition(QTabWidget.North)

        # Create 10 tabs
        for i in range(1, 6):
            tab = QWidget()
            tab.layout = QVBoxLayout()

            if i == 1:
                self.label = QLabel()
                self.error_label = QLabel()
                self.text_field = QLineEdit()
                self.text_field.returnPressed.connect(self.check_answer)
                self.ok_button = QPushButton('OK')
                self.ok_button.clicked.connect(self.check_answer)
                hbox_input = QHBoxLayout()
                hbox_input.addWidget(self.label)
                hbox_input.addWidget(self.text_field)
                hbox_input.addWidget(self.ok_button)
                tab.layout.addLayout(hbox_input)

                tab.layout.addWidget(self.error_label)

                line = QFrame()
                line.setFrameShape(QFrame.HLine)
                line.setFrameShadow(QFrame.Sunken)
                tab.layout.addWidget(line)

                self.memory_label = QLabel()
                self.memory_field = QLineEdit()
                self.memory_ok_button = QPushButton('OK')
                self.memory_ok_button.clicked.connect(self.hide_number)
                self.show_button = QPushButton('Show')
                self.show_button.clicked.connect(self.show_number)
                self.new_button = QPushButton('New')
                self.new_button.clicked.connect(self.new_number)
                hbox_memory = QHBoxLayout()
                hbox_memory.addWidget(self.memory_label)
                hbox_memory.addWidget(self.memory_field)
                hbox_memory.addWidget(self.memory_ok_button)
                tab.layout.addLayout(hbox_memory)

                hbox_buttons = QHBoxLayout()
                hbox_buttons.addWidget(self.show_button)
                hbox_buttons.addWidget(self.new_button)
                tab.layout.addLayout(hbox_buttons)

                self.generate_question()

            tab.setLayout(tab.layout)
            self.tab_widget.addTab(tab, f'Tab-{i}')

        # Set the tab widget as the central widget
        self.setCentralWidget(self.tab_widget)

    def generate_question(self):
        self.num1 = random.randint(10, 99)
        self.num2 = random.randint(10, 99)
        self.operation = random.choice(['+', '-'])
        self.label.setText(f'{self.num1} {self.operation} {self.num2}')
        self.memory_number = random.randint(100000, 999999)
        self.memory_label.setText(str(self.memory_number))
        self.text_field.setFocus()

    def check_answer(self):
        try:
            answer = float(self.text_field.text())
            if self.operation == '+':
                correct_answer = self.num1 + self.num2
            elif self.operation == '-':
                correct_answer = self.num1 - self.num2
            else:
                correct_answer = self.num1 * self.num2
            if abs(answer - correct_answer) < 0.01:
                self.error_label.setStyleSheet('color: green')
                self.error_label.setText('Correct!')
            else:
                self.error_label.setStyleSheet('color: red')
                self.error_label.setText(f'Incorrect! The correct answer is {correct_answer}')
            self.text_field.clear()
            self.generate_question()
        except ValueError:
            self.error_label.setStyleSheet('color: red')
            self.error_label.setText('The input field is empty.')

    def hide_number(self):
        self.memory_label.clear()

    def show_number(self):
        try:
            answer = int(self.memory_field.text())
            if answer == self.memory_number:
                self.memory_label.setStyleSheet('color: green')
                self.memory_label.setText('Correct!')
            else:
                self.memory_label.setStyleSheet('color: red')
                self.memory_label.setText(f'Incorrect! The correct number is {self.memory_number}')
            self.memory_field.clear()
        except ValueError:
            self.memory_label.setStyleSheet('color: red')
            self.memory_label.setText('The input field is empty.')

    def new_number(self):
        self.memory_number = random.randint(100000, 999999)
        self.memory_label.setText(str(self.memory_number))


def main():
    app = QApplication(sys.argv)

    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
