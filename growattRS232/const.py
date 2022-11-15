"""Constants for growattRS232 library."""

# Defaults
DEFAULT_PORT = "/dev/ttyUSB0"
DEFAULT_ADDRESS = 0x1

# ATTRIBUTES
ATTR_SERIAL_NUMBER = "serial_number"
ATTR_MODEL_NUMBER = "model_number"
ATTR_FIRMWARE = "firmware"

ATTR_AC_CHR_CURR = "ac_chr_curr"  # A
ATTR_AC_CHR_TODAY_H = "ac_chr_today_h"
ATTR_AC_CHR_TODAY_L = "ac_chr_today_l"  # kWh
ATTR_AC_CHR_TOTAL_H = "ac_chr_total_h"
ATTR_AC_CHR_TOTAL_L = "ac_chr_total_l"  # kWh
ATTR_AC_CHR_VA_H = "ac_chr_va_h"  # VA
ATTR_AC_CHR_VA_L = "ac_chr_va_l"  # VA
ATTR_AC_CHR_WATT_H = "ac_chr_watt_h"  # W
ATTR_AC_CHR_WATT_L = "ac_chr_watt_l"  # W
ATTR_AC_DISCHR_TODAY_H = "ac_dischr_today_h"
ATTR_AC_DISCHR_TODAY_L = "ac_dischr_today_l"  # kWh
ATTR_AC_DISCHR_TOTAL_H = "ac_dischr_total_h"
ATTR_AC_DISCHR_TOTAL_L = "ac_dischr_total_l"  # kWh
ATTR_AC_DISCHR_VA_H = "ac_dischr_va_h"  # VA
ATTR_AC_DISCHR_VA_L = "ac_dischr_va_l"  # VA
ATTR_AC_DISCHR_WATT_H = "ac_dischr_watt_h"  # W
ATTR_AC_DISCHR_WATT_L = "ac_dischr_watt_l"  # W
ATTR_AC_IN_FREQ = "ac_in_freq"  # Hz
ATTR_AC_IN_V = "ac_in_v"  # V
ATTR_AC_IN_VA_H = "ac_in_va_h"  # VA
ATTR_AC_IN_VA_L = "ac_in_va_l"  # VA
ATTR_AC_IN_WATT_H = "ac_in_watt_h"  # W
ATTR_AC_IN_WATT_L = "ac_in_watt_l"  # W

ATTR_BAT_DISCHR_TODAY_H = "bat_dischr_today_h"
ATTR_BAT_DISCHR_TODAY_L = "bat_dischr_today_l"  # kWh
ATTR_BAT_DISCHR_TOTAL_H = "bat_dischr_total_h"
ATTR_BAT_DISCHR_TOTAL_L = "bat_dischr_total_l"  # kWh
ATTR_BAT_DISCHR_VA_H = "bat_dischr_va_h"  # VA
ATTR_BAT_DISCHR_VA_L = "bat_dischr_va_l"  # VA
ATTR_BAT_DISCHR_WATT_H = "bat_dischr_watt_h"  # W
ATTR_BAT_DISCHR_WATT_L = "bat_dischr_watt_l"  # W
ATTR_BAT_DSP_V = "bat_dsp_v"  # V
ATTR_BAT_OVERCHARGE = "bat_overcharge"
ATTR_BAT_S_V = "bat_s_v"  # V
ATTR_BAT_SOC = "bat_soc"
ATTR_BAT_V = "bat_v"  # V
ATTR_BAT_WATT_H = "bat_watt_h"  # W
ATTR_BAT_WATT_L = "bat_watt_l"  # W

