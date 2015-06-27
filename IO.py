from Response.AbsoluteLoadValue import AbsoluteLoadValue
from Response.AuxInputStatus import AuxInputStatus
from Response.BarometricPressure import BarometricPressure
from Response.CalculatedEngineLoad import CalculatedEngineLoad
from Response.Catalyst.Sensors import B2S2
from Response.Catalyst.Sensors import B1S2
from Response.Catalyst.Sensors import B2S1
from Response.Catalyst.Sensors import B1S1
from Response.ControlModuleVoltage import ControlModuleVoltage
from Response.DTCInfo.DistTraveledSinceCodesCleared import DistTraveledSinceCodesCleared
from Response.DTCInfo.DistanceWithMIL import DistanceWithMIL
from Response.DTCInfo.FreezeDTC import FreezeDTC
from Response.DTCInfo.MonitorStatus import MonitorStatus
from Response.DTCInfo.MonitorStatusThisDriveCycle import MonitorStatusThisDriveCycle
from Response.DTCInfo.NumWarmUpsSinceCodesCleared import NumWarmUpsSinceCodesCleared
from Response.DTCInfo.RunTimeSinceEngineStart import RunTimeSinceEngineStart
from Response.DTCInfo.TimeSinceCodesCleared import TimeSinceCodesCleared
from Response.DTCInfo.TimeWithMILOn import TimeWithMILOn
from Response.EGR import EGR
from Response.EGRError import EGRError
from Response.EngineRPM import EngineRPM
from Response.Evap.EvapPressureAbsolute import EvapPressureAbsolute
from Response.Evap.EvapPurge import EvapPurge
from Response.Evap.EvapSystemVaporPressure import EvapSystemVaporPressure
from Response.Evap.EvapVaporPressure import EvapVaporPressure
from Response.Fuel.EngineFuelRate import EngineFuelRate
from Response.Fuel.EthanolFuelPercent import EthanolFuelPercent
from Response.Fuel.FuelInjectionTiming import FuelInjectionTiming
from Response.Fuel.FuelLevel import FuelLevel
from Response.Fuel.FuelPressure import FuelPressure
from Response.Fuel.FuelRailPressureAbsolute import FuelRailPressureAbsolute
from Response.Fuel.FuelRailPressureDirect import FuelRailPressureDirect
from Response.Fuel.FuelRailPressureRelative import FuelRailPressureRelative
from Response.Fuel.FuelSystemStatus import FuelSystemStatus
from Response.Fuel.FuelTrim.FuelTrims import LTFuelTrimB2
from Response.Fuel.FuelTrim.FuelTrims import STFuelTrimB2
from Response.Fuel.FuelTrim.FuelTrims import LTFuelTrimB1
from Response.Fuel.FuelTrim.FuelTrims import STFuelTrimB1
from Response.Fuel.FuelType import FuelType
from Response.HybridBatteryLifeRemaining import HybridBatteryLifeRemaining
from Response.IntakeManifoldPressure import IntakeManifoldPressure
from Response.MAFAirFlowRate import MAFAirFlowRate
from Response.MaxValueMAF import MaxValueMAF
from Response.MaxValues import MaxValues
from Response.O2.AirFuelRatio import AirFuelRatio
from Response.O2.Lambda.O2_Lambda import O2S8L
from Response.O2.Lambda.O2_Lambda import O2S7L
from Response.O2.Lambda.O2_Lambda import O2S6L
from Response.O2.Lambda.O2_Lambda import O2S5L
from Response.O2.Lambda.O2_Lambda import O2S4L
from Response.O2.Lambda.O2_Lambda import O2S3L
from Response.O2.Lambda.O2_Lambda import O2S2L
from Response.O2.Lambda.O2_Lambda import O2S1L
from Response.O2.NarrowBand.O2_Narrow import O2_B2S2n, O2_B2S4n, O2_B2S3n
from Response.O2.NarrowBand.O2_Narrow import O2_B2S1n
from Response.O2.NarrowBand.O2_Narrow import O2_B1S4n
from Response.O2.NarrowBand.O2_Narrow import O2_B1S3n
from Response.O2.NarrowBand.O2_Narrow import O2_B1S2n
from Response.O2.NarrowBand.O2_Narrow import O2_B1S1n
from Response.O2.O2SensorsPresent import O2SensorsPresent
from Response.O2.OxygenSensorsPresent import OxygenSensorsPresent
from Response.O2.Secondary.O2_Secondary import LTB2B4
from Response.O2.Secondary.O2_Secondary import STB2B4
from Response.O2.Secondary.O2_Secondary import LTB1B3
from Response.O2.Secondary.O2_Secondary import STB1B3
from Response.O2.WideBand.O2_Wide import O2S8w
from Response.O2.WideBand.O2_Wide import O2S7w
from Response.O2.WideBand.O2_Wide import O2S6w
from Response.O2.WideBand.O2_Wide import O2S5w
from Response.O2.WideBand.O2_Wide import O2S4w
from Response.O2.WideBand.O2_Wide import O2S3w
from Response.O2.WideBand.O2_Wide import O2S2w
from Response.O2.WideBand.O2_Wide import O2S1w
from Response.OBDStandards import OBDStandards
from Response.PIDsSupported.PIDs import PIDsSupported1, PIDsSupported21, PIDsSupported41, PIDsSupported61
from Response.SecondaryAirStatus import SecondaryAirStatus
from Response.Temps.Temperatures import CoolantTemp, IntakeAirTemp, AmbientAirTemp, EngineOilTemp
from Response.Throttle.Positions import ThrottlePositionA, ThrottleActuator, AcceleratorPositionF, AcceleratorPositionE, \
    AcceleratorPositionD, ThrottlePositionC, ThrottlePositionB, ThrottlePositionRelative, AcceleratorPositionRelative
