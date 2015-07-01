from Mode01.BaseClasses.OBDResponse import OBDResponse

class OBDStandards(OBDResponse):    # TODO Implement all standards

    def getvalue(self):
        return 'OBD-II as defined by the CARB'

    def responsecode(self):
        return '41 1C'

    def __init__(self):
        self.byteA = '01'
