from Mode01.BaseClasses.OBDResponse import OBDResponse

class ClearStoredDTCs(OBDResponse):

    def getvalue(self):
        return self.responsecode()

    def responsecode(self):
        return 'OK'

    def __init__(self):
        pass
