from PyQt6.QtWidgets import QWidget,QMainWindow,QVBoxLayout,QMenuBar,QMenu,QApplication
from PyQt6.QtGui import QIcon,QPixmap,QAction
from PyQt6.QtCore import QRect
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


        #设置菜单栏
        self.menuBar = QMenuBar(parent=self)
        self.menuBar.setGeometry(QRect(0,0,901,22))
        self.menuBar.setObjectName('MenuBar')

        #文件菜单
        self.fileMenu = QMenu(parent=self.menuBar)
        self.fileMenu.setObjectName('FileMenu')
        self.fileMenu.setTitle('文件')

        #配置菜单
        self.configMenu = QMenu(parent=self.menuBar)
        self.configMenu.setObjectName('ConfigMenu')
        self.configMenu.setTitle('配置')

        #文件导入操作
        self.importProdFile = QAction(parent=self.fileMenu)
        self.importProdFile.setObjectName('importProdFile')
        self.importProdFile.setText('导入需求表')

        #SCC配置文件搜索
        self.sccConfigFileRead = QAction(parent=self.configMenu)
        self.sccConfigFileRead.setObjectName('sccConfigFileRead')
        self.sccConfigFileRead.setText('SCC配置文件搜索')

        #退出菜单
        self.exit = QAction("&Exit",parent=self.fileMenu)
        self.exit.setShortcut('ctrl+q')
        self.exit.setObjectName('Exit')
        self.exit.setText('退出')
        self.exit.triggered.connect(QApplication.instance().quit)

        self.fileMenu.addAction(self.importProdFile)
        self.fileMenu.addAction(self.exit)
        self.configMenu.addAction(self.sccConfigFileRead)

        self.menuBar.addAction(self.fileMenu.menuAction())
        self.menuBar.addAction(self.configMenu.menuAction())

        self.centralWidget = CentralWidget(parent=self)

        # 加载CentralWidget
        self.setCentralWidget(self.centralWidget)

        self.show()