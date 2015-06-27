import Utils
from Response.BaseClasses.OBDResponse import OBDResponse

class EthanolFuelPercent(OBDResponse):

    def getvalue(self):
        return int(self.byteA, 16) * 100 / 255

    def responsecode(self):
        return '41 52'

    def __init__(self):
        self.byteA = Utils.getrandhex()
