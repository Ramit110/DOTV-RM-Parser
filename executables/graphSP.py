import sys
from pylab import *

lines = []
with open(sys.argv[1]) as f:
    for line in f:
        if("raidName  raidDifficulty" not in line):
            lines.append(line.replace('"', "").replace("\n", "").split("\t"))

# lines is in the format [["name + diff", "damage/sp|damage/sp...."], ...]

# handles = []
# names = []
# colours = ['red', 'green', 'blue', 'magenta', 'cyan', 'yellow', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
for raids in lines:
    data = raids[1].split("|")
    analysed = {}

    for points in data:
        if(int(points.split("/")[0]) // 12500 not in analysed):
            analysed[int(points.split("/")[0]) // 12500] = []
        analysed[int(points.split("/")[0]) // 12500].append(int(points.split("/")[1].split(" ")[2]))

    print("===========================")
    for key in analysed:
        if(len(analysed[key]) > 20):
            print(raids[0] + " Damage Between " + str((key-1) * 12500) + "-" + str(key * 12500) + "  Average: " + str(sum(analysed[key]) / len(analysed[key])))
        
    
#     x = [0]
#     y = [0]
#     names.append(raids[0])
#     handles.append(scatter(x, y, c=colours.pop(), s=50))

# legend(handles, names)
# grid(True)

# show()
