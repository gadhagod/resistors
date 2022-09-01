from . import util
from . import errors

colors = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "gray",
    "white",
    "gold",
    "silver",
    "clear"
]

class Resistor():
    sig_figs = colors[:10]
    multiplier = {**dict(zip(colors[0:10], map(lambda x: 10 ** x, range(10)))), **{"gold": 10 ** -1, "silver": 10 ** -2, "black": 1}}
    tolerance = {
        "brown": 1.0,
        "red": 2.0,
        "green": 0.5,
        "blue": 0.25,
        "violet": 0.1,
        "grey": 0.05,
        "gold": 5.0,
        "silver": 10.0
    }

    def __init__(self, first_color, second_color, third_color, fourth_color, fifth_color=None):
        """
        Creates a Resistor object given 4 or 5 colors

        Parameters:
        first_color (str)   : First color on resistor 
        second_color (str)  : Second color on resistor
        third_color (str)   : Third color on resistor
        fourth_color (str)  : Fourth color on resistor
        fifth_color (str)   : Fifth color on resistor (optional)
        """
        self.first_color = first_color
        self.second_color = second_color
        self.third_color = third_color
        self.fourth_color = fourth_color
        self.fifth_color = fifth_color
        self.isFiveBand = bool(fifth_color)

    def get_colors(self):
        """
        Returns the resistor's color code

        Returns:
        list[str]: The colors in order
        """
        colors = [self.first_color, self.second_color, self.third_color, self.fourth_color]
        if (self.fifth_color):
            colors.append(self.fifth_color)
        return colors

    def get_resistance(self):
        """
        Returns the resistor's resistance in ohms and tolerance in percent

        Returns:
        {"value": float, "tolerance": float}
        """
        if(self.isFiveBand):
            value = (Resistor.sig_figs.index(self.first_color) * 100 + Resistor.sig_figs.index(self.second_color) * 10 + Resistor.sig_figs.index(self.third_color)) * Resistor.multiplier[self.fourth_color]
            tolerance = dict(Resistor.tolerance)[self.fifth_color]
        else:
            value = (Resistor.sig_figs.index(self.first_color) * 10 + Resistor.sig_figs.index(self.second_color)) * Resistor.multiplier[self.third_color]
            tolerance = dict(Resistor.tolerance)[self.fourth_color]

        return {"value": float(round(value, 4)), "tolerance": tolerance}


    @classmethod
    def with_resistance(cls, value, tolerance, bands):
        """
        Creates a Resistor object given a resistance

        Parameters:
        value (float,int):  The resistance in ohms
        tolerance (float):  The tolerance in percent
        bands (int):        Number of bands on the resistor; can be only 4 or 5
        """
        colors = []
        base = util.get_sig_figs(value)
        multiplier = round(value / base, 4)
        baseDigits = util.get_digits(base)
        for i in baseDigits:
            colors.append(Resistor.sig_figs[i])
        if (bands == 4 and len(colors) > 2) or not (bands == 4 or bands == 5):
            raise errors.BandsOutOfBoundsError(bands, value)
        if len(colors) <= 2 and bands == 5:
            colors = ["black"] + colors
        colors.append(util.reverse_dict(Resistor.multiplier)[multiplier])
        colors.append(util.reverse_dict(Resistor.tolerance)[tolerance])
        return cls(*colors)