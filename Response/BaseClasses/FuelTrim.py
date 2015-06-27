import abc

import Utils
from Response.BaseClasses.OBDResponse import OBDResponse


class FuelTrim(OBDResponse):
    __metaclass__ = abc.ABCMeta

    def getvalue(self):
        return (int(self.byteA, 16) - 128) * (100 / 128)

    def __init__(self):
        self.byteA = Utils.getrandhex()

    @abc.abstractproperty
    def responsecode(self):
        pass
