"""
Reads the pickled arrays (X, Y, C) and does a plot using pcolor() and saves all
frames as png files. To create an animation, use for example:

mencoder "mf://density0*.png" -mf fps=20 -o density.avi -ovc lavc -lavcopts vcodec=mpeg4
"""

import sys
from cPickle import load

from numpy import array
from pylab import pcolor, pcolormesh, show, savefig, clf, colorbar, gca

from tables import IsDescription, openFile, Float64Col

class TimeStep(IsDescription):
    n = Float64Col()
    C = Float64Col(shape=(3201, 800))

h5file = openFile("data.h5", mode="a", title="MHD data")
#common = h5file.createGroup("/", 'common', 'common stuff')
#group = h5file.createGroup("/", 'data', 'data to be plotted')
#table = h5file.createTable(group, 'Cdata', TimeStep, "C data for plotting")
table = h5file.root.data.Cdata

C_min = 0.174630617373
C_max = 2.23176607373

files = [
        "../plot1to155",
        "../plot157to189",
        "../plot191to215",
        "../plot217to249",
        ]
file = files[0]
f = open(file)
print "load"
data = load(f)
X, Y, C = data[0]
#h5file.createArray(common, 'X', X, "the X array")
#h5file.createArray(common, 'Y', Y, "the Y array")
print C.shape
i = 1
for X, Y, C in data:
    print i
    step = table.row
    step["n"] = i
    step["C"] = C
    step.append()
    i += 1

stop
print "pcolor"
print C.shape
print "min/max", C.min(), C.max()
pcolormesh(X, Y, C, vmin=C_min, vmax=C_max)
colorbar()
gca().set_aspect("equal")
print "show"
show()
