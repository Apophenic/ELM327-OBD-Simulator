import abc

import Utils
from Response.BaseClasses.OBDResponse import OBDResponse


class PIDsSupported(OBDResponse):
    __metaclass__ = abc.ABCMeta

    @abc.abstractproperty
    def responsecode(self):
        pass

    def getvalue(self):
        bits = ''
        supported = []
        byteList = [self.byteA, self.byteB, self.byteC, self.byteD]

        for byte in byteList:
            bits += bin(int(byte, 16))[2:].rjust(8, '0')

        for index, char in enumerate(bits):
            if char is '1':
                supported.append\
                    (hex(index + 1 + self.bitshift())[2:].rjust(2, '0').upper())

        return supported

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()
        self.byteC = Utils.getrandhex()
        self.byteD = Utils.getrandhex()

    @abc.abstractproperty
    def bitshift(self):
        pass
