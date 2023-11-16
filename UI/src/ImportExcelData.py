import xlrd
from APP.src.FormDataObject import FormDataObject

class ExcelDataHandle:

    def importData(self,data_path,sheetname):
        DataRowArray = []