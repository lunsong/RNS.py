from ctypes import *
from numpy.ctypeslib import ndpointer

def _RNS(SDIV, LMAX):
    so_file = f"spin-{MDIV}-{LMAX}.so"

    if not exists(so_file):
        cmd = f"gcc -fPIC --shared -DMDIV={MDIV} -DLMAX={LMAX} "\
              f"equil_util.c spin.c nrutil.c -lm -o {so_file}"
        if Popen(cmd.split()).wait() != 0:
            raise RuntimeError("compilation failed")

    rns = cdll.LoadLibrary("./"+so_file)
    rns.set_transition.argtypes = [c_double, c_double]
    rns.sphere.argtypes = [
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            c_int,
            c_char_p,
            c_double,
            c_double,
            c_double,
            c_double,
            c_double,
            c_double,
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            POINTER(c_double)]

    rns.spin.argtypes = [
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            c_int,
            c_char_p,
            c_double,
            c_double,
            c_double,
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            c_int,
            c_double,
            c_double,
            c_int,
            POINTER(c_int),
            c_int,
            c_double,
            POINTER(c_double),
            POINTER(c_double)]

    self.rns.mass_radius.argtypes = [
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            c_int,
            c_char_p,
            c_double,
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            ndpointer(np.float64),
            c_double,
            c_double,
            c_double,
            c_double,
            POINTER(c_double),
            POINTER(c_double),
            POINTER(c_double),
            POINTER(c_double),
            ndpointer(np.float64),
            ndpointer(np.float64),
            POINTER(c_double),
            POINTER(c_double)]




