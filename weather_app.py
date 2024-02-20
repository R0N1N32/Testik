import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

# Класс, представляющий главное окно приложения
class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        # Инициализация пользовательского интерфейса
        self.init_ui()

    def init_ui(self):
        # Установка основных свойств окна
        self.setWindowTitle('Weather App')
        self.setGeometry(100, 100, 400, 200)

        # Создание вертикального макета для удобного размещения виджетов
        layout = QVBoxLayout()

        # Виджеты: метка, поле ввода, метка для результата и кнопка
        self.city_label = QLabel('Enter City:')
        self.city_input = QLineEdit()
        self.result_label = QLabel('')

        self.get_weather_button = QPushButton('Get Weather')
        # Подключение события нажатия на кнопку к соответствующему методу
        self.get_weather_button.clicked.connect(self.get_weather)

        # Добавление виджетов в макет
        layout.addWidget(self.city_label)
        layout.addWidget(self.city_input)
        layout.addWidget(self.get_weather_button)
        layout.addWidget(self.result_label)

        # Установка макета для главного окна
        self.setLayout(layout)

    def get_weather(self):
        # Получение названия города из поля ввода
        city = self.city_input.text()

        # Проверка наличия введенного города
        if not city:
            self.result_label.setText('Please enter a city.')
            return

        # Замените "YOUR_API_KEY" на ваш реальный ключ API OpenWeatherMap
        api_key = "bf6952d123d96f6e5ac1df111062effe"
        base_url = "http://api.openweathermap.org/data/2.5/weather"

        # Параметры запроса к API OpenWeatherMap
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric'  # Метрическая система для температуры в градусах Цельсия
        }

        try:
            # Отправка запроса к API OpenWeatherMap
            response = requests.get(base_url, params=params)
            data = response.json()

            # Извлечение температуры из ответа и отображение результата
            temperature = data['main']['temp']
            self.result_label.setText(f'Temperature in {city}: {temperature} °C')
        except Exception as e:
            # Обработка ошибок при запросе к API
            self.result_label.setText(f'Error fetching weather data: {str(e)}')

# Создание объекта приложения PyQt
app = QApplication([])
# Создание объекта главного окна приложения
weather_app = WeatherApp()
# Отображение главного окна
weather_app.show()
# Запуск цикла обработки событий приложения
app.exec()