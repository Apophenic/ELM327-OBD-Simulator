import random
from Mode01.BaseClasses.OBDResponse import OBDResponse
from Utils import Switch

class SecondaryAirStatus(OBDResponse):

    validBytes = ['01', '02', '04', '08']

    def getvalue(self):
        for case in Switch(self.byteA):
            if case('01'):
                return 'Upstream'
            elif case('02'):
                return 'Downstream of catalytic converter'
            elif case('04'):
                return 'From the outside atmosphere or off'
            elif case('08'):
                return 'Pump commanded on for diagnostics'
            elif case():
                return None

    def responsecode(self):
        return '41 12'

    def __init__(self):
        self.byteA = random.choice(self.validBytes)
