import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class NumWarmUpsSinceCodesCleared(OBDResponse):

    def getvalue(self):
        return int(self.byteA, 16)

    def responsecode(self):
        return '41 30'

    def __init__(self):
        self.byteA = Utils.getrandhex()
