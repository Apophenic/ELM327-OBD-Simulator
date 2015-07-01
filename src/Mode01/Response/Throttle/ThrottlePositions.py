from Mode01.BaseClasses.ThrottlePosition import ThrottlePosition

class ThrottlePositionRelative(ThrottlePosition):

    def responsecode(self):
        return '41 45'

class ThrottleActuator(ThrottlePosition):

    def responsecode(self):
        return '41 4C'

class ThrottlePositionA(ThrottlePosition):

    def responsecode(self):
        return '41 11'

class ThrottlePositionB(ThrottlePosition):

    def responsecode(self):
        return '41 47'

class ThrottlePositionC(ThrottlePosition):

    def responsecode(self):
        return '41 48'

class AcceleratorPositionD(ThrottlePosition):

    def responsecode(self):
        return '41 49'

class AcceleratorPositionE(ThrottlePosition):

    def responsecode(self):
        return '41 4A'

class AcceleratorPositionF(ThrottlePosition):

    def responsecode(self):
        return '41 4B'

class AcceleratorPositionRelative(ThrottlePosition):

    def responsecode(self):
        return '41 5A'
