from Response.BaseClasses.FuelTrim import FuelTrim;


class LTFuelTrimB1(FuelTrim):

    def responsecode(self):
        return '41 07'

class LTFuelTrimB2(FuelTrim):

    def responsecode(self):
        return '41 09'

class STFuelTrimB1(FuelTrim):

    def responsecode(self):
        return '41 06'

class STFuelTrimB2(FuelTrim):

    def responsecode(self):
        return '41 08'
