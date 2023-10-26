import sys

from PyQt6.QtWidgets import QWidget,QVBoxLayout,QTableWidget,QCheckBox,QHeaderView,QStyle,QStyleOptionButton,QTableWidgetItem
from PyQt6.QtCore import Qt,pyqtSignal,QRect

class CheckBoxHeader(QHeaderView):

    #定义全选信号
    select_all_clicked = pyqtSignal(bool)

    #确定组件坐标
    _x_offset = 0
    _y_offset = 0
    _height = 20
    _width = 20
   #orientation=Hrizontal表示表头为水平表头
    def __init__(self,orientation=Qt.Orientation.Horizontal,parent=None):
        super().__init__(orientation,parent)
        self.isOn = False  #初始化勾选状态为False

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super().paintSection(painter,rect,logicalIndex)
        painter.restore()

