from numpy import meshgrid, arange, pi, sin, cos
from pylab import pcolor, show

r, phi = meshgrid(arange(0, 10., 1), arange(0, 2*pi, 0.1))

f = r**2

x = r * cos(phi)
y = r * sin(phi)
pcolor(x, y, f)
show()