ATTR_BMS_BAT_CURR = "bms_bat_curr"  # A
ATTR_BMS_BAT_TEMP = "bms_bat_temp"  # C
ATTR_BMS_BAT_V = "bms_bat_v"  # V
ATTR_BMS_BMSINFO = "bms_bmsinfo"
ATTR_BMS_CELL01_V = "bms_cell01_v"  # V
ATTR_BMS_CELL02_V = "bms_cell02_v"  # V
ATTR_BMS_CELL03_V = "bms_cell03_v"  # V
ATTR_BMS_CELL04_V = "bms_cell04_v"  # V
ATTR_BMS_CELL05_V = "bms_cell05_v"  # V
ATTR_BMS_CELL06_V = "bms_cell06_v"  # V
ATTR_BMS_CELL07_V = "bms_cell07_v"  # V
ATTR_BMS_CELL08_V = "bms_cell08_v"  # V
ATTR_BMS_CELL09_V = "bms_cell09_v"  # V
ATTR_BMS_CELL10_V = "bms_cell10_v"  # V
ATTR_BMS_CELL11_V = "bms_cell11_v"  # V
ATTR_BMS_CELL12_V = "bms_cell12_v"  # V
ATTR_BMS_CELL13_V = "bms_cell13_v"  # V
ATTR_BMS_CELL14_V = "bms_cell14_v"  # V
ATTR_BMS_CELL15_V = "bms_cell15_v"  # V
ATTR_BMS_CELL16_V = "bms_cell16_v"  # V
ATTR_BMS_CONSTANT_V = "bms_constant_v"  # V
ATTR_BMS_ERROR = "bms_error"
ATTR_BMS_MAX_CURR = "bms_max_curr"
ATTR_BMS_PACKINFO = "bms_packinfo"
ATTR_BMS_SOC = "bms_soc"
ATTR_BMS_STATUS = "bms_status"
ATTR_BMS_USINGCAP = "bms_usingcap"
ATTR_BMS_WARNINFO = "bms_warninfo"

ATTR_BUCK1_CURR = "buck1_curr"  # A
ATTR_BUCK1_NTC = "buck1_ntc"  # C
ATTR_BUCK2_CURR = "buck2_curr"  # A
ATTR_BUCK2_NTC = "buck2_ntc"  # C
ATTR_BUS_V = "bus_v"  # V
ATTR_CHECK_STEP = "check_step"
ATTR_CONSTANT_POWER_OK_FLAG = "constant_power_ok_flag"
ATTR_DCDC_TEMP = "dcdc_temp"  # C
ATTR_DTC = "dtc"
ATTR_INV_CURR = "inv_curr"  # A
ATTR_INV_FANSPEED = "inv_fanspeed"
ATTR_INV_TEMP = "inv_temp"  # C
ATTR_MPPT_FANSPEED = "mppt_fanspeed"

ATTR_OP_CURR = "op_curr"  # A
ATTR_OP_DC_V = "op_dc_v"  # V
ATTR_OP_FREQ = "op_freq"  # Hz
ATTR_OP_PERCENT = "op_percent"
ATTR_OP_V = "op_v"  # V
ATTR_OP_VA_H = "op_va_h"  # VA
ATTR_OP_VA_L = "op_va_l"  # VA
ATTR_OP_WATT_H = "op_watt_h"  # W
ATTR_OP_WATT_L = "op_watt_l"  # W
ATTR_PRODUCTION_LINE_MODE = "production_line_mode"
ATTR_PV1_V = "pv1_v"  # V
ATTR_PV2_V = "pv2_v"  # V
ATTR_TIME_TOTAL_H = "time_total_h"  # S
ATTR_TIME_TOTAL_L = "time_total_l"  # S


# Warnings and Faults
ATTR_FAULT_BIT = "fault_bit"
ATTR_FAULT_BIT_DESC = "fault_bit_desc" # Derived from FAULTCODES
ATTR_FAULT_VALUE = "fault_value"
ATTR_WARNING_BIT = "warning_bit"
ATTR_WARNING_BIT_DESC = "warning_bit_desc" # Derived from WARNINGCODES
ATTR_WARNING_VALUE = "warning_value"
ATTR_SYSTEM_STATUS = "system_status"
ATTR_SYSTEM_STATUS_DESC = "system_status_desc" # Derived from STATUSCODES

# Registers
REG_AC_CHR_CURR = 23
REG_AC_CHR_TODAY_H = 11
REG_AC_CHR_TODAY_L = 12
REG_AC_CHR_TOTAL_H = 13
REG_AC_CHR_TOTAL_L = 14
REG_AC_CHR_VA_H = 15
REG_AC_CHR_VA_L = 16
REG_AC_CHR_WATT_H = 13
REG_AC_CHR_WATT_L = 14
REG_AC_DISCHR_TODAY_H = 19
REG_AC_DISCHR_TODAY_L = 20
REG_AC_DISCHR_TOTAL_H = 21
REG_AC_DISCHR_TOTAL_L = 22
REG_AC_DISCHR_VA_H = 26
REG_AC_DISCHR_VA_L = 27
REG_AC_DISCHR_WATT_H = 24
REG_AC_DISCHR_WATT_L = 25
REG_AC_IN_FREQ = 21
REG_AC_IN_V = 20
REG_AC_IN_VA_H = 38
REG_AC_IN_VA_L = 39
REG_AC_IN_WATT_H = 36
REG_AC_IN_WATT_L = 37