from Response.TimingAdvance import TimingAdvance
from Response.VehicleEmissionsRequirements import VehicleEmissionsRequirements
from Response.VehicleSpeed import VehicleSpeed

from Utils import Switch

def readinputbytes(query):
    """Accepts a byte query (as a string), identifies the type of query,
    and returns an appropriate response (a subclass of OBDResponse)"""
    if isinstance(query, str):
        pass
    else:
        try:
            query = hex(query)[2:].rjust(2, '0').upper()
        except:
            return None

    for case in Switch(query):
        if case('01 00'):
            return PIDsSupported1()
        elif case('01 01'):
            return MonitorStatus()
        elif case('01 02'):
            return FreezeDTC()
        elif case('01 03'):
            return FuelSystemStatus()
        elif case('01 04'):
            return CalculatedEngineLoad()
        elif case('01 05'):
            return CoolantTemp()
        elif case('01 06'):
            return STFuelTrimB1()
        elif case('01 07'):
            return LTFuelTrimB1()
        elif case('01 08'):
            return STFuelTrimB2()
        elif case('01 09'):
            return LTFuelTrimB2()
        elif case('01 0A'):
            return FuelPressure()
        elif case('01 0B'):
            return IntakeManifoldPressure()
        elif case('01 0C'):
            return EngineRPM()
        elif case('01 0D'):
            return VehicleSpeed()
        elif case('01 0E'):
            return TimingAdvance()
        elif case('01 0F'):
            return IntakeAirTemp()
        elif case('01 10'):
            return MAFAirFlowRate()
        elif case('01 11'):
            return ThrottlePositionA()
        elif case('01 12'):
            return SecondaryAirStatus()
        elif case('01 13'):
            return OxygenSensorsPresent()
        elif case('01 14'):
            return O2_B1S1n()
        elif case('01 15'):
            return O2_B1S2n()
        elif case('01 16'):
            return O2_B1S3n()
        elif case('01 17'):
            return O2_B1S4n()
        elif case('01 18'):
            return O2_B2S1n()
        elif case('01 19'):
            return O2_B2S2n()
        elif case('01 1A'):
            return O2_B2S3n()
        elif case('01 1B'):
            return O2_B2S4n()
        elif case('01 1C'):
            return OBDStandards()
        elif case('01 1D'):
            return O2SensorsPresent()
        elif case('01 1E'):
            return AuxInputStatus()
        elif case('01 1F'):
            return RunTimeSinceEngineStart()
        elif case('01 20'):
            return PIDsSupported21()
        elif case('01 21'):
            return DistanceWithMIL()
        elif case('01 22'):
            return FuelRailPressureRelative()
        elif case('01 23'):
            return FuelRailPressureDirect()
        elif case('01 24'):
            return O2S1w()
        elif case('01 25'):
            return O2S2w()
        elif case('01 26'):
            return O2S3w()
        elif case('01 27'):
            return O2S4w()
        elif case('01 28'):
            return O2S5w()
        elif case('01 29'):
            return O2S6w()
        elif case('01 2A'):
            return O2S7w()
        elif case('01 2B'):
            return O2S8w()
        elif case('01 2C'):
            return EGR()
        elif case('01 2D'):
            return EGRError()
        elif case('01 2E'):
            return EvapPurge()
        elif case('01 2F'):
            return FuelLevel()
        elif case('01 30'):
            return NumWarmUpsSinceCodesCleared()
        elif case('01 31'):
            return DistTraveledSinceCodesCleared()
        elif case('01 32'):
            return EvapVaporPressure()
        elif case('01 33'):
            return BarometricPressure()
        elif case('01 34'):
            return O2S1L()
        elif case('01 35'):
            return O2S2L()
        elif case('01 36'):
            return O2S3L()
        elif case('01 37'):
            return O2S4L()
        elif case('01 38'):
            return O2S5L()
        elif case('01 39'):
            return O2S6L()
        elif case('01 3A'):
            return O2S7L()
        elif case('01 3B'):
            return O2S8L()
        elif case('01 3C'):
            return B1S1()
        elif case('01 3D'):
            return B2S1()
        elif case('01 3E'):
            return B1S2()
        elif case('01 3F'):
            return B2S2()
        elif case('01 40'):
            return PIDsSupported41()
        elif case('01 41'):
            return MonitorStatusThisDriveCycle()
        elif case('01 42'):
            return ControlModuleVoltage()
        elif case('01 43'):
            return AbsoluteLoadValue()
        elif case('01 44'):
            return AirFuelRatio()
        elif case('01 45'):
            return ThrottlePositionRelative()
        elif case('01 46'):
            return AmbientAirTemp()
        elif case('01 47'):
            return ThrottlePositionB()
        elif case('01 48'):
            return ThrottlePositionC()
        elif case('01 49'):
            return AcceleratorPositionD()
        elif case('01 4A'):
            return AcceleratorPositionE()
        elif case('01 4B'):
            return AcceleratorPositionF()
        elif case('01 4C'):
            return ThrottleActuator()
        elif case('01 4D'):
            return TimeWithMILOn()
        elif case('01 4E'):
            return TimeSinceCodesCleared()
        elif case('01 4F'):
            return MaxValues()
        elif case('01 50'):
            return MaxValueMAF()
        elif case('01 51'):
            return FuelType()
        elif case('01 52'):
            return EthanolFuelPercent()
        elif case('01 53'):
            return EvapPressureAbsolute()
        elif case('01 54'):
            return EvapSystemVaporPressure()
        elif case('01 55'):
            return STB1B3()
        elif case('01 56'):
            return LTB1B3()
        elif case('01 57'):
            return STB2B4()
        elif case('01 58'):
            return LTB2B4()
        elif case('01 59'):
            return FuelRailPressureAbsolute()
        elif case('01 5A'):
            return AcceleratorPositionRelative()
        elif case('01 5B'):
            return HybridBatteryLifeRemaining()
        elif case('01 5C'):
            return EngineOilTemp()
        elif case('01 5D'):
            return FuelInjectionTiming()
        elif case('01 5E'):
            return EngineFuelRate()
        elif case('01 5F'):
            return VehicleEmissionsRequirements()
        elif case('01 60'):
            return PIDsSupported61()
        elif case():
            return None
