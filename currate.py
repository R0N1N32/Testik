import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QPushButton, QMessageBox

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Выберите валюту для конвертации", self)
        layout.addWidget(self.label)
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("EUR")
        self.comboBox.addItem("GBP")
        layout.addWidget(self.comboBox)

        self.button = QPushButton("Конвертировать", self)
        self.button.clicked.connect(self.on_click)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def on_click(self):
        selected_currency = self.comboBox.currentText()
        self.convert_currency(selected_currency)

    def convert_currency(self, currency):
        api_key = "ваш_ключ_api"
        base_url = f"https://currate.ru/api/?get=rates&pairs={currency}RUB&key={api_key}"
        response = requests.get(base_url)
        data = response.json()

        if "error" in data:
            QMessageBox.warning(self, "Ошибка", data["error"])
        else:
            rate = data["data"][f"{currency}RUB"]
            QMessageBox.information(self, "Курс валюты", f"1 {currency} = {rate} RUB")

def main():
    app = QApplication(sys.argv)

    converter = CurrencyConverter()
    converter.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()