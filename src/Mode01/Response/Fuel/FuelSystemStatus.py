import random

from Mode01.BaseClasses.OBDResponse import OBDResponse
from Utils import Switch


class FuelSystemStatus(OBDResponse):

    validBytes = ['01', '02', '04', '08', '10']

    def getvalue(self):
        return ['System1=' + self.determinestatus(self.byteA),
                'System2=' + self.determinestatus(self.byteB)]

    def determinestatus(self, byte):
        for case in Switch(byte):
            if case('01'):
                return 'Open loop due to insufficient engine temperature'
            elif case('02'):
                return 'Closed loop, using oxygen sensor feedback to determine fuel mix'
            elif case('04'):
                return 'Open loop due to engine load OR fuel cut due to deceleration'
            elif case('08'):
                return 'Open loop due to system failure'
            elif case('10'):
                return 'Closed loop, using at least one oxygen sensor but there is a fault in the feedback system'
            elif case():
                return None

    def responsecode(self):
        return '41 03'

    def __init__(self):
        self.byteA = random.choice(self.validBytes)
        self.byteB = random.choice(self.validBytes)