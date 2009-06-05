from numpy import load

from pylab import pcolor, show

f = load("/tmp/plot.npz")
X = f["X"]
Y = f["Y"]
C = f["C"]
print "pcolor"
pcolor(X, Y, C)
print "show"
show()
