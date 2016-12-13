"""
Assert function for validating values.
"""
from . import constants

def device(value):
    "Did we find any devices?"
    if value is None:
        raise ValueError("Can't find Luxafor device.")

def mode(value):
    "Is the right mode selected?"
    if value not in constants.MODES:
        text = "Mode value {} not one of {}"
        raise ValueError(text.format(value, str(constants.MODES)))

def byte(value, name):
    "Is the value, by the label of name, not larger than as unsigned byte?"
    if value < 0 or value > 255:
        text = "Invalid {} '{}', must be between 0 and 255."
        raise ValueError(text.format(name, str(value)))

def rgb(value):
    "Is the rgb value valid?"
    if not isinstance(value, (list, tuple)):
        text = 'RGB {} not a sequence type.'.format(type(value))
        raise ValueError(text)

    if len(value) != 3:
        text = 'RGB {} must be an array with 3 items.'.format(str(value))
        raise ValueError(text)

    for colour in value:
        if colour < 0 or colour > 255:
            text = 'Invalid RGB {} each set must be between 0-255.'
            raise ValueError(text.format(str(value)))

def led(value):
    "Is the value a valid LED id to be addressed?"
    if value not in constants.LEDS:
        text = 'LED number {} must be one of: {}'
        raise ValueError(text.format(value, str(constants.LEDS)))

def wave(value):
    "Is the wave pattern valid?"
    if value < 1 or value > 5:
        text = 'Wave pattern must be between 1 and 5'
        raise ValueError(text)

def demo(value):
    "Is the demo pattern valid>"
    if value < 1 or value > 8:
        text = 'Demo pattern must be between 1 and 8'
        raise ValueError(text)
