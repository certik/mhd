"""
Reads data from data.h5 file and plots it using pcolor().
"""

import sys
from cPickle import load

from numpy import array
from pylab import pcolor, pcolormesh, show, savefig, clf, colorbar, gca

from tables import IsDescription, openFile, Float64Col

print "opening data"
h5 = openFile("../data.h5")
Cdata = h5.root.data.Cdata
print "  done."

C_min = 0.174630617373
C_max = 2.23176607373

print "read X, Y:"
X = array(h5.root.data.X)
Y = array(h5.root.data.Y)
print "  done."

print "read C:"
C = Cdata.cols.C[0]
print "  done."

C_min = C.min()
C_max = C.max()

print "pcolor"
print C.shape
print "min/max", C.min(), C.max()
pcolormesh(X, Y, C, vmin=C_min, vmax=C_max)
colorbar()
gca().set_aspect("equal")
print "savefig"
savefig("a.png")
print "show"
show()
