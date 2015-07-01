import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse


class TimingAdvance(OBDResponse):

    def getvalue(self):
        return (int(self.byteA, 16) - 128) / 2

    def responsecode(self):
        return '41 0E'

    def __init__(self):
        self.byteA = Utils.getrandhex()
