from numpy import load

from pylab import pcolor, show, savefig

f = load("/tmp/plot.npz")
X = f["X"]
Y = f["Y"]
C = f["C"]
print X.shape
print Y.shape
print C.shape
print "pcolor"
pcolor(X, Y, C)
print "save"
savefig("a.png")
