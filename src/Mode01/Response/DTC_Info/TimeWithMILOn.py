import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class TimeWithMILOn(OBDResponse):

    def getvalue(self):
        return (int(self.byteA, 16) * 256) + int(self.byteB, 16)

    def responsecode(self):
        return '41 4D'

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()
