import Utils
from Utils import Switch
from Mode01.BaseClasses.OBDResponse import OBDResponse

class FuelType(OBDResponse):

    def getvalue(self):
        value = int(self.byteA, 16)
        for case in Switch(value):
            if case(0):
                return 'N/A'
            elif case(1):
                return 'Gasoline'
            elif case(2):
                return 'Methanol'
            elif case(3):
                return 'Ethanol'
            elif case(4):
                return 'Diesel'
            elif case(5):
                return 'LPG'
            elif case(6):
                return 'CNG'
            elif case(7):
                return 'Propane'
            elif case(8):
                return 'Electric'
            elif case(9):
                return 'Bifuel running Gasoline'
            elif case(10):
                return 'Bifuel running Methanol'
            elif case(11):
                return 'Bifueld running Ethanol'
            elif case(12):
                return 'Bifuel running LPG'
            elif case(13):
                return 'Bifuel running CNG'
            elif case(14):
                return 'Bifuel running Propane'
            elif case(15):
                return 'Bifuel running Electricity'
            elif case(16):
                return 'Bifuel running Electric and Combustion'
            elif case(17):
                return 'Hybrid Gasoline'
            elif case(18):
                return 'Hybrid Ethanol'
            elif case(19):
                return 'Hybrid Diesel'
            elif case(20):
                return 'Hybrid Electric'
            elif case(21):
                return 'Hybrid running Electric and Combustion'
            elif case(22):
                return 'Hybrid Regenerative'
            elif case(23):
                return 'Bifuel running Diesel'
            elif case():
                return None

    def responsecode(self):
        return '41 51'

    def __init__(self):
        self.byteA = Utils.getrandhex()
