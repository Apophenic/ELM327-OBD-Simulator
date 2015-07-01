import Utils
from Mode01.BaseClasses.OBDResponse import OBDResponse

class MonitorStatus(OBDResponse):

    def getvalue(self):
        bitsA = bin(int(self.byteA, 16))[2:].rjust(8, '0')
        mil = bitsA[0]
        codecount = int(bitsA[1:], 2)

        bitsB = bin(int(self.byteA, 16))[2:].rjust(8, '0')
        misfire = [self.availability(bitsB[7]), self.completeness(bitsB[3])]
        fuelsystem = [self.availability(bitsB[6]), self.completeness(bitsB[2])]
        components = [self.availability(bitsB[5]), self.completeness(bitsB[1])]
        ignition = None
        if bitsB[4] == '0':
            ignition = 'Spark Ignition'
        else:
            ignition = 'Compression Ignition'

        # TODO Implement Bytes C + D (Also add this to $MonitorStatusThisDriveCycle)

        return ['MIL=' + mil, 'Codes=' + str(codecount), 'Misfire=' + str(misfire), 'FuelSystem=' + str(fuelsystem),
                'Components=' + str(components), 'Ignition=' + ignition]

    def responsecode(self):
        return '41 01'

    def availability(self, bit):
        if bit == '0':
            return 'Unavailable'
        else:
            return 'Available'

    def completeness(self, bit):
        if bit == '0':
            return 'Complete'
        else:
            return 'Incomplete'

    def __init__(self):
        self.byteA = Utils.getrandhex()
        self.byteB = Utils.getrandhex()
        self.byteC = Utils.getrandhex()
        self.byteD = Utils.getrandhex()
