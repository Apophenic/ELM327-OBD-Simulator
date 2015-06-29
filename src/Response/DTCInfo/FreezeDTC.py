import Utils
from Response.BaseClasses.OBDResponse import OBDResponse


class FreezeDTC(OBDResponse):

    def getvalue(self):
        pass    # No value

    def responsecode(self):
        return '41 02'

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()