import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class EGRError(OBDResponse):

    def getvalue(self):
        return (int(self.byteA, 16) - 128) * 100 / 128

    def responsecode(self):
        return '41 2D'

    def __init__(self):
        self.byteA = Utils.getrandhex()
