import abc

import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse


class ThrottlePosition(OBDResponse):
    __metaclass__ = abc.ABCMeta

    def getvalue(self):
        return int(self.byteA, 16) * 100 / 255

    def __init__(self):
        self.byteA = Utils.getrandhex()

    @abc.abstractproperty
    def responsecode(self):
        pass