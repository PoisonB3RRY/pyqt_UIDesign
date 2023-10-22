from PyQt6.QtWidgets import QWidget,QVBoxLayout,QTableWidget,QTableWidgetItem,QCheckBox,QHBoxLayout

class CentralWidget(QWidget):

    def __init__(self,parent):
        super().__init__()
        self.setUpUI(parent)

    def setUpUI(self,parent):
        self.setObjectName('CentralWidget')

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName('Central Layout')

        #创建CentralWidget中的表格
        self.importedForm = QTableWidget(self)
        self.importedForm.setObjectName('Imported Form')
        self.importedForm.setColumnCount(7)

        #设置表头
        #第一列表头为全选复选框

        CBWidget = QWidget()
        CBWidget.columnName1CB = QCheckBox()
        CBWidget.columnName1CB.setText('全选')
        CBWidget.columnName1CB.setChecked(True)
        CBLayout = QHBoxLayout()
        CBLayout.addWidget(CBWidget.columnName1CB)
        CBWidget.setLayout(CBLayout)
        columnName1 = QTableWidgetItem(CBWidget)



        columnName2 = QTableWidgetItem('应用名称')
        columnName3 = QTableWidgetItem('Deployment')
        columnName4 = QTableWidgetItem('ConfigMap')
        columnName5 = QTableWidgetItem('Service')
        columnName6 = QTableWidgetItem('镜像版本')
        columnName7 = QTableWidgetItem('操作')

        self.importedForm.setHorizontalHeaderItem(0,columnName1)
        self.importedForm.setHorizontalHeaderItem(1,columnName2)
        self.importedForm.setHorizontalHeaderItem(2,columnName3)
        self.importedForm.setHorizontalHeaderItem(3,columnName4)
        self.importedForm.setHorizontalHeaderItem(4,columnName5)
        self.importedForm.setHorizontalHeaderItem(5,columnName6)
        self.importedForm.setHorizontalHeaderItem(6,columnName7)

        #级联对象的缩放
        self.importedForm.horizontalHeader().setCascadingSectionResizes(False)
        self.importedForm.horizontalHeader().setDefaultSectionSize(120)
        self.importedForm.horizontalHeader().setStretchLastSection(True)
        self.importedForm.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.importedForm)
