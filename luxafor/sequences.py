"""
Generates sequences that can be played with Luxafor.play_sequence
"""


def wave(rgb, time, reverse=False):
    leds = [1, 2, 3, 6, 5, 4] # Wave wraps around
    if reverse:
        leds.reverse()
    sequence = list()
    for led in leds:
        sequence.append([led, rgb, time])
        sequence.append([led, (0, 0, 0), 0])

    return sequence


def demo_luxafor(times=1, wait=0.8):
    sequence = [
        [(1, 4), (255, 0, 0), wait],
        [(2, 5), (255, 255, 0), wait],
        [(1, 4), (0, 0, 0), 0],
        [(2, 5), (0, 0, 0), 0],
        [(3, 6), (0, 255, 0), wait],
        [(3, 6), (0, 0, 0), 0],
    ]
    while times > 0:
        times -= 1
        for row in sequence:
            yield row

def demo_police():
    pass