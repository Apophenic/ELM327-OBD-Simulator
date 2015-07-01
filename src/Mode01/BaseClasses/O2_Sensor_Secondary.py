import abc
import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class O2_Sensor_Secondary(OBDResponse):
    def responsecode(self):
        pass

    __metaclass__ = abc.ABCMeta

    def getvalue(self):
        bankA = (int(self.byteA, 16) - 128) * 100 / 128
        bankB = (int(self.byteB, 16) - 128) * 100 / 128
        return [bankA, bankB]

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()