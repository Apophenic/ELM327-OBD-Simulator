import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class MonitorStatusThisDriveCycle(OBDResponse):

    def getvalue(self):
        pass    # TODO

    def responsecode(self):
        return '41 41'

    def __init__(self):
        self.byteA = '00'
        self.byteB = Utils.getrandhex()
        self.byteC = Utils.getrandhex()
        self.byteD = Utils.getrandhex()
