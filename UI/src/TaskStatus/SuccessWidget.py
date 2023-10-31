import sys

from PyQt6.QtWidgets import QWidget,QVBoxLayout,QApplication,QGraphicsScene,QGraphicsView,QGraphicsItem
from PyQt6.QtGui import QColor,QPainter
from PyQt6.QtSvgWidgets import QSvgWidget,QGraphicsSvgItem
from UI.src.const_res_path import ResPath


#状态为成功的Widget，尺寸等属性从父对象继承
#当前Widget中放置一个QSvgWidget用以显示Svg图形
class SuccessWidget(QWidget):

    def __init__(self,parent=None):
        super().__init__()
        self.setupUI(parent)


    def setupUI(self,parent):
        self.setObjectName('Success')

        self.vlayout = QVBoxLayout(self)
        self.vlayout.setObjectName('Internal Layout')

        #创建QSvgWidget
        self.successSvg = QSvgWidget(ResPath.SUCCESS_ICON_PATH,self)
        self.vlayout.addWidget(self.successSvg)
        self.setLayout(self.vlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    item = QGraphicsSvgItem(ResPath.FAILED_ICON_PATH)
    item.setFlag(QGraphicsItem.GraphicsItemFlag.ItemIsMovable)
    scene = QGraphicsScene()
    scene.addItem(item)

    view = QGraphicsView()
    view.setScene(scene)
    view.show()

    sys.exit(app.exec())