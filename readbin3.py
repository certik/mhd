nplanets = 1
nr = 800
nphi = 4*nr
nvar = 4+nplanets

dr = 1.6/nr
hdr = dr/2
dp = 2.*pi/nphi
hdp = dp/2.0

r, phi = meshgrid(0.4+dr*(1:nr)-hdr, 0+dp*(0:nphi)+hdp)
x = r.*cos(phi)
y = r.*sin(phi)
radi = 0.4+dr*(1:nr)-hdr

beta = 1.5  # power law for density profile
