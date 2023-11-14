import sys

from PyQt6.QtGui import QPainter,QImage,QColor,QPixmap
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtSvgWidgets import QGraphicsSvgItem
from PyQt6.QtWidgets import QApplication, QWidget, QGraphicsScene, QGraphicsView
from PyQt6.QtCore import QSize,Qt

from UI.src.const_res_path import ResPath


#状态为成功的Widget，尺寸等属性从父对象继承
#当前Widget中放置一个QSvgWidget用以显示Svg图形
class SuccessWidget(QWidget):

    def __init__(self,parent=None):
        super().__init__()
        self.setupUI(parent)


    def setupUI(self,parent):
        self.setObjectName('Success')

        self.item = QGraphicsSvgItem(ResPath.SUCCESS_ICON_PATH)
        self.item.setScale(0.15)
        self.scene = QGraphicsScene(20,32,50,50)
        self.scene.addItem(self.item)
        self.item.setPos(0, 0)

        self.scene.setBackgroundBrush(Qt.GlobalColor.blue)


        self.view = QGraphicsView(self)
        self.view.setScene(self.scene)
        #后续将尺寸、坐标更改为TableWidgetItem的大小
        self.view.setGeometry(0,0,100,100)
        self.show()




if __name__ == '__main__':
    app = QApplication(sys.argv)

    ex = SuccessWidget()

    sys.exit(app.exec())