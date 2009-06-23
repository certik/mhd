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

h5 = openFile("../data.h5")
Cdata = h5.root.data.Cdata

C_min = 0.174630617373
C_max = 2.23176607373

X = array(h5.root.data.X)
Y = array(h5.root.data.Y)
C = Cdata.cols.C[0]

print "pcolor"
print C.shape
print "min/max", C.min(), C.max()
pcolormesh(X, Y, C, vmin=C_min, vmax=C_max)
colorbar()
gca().set_aspect("equal")
print "show"
show()
