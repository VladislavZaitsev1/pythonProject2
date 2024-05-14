from PySide6 import QtWidgets
from UI.b_ship import Ui_widget_ship


DEBUG = True
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_widget_ship()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()