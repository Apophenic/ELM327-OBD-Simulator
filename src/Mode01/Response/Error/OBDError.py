from Mode01.BaseClasses.OBDResponse import OBDResponse

class OBDError(OBDResponse):

    def getvalue(self):
        return self.responsecode()

    def responsecode(self):
        return 'NO DATA'

    def __init__(self):
        pass
