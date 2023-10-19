from PyQt6 import QtCore
from PyQt6.QtWidgets import QWidget,QMainWindow
from PyQt6.QtGui import QIcon,QPixmap
from const_res_path import ResPath
from CentralWidget import CentralWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setUpUI()

    def setUpUI(self):
        self.setObjectName('MainWindow')
        self.resize(901,670)
        self.setMouseTracking(False)

        self.icon = QIcon()
        self.icon.addPixmap(QPixmap(ResPath.SPDB_ICON_PATH),QIcon.Mode.Normal,QIcon.State.Off)
        self.setWindowIcon(self.icon)
        self.setWindowTitle('云管综合发布系统')

        #加载CentralWidget
        self.centralWidget = CentralWidget()


        self.show()