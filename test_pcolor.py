from timeit import default_timer as clock
from numpy import meshgrid, arange, pi, sin, cos
from pylab import pcolor, show, pcolormesh, savefig

r, phi = meshgrid(arange(0, 10., 0.01), arange(0, 2*pi, 0.001))

f = r**2

x = r * cos(phi)
y = r * sin(phi)
t = clock()
#pcolor(x, y, f)
pcolormesh(x, y, f)
t = clock() - t
print "pcolor:", t
t = clock()
savefig("c.png")
t = clock() - t
print "save:  ", t
#show()
