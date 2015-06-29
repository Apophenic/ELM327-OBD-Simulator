from Response.BaseClasses.O2_Sensor_Secondary import O2_Sensor_Secondary

class STB1B3(O2_Sensor_Secondary):

    def responsecode(self):
        return '41 55'

class LTB1B3(O2_Sensor_Secondary):

    def responsecode(self):
        return '41 56'

class STB2B4(O2_Sensor_Secondary):
    
    def responsecode(self):
        return '41 57'

class LTB2B4(O2_Sensor_Secondary):

    def responsecode(self):
        return '41 58'
