import abc

import Utils
from Response.BaseClasses.OBDResponse import OBDResponse

class O2_Sensor_Lambda(OBDResponse):
    __metaclass__ = abc.ABCMeta

    ratio = None
    current = None

    def getvalue(self):
        ratio = (int(self.byteA, 16) * 256 + int(self.byteB, 16)) / 32768
        current = (int(self.byteC, 16) * 256 + int(self.byteD, 16)) / 256 - 128
        return [ratio, current]

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()
        self.byteC = Utils.getrandhex()
        self.byteD = Utils.getrandhex()

    def responsecode(self):
        pass
