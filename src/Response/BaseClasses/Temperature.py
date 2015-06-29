import abc

import Utils
from Response.BaseClasses.OBDResponse import OBDResponse


class Temperature(OBDResponse):
    __metaclass__ = abc.ABCMeta

    def getvalue(self):
        return int(self.byteA, 16) - 40

    def __init__(self):
        self.byteA = Utils.getrandhex()