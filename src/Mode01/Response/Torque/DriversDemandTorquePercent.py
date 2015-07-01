import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class DriversDemandTorquePercent(OBDResponse):

    def getvalue(self):
        return int(self.byteA, 16) - 125

    def responsecode(self):
        return '41 61'

    def __init__(self):
        self.byteA = Utils.getrandhex()
