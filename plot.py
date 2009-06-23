"""
Reads data from data.h5 file and plots it using pcolor().
"""

print "Importing libraries"
import sys
from cPickle import load

from numpy import array
import matplotlib
matplotlib.use("Agg")
from pylab import pcolor, pcolormesh, show, savefig, clf, colorbar, gca, title

from tables import IsDescription, openFile, Float64Col
print "  done."

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

N = len(Cdata.cols)

def plot_frame(n=0):
    print "  read C:"
    C = Cdata.cols.C[n]
    print "    done."
    #C_min = C.min()
    #C_max = C.max()
    print "  min/max", C.min(), C.max()
    clf()
    pcolormesh(X, Y, C, vmin=C_min, vmax=C_max)
    colorbar()
    gca().set_aspect("equal")
    title("time: %d" % (n*10))
    print "  savefig"
    savefig("frame%04d.png" % n, dpi=100)
    print "    done"

for i in range(N):
    print "frame:", i
    plot_frame(i)

print "To encode using theora:"
print "ffmpeg2theora -F 15 -v 10 frame%04d.png -o density.ogv"
