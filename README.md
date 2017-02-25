# Perler Bead Map
Finds the number of beads of each color you need to make a design.

## Requirements
* PIL (preferably pillow, pip install pillow)
* Python 2.7 or better

## Usage
1. Make a design in GIMP or other software
1. Index it to a Perler palette (one is included for GIMP to get you started)
1. Save it as a BMP or PNG
1. Run the tool like shown in the example below

Example:
```
% python perler_colors.py foo.bmp
Perler Peach: 1129
Perler Evergreen: 9
Perler Light Brown: 1302
Perler Grey: 228
Perler Tan: 22
Perler Lavender: 1
Perler Bubblegum: 47
Perler Rust: 1
Perler Pearl Light Pink: 1088
Perler Brown: 2092
Perler Silver: 505
Perler White: 4497
Perler Light Pink: 133
Perler Dark Grey: 495
Perler Cranapple: 34
Perler Light Gray: 44
Perler Black: 973
```
