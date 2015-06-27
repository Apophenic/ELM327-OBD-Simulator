import abc

import Utils
from Response.BaseClasses.OBDResponse import OBDResponse


class O2_Sensor_Secondary(OBDResponse):
    __metaclass__ = abc.ABCMeta

    def getvalue(self):
        bankA = (int(self.byteA, 16) - 128) * 100 / 128
        bankB = (int(self.byteB, 16) - 128) * 100 / 128
        return [bankA, bankB]

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()