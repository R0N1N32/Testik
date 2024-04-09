from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog, QUndoStack
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
import os, sys

app = QApplication([])

window = QWidget()
window.resize(700, 500)
window.show()

# Виджеты левой части
dir_btn = QPushButton('Открыть папку')
files_list = QListWidget()
btn_save = QPushButton('Сохранить')
btn_save_as = QPushButton('Сохранить как')

# Левый лэйаут
left_col = QVBoxLayout()

# Размещение виджетов на левом лэйауте
left_col.addWidget(dir_btn)
left_col.addWidget(files_list)
left_col.addWidget(btn_save)
left_col.addWidget(btn_save_as)

# Виджеты правой части
image_preview = QLabel("Выберите изображение")
# Тулбар
toolbar = QHBoxLayout()

# Кнопки
btn_left = QPushButton('Влево')
btn_right = QPushButton('Вправо')
btn_flip = QPushButton('Зеркало')
btn_bw = QPushButton('Ч/Б')
btn_blur = QPushButton('Размытие')

# Размещение виджетов на тулбаре
toolbar.addWidget(btn_left)
toolbar.addWidget(btn_right)
toolbar.addWidget(btn_flip)
toolbar.addWidget(btn_bw)
toolbar.addWidget(btn_blur)

# Правый лэйаут
right_col = QVBoxLayout()

# Размещение виджетов на правом лэйауте
right_col.addWidget(image_preview)
right_col.addLayout(toolbar)


# Основной лэйаут
main_layout = QHBoxLayout()

# Размещение на основном лэйауте
main_layout.addLayout(left_col, 1)
main_layout.addLayout(right_col, 4)

# Установка основного лэйаута
window.setLayout(main_layout)

@pyqtSlot()
def on_close(obj):
    try:
        path = os.path.join(img.dir, img.save_dir, 'temp.png')
        if os.path.exists(path):
            os.remove(path)
    except:
        pass
    sys.exit(0)

window.closeEvent = on_close

def filter_files(files):
    ext = ['.png', '.jpg', '.jpeg', '.gif', '.bmp']
    filtered = []
    for f in files:
        for e in ext:
            if f.endswith(e):
                filtered.append(f)
    return filtered

app.exec()

