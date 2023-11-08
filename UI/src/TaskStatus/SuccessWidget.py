import sys

from PyQt6.QtGui import QPainter
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QSize

from UI.src.const_res_path import ResPath


#状态为成功的Widget，尺寸等属性从父对象继承
#当前Widget中放置一个QSvgWidget用以显示Svg图形
class SuccessWidget(QWidget):

    def __init__(self,parent=None):
        super().__init__()
        self.setupUI(parent)


    def setupUI(self,parent):
        self.setObjectName('Success')

        # self.item = QGraphicsSvgItem(ResPath.SUCCESS_ICON_PATH)
        # self.scene = QGraphicsScene()
        # self.scene.addItem(self.item)
        #
        # self.view = QGraphicsView()
        # self.view.setScene(self.scene)
        # # self.view.show()
        # self.view.setGeometry(300,300,100,100)
        # self.view.show()

        painter = QPainter()
        svgRender = QSvgRenderer(ResPath.SUCCESS_ICON_PATH)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = SuccessWidget()

    sys.exit(app.exec())