from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QGridLayout, QLabel, QVBoxLayout

app = QApplication([])

window = QWidget()
window.setWindowTitle("Калькулятор")
window.show()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

grid = QGridLayout()

for b in buttons:
    temp = QPushButton(b)
    grid.addWidget(temp, buttons.index(b) // 4, buttons.index(b) % 4)

main_layout = QVBoxLayout()

main_layout.addLayout(grid)

window.setLayout(main_layout)

app.exec()


