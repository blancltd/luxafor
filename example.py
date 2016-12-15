"""
Examples
"""
import time
import luxafor
from luxafor import sequences

def set_blue_api():
    """
    Set all 6 led's red with the API.
    """
    api = luxafor.API()
    api.mode_colour(rgb=(0, 0, 255))
    # Wait a second and reset it
    time.sleep(1)
    api.reset()

def set_blue_abstract():
    """
    Set all 6 led's red with the abstracted interface.
    """
    lux = luxafor.Luxafor()
    lux.set_all(rgb=(0, 0, 255))
    lux.push()
    # Wait a second and reset it.
    time.sleep(1)
    lux.reset()
    lux.push()

def set_green_top_bottom_api():
    """
    Set the top and bottom leds on both the flag and pole side green.
    """
    api = luxafor.API()
    rgb = (0, 255, 0)
    api.mode_colour(rgb, luxafor.LED_FLAG_TOP)
    api.mode_colour(rgb, luxafor.LED_POLE_TOP)
    api.mode_colour(rgb, luxafor.LED_FLAG_BOTTOM)
    api.mode_colour(rgb, luxafor.LED_POLE_BOTTOM)
    # Wait a second and reset it.
    time.sleep(1)
    api.reset()

def set_green_top_bottom_abstract():
    """
    Set the top and bottom leds on both the flag and pole side green.
    """
    lux = luxafor.Luxafor()
    rgb = (0, 255, 0)
    lux.set_leds(rgb, [1, 3, 4, 6])
    lux.push()
    # Wait a second and reset it.
    time.sleep(1)
    lux.reset()
    lux.push()

def demo_luxafor_with_the_api():
    """
    This is the luxafor demo as available on the API.
    """
    api = luxafor.API()
    api.mode_demo(luxafor.PATTERN_DEMO_LUXAFOR, repeat=3)
    # The API calls are non-blocking so we have to wait the appropriate time
    # before returning
    time.sleep(6)

def demo_luxafor_abstracted():
    """
    A reimplementation of the luxafor api demo using the abstracted interface.
    """
    # The abstracted interface Luxafor still uses the API in the back-end.
    lux = luxafor.Luxafor()
    sequence = sequences.demo_luxafor(times=3)
    lux.play_sequence(sequence)
    # sequence is a list of instructions, thus not limited to what is built-in
    # to the api.


if __name__ == '__main__':
    set_blue_api()
    set_blue_abstract()
    set_green_top_bottom_api()
    set_green_top_bottom_abstract()
    demo_luxafor_with_the_api()
    demo_luxafor_abstracted()
