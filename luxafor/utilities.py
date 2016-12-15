"""
Tools and Utilities
"""

def _transform_int(one, two, steps):
    delta = (two - one) / (steps -1)
    one -= delta
    while steps > 0:
        steps -= 1
        one += delta
        yield int(one)

def transform_rgb(rgb_first, rgb_last, steps):
    "Return a sequence of rgb's that go from first to last in given steps."
    rgb_sequence = zip(
        _transform_int(rgb_first[0], rgb_last[0], steps),
        _transform_int(rgb_first[1], rgb_last[1], steps),
        _transform_int(rgb_first[2], rgb_last[2], steps)
    )
    return rgb_sequence
