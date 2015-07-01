import abc
import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class Catalyst(OBDResponse):
    __metaclass__ = abc.ABCMeta

    def getvalue(self):
        return (int(self.byteA, 16) * 256 + int(self.byteB, 16)) / 10 - 40

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()

    @abc.abstractproperty
    def responsecode(self):
        pass
