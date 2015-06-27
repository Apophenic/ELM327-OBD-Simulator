import Utils
from Response.BaseClasses.OBDResponse import OBDResponse

class BarometricPressure(OBDResponse):

    def getvalue(self):
        return int(self.byteA)

    def responsecode(self):
        return '41 33'

    def __init__(self):
        self.byteA = Utils.getrandhex()
