import sys
from pylab import *

lines = []
with open(sys.argv[1]) as f:
    for line in f:
        lines.append(line.replace('"', "").replace("\n", "").split("\t"))

# lines is in the format [["name + diff", "damage/sp|damage/sp...."], ...]

handles = []
names = []
colours = ['red', 'green', 'blue', 'magenta', 'cyan', 'yellow', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
for raids in lines:
    x = [0]
    y = [0]
    names.append(raids[0])
    handles.append(scatter(x, y, c=colours.pop(), s=50))

legend(handles, names)
grid(True)

show()
