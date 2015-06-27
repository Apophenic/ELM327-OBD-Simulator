import Utils
from Response.BaseClasses.OBDResponse import OBDResponse


class IntakeManifoldPressure(OBDResponse):

    def getvalue(self):
        return int(self.byteA, 16)

    def responsecode(self):
        return '41 0B'

    def __init__(self):
        self.byteA = Utils.getrandhex()
