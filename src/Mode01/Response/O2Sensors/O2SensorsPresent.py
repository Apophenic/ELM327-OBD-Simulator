import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse


class O2SensorsPresent(OBDResponse):

    def getvalue(self):
        pass    # TODO

    def responsecode(self):
        return '41 1D'

    def __init__(self):
        self.byteA = Utils.getrandhex()
