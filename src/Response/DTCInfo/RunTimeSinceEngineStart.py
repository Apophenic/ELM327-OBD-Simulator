import Utils
from Response.BaseClasses.OBDResponse import OBDResponse


class RunTimeSinceEngineStart(OBDResponse):

    def getvalue(self):
        return (int(self.byteA, 16) * 256) + int(self.byteB, 16)

    def responsecode(self):
        return '41 1F'

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()
