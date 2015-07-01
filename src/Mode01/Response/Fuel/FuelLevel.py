import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class FuelLevel(OBDResponse):

    def getvalue(self):
        return int(self.byteA, 16) * 100 / 255

    def responsecode(self):
        return '41 2F'

    def __init__(self):
        self.byteA = Utils.getrandhex()
