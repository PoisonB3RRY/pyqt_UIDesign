#定义表格内数据类
class FormDataObject(object):

    def __init__(self):
        AppName = None
        Deployment = None
        ConfigMap = None
        Service = None
        ImageVersion = None

    @property
    def AppName(self):
        return self.AppName

    @AppName.setter
    def AppName(self, value):
        self.AppName = value

    @property
    def Deployment(self):
        return self.Deployment

    @Deployment.setter
    def Deployment(self, value):
        self.Deployment = value

    @property
    def ConfigMap(self):
        return self.ConfigMap

    @ConfigMap.setter
    def ConfigMap(self, value):
        self.ConfigMap = value

    @property
    def Service(self):
        return self.Service

    @Service.setter
    def Service(self, value):
        self.Service = value

    @property
    def ImageVersion(self):
        return self.ImageVersion

    @ImageVersion.setter
    def ImageVersion(self, value):
        self.ImageVersion = value
