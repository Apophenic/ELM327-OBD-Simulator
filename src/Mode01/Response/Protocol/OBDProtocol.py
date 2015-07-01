import random
from enum import Enum
from Mode01.BaseClasses.OBDResponse import OBDResponse

class Protocols(Enum):
    x0 = 'Auto'
    x1 = 'SAE J1850 PWM'
    x2 = 'SAE J1850 VPW'
    x3 = 'ISO 9141 - 2'
    x4 = 'ISO 14230 - 4KWP (5 BAUD INIT)'
    x5 = 'ISO 14230 - 4 KWP (FAST INIT)'
    x6 = 'ISO 15765 - 4 CAN (11 BIT ID, 500 KBAUD)'
    x7 = 'ISO 15765 - 4 CAN (29 BIT ID, 500 KBAUD)'
    x8 = 'ISO 15765 - 4 CAN (11 BIT ID, 250 KBAUD)'
    x9 = 'ISO 15765 - 4 CAN (29 BIT ID, 250 KBAUD)'
    xA = 'SAE J1939 CAN (29 BIT ID, 250 KBAUD)'

class OBDProtocol(OBDResponse):

    def getvalue(self):
        return self.responsecode()

    def responsecode(self):
        return random.choice(list(Protocols)).value

    def __init__(self):
        pass
