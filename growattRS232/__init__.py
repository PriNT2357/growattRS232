"""
Python wrapper for getting data asynchronously from Growatt inverters
via serial usb RS232 connection and modbus RTU protocol.
"""
import logging
import os

from datetime import datetime
from pymodbus.client.sync import ModbusSerialClient as ModbusClient

from growattRS232.const import (
    ATTR_SERIAL_NUMBER,
    ATTR_MODEL_NUMBER,
    ATTR_FIRMWARE,
    ATTR_AC_CHR_CURR,
    ATTR_AC_CHR_TODAY_H,
    ATTR_AC_CHR_TODAY_L,
    ATTR_AC_CHR_TOTAL_H,
    ATTR_AC_CHR_TOTAL_L,
    ATTR_AC_CHR_VA_H,
    ATTR_AC_CHR_VA_L,
    ATTR_AC_CHR_WATT_H,
    ATTR_AC_CHR_WATT_L,
    ATTR_AC_DISCHR_TODAY_H,
    ATTR_AC_DISCHR_TODAY_L,
    ATTR_AC_DISCHR_TOTAL_H,
    ATTR_AC_DISCHR_TOTAL_L,
    ATTR_AC_DISCHR_VA_H,
    ATTR_AC_DISCHR_VA_L,
    ATTR_AC_DISCHR_WATT_H,
    ATTR_AC_DISCHR_WATT_L,
    ATTR_AC_IN_FREQ,
    ATTR_AC_IN_V,
    ATTR_AC_IN_VA_H,
    ATTR_AC_IN_VA_L,
    ATTR_AC_IN_WATT_H,
    ATTR_AC_IN_WATT_L,
    ATTR_BAT_DISCHR_TODAY_H,
    ATTR_BAT_DISCHR_TODAY_L,
    ATTR_BAT_DISCHR_TOTAL_H,
    ATTR_BAT_DISCHR_TOTAL_L,
    ATTR_BAT_DISCHR_VA_H,
    ATTR_BAT_DISCHR_VA_L,
    ATTR_BAT_DISCHR_WATT_H,
    ATTR_BAT_DISCHR_WATT_L,
    ATTR_BAT_DSP_V,
    ATTR_BAT_OVERCHARGE,
    ATTR_BAT_S_V,
    ATTR_BAT_SOC,
    ATTR_BAT_V,
    ATTR_BAT_WATT_H,
    ATTR_BAT_WATT_L,
    ATTR_BMS_BAT_CURR,
    ATTR_BMS_BAT_TEMP,
    ATTR_BMS_BAT_V,
    ATTR_BMS_BMSINFO,
    ATTR_BMS_CELL01_V,
    ATTR_BMS_CELL02_V,
    ATTR_BMS_CELL03_V,
    ATTR_BMS_CELL04_V,
    ATTR_BMS_CELL05_V,
    ATTR_BMS_CELL06_V,
    ATTR_BMS_CELL07_V,
    ATTR_BMS_CELL08_V,
    ATTR_BMS_CELL09_V,
    ATTR_BMS_CELL10_V,
    ATTR_BMS_CELL11_V,
    ATTR_BMS_CELL12_V,
    ATTR_BMS_CELL13_V,
    ATTR_BMS_CELL14_V,
    ATTR_BMS_CELL15_V,
    ATTR_BMS_CELL16_V,
    ATTR_BMS_CONSTANT_V,
    ATTR_BMS_ERROR,
    ATTR_BMS_MAX_CURR,
    ATTR_BMS_PACKINFO,
    ATTR_BMS_SOC,
    ATTR_BMS_STATUS,
    ATTR_BMS_USINGCAP,
    ATTR_BMS_WARNINFO,
    ATTR_BUCK1_CURR,
    ATTR_BUCK1_NTC,
    ATTR_BUCK2_CURR,
    ATTR_BUCK2_NTC,
    ATTR_BUS_V,
    ATTR_CHECK_STEP,
    ATTR_CONSTANT_POWER_OK_FLAG,
    ATTR_DCDC_TEMP,
    ATTR_DTC,
    ATTR_INV_CURR,
    ATTR_INV_FANSPEED,
    ATTR_INV_TEMP,
    ATTR_MPPT_FANSPEED,
    ATTR_OP_CURR,
    ATTR_OP_DC_V,
    ATTR_OP_FREQ,
    ATTR_OP_PERCENT,
    ATTR_OP_V,
    ATTR_OP_VA_H,
    ATTR_OP_VA_L,
    ATTR_OP_WATT_H,
    ATTR_OP_WATT_L,
    ATTR_PRODUCTION_LINE_MODE,
    ATTR_PV1_V,
    ATTR_PV2_V,
    ATTR_TIME_TOTAL_H,
    ATTR_TIME_TOTAL_L,
    ATTR_FAULT_BIT,
    ATTR_FAULT_BIT_DESC,
    ATTR_FAULT_VALUE,
    ATTR_WARNING_BIT,
    ATTR_WARNING_BIT_DESC,
    ATTR_WARNING_VALUE,
    ATTR_SYSTEM_STATUS,
    ATTR_SYSTEM_STATUS_DESC,
    REG_AC_CHR_CURR,
    REG_AC_CHR_TODAY_H,
    REG_AC_CHR_TODAY_L,
    REG_AC_CHR_TOTAL_H,
    REG_AC_CHR_TOTAL_L,
    REG_AC_CHR_VA_H,
    REG_AC_CHR_VA_L,
    REG_AC_CHR_WATT_H,
    REG_AC_CHR_WATT_L,
    REG_AC_DISCHR_TODAY_H,
    REG_AC_DISCHR_TODAY_L,
    REG_AC_DISCHR_TOTAL_H,
    REG_AC_DISCHR_TOTAL_L,
    REG_AC_DISCHR_VA_H,
    REG_AC_DISCHR_VA_L,
    REG_AC_DISCHR_WATT_H,
    REG_AC_DISCHR_WATT_L,
    REG_AC_IN_FREQ,
    REG_AC_IN_V,
    REG_AC_IN_VA_H,
    REG_AC_IN_VA_L,
    REG_AC_IN_WATT_H,
    REG_AC_IN_WATT_L,
    REG_BAT_DISCHR_TODAY_H,
    REG_BAT_DISCHR_TODAY_L,
    REG_BAT_DISCHR_TOTAL_H,
    REG_BAT_DISCHR_TOTAL_L,
    REG_BAT_DISCHR_VA_H,
    REG_BAT_DISCHR_VA_L,
    REG_BAT_DISCHR_WATT_H,
    REG_BAT_DISCHR_WATT_L,
    REG_BAT_DSP_V,
    REG_BAT_OVERCHARGE,
    REG_BAT_S_V,
    REG_BAT_SOC,
    REG_BAT_V,
    REG_BAT_WATT_H,
    REG_BAT_WATT_L,
    REG_BMS_BAT_CURR,
    REG_BMS_BAT_TEMP,
    REG_BMS_BAT_V,
    REG_BMS_BMSINFO,
    REG_BMS_CELL01_V,
    REG_BMS_CELL02_V,
    REG_BMS_CELL03_V,
    REG_BMS_CELL04_V,
    REG_BMS_CELL05_V,
    REG_BMS_CELL06_V,
    REG_BMS_CELL07_V,
    REG_BMS_CELL08_V,
    REG_BMS_CELL09_V,
    REG_BMS_CELL10_V,
    REG_BMS_CELL11_V,
    REG_BMS_CELL12_V,
    REG_BMS_CELL13_V,
    REG_BMS_CELL14_V,
    REG_BMS_CELL15_V,
    REG_BMS_CELL16_V,
    REG_BMS_CONSTANT_V,
    REG_BMS_ERROR,
    REG_BMS_MAX_CURR,
    REG_BMS_PACKINFO,
    REG_BMS_SOC,
    REG_BMS_STATUS,
    REG_BMS_USINGCAP,
    REG_BMS_WARNINFO,
    REG_BUCK1_CURR,
    REG_BUCK1_NTC,
    REG_BUCK2_CURR,
    REG_BUCK2_NTC,
    REG_BUS_V,
    REG_CHECK_STEP,
    REG_CONSTANT_POWER_OK_FLAG,
    REG_DCDC_TEMP,
    REG_DTC,
    REG_INV_CURR,
    REG_INV_FANSPEED,
    REG_INV_TEMP,
    REG_MPPT_FANSPEED,
    REG_OP_CURR,
    REG_OP_DC_V,
    REG_OP_FREQ,
    REG_OP_PERCENT,
    REG_OP_V,
    REG_OP_VA_H,
    REG_OP_VA_L,
    REG_OP_WATT_H,
    REG_OP_WATT_L,
    REG_PRODUCTION_LINE_MODE,
    REG_PV1_V,
    REG_PV2_V,
    REG_TIME_TOTAL_H,
    REG_TIME_TOTAL_L,
    REG_FAULT_BIT,
    REG_FAULT_VALUE,
    REG_WARNING_BIT,
    REG_WARNING_VALUE,
    REG_SYSTEM_STATUS,
    DEFAULT_ADDRESS,
    DEFAULT_PORT,
    DERATINGMODES,
    FAULTCODES,
    STATUSCODES,
    WARNINGCODES,
)


