import Utils
from Response.BaseClasses.OBDResponse import OBDResponse

class EngineRPM(OBDResponse):

    def getvalue(self):
        return ((int(self.byteA, 16) * 256) + int(self.byteB, 16)) / 4

    def responsecode(self):
        return '41 0C'

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()
