from PyQt6.QtCore import Qt, pyqtSignal, QRect
from PyQt6.QtWidgets import QHeaderView, QStyle, QStyleOptionButton

# 存储所有勾选项目的数组
all_header_combobox = []


class CheckBoxHeader(QHeaderView):
    # 定义全选信号
    select_all_clicked = pyqtSignal(bool)

    # 确定组件坐标
    _x_offset = 15
    _y_offset = 0
    _height = 20
    _width = 20

    # orientation=Hrizontal表示表头为水平表头
    def __init__(self, orientation=Qt.Orientation.Horizontal, parent=None):
        super().__init__(orientation, parent)
        self.isOn = False  # 初始化勾选状态为False

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super().paintSection(painter, rect, logicalIndex)
        painter.restore()

        self._y_offset = int((rect.height() - self._width) / 2)

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.StateFlag.State_Enabled | QStyle.StateFlag.State_Active
            if self.isOn == True:
                option.state |= QStyle.StateFlag.State_On
            else:
                option.state |= QStyle.StateFlag.State_Off
            self.style().drawControl(QStyle.ControlElement.CE_CheckBox, option, painter)

    def mousePressEvent(self, e):
        index = self.logicalIndexAt(e.pos())
        if 0 == index:
            x = self.sectionPosition(index)
            if x + self._x_offset < e.pos().x() < x + self._x_offset + self._width and self._y_offset < e.pos().y() < self._y_offset + self._height:
                if self.isOn:
                    self.isOn = False
                else:
                    self.isOn = True
                # 当用户点击了行表头复选框，发射自定义信号 select_all_clicked()
                self.select_all_clicked.emit(self.isOn)
                self.updateSection(0)
        super().mousePressEvent(e)

    def change_state(self, isOn):
        if isOn:
            for i in all_header_combobox:
                i.setCheckState(Qt.CheckState.Checked)
        else:
            for i in all_header_combobox:
                i.setCheckState(Qt.CheckState.Unchecked)
