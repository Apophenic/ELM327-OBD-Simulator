from Mode01.Response.Other.AuxInputStatus import AuxInputStatus
from Mode01.Response.Load.CalculatedEngineLoad import CalculatedEngineLoad
from Mode01.Response.Load.AbsoluteLoadValue import AbsoluteLoadValue
from Mode01.Response.Catalyst.CatalystSensors import B2S2
from Mode01.Response.Catalyst.CatalystSensors import B1S2
from Mode01.Response.Catalyst.CatalystSensors import B2S1
from Mode01.Response.Catalyst.CatalystSensors import B1S1
from Mode01.Response.DTC_Info.DistTraveledSinceCodesCleared import DistTraveledSinceCodesCleared
from Mode01.Response.DTC_Info.DistanceWithMIL import DistanceWithMIL
from Mode01.Response.DTC_Info.FreezeDTC import FreezeDTC
from Mode01.Response.DTC_Info.MonitorStatus import MonitorStatus
from Mode01.Response.DTC_Info.MonitorStatusThisDriveCycle import MonitorStatusThisDriveCycle
from Mode01.Response.DTC_Info.NumWarmUpsSinceCodesCleared import NumWarmUpsSinceCodesCleared
from Mode01.Response.DTC_Info.RunTimeSinceEngineStart import RunTimeSinceEngineStart
from Mode01.Response.DTC_Info.TimeSinceCodesCleared import TimeSinceCodesCleared
from Mode01.Response.DTC_Info.TimeWithMILOn import TimeWithMILOn
from Mode01.Response.EGR.EGR import EGR
from Mode01.Response.EGR.EGRError import EGRError
from Mode01.Response.Other.EngineRPM import EngineRPM
from Mode01.Response.Evap.EvapPressureAbsolute import EvapPressureAbsolute
from Mode01.Response.Evap.EvapPurge import EvapPurge
from Mode01.Response.Evap.EvapSystemVaporPressure import EvapSystemVaporPressure
from Mode01.Response.Evap.EvapVaporPressure import EvapVaporPressure
from Mode01.Response.Fuel.EngineFuelRate import EngineFuelRate
from Mode01.Response.Fuel.EthanolFuelPercent import EthanolFuelPercent
from Mode01.Response.Fuel.FuelInjectionTiming import FuelInjectionTiming
from Mode01.Response.Fuel.FuelLevel import FuelLevel
from Mode01.Response.Fuel.FuelPressure import FuelPressure
from Mode01.Response.Fuel.FuelRailPressureAbsolute import FuelRailPressureAbsolute
from Mode01.Response.Fuel.FuelRailPressureDirect import FuelRailPressureDirect
from Mode01.Response.Fuel.FuelRailPressureRelative import FuelRailPressureRelative
from Mode01.Response.Fuel.FuelSystemStatus import FuelSystemStatus
from Mode01.Response.Fuel.FuelTrim.FuelTrims import LTFuelTrimB2
from Mode01.Response.Fuel.FuelTrim.FuelTrims import STFuelTrimB2
from Mode01.Response.Fuel.FuelTrim.FuelTrims import LTFuelTrimB1
from Mode01.Response.Fuel.FuelTrim.FuelTrims import STFuelTrimB1
from Mode01.Response.Fuel.FuelType import FuelType
from Mode01.Response.Other.HybridBatteryLifeRemaining import HybridBatteryLifeRemaining
from Mode01.Response.Air.MAFAirFlowRate import MAFAirFlowRate
from Mode01.Response.Air.IntakeManifoldPressure import IntakeManifoldPressure
from Mode01.Response.Air.BarometricPressure import BarometricPressure
from Mode01.Response.Air.MaxValueMAF import MaxValueMAF
from Mode04.ClearStoredDTCs import ClearStoredDTCs
from Mode01.Response.O2Sensors.AirFuelRatio import AirFuelRatio
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S8L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S7L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S6L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S5L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S4L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S3L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S2L
from Mode01.Response.O2Sensors.Lambda.O2_Lambda import O2S1L
from Mode01.Response.O2Sensors.NarrowBand.O2_Narrow import O2_B2S2n, O2_B2S4n, O2_B2S3n
from Mode01.Response.O2Sensors.NarrowBand.O2_Narrow import O2_B2S1n
from Mode01.Response.O2Sensors.NarrowBand.O2_Narrow import O2_B1S4n
from Mode01.Response.O2Sensors.NarrowBand.O2_Narrow import O2_B1S3n
from Mode01.Response.O2Sensors.NarrowBand.O2_Narrow import O2_B1S2n
from Mode01.Response.O2Sensors.NarrowBand.O2_Narrow import O2_B1S1n
from Mode01.Response.O2Sensors.O2SensorsPresent import O2SensorsPresent
from Mode01.Response.O2Sensors.OxygenSensorsPresent import OxygenSensorsPresent
from Mode01.Response.O2Sensors.Secondary.O2_Secondary import LTB2B4
from Mode01.Response.O2Sensors.Secondary.O2_Secondary import STB2B4
from Mode01.Response.O2Sensors.Secondary.O2_Secondary import LTB1B3
from Mode01.Response.O2Sensors.Secondary.O2_Secondary import STB1B3
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S8w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S7w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S6w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S5w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S4w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S3w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S2w
from Mode01.Response.O2Sensors.WideBand.O2_Wide import O2S1w
from Mode01.Response.Error.OBDError import OBDError
from Mode01.Response.OBD_Info.OBDStandards import OBDStandards
from Mode01.Response.OBD_Info.ControlModuleVoltage import ControlModuleVoltage
from Mode01.Response.OBD_Info.MaxValues import MaxValues
from Mode01.Response.PIDs_Supported.PIDs import PIDsSupported1, PIDsSupported21, PIDsSupported41, PIDsSupported61
from Mode01.Response.Protocol.OBDProtocol import OBDProtocol
from Mode01.Response.Air.SecondaryAirStatus import SecondaryAirStatus
from Mode01.Response.Temperature.Temperatures import CoolantTemp, IntakeAirTemp, AmbientAirTemp, EngineOilTemp
from Mode01.Response.Throttle.ThrottlePositions import ThrottlePositionA, ThrottleActuator, AcceleratorPositionF, AcceleratorPositionE, \
    AcceleratorPositionD, ThrottlePositionC, ThrottlePositionB, ThrottlePositionRelative, AcceleratorPositionRelative