def rssf(rr, index, scale=10):
    """Read and scale single to float."""
    return float(rr.registers[index]) / scale


def rsdf(rr, index, scale=10):
    """Read and scale double to float."""
    return float((rr.registers[index] << 16) + rr.registers[index + 1]) / scale


class GrowattRS232:
    """Main class to communicate with the Growatt inverter."""

    def __init__(
        self, port=DEFAULT_PORT, address=DEFAULT_ADDRESS, logger=None
    ):
        """Initialize."""
        if logger is None:
            self._logger = logging.getLogger(__name__)
            self._logger.addHandler(logging.NullHandler())
        else:
            self._logger = logger

        # Inverter properties."""
        self._serial_number = ""
        self._model_number = ""
        self._firmware = ""
        self._last_update = None
        # usb port
        self._port = port
        # Modbus address (1-247)
        self._unit = address
        # Modbus serial rtu communication client
        self._client = ModbusClient(
            method="rtu",
            port=port,
            baudrate=9600,
            stopbits=1,
            parity="N",
            bytesize=8,
            timeout=1,
        )

        self._logger.debug(
            (
                f"GrowattRS232 initialized with usb port {self._port} "
                f"and modbus address {self._unit}."
            )
        )

    async def async_update(self):
        """
        Read Growatt data.

        Modbus rtu information from
        "Growatt OffGrid SPF5000 Modbus RS485 RTU Protocol V0.11 2017-8-09".
        The availability of the attributes depends
        on the firmware version of your inverter.
        """

        data = {}

        if not os.path.exists(self._port):
            self._logger.debug(f"USB port {self._port} is not available")
            raise PortException(f"USB port {self._port} is not available")

        self._client.timeout = True
        if not self._client.connect():
            self._logger.debug(
                f"Modbus connection failed for address {self._unit}."
            )
            raise ModbusException(
                f"Modbus connection failed for address {self._unit}."
            )

        if self._serial_number == "":
            # Assuming the serial number doesn't change, it is read only once
            rhr = self._client.read_holding_registers(0, 30, unit=self._unit)
            if rhr.isError():
                self._client.close()
                self._logger.debug("Modbus read failed for rhr.")
                raise ModbusException("Modbus read failed for rhr.")

            self._firmware = str(
                chr(rhr.registers[9] >> 8)
                + chr(rhr.registers[9] & 0x000000FF)
                + chr(rhr.registers[10] >> 8)
                + chr(rhr.registers[10] & 0x000000FF)
                + chr(rhr.registers[11] >> 8)
                + chr(rhr.registers[11] & 0x000000FF)
            )

            self._serial_number = str(
                chr(rhr.registers[23] >> 8)
                + chr(rhr.registers[23] & 0x000000FF)
                + chr(rhr.registers[24] >> 8)
                + chr(rhr.registers[24] & 0x000000FF)
                + chr(rhr.registers[25] >> 8)
                + chr(rhr.registers[25] & 0x000000FF)
                + chr(rhr.registers[26] >> 8)
                + chr(rhr.registers[26] & 0x000000FF)
                + chr(rhr.registers[27] >> 8)
                + chr(rhr.registers[27] & 0x000000FF)
            )

            mo = (rhr.registers[28] << 16) + rhr.registers[29]
            self._model_number = (
                "T"
                + str((mo & 0xF00000) >> 20)
                + " Q"
                + str((mo & 0x0F0000) >> 16)
                + " P"
                + str((mo & 0x00F000) >> 12)
                + " U"
                + str((mo & 0x000F00) >> 8)
                + " M"
                + str((mo & 0x0000F0) >> 4)
                + " S"
                + str((mo & 0x00000F))
            )

            self._logger.debug(
                (
                    f"GrowattRS232 with serial number {self._serial_number} "
                    f"is model {self._model_number} "
                    f"and has firmware {self._firmware}."
                )
            )

        # Begin reading input registers
        self._logger.debug("Modbus read rir1.")
        rir1 = self._client.read_input_registers(0, 44, unit=self._unit)
        if rir1.isError():
            self._client.close()
            self._logger.debug("Modbus read failed for rir1.")
            raise ModbusException("Modbus read failed for rir1.")

        self._logger.debug("Modbus read rir2.")
        rir2 = self._client.read_input_registers(45, 44, unit=self._unit)
        if rir2.isError():
            self._client.close()
            self._logger.debug("Modbus read failed for rir2.")
            raise ModbusException("Modbus read failed for rir2")
            
        # BMS Info
        self._logger.debug("Modbus read rir3.")
        rir3 = self._client.read_input_registers(90, 44, unit=self._unit)
        if rir3.isError():
            self._client.close()
            self._logger.debug("Modbus read failed for 3.")
            raise ModbusException("Modbus read failed for rir3")

        self._client.close()

        # Inverter properties
        self._logger.debug("Setting Inverter Properties.")
        data[ATTR_SERIAL_NUMBER] = self._serial_number
        data[ATTR_MODEL_NUMBER] = self._model_number
        data[ATTR_FIRMWARE] = self._firmware

        # DC input string 1 PV
        #data[ATTR_INPUT_1_VOLTAGE] = rssf(rir1, 3)
        #data[ATTR_INPUT_1_AMPERAGE] = rssf(rir1, 4)
        #data[ATTR_INPUT_1_POWER] = rsdf(rir1, 5)
        #data[ATTR_INPUT_1_ENERGY_TODAY] = rsdf(rir2, 3)
        #data[ATTR_INPUT_1_ENERGY_TOTAL] = rsdf(rir2, 5)

        # AC Information
        self._logger.debug("Setting AC Information.")
        data[ATTR_AC_CHR_CURR] = rssf(rir2, REG_AC_CHR_CURR)
        data[ATTR_AC_CHR_TODAY_H] = rssf(rir2, REG_AC_CHR_TODAY_H)
        data[ATTR_AC_CHR_TODAY_L] = rssf(rir2, REG_AC_CHR_TODAY_L)
        data[ATTR_AC_CHR_TOTAL_H] = rssf(rir2, REG_AC_CHR_TOTAL_H)
        data[ATTR_AC_CHR_TOTAL_L] = rssf(rir2, REG_AC_CHR_TOTAL_L)
        data[ATTR_AC_CHR_VA_H] = rssf(rir1, REG_AC_CHR_VA_H)
        data[ATTR_AC_CHR_VA_L] = rssf(rir1, REG_AC_CHR_VA_L)
        data[ATTR_AC_CHR_WATT_H] = rssf(rir1, REG_AC_CHR_WATT_H)
        data[ATTR_AC_CHR_WATT_L] = rssf(rir1, REG_AC_CHR_WATT_L)
        data[ATTR_AC_DISCHR_TODAY_H] = rssf(rir2, REG_AC_DISCHR_TODAY_H)
        data[ATTR_AC_DISCHR_TODAY_L] = rssf(rir2, REG_AC_DISCHR_TODAY_L)
        data[ATTR_AC_DISCHR_TOTAL_H] = rssf(rir2, REG_AC_DISCHR_TOTAL_H)
        data[ATTR_AC_DISCHR_TOTAL_L] = rssf(rir2, REG_AC_DISCHR_TOTAL_L)
        data[ATTR_AC_DISCHR_VA_H] = rssf(rir2, REG_AC_DISCHR_VA_H)
        data[ATTR_AC_DISCHR_VA_L] = rssf(rir2, REG_AC_DISCHR_VA_L)
        data[ATTR_AC_DISCHR_WATT_H] = rssf(rir2, REG_AC_DISCHR_WATT_H)
        data[ATTR_AC_DISCHR_WATT_L] = rssf(rir2, REG_AC_DISCHR_WATT_L)
        data[ATTR_AC_IN_FREQ] = rssf(rir1, REG_AC_IN_FREQ, 100)
        data[ATTR_AC_IN_V] = rssf(rir1, REG_AC_IN_V)
        data[ATTR_AC_IN_VA_H] = rssf(rir1, REG_AC_IN_VA_H)
        data[ATTR_AC_IN_VA_L] = rssf(rir1, REG_AC_IN_VA_L)
        data[ATTR_AC_IN_WATT_H] = rssf(rir1, REG_AC_IN_WATT_H)
        data[ATTR_AC_IN_WATT_L] = rssf(rir1, REG_AC_IN_WATT_L)

        # Battery Information
        self._logger.debug("Setting Battery Information.")
        data[ATTR_BAT_DISCHR_TODAY_H] = rssf(rir2, REG_BAT_DISCHR_TODAY_H)
        data[ATTR_BAT_DISCHR_TODAY_L] = rssf(rir2, REG_BAT_DISCHR_TODAY_L)
        data[ATTR_BAT_DISCHR_TOTAL_H] = rssf(rir2, REG_BAT_DISCHR_TOTAL_H)
        data[ATTR_BAT_DISCHR_TOTAL_L] = rssf(rir2, REG_BAT_DISCHR_TOTAL_L)
        data[ATTR_BAT_DISCHR_VA_H] = rssf(rir2, REG_BAT_DISCHR_VA_H)
        data[ATTR_BAT_DISCHR_VA_L] = rssf(rir2, REG_BAT_DISCHR_VA_L)
        data[ATTR_BAT_DISCHR_WATT_H] = rssf(rir2, REG_BAT_DISCHR_WATT_H)
        data[ATTR_BAT_DISCHR_WATT_L] = rssf(rir2, REG_BAT_DISCHR_WATT_L)
        data[ATTR_BAT_DSP_V] = rssf(rir1, REG_BAT_DSP_V, 100)
        data[ATTR_BAT_OVERCHARGE] = rssf(rir2, REG_BAT_OVERCHARGE)
        data[ATTR_BAT_S_V] = rssf(rir1, REG_BAT_S_V, 100)
        data[ATTR_BAT_SOC] = 100 - rir2.registers[REG_BAT_SOC] # ex: 95% SOC comes back as 5
        data[ATTR_BAT_V] = rssf(rir1, REG_BAT_V, 100)
        data[ATTR_BAT_WATT_H] = rssf(rir2, REG_BAT_WATT_H)
        data[ATTR_BAT_WATT_L] = rssf(rir2, REG_BAT_WATT_L)

        # BMS Information
        self._logger.debug("Setting BMS Information.")
        data[ATTR_BMS_BAT_CURR] = rssf(rir3, REG_BMS_BAT_CURR)
        data[ATTR_BMS_BAT_TEMP] = rir3.registers[REG_BMS_BAT_TEMP]
        data[ATTR_BMS_BAT_V] = rssf(rir3, REG_BMS_BAT_V)
        data[ATTR_BMS_BMSINFO] = rir3.registers[REG_BMS_BMSINFO]
        data[ATTR_BMS_CELL01_V] = rssf(rir3, REG_BMS_CELL01_V)
        data[ATTR_BMS_CELL02_V] = rssf(rir3, REG_BMS_CELL02_V)
        data[ATTR_BMS_CELL03_V] = rssf(rir3, REG_BMS_CELL03_V)
        data[ATTR_BMS_CELL04_V] = rssf(rir3, REG_BMS_CELL04_V)
        data[ATTR_BMS_CELL05_V] = rssf(rir3, REG_BMS_CELL05_V)
        data[ATTR_BMS_CELL06_V] = rssf(rir3, REG_BMS_CELL06_V)
        data[ATTR_BMS_CELL07_V] = rssf(rir3, REG_BMS_CELL07_V)
        data[ATTR_BMS_CELL08_V] = rssf(rir3, REG_BMS_CELL08_V)
        data[ATTR_BMS_CELL09_V] = rssf(rir3, REG_BMS_CELL09_V)
        data[ATTR_BMS_CELL10_V] = rssf(rir3, REG_BMS_CELL10_V)
        data[ATTR_BMS_CELL11_V] = rssf(rir3, REG_BMS_CELL11_V)
        data[ATTR_BMS_CELL12_V] = rssf(rir3, REG_BMS_CELL12_V)
        data[ATTR_BMS_CELL13_V] = rssf(rir3, REG_BMS_CELL13_V)
        data[ATTR_BMS_CELL14_V] = rssf(rir3, REG_BMS_CELL14_V)
        data[ATTR_BMS_CELL15_V] = rssf(rir3, REG_BMS_CELL15_V)
        data[ATTR_BMS_CELL16_V] = rssf(rir3, REG_BMS_CELL16_V)
        data[ATTR_BMS_CONSTANT_V] = rssf(rir3, REG_BMS_CONSTANT_V)
        data[ATTR_BMS_ERROR] = rir3.registers[REG_BMS_ERROR]
        data[ATTR_BMS_MAX_CURR] = rssf(rir3, REG_BMS_MAX_CURR)
        data[ATTR_BMS_PACKINFO] = rir3.registers[REG_BMS_PACKINFO]
        data[ATTR_BMS_SOC] = rir3.registers[REG_BMS_SOC]
        data[ATTR_BMS_STATUS] = rir3.registers[REG_BMS_STATUS]
        data[ATTR_BMS_USINGCAP] = rir3.registers[REG_BMS_USINGCAP]
        data[ATTR_BMS_WARNINFO] = rir3.registers[REG_BMS_WARNINFO]

        # Output Information
        self._logger.debug("Setting Output Information.")
        data[ATTR_OP_CURR] = rssf(rir1, REG_OP_CURR)
        data[ATTR_OP_DC_V] = rssf(rir1, REG_OP_DC_V)
        data[ATTR_OP_FREQ] = rssf(rir1, REG_OP_FREQ, 100)
        data[ATTR_OP_PERCENT] = rssf(rir1, REG_OP_PERCENT)
        data[ATTR_OP_V] = rssf(rir1, REG_OP_V)
        data[ATTR_OP_VA_H] = rssf(rir1, REG_OP_VA_H)
        data[ATTR_OP_VA_L] = rssf(rir1, REG_OP_VA_L)
        data[ATTR_OP_WATT_H] = rssf(rir1, REG_OP_WATT_H)
        data[ATTR_OP_WATT_L] = rssf(rir1, REG_OP_WATT_L)
        
        #TODO
        # PV Information
        self._logger.debug("Setting PV Information.")
        data[ATTR_PV1_V] = rssf(rir1, REG_PV1_V)
        data[ATTR_PV2_V] = rssf(rir1, REG_PV2_V)

        # Miscellaneous Information
        self._logger.debug("Setting Miscellaneous Information.")
        data[ATTR_BUCK1_CURR] = rssf(rir1, REG_BUCK1_CURR)
        data[ATTR_BUCK1_NTC] = rssf(rir1, REG_BUCK1_NTC)
        data[ATTR_BUCK2_CURR] = rssf(rir1, REG_BUCK2_CURR)
        #data[ATTR_BUCK2_NTC] = rssf(rir1, REG_BUCK2_NTC) #Error: IndexError('list index out of range')
        data[ATTR_BUS_V] = rssf(rir1, REG_BUS_V)
        data[ATTR_CHECK_STEP] = rir2.registers[REG_CHECK_STEP]        #TODO - Validate return value "1251"
        data[ATTR_PRODUCTION_LINE_MODE] = rir2.registers[REG_PRODUCTION_LINE_MODE]        #TODO - Validate return value "0"
        data[ATTR_CONSTANT_POWER_OK_FLAG] = rir2.registers[REG_CONSTANT_POWER_OK_FLAG]        #TODO - Validate return value "0"
        #data[ATTR_DCDC_TEMP] = rssf(rir1, REG_DCDC_TEMP) #Error: IndexError('list index out of range')
        #data[ATTR_DTC] = rssf(rir1, REG_DTC) #Error: IndexError('list index out of range')
        data[ATTR_INV_CURR] = rssf(rir1, REG_INV_CURR)
        data[ATTR_INV_FANSPEED] = rir2.registers[REG_INV_FANSPEED]
        data[ATTR_INV_TEMP] = rssf(rir1, REG_INV_TEMP)
        data[ATTR_MPPT_FANSPEED] = rir2.registers[REG_MPPT_FANSPEED]
        data[ATTR_TIME_TOTAL_H] = rir1.registers[REG_TIME_TOTAL_H]
        data[ATTR_TIME_TOTAL_L] = rir1.registers[REG_TIME_TOTAL_L]

        # Status, faults & warnings
        self._logger.debug("Setting Status, faults & warnings.")
        data[ATTR_FAULT_BIT] = rir1.registers[REG_FAULT_BIT]
        data[ATTR_FAULT_BIT_DESC] = FAULTCODES[rir1.registers[REG_FAULT_BIT]]
        data[ATTR_FAULT_VALUE] = rssf(rir1, REG_FAULT_VALUE)
        data[ATTR_WARNING_BIT] = rir1.registers[REG_WARNING_BIT]
        data[ATTR_WARNING_BIT_DESC] = WARNINGCODES[rir1.registers[REG_WARNING_BIT]]
        data[ATTR_WARNING_VALUE] = rssf(rir1, REG_WARNING_VALUE)
        data[ATTR_SYSTEM_STATUS] = rir1.registers[REG_SYSTEM_STATUS]
        data[ATTR_SYSTEM_STATUS_DESC] = STATUSCODES[rir1.registers[REG_SYSTEM_STATUS]]

        self._logger.debug("DATA:")
        self._logger.debug(data)

        if not data:
            return {}

        self._last_update = datetime.now()
        return data


class PortException(Exception):
    """Raised when the USB port in not available."""

    def __init__(self, status):
        """Initialize."""
        super(PortException, self).__init__(status)
        self.status = status


class ModbusException(Exception):
    """Raised when the Modbus communication has error."""

    def __init__(self, status):
        """Initialize."""
        super(ModbusException, self).__init__(status)
        self.status = status
