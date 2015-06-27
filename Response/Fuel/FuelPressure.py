import Utils
from Response.BaseClasses.OBDResponse import OBDResponse


class FuelPressure(OBDResponse):

    def getvalue(self):
        return int(self.byteA, 16) * 3

    def responsecode(self):
        return '41 0A'

    def __init__(self):
        self.byteA = Utils.getrandhex()
