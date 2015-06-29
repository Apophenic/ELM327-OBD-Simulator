import Utils
from Response.BaseClasses.OBDResponse import OBDResponse

class EngineFuelRate(OBDResponse):

    def getvalue(self):
        return (int(self.byteA, 16) * 256 + int(self.byteB, 16)) * .05

    def responsecode(self):
        return '41 5E'

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()
