import abc

import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse


class O2_Sensor_Narrow(OBDResponse):
    __metaclass__ = abc.ABCMeta

    volt = None
    percent = None

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()

    def getvalue(self):
        volt = int(self.byteA, 16) / 200
        if self.byteB != 'FF':
            percent = (int(self.byteB, 16) - 128) * (100 / 128)
        return [volt, percent]

    def responsecode(self):
        pass
