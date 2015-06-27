from Response.BaseClasses.Temperature import Temperature

class IntakeAirTemp(Temperature):

    def responsecode(self):
        return '41 0F'

class AmbientAirTemp(Temperature):

    def responsecode(self):
        return '41 46'

class CoolantTemp(Temperature):

    def responsecode(self):
        return '41 05'

class EngineOilTemp(Temperature):

    def responsecode(self):
        return '41 5C'
