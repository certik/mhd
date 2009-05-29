from math import pi

from numpy import arange, meshgrid, sin, cos

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
