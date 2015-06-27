from Response.BaseClasses.PIDsSupported import PIDsSupported

class PIDsSupported1(PIDsSupported):

    def bitshift(self):
        return 0x00

    def responsecode(self):
        return '41 00'

class PIDsSupported21(PIDsSupported):

    def bitshift(self):
        return 0x20

    def responsecode(self):
        return '41 20'

class PIDsSupported41(PIDsSupported):

    def bitshift(self):
        return 0x40

    def responsecode(self):
        return '41 40'

class PIDsSupported61(PIDsSupported):

    def bitshift(self):
        return 0x60

    def responsecode(self):
        return '41 60'

class PIDsSupported81(PIDsSupported):

    def bitshift(self):
        return 0x80

    def responsecode(self):
        return '41 80'
