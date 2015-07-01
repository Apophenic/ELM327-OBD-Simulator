import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class VehicleEmissionsRequirements(OBDResponse):

    def getvalue(self):
        pass    # TODO

    def responsecode(self):
        return '41 5F'

    def __init__(self):
        self.byteA = Utils.getrandhex()
