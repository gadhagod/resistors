# Resistors
A Python library for decoding resistor color codes and encoding resistance values.

* Converts colors to value
* Converts value to colors
* Supports four and five-band resistors
* Zero dependencies

The library *strictly* follows the following chart:
![](https://github.com/gadhagod/resistors/raw/master/docs/chart.jpg)

Any colors used in a program not included in this chart will result in a `KeyError`.

## Installation

    pip3 install resistors

## Usage

```
from resistors import Resistor

r1 = Resistor("red", "red", "black", "black", "brown")
print(r1.get_resistance())  # {'value': 220.0, 'tolerance': 1.0}
r2 = Resistor.with_resistance(1230, 2, 5)   # create resistor object with value of 1230Ω, tolerance of +-2%, and 5 bands
print(r2.get_colors())  # ['brown', 'red', 'orange', 'brown', 'red']
```