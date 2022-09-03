class NoColorError(Exception):
    def __init__(self, color):
        super().__init__(f"No such color on a resistor: {color}")

class BandsOutOfBoundsError(Exception):
    def __init__(self, bands):
        super().__init__(f"Resistor can only have 4 or 5 bands, not {bands} bands")

class TooManySigFigsError(Exception):
    def __init__(self, bands, resistance=None):
        super().__init__(f"Cannot create resistor with {bands} bands and resistance of {resistance}")