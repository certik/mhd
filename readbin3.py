import sys
from math import pi
from struct import calcsize, unpack

from numpy import arange, meshgrid, sin, cos, zeros

def read(f, fmt):
    return unpack(fmt, f.read(calcsize(fmt)))

nplanets = 1
nr = 800
nphi = 4*nr
nvar = 4+nplanets

dr = 1.6/nr
hdr = dr/2
dp = 2.*pi/nphi
hdp = dp/2.0

X = 0.4+dr*arange(1, nr+1)-hdr
Y = 0+dp*arange(nphi+1)+hdp
r, phi = meshgrid(X, Y)

x = r * cos(phi)
y = r * sin(phi)
radi = X

beta = 1.5  # power law for density profile

base = 'fortb.u';
for n in [1, 2, 3]:
    ext = "%04d" % n
    filename = "%s%s%s" % ("../data/", base, ext)
    f = open(filename)
    print f
    rp = zeros(nplanets)
    phip = zeros(nplanets)
    vx = zeros(nplanets)
    vy = zeros(nplanets)
    n4 = read(f, 4*"i")
    if not ((nplanets == n4[0]) and (nr == n4[1]) and (nphi == n4[2]) and \
            (nvar == n4[3])):
        print "The nplanets, nr, nphi, nvar should be:", n4[0], n4[1], n4[2], \
            n4[3]
        print "but are:", nplanets, nr, nphi, nvar
        sys.exit()
