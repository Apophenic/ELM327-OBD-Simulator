import Utils
from Response.BaseClasses.OBDResponse import OBDResponse

class MaxValueMAF(OBDResponse):

    def getvalue(self):
        return int(self.byteA, 16) * 10
        # b, c, d are reserved

    def responsecode(self):
        return '41 50'

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()
        self.byteC = Utils.getrandhex()
        self.byteD = Utils.getrandhex()
