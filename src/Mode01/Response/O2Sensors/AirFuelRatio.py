import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class AirFuelRatio(OBDResponse):

    def getvalue(self):
        return (int(self.byteA, 16) * 256 + int(self.byteB, 16)) / 32768

    def responsecode(self):
        return '41 44'

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()
