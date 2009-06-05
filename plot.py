"""
Reads the pickled arrays (X, Y, C) and does a plot using pcolor() and saves all
frames as png files. To create an animation, use for example:

mencoder "mf://density0*.png" -mf fps=20 -o density.avi -ovc lavc -lavcopts vcodec=mpeg4
"""

from cPickle import load

from pylab import pcolor, pcolormesh, show, savefig, clf, colorbar, gca

f = open("../plot217to249")
#f = open("../plot191to215")
#f = open("../plot157to189")
#f = open("../plot1to155")
print "load"
data = load(f)
X, Y, C = data[-1]
print "pcolor"
print C.shape
pcolormesh(X, Y, C)
#colorbar()
gca().set_aspect("equal")
print "show"
show()
