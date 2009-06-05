from cPickle import load

from pylab import pcolor, pcolormesh, show, savefig

f = open("/tmp/plot")
data = load(f)
for i in range(len(data)):
    X, Y, C = data[i]
    print "it=%d" % i
    print "  pcolor..."
    pcolormesh(X, Y, C)
    print "  save..."
    savefig("density%04d.png" % i)
    print "  done."
