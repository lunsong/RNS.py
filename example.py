import numpy as np
from RNS import *

rns = RNS(MDIV=65, SDIV=129)

rns.eos = load_quark_eos(.3, 1)

dr = .01
dec = .001
rns.cf = .5
rns.ec = 1.13
end_ec = 1.18
rns.criteria = 6
rns.max_refine = 30

if rns.eos.start > 0 and rns.ec > rns.e1:
    # following works for ec > e1
    rns.refine_dx = rns.dx / 30
    rns.refine_range = .1
else:
    rns.max_n = 100
    rns.max_refine = 0

rns.spin(.999)

series = []
try:
    while rns.ec < end_ec:
        print('ec=',rns.ec)
        while rns.Omega.value < rns.Omega_K.value:
            print("r=",rns.r_ratio)
            series.append(rns.values)
            rns.spin(rns.r_ratio - dr)
        rns.spin(rns.r_ratio, rns.ec + dec)
        if rns.ec > end_ec: break
        print('ec=',rns.ec)
        for r_ratio in np.mgrid[rns.r_ratio:.9999:dr]:
            print("r=",r_ratio)
            series.append(rns.spin(r_ratio).values)
        rns.spin(rns.r_ratio, rns.ec + dec)
except Exception as E:
    np.save("result", series)
    raise E

