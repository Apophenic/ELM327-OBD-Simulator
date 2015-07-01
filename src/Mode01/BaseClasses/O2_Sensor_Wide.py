import abc

import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse


class O2_Sensor_Wide(OBDResponse):
    __metaclass__ = abc.ABCMeta

    ratio = None
    volt = None

    def getvalue(self):
        ratio = (int(self.byteA, 16) * 256 + int(self.byteB, 16)) * (2 / 65535)
        volt = (int(self.byteC, 16) * 256 + int(self.byteD, 16)) * (8 / 65535)
        return [ratio, volt]

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()
        self.byteC = Utils.getrandhex()
        self.byteD = Utils.getrandhex()

    @abc.abstractproperty
    def responsecode(self):
        pass
