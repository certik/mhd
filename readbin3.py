import sys
from math import pi, floor
from struct import calcsize, unpack

from numpy import arange, meshgrid, sin, cos, zeros, array, concatenate, savez

import pylab

def fread(f, fmt):
    u = unpack(fmt, f.read(calcsize(fmt)))
    if len(fmt) == 1:
        return u[0]
    else:
        return u

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
for n in [14]:
    print n
    ext = "%04d" % n
    filename = "%s%s%s" % ("../data/", base, ext)
    f = open(filename)
    rp = zeros(nplanets)
    phip = zeros(nplanets)
    vx = zeros(nplanets)
    vy = zeros(nplanets)
    mplanet = zeros(nplanets)
    roche = zeros(nplanets)
    n4 = fread(f, 4*"i")
    if not ((nplanets == n4[0]) and (nr == n4[1]) and (nphi == n4[2]) and \
            (nvar == n4[3])):
        print "The nplanets, nr, nphi, nvar should be:", n4[0], n4[1], n4[2], \
            n4[3]
        print "but are:", nplanets, nr, nphi, nvar
        sys.exit()
    turn = round(fread(f, "f")/2/pi)
    cs = fread(f, "f")
    for np in range(nplanets):
        rp[np] = fread(f, "f")
        phip[np] = fread(f, "f")
        vx[np] = fread(f, "f")
        vy[np] = fread(f, "f")
        mplanet[np] = fread(f, "f")
        roche[np] = (mplanet[np]/3.0/(1+mplanet[np]))**(1./3) * rp[np]
    print roche

    data = fread(f, nvar*nr*nphi*"f")
    f.close()
    #print "-"*40
    #print array(data)[:10]
    #print "-"*40
    #sys.exit()
    data = array(data).reshape((nvar, nphi, nr), order="F")

    iphi = -int(floor((phip[0]-pi)/dp + 0.5))
    #import IPython
    #IPython.Shell.IPShell(user_ns=dict(globals(), **locals())).mainloop()
    iphi1 = arange(nphi)
    newiphi1 = (iphi1 + iphi) % nphi
    print newiphi1
    print len(newiphi1)
    print newiphi1.min()
    print newiphi1.max()
    print "---"
    print data.shape
    #print data[:, 3000, :3]
    data_mov = data.copy()
    data_mov[:, newiphi1, :] = data[:, iphi1, :]
    data = data_mov
    #print data[:, 3000, :3]
    newphip = zeros(nplanets)
    for np in range(nplanets):
        newphip[np] = (phip[np] + iphi * dp) % (2*pi)
    data = concatenate((data, data[:, 0, :].reshape((nvar, 1, nr), order="F")),
            axis=1)
    rho  = data[0, :, :].reshape((nphi+1, nr), order="F")
    pv   = data[3, :, :].reshape((nphi+1, nr), order="F")
    torq = data[4, :, :].reshape((nphi+1, nr), order="F")
    rhos = rho * r**beta
    rt3 = (radi-rp[0])/roche[0]
    X = (r-rp[0])/roche[0]
    Y = phi
    C = pv
    print "saving"
    f = open("/tmp/plot", "w")
    savez("/tmp/plot", X=X, Y=Y, C=C)
    print "done"
    #print (rp[0]-rp[0])/roche[0]
    #print newphip[0]
