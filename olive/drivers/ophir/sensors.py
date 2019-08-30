"""
Ophir offers a complete range of laser power and energy sensors measuring femtowatts to hundreds of kilowatts and picojoules to hundreds of joules.

According to the manual, there are 8 types of head:
- Thermopile
- BC20
- Temperature probe
- Photodiode
- CIE head
- RP head
- Pyroelectric
- nanoJoule meter
"""
from enum import Enum
import logging

from olive.core import DeviceInfo
from olive.core.utils import retry
from olive.devices import PowerSensor
from olive.devices.errors import UnsupportedDeviceError

__all__ = ["Photodiode", "DiffuserSetting"]

logger = logging.getLogger(__name__)


class DiffuserSetting(Enum):
    FILTER_OUT = "1"
    FILTER_IN = "2"


class Photodiode(PowerSensor):
    """
    Photodiode sensors have a high degree of linearity over a large range of light
    power levels.
    """

    def __init__(self, driver, parent):
        super().__init__(driver, parent=parent)
        self._handle = self.parent.handle

    ##

    @retry(UnsupportedDeviceError, logger=logger)
    def test_open(self):
        self.handle.open()
        try:
            logger.info(f".. {self.info()}")
        except SyntaxError:
            raise UnsupportedDeviceError
        finally:
            self.handle.close()

    def open(self):
        super().open()

        # using a power sensor, auto switch to 'Power screen'
        self.handle.write(b"$FP\r")
        self.handle.read_until("\r")

    ##

    def info(self) -> DeviceInfo:
        self.handle.write(b"$HI\r")
        try:
            response = self.handle.read_until("\r").decode("utf-8")
            _, sn, name, _ = tuple(response.strip("* ").split())
        except (ValueError, UnicodeDecodeError):
            raise SyntaxError("unable to parse device info")
        return DeviceInfo(version=None, vendor="Ophir", model=name, serial_number=sn)

    def enumerate_properties(self):
        return (
            "current_range",  # TODO move to PowerSensor
            "diffuser",
            "unit",  # TODO move to Sensor
            "valid_ranges",  # TODO move to PowerSensor
            "valid_wavelengths",
        )

    ##

    def get_reading(self):
        self.handle.write(b"$SP\r")
        response = self.handle.read_until("\r").decode("utf-8")
        try:
            return float(response.strip("* "))
        except ValueError:
            if "OVER" in response:
                raise ValueError("sensor reading out-of-range")

    def set_wavelength(self):
        pass

    ##

    @property
    def handle(self):
        return self._handle

    """
    Property accessors.
    """

    def _get_current_range(self):
        """
        Return presnetly active range.

        Note:
            Since index of AUTO is 1, and dBm is 2, subscript needs to be offset by 2.
        """
        self.handle.write(b"$AR\r")
        response = self.handle.read_until("\r").decode("utf-8")
        index, *options = tuple(response.strip("* ").split())
        return options[int(index) + 2]

    def _get_diffuser(self):
        self.handle.write(b"$FQ0\r")
        response = self.handle.read_until("\r").decode("utf-8")
        mode, *options = tuple(response.strip("* ").split())
        return DiffuserSetting(mode)

    def _set_diffuser(self, setting: DiffuserSetting):
        self.handle.write(f"$FQ{setting.value}\r".encode())
        response = self.handle.read_until("\r").decode("utf-8")
        mode = response.strip("* ").split()[0]
        try:
            DiffuserSetting(mode)
        except ValueError:
            raise ValueError(f"failed to set diffuser property ({setting})")

    def _get_unit(self):
        self.handle.write(b"$SI\r")
        response = self.handle.read_until("\r").decode("utf-8")
        unit = response.strip("* ").split()[0]
        try:
            # some units use abbreviations
            return {"d": "dBm", "l": "lux", "c": "fc"}[unit]
        except KeyError:
            return unit

    def _get_valid_ranges(self):
        self.handle.write(b"$AR\r")
        response = self.handle.read_until("\r").decode("utf-8")
        _, *options = tuple(response.strip("* ").split())
        return tuple(options)

    def _get_valid_wavelengths(self):
        self.handle.write(b"$AW\r")
        response = self.handle.read_until("\r").decode("utf-8")
        mode, *args = tuple(response.strip("* ").split())
        if mode == "CONTINUOUS":
            fmin, fmax, *options = tuple(args)
            return (fmin, fmax)
        elif mode == "DISCRETE":
            _, *options = tuple(args)
            return options
        else:
            raise RuntimeError(f'unknown mode "{mode}""')

    """
    Private helper functions and constants.
    """