from Mode01.Response.Other.TimingAdvance import TimingAdvance
from Mode01.Response.OBD_Info.VehicleEmissionsRequirements import VehicleEmissionsRequirements
from Mode01.Response.Other.VehicleSpeed import VehicleSpeed

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
            return OBDError()

    mode = query[:2]
    for case in Switch(mode):
        if case('01'):
            return getmode01response(query)
        elif case('02'):
            return getmode02response(query)
        elif case('03'):
            return getmode03response(query)
        elif case('04'):
            return getmode04response(query)
        elif case('AT'):
            return getmodeATresponse(query)
        elif case():
            return OBDError()

def getmode01response(query):
    pid = query[3:]
    for case in Switch(pid):
        if case('00'):
            return PIDsSupported1()
        elif case('01'):
            return MonitorStatus()
        elif case('02'):
            return FreezeDTC()
        elif case('03'):
            return FuelSystemStatus()
        elif case('04'):
            return CalculatedEngineLoad()
        elif case('05'):
            return CoolantTemp()
        elif case('06'):
            return STFuelTrimB1()
        elif case('07'):
            return LTFuelTrimB1()
        elif case('08'):
            return STFuelTrimB2()
        elif case('09'):
            return LTFuelTrimB2()
        elif case('0A'):
            return FuelPressure()
        elif case('0B'):
            return IntakeManifoldPressure()
        elif case('0C'):
            return EngineRPM()
        elif case('0D'):
            return VehicleSpeed()
        elif case('0E'):
            return TimingAdvance()
        elif case('0F'):
            return IntakeAirTemp()
        elif case('10'):
            return MAFAirFlowRate()
        elif case('11'):
            return ThrottlePositionA()
        elif case('12'):
            return SecondaryAirStatus()
        elif case('13'):
            return OxygenSensorsPresent()
        elif case('14'):
            return O2_B1S1n()
        elif case('15'):
            return O2_B1S2n()
        elif case('16'):
            return O2_B1S3n()
        elif case('17'):
            return O2_B1S4n()
        elif case('18'):
            return O2_B2S1n()
        elif case('19'):
            return O2_B2S2n()
        elif case('1A'):
            return O2_B2S3n()
        elif case('1B'):
            return O2_B2S4n()
        elif case('1C'):
            return OBDStandards()
        elif case('1D'):
            return O2SensorsPresent()
        elif case('1E'):
            return AuxInputStatus()
        elif case('1F'):
            return RunTimeSinceEngineStart()
        elif case('20'):
            return PIDsSupported21()
        elif case('21'):
            return DistanceWithMIL()
        elif case('22'):
            return FuelRailPressureRelative()
        elif case('23'):
            return FuelRailPressureDirect()
        elif case('24'):
            return O2S1w()
        elif case('25'):
            return O2S2w()
        elif case('26'):
            return O2S3w()
        elif case('27'):
            return O2S4w()
        elif case('28'):
            return O2S5w()
        elif case('29'):
            return O2S6w()
        elif case('2A'):
            return O2S7w()
        elif case('2B'):
            return O2S8w()
        elif case('2C'):
            return EGR()
        elif case('2D'):
            return EGRError()
        elif case('2E'):
            return EvapPurge()
        elif case('2F'):
            return FuelLevel()
        elif case('30'):
            return NumWarmUpsSinceCodesCleared()
        elif case('31'):
            return DistTraveledSinceCodesCleared()
        elif case('32'):
            return EvapVaporPressure()
        elif case('33'):
            return BarometricPressure()
        elif case('34'):
            return O2S1L()
        elif case('35'):
            return O2S2L()
        elif case('36'):
            return O2S3L()
        elif case('37'):
            return O2S4L()
        elif case('38'):
            return O2S5L()
        elif case('39'):
            return O2S6L()
        elif case('3A'):
            return O2S7L()
        elif case('3B'):
            return O2S8L()
        elif case('3C'):
            return B1S1()
        elif case('3D'):
            return B2S1()
        elif case('3E'):
            return B1S2()
        elif case('3F'):
            return B2S2()
        elif case('40'):
            return PIDsSupported41()
        elif case('41'):
            return MonitorStatusThisDriveCycle()
        elif case('42'):
            return ControlModuleVoltage()
        elif case('43'):
            return AbsoluteLoadValue()
        elif case('44'):
            return AirFuelRatio()
        elif case('45'):
            return ThrottlePositionRelative()
        elif case('46'):
            return AmbientAirTemp()
        elif case('47'):
            return ThrottlePositionB()
        elif case('48'):
            return ThrottlePositionC()
        elif case('49'):
            return AcceleratorPositionD()
        elif case('4A'):
            return AcceleratorPositionE()
        elif case('4B'):
            return AcceleratorPositionF()
        elif case('4C'):
            return ThrottleActuator()
        elif case('4D'):
            return TimeWithMILOn()
        elif case('4E'):
            return TimeSinceCodesCleared()
        elif case('4F'):
            return MaxValues()
        elif case('50'):
            return MaxValueMAF()
        elif case('51'):
            return FuelType()
        elif case('52'):
            return EthanolFuelPercent()
        elif case('53'):
            return EvapPressureAbsolute()
        elif case('54'):
            return EvapSystemVaporPressure()
        elif case('55'):
            return STB1B3()
        elif case('56'):
            return LTB1B3()
        elif case('57'):
            return STB2B4()
        elif case('58'):
            return LTB2B4()
        elif case('59'):
            return FuelRailPressureAbsolute()
        elif case('5A'):
            return AcceleratorPositionRelative()
        elif case('5B'):
            return HybridBatteryLifeRemaining()
        elif case('5C'):
            return EngineOilTemp()
        elif case('5D'):
            return FuelInjectionTiming()
        elif case('5E'):
            return EngineFuelRate()
        elif case('5F'):
            return VehicleEmissionsRequirements()
        elif case('60'):
            return PIDsSupported61()

def getmode02response(query):
    pid = query[3:]

def getmode03response(query):
    pid = query[3:]

def getmode04response(query):
    return ClearStoredDTCs()

def getmodeATresponse(query):
    pid = query[3:]
    for case in Switch(pid):
        if case('DP'):
            return OBDProtocol()
        elif case():
            return OBDError()
