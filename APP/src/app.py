import sys
from PyQt6.QtWidgets import QApplication
# from UI.template.Ui_demo1_helloworld import Ui_MainWindow
from UI.src.MainWindows import MainWindow

class SIPS(MainWindow):

    def __init__(self):
        super().__init__()
        # self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    sips = SIPS()

    sys.exit(app.exec())