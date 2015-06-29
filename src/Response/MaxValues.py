import Utils
from Response.BaseClasses.OBDResponse import OBDResponse

class MaxValues(OBDResponse):

    def getvalue(self):
        ratio = int(self.byteA, 16)
        o2Voltage = int(self.byteB, 16)
        o2Current = int(self.byteC, 16)
        intakePressure = int(self.byteD, 16) * 10
        return [ratio, o2Voltage, o2Current, intakePressure]

    def responsecode(self):
        return '41 4F'

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()
        self.byteC = Utils.getrandhex()
        self.byteD = Utils.getrandhex()
