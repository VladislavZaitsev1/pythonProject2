from PySide6 import QtWidgets
from UI.login_form import Ui_Form


DEBUG = True
class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if DEBUG:
            self.ui.lineEdit_login.setText("ZVV")
            self.ui.lineEdit_password.setText("ZVV")

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()