REG_BAT_DISCHR_TODAY_H = 15
REG_BAT_DISCHR_TODAY_L = 16
REG_BAT_DISCHR_TOTAL_H = 17
REG_BAT_DISCHR_TOTAL_L = 18
REG_BAT_DISCHR_VA_H = 30
REG_BAT_DISCHR_VA_L = 31
REG_BAT_DISCHR_WATT_H = 28
REG_BAT_DISCHR_WATT_L = 29
REG_BAT_DSP_V = 29
REG_BAT_OVERCHARGE = 35
REG_BAT_S_V = 28
REG_BAT_SOC = 18
REG_BAT_V = 17
REG_BAT_WATT_H = 32
REG_BAT_WATT_L = 33

REG_BMS_BAT_CURR = 5
REG_BMS_BAT_TEMP = 6
REG_BMS_BAT_V = 4
REG_BMS_BMSINFO = 9
REG_BMS_CELL01_V = 12
REG_BMS_CELL02_V = 13
REG_BMS_CELL03_V = 14
REG_BMS_CELL04_V = 15
REG_BMS_CELL05_V = 16
REG_BMS_CELL06_V = 17
REG_BMS_CELL07_V = 18
REG_BMS_CELL08_V = 19
REG_BMS_CELL09_V = 20
REG_BMS_CELL10_V = 21
REG_BMS_CELL11_V = 22
REG_BMS_CELL12_V = 23
REG_BMS_CELL13_V = 24
REG_BMS_CELL14_V = 25
REG_BMS_CELL15_V = 26
REG_BMS_CELL16_V = 27
REG_BMS_CONSTANT_V = 8
REG_BMS_ERROR = 1
REG_BMS_MAX_CURR = 7
REG_BMS_PACKINFO = 10
REG_BMS_SOC = 3
REG_BMS_STATUS = 0
REG_BMS_USINGCAP = 11
REG_BMS_WARNINFO = 2

REG_BUCK1_CURR = 7
REG_BUCK1_NTC = 32
REG_BUCK2_CURR = 8
REG_BUCK2_NTC = 33
REG_BUS_V = 19
REG_CHECK_STEP = 0
REG_CONSTANT_POWER_OK_FLAG = 2
REG_DCDC_TEMP = 26
REG_DTC = 44
REG_INV_CURR = 35
REG_INV_FANSPEED = 37
REG_INV_TEMP = 25
REG_MPPT_FANSPEED = 36

REG_OP_CURR = 34
REG_OP_DC_V = 24
REG_OP_FREQ = 23
REG_OP_PERCENT = 27
REG_OP_V = 22
REG_OP_VA_H = 11
REG_OP_VA_L = 12
REG_OP_WATT_H = 9
REG_OP_WATT_L = 10
REG_PRODUCTION_LINE_MODE = 1
REG_PV1_V = 1
REG_PV2_V = 2
REG_TIME_TOTAL_H = 30
REG_TIME_TOTAL_L = 31

REG_FAULT_BIT = 40
REG_FAULT_VALUE = 42
REG_WARNING_BIT = 41
REG_WARNING_VALUE = 43
REG_SYSTEM_STATUS = 0


# Codes
STATUSCODES = {
    0: "Standby", 
    1: "（No Use）", 
    2: "Discharge", 
    3: "Fault", 
    4: "Flash", 
    5: "PV charge", 
    6: "AC charge", 
    7: "Combine charge", 
    8: "Combine charge and Bypass", 
    9: "PV charge and Bypass", 
    10: "AC charge and Bypass", 
    11: "Bypass", 
    12: "PV charge and Discharge"
}

FAULTCODES = {
    0: "None",
    8: "Auto Test Failed",
    9: "No AC Connection",
    10: "PV Isolation Low",
    25: "Residual I High",
    26: "Output High DCI",
    27: "PV Voltage High",
    0x00000001:	"",
    0x00000002:	"CPU A to B Communication error",
    0x00000004:	"Battery sample inconsistent",
    0x00000008:	"BUCK over current",
    0x00000010:	"BMS communication fault",
    0x00000020:	"Battery unnormal",
    0x00000040:	"",
    0x00000080:	"Battery voltage high",
    0x00000100:	"Over temprature",
    0x00000200:	"Over load",
    0x00000400:	"",
    0x00000800:	"",
    0x00001000:	"",
    0x00002000:	"",
    0x00004000:	"",
    0x00008000:	"",
    0x00010000:	"Battery reverse connection",
    0x00020000:	"BUS soft start fail",
    0x00040000:	"DC‐DC unnormal",
    0x00080000:	"DC voltage high",
    0x00100000:	"CT detect failed",
    0x00200000:	"CPU B to A Communication error",
    0x00400000:	"BUS voltage high",
    0x00800000:	"",
    0x01000000:	"MOV break",
    0x02000000:	"Output short circuit",
    0x04000000:	"Li‐Battery over load",
    0x08000000:	"Output voltage high",
    0x10000000:	"",
    0x20000000:	"",
    0x40000000:	"",
    0x80000000:	"",
}
for i in range(1, 7):
    FAULTCODES[i] = "Generic Error Code: %s" % str(99 + i)
for i in range(11, 24):
    FAULTCODES[i] = "Generic Error Code: %s" % str(99 + i)
for i in range(28, 32):
    FAULTCODES[i] = "Generic Error Code: %s" % str(99 + i)

WARNINGCODES = {
    0x0000: "None",
    0x0001: "Battery voltage low warning",
    0x0002: "Over temprature warning",
    0x0004: "Over load warning",
    0x0008: "Fail to read EEPROM",
    0x0010: "Firmware version unmacth",
    0x0020: "Fail to write EEPROM",
    0x0040: "BMS warning",
    0x0080: "Li‐Battery over load warning",
    0x0100: "Li‐Battery aging warning",
    0x0200: "Fan lock warning",
    0x0400: "",
    0x0800: "",
    0x1000: "",
    0x2000: "",
    0x4000: "",
    0x8000: "",
}
#TOVALIDATE
DERATINGMODES = {
    0: "No Deratring",
    1: "PV",
    2: "",
    3: "Vac",
    4: "Fac",
    5: "Tboost",
    6: "Tinv",
    7: "Control",
    8: "*LoadSpeed",
    9: "*OverBackByTime",
}

#TODO - &*6
DEVICETYPECODES = {
}

# Unit of measurement
ELECTRICAL_POTENTIAL_VOLT = "V"
ELECTRICAL_CURRENT_AMPERE = "A"
APPARENT_POWER = "VA"
POWER_WATT = "W"
#REACTIVE_POWER_VAR = "var"
#TIME_HOURS = "h"
TIME_SECONDS = "s"
ENERGY_KILO_WATT_HOUR = "kWh"
#REACTIVE_ENERGY_KILO_VAR_HOUR = "kvarh"
FREQUENCY_HERTZ = "Hz"
TEMP_CELSIUS = "°C"

# Provided attributes and their associated unit of measurement
ATTRIBUTES = {
    ATTR_SERIAL_NUMBER: None,
    ATTR_MODEL_NUMBER: None,
    ATTR_FIRMWARE: None,
    ATTR_AC_CHR_CURR: ELECTRICAL_CURRENT_AMPERE,
    ATTR_AC_CHR_TODAY_H: None,
    ATTR_AC_CHR_TODAY_L: ENERGY_KILO_WATT_HOUR,
    ATTR_AC_CHR_TOTAL_H: None,
    ATTR_AC_CHR_TOTAL_L: ENERGY_KILO_WATT_HOUR,
    ATTR_AC_CHR_VA_H: APPARENT_POWER,
    ATTR_AC_CHR_VA_L: APPARENT_POWER,
    ATTR_AC_CHR_WATT_H: POWER_WATT,
    ATTR_AC_CHR_WATT_L: POWER_WATT,
    ATTR_AC_DISCHR_TODAY_H: None,
    ATTR_AC_DISCHR_TODAY_L: ENERGY_KILO_WATT_HOUR,
    ATTR_AC_DISCHR_TOTAL_H: None,
    ATTR_AC_DISCHR_TOTAL_L: ENERGY_KILO_WATT_HOUR,
    ATTR_AC_DISCHR_VA_H: APPARENT_POWER,
    ATTR_AC_DISCHR_VA_L: APPARENT_POWER,
    ATTR_AC_DISCHR_WATT_H: POWER_WATT,
    ATTR_AC_DISCHR_WATT_L: POWER_WATT,
    ATTR_AC_IN_FREQ: FREQUENCY_HERTZ,
    ATTR_AC_IN_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_AC_IN_VA_H: APPARENT_POWER,
    ATTR_AC_IN_VA_L: APPARENT_POWER,
    ATTR_AC_IN_WATT_H: POWER_WATT,
    ATTR_AC_IN_WATT_L: POWER_WATT,
    ATTR_BAT_DISCHR_TODAY_H: None,
    ATTR_BAT_DISCHR_TODAY_L: ENERGY_KILO_WATT_HOUR,
    ATTR_BAT_DISCHR_TOTAL_H: None,
    ATTR_BAT_DISCHR_TOTAL_L: ENERGY_KILO_WATT_HOUR,
    ATTR_BAT_DISCHR_VA_H: APPARENT_POWER,
    ATTR_BAT_DISCHR_VA_L: APPARENT_POWER,
    ATTR_BAT_DISCHR_WATT_H: POWER_WATT,
    ATTR_BAT_DISCHR_WATT_L: POWER_WATT,
    ATTR_BAT_DSP_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BAT_OVERCHARGE: None,
    ATTR_BAT_S_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BAT_SOC: None,
    ATTR_BAT_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BAT_WATT_H: POWER_WATT,
    ATTR_BAT_WATT_L: POWER_WATT,
    ATTR_BMS_BAT_CURR: ELECTRICAL_CURRENT_AMPERE,
    ATTR_BMS_BAT_TEMP: TEMP_CELSIUS,
    ATTR_BMS_BAT_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_BMSINFO: None,
    ATTR_BMS_CELL01_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL02_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL03_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL04_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL05_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL06_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL07_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL08_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL09_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL10_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL11_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL12_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL13_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL14_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL15_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CELL16_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_CONSTANT_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_BMS_ERROR: None,
    ATTR_BMS_MAX_CURR: None,
    ATTR_BMS_PACKINFO: None,
    ATTR_BMS_SOC: None,
    ATTR_BMS_STATUS: None,
    ATTR_BMS_USINGCAP: None,
    ATTR_BMS_WARNINFO: None,
    ATTR_BUCK1_CURR: ELECTRICAL_CURRENT_AMPERE,
    ATTR_BUCK1_NTC: TEMP_CELSIUS,
    ATTR_BUCK2_CURR: ELECTRICAL_CURRENT_AMPERE,
    ATTR_BUCK2_NTC: TEMP_CELSIUS,
    ATTR_BUS_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_CHECK_STEP: None,
    ATTR_CONSTANT_POWER_OK_FLAG: None,
    ATTR_DCDC_TEMP: TEMP_CELSIUS,
    ATTR_DTC: None,
    ATTR_INV_CURR: ELECTRICAL_CURRENT_AMPERE,
    ATTR_INV_FANSPEED: None,
    ATTR_INV_TEMP: TEMP_CELSIUS,
    ATTR_MPPT_FANSPEED: None,
    ATTR_OP_CURR: ELECTRICAL_CURRENT_AMPERE,
    ATTR_OP_DC_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_OP_FREQ: FREQUENCY_HERTZ,
    ATTR_OP_PERCENT: None,
    ATTR_OP_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_OP_VA_H: APPARENT_POWER,
    ATTR_OP_VA_L: APPARENT_POWER,
    ATTR_OP_WATT_H: POWER_WATT,
    ATTR_OP_WATT_L: POWER_WATT,
    ATTR_PRODUCTION_LINE_MODE: None,
    ATTR_PV1_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_PV2_V: ELECTRICAL_POTENTIAL_VOLT,
    ATTR_TIME_TOTAL_H: TIME_SECONDS,
    ATTR_TIME_TOTAL_L: TIME_SECONDS,
    ATTR_FAULT_BIT: None,
    ATTR_FAULT_BIT_DESC: None,
    ATTR_FAULT_VALUE: None,
    ATTR_WARNING_BIT: None,
    ATTR_WARNING_BIT_DESC: None,
    ATTR_WARNING_VALUE: None,
    ATTR_SYSTEM_STATUS: None,
    ATTR_SYSTEM_STATUS_DESC: None,
}
