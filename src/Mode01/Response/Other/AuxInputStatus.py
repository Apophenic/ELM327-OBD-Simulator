import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class AuxInputStatus(OBDResponse):

    def getvalue(self):
        pass    # TODO

    def responsecode(self):
        return '41 1E'

    def __init__(self):
        self.byteA = Utils.getrandhex()
