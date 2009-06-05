from cPickle import load

from pylab import pcolor, pcolormesh, show, savefig, clf

#f = open("../plot217to249")
#f = open("../plot191to215")
#f = open("../plot157to189")
f = open("../plot1to155")
i_start = 1
data = load(f)
for i in range(len(data)):
    j = i_start + i
    clf()
    X, Y, C = data[i]
    print "it=%d" % j
    print "  pcolor..."
    pcolormesh(X, Y, C)
    print "  save..."
    savefig("density%04d.png" % j)
    print "  done."
