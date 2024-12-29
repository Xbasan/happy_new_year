# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

from PySide6.QtCore import QTimer

import datetime


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.update_time()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        day = datetime.datetime.now().strftime("%d")
        minutes = datetime.datetime.now().strftime("%M")
        hours = datetime.datetime.now().strftime("%H")
        seconds = datetime.datetime.now().strftime("%S")

        self.ui.time_HNY.setText(f"{self.format_time(x=31, y=day)} Дней {self.format_time(x=23  , y=hours)} Часов {self.format_time(x=59, y=minutes)} Минут {self.format_time(x=59, y=seconds)} Секунд")

    def format_time(self, x, y):
        return x - int(y) if len(str(x - int(y))) == 2 else f'0{x - int(y)}'


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
