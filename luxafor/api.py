"""
API for Luxafor USB status lights.
"""

from . import asserts
from .constants import (
    LED_ALL, MODE_DEMO, MODE_COLOUR, MODE_FADE, MODE_STROBE, MODE_WAVE
)
from .device import find as find_device


class API(object):
    """
    Luxafor USB status light.
    The light has 6 RGB LED's in total, 3 on the 'flag' side and 3 on the 'pole'
    side.

    Each LED can be addressed individually, or grouped via pole, flag or all.
    The specific value for the each address is defined in constants under values
    starting with LED. The positions 'BOTTOM, MIDDLE, TOP' are respective of
    the USB cable being plugged in at the bottom of the device.

    Further more the device has 5 modes; colour, fade, strob, wave and demo.
    Except for demo, all modes require as first parameter a RGB value.
    This is simply a triple byte tuple like (0, 0, 0) for off and
    (255, 255, 255) for the brightest white.

    The device for most modes act as a state device, continuing to display the
    last value a LED is set to.
    """
    def __init__(self, device=find_device(), endpoint=1):
        self._dev = device
        self.endpoint = endpoint

    def _write(self, endpoint, values):
        # pylint: disable=no-member
        self._dev.write(endpoint, None) # First write to 'wake up' device.
        self._dev.write(endpoint, values)

    def _set_mode(self, mode, values):
        asserts.mode(mode)
        args = [mode] + list(values)
        self._write(self.endpoint, args)

    def mode_colour(self, rgb, led=LED_ALL):
        "Set the color 'rgb' to LED(s) 'led'."
        asserts.rgb(rgb)
        asserts.led(led)
        values = [led] + list(rgb)
        self._set_mode(MODE_COLOUR, values)

    def mode_fade(self, rgb, speed, led=LED_ALL):
        """
        Fade from the previous rgb value to the new one, where speed 255 is the
        slowest it can be and 0 the fastest.
        """
        asserts.rgb(rgb)
        asserts.led(led)
        asserts.byte(speed, 'speed')
        values = [led] + list(rgb) + [speed]
        self._set_mode(MODE_FADE, values)

    def mode_strobe(self, rgb, speed, repeat, led=LED_ALL):
        """
        Flicker the rgb value, where speed 255 is the slowest and repeat 255 the
        most often.
        """
        asserts.rgb(rgb)
        asserts.led(led)
        asserts.byte(speed, 'speed')
        asserts.byte(repeat, 'repeat')
        values = [led] + list(rgb) + [speed, 0, repeat]
        self._set_mode(MODE_STROBE, values)

    def mode_wave(self, rgb, pattern, speed, repeat):
        """
        A wave (flowing from one led to another), of which there are 5 patterns
        (1 to 5) with given speed and repetition.
        """
        asserts.rgb(rgb)
        asserts.wave(pattern)
        asserts.byte(speed, 'speed')
        asserts.byte(repeat, 'repeat')
        values = [pattern] + list(rgb) + [0, repeat, speed]
        self._set_mode(MODE_WAVE, values)

    def mode_demo(self, pattern, repeat):
        """
        One of 8 (1-8) demo patterns that can be tried, with a maximum of 255
        repeats.
        """
        asserts.demo(pattern)
        asserts.byte(repeat, 'repeat')
        values = [pattern] + [repeat]
        self._set_mode(MODE_DEMO, values)
