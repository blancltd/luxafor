"""
Luxafor abstracted interface
"""
import time

from .api import API
from .constants import (
    LED_FLAG_BOTTOM, LED_FLAG_MIDDLE, LED_FLAG_TOP,
    LED_POLE_BOTTOM, LED_POLE_MIDDLE, LED_POLE_TOP
)

LEDS = [
    ['LED_FLAG_TOP', 1, LED_FLAG_TOP],
    ['LED_FLAG_MIDDLE', 2, LED_FLAG_MIDDLE],
    ['LED_FLAG_BOTTOM', 3, LED_FLAG_BOTTOM],
    ['LED_POLE_TOP', 4, LED_POLE_TOP],
    ['LED_POLE_MIDDLE', 5, LED_POLE_MIDDLE],
    ['LED_POLE_BOTTOM', 6, LED_POLE_BOTTOM],
]

class Luxafor(object):
    def __init__(self, api=API()):
        self.api = api
        self.led = {}

        self.reset()
        self.push()

    def reset(self):
        for row in LEDS:
            self.led[row[1]] = (0, 0, 0)

    def _set_by_part(self, rgb, part):
        for row in LEDS:
            if part in row[0]:
                self.led[row[1]] = rgb

    def set_flag(self, rgb):
        self._set_by_part(rgb, 'FLAG')

    def set_pole(self, rgb):
        self._set_by_part(rgb, 'POLE')

    def set_top(self, rgb):
        self._set_by_part(rgb, 'TOP')

    def set_middle(self, rgb):
        self._set_by_part(rgb, 'MIDDLE')

    def set_bottom(self, rgb):
        self._set_by_part(rgb, 'BOTTOM')

    def set_leds(self, rgb, leds=None):
        if not leds:
            leds = []

        if not isinstance(leds, (list, tuple)):
            leds = [leds]

        for led in leds:
            self.led[led] = rgb

    def set_all(self, rgb):
        self._set_by_part(rgb, 'LED')

    def push(self, delta_only=False):
        if not delta_only:
            # Don't cut any corners, just push what it is.
            for index, rgb in self.led.items():
                index -= 1
                api_led_id = LEDS[index][2]
                self.api.mode_colour(rgb, api_led_id)
            
            return

        # No change
        # - Just return
        
        # All the same
        # - set led-id to all
        
        # Only flag changed to the same colour
        # - set led-id to flag

        # Only pole changed to the same colour
        # - set led-id to pole
        
        # Only set led-id's that have changed
        

    def play_sequence(self, sequence):
        for leds, rgb, wait_time in sequence:
            self.set_leds(rgb, leds)
            if wait_time > 0:
                self.push()
                time.sleep(wait_time)

        self.reset()
        self.push()
    