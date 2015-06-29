from Response.BaseClasses.OBDResponse import OBDResponse

class ClearStoredDTCs(OBDResponse):

    def getvalue(self):
        return self.responsecode()

    def responsecode(self):
        return 'OK'

    def getresponse(self):
        return self.responsecode()

    def __init__(self):
        pass
