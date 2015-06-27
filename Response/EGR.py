import Utils
from Response.BaseClasses.OBDResponse import OBDResponse

class EGR(OBDResponse):

    def getvalue(self):
        return int(self.byteA, 16) * 100 / 255

    def responsecode(self):
        return '41 2C'

    def __init__(self):
        self.byteA = Utils.getrandhex()
