from numpy import load

from pylab import pcolor, pcolormesh, show, savefig

f = load("/tmp/plot.npz")
X = f["X1"]
Y = f["Y1"]
C = f["C1"]
print X.shape
print Y.shape
print C.shape
print "pcolor"
pcolormesh(X, Y, C)
print "save"
savefig("density.png")
