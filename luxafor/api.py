"""
API for Luxafor Fag USB device.
"""

from . import asserts
from .constants import COLOUR_NONE as NONE
from .constants import COLOUR_WHITE as WHITE
from .constants import LED_ALL as ALL
from .constants import MODE_COLOUR, MODE_DEMO, MODE_FADE, MODE_BLINK, MODE_WAVE
from .constants import PATTERN_DEMO_LUXAFOR as PATTERN_DEMO
from .constants import PATTERN_WAVE_SINGLE_SMALL as PATTERN_WAVE
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

    def mode_colour(self, rgb=WHITE, led=ALL):
        "Set the color 'rgb' to LED(s) 'led'."
        asserts.rgb(rgb)
        asserts.led(led)
        values = [led] + list(rgb)
        self._set_mode(MODE_COLOUR, values)

    def mode_fade(self, rgb=WHITE, speed=24, led=ALL):
        """
        Fade from the previous rgb value to the new one, where speed 255 is the
        slowest it can be and 0 the fastest.
        """
        asserts.rgb(rgb)
        asserts.led(led)
        asserts.byte(speed, 'speed')
        values = [led] + list(rgb) + [speed]
        self._set_mode(MODE_FADE, values)

    def mode_blink(self, rgb=WHITE, speed=24, repeat=5, led=ALL):
        """
        Blink the rgb value, where speed 255 is the slowest and repeat 255 the
        most often.
        """
        asserts.rgb(rgb)
        asserts.led(led)
        asserts.byte(speed, 'speed')
        asserts.byte(repeat, 'repeat')
        values = [led] + list(rgb) + [speed, 0, repeat]
        self._set_mode(MODE_BLINK, values)

    def mode_wave(self, rgb=NONE, pattern=PATTERN_WAVE, speed=24, repeat=3):
        """
        A wave (flowing from one led to another), of which there are 5 patterns
        (1 to 5) where repeat 255 is the max and speed 255 is the slowest.
        """
        asserts.rgb(rgb)
        asserts.wave(pattern)
        asserts.byte(speed, 'speed')
        asserts.byte(repeat, 'repeat')
        values = [pattern] + list(rgb) + [0, repeat, speed]
        self._set_mode(MODE_WAVE, values)

    def mode_demo(self, pattern=PATTERN_DEMO, repeat=1):
        """
        One of 8 (1-8) demo patterns that can be tried, with a maximum of 255
        repeats.
        """
        asserts.demo(pattern)
        asserts.byte(repeat, 'repeat')
        values = [pattern] + [repeat]
        self._set_mode(MODE_DEMO, values)

    def reset(self):
        """
        Reset the LEDs actually, setting all LEDs to RGB value (0, 0, 0)
        """
        self.mode_colour(NONE)
