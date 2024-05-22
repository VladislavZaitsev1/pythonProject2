"""
Файл для повторения темы генерации сигналов и передачи данных из одного виджета в другой

Напомнить про работу с пользовательскими сигналами.

Предлагается создать 2 формы:
* На первый форме label с надписью "Пройдите регистрацию" и pushButton с текстом "Зарегистрироваться"
* На второй (QDialog) форме:
  * lineEdit с placeholder'ом "Введите логин"
  * lineEdit с placeholder'ом "Введите пароль"
  * pushButton "Зарегистрироваться"

  при нажатии на кнопку, данные из lineEdit'ов передаются в главное окно, в
  котором надпись "Пройдите регистрацию", меняется на "Добро пожаловать {данные из lineEdit с логином}"
  (пароль можно показать в терминале в захешированном виде)
"""

from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QSettings

ORG_NAME = "PCMaster"
APP_NAME = "MyApp"


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()
        self.__loadSettings()

    def __initUi(self):
        self.__plainTextEdit = QtWidgets.QPlainTextEdit()

        l = QtWidgets.QVBoxLayout()
        l.addWidget(self.__plainTextEdit)

        self.setLayout(l)

    def __loadSettings(self):
        settings = QtCore.QSettings(ORG_NAME, APP_NAME)
        self.__plainTextEdit.setPlainText(settings.value('text', ''))

    def __saveSettings(self):
        settings = QtCore.QSettings(ORG_NAME, APP_NAME)
        settings.setValue('text', self.__plainTextEdit.toPlainText())

    def closeEvent(self, event):
        self.__saveSettings()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
