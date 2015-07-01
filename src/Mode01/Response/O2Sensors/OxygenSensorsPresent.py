import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse


class OxygenSensorsPresent(OBDResponse):

    def getvalue(self):
        pass    # TODO

    def responsecode(self):
        return '41 13'

    def __init__(self):
        self.byteA = Utils.getrandhex()
