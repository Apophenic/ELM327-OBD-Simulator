import Utils
from Response.BaseClasses.OBDResponse import OBDResponse

class FuelInjectionTiming(OBDResponse):

    def getvalue(self):
        return (int(self.byteA, 16) * 256 + int(self.byteB, 16) - 26880) / 128

    def responsecode(self):
        return '41 5D'

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()
