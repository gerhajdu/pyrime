#!/usr/bin/env python

from __future__ import print_function
from builtins import range
import numpy as np
import pickle
from sys import argv, exit, version_info
from os import path

import matplotlib.pylab as plt

is_python3 = version_info >= (3, 0)

try:
    FILE = argv[1]
except:
    print("Usage:",argv[0],"FILE_PATH")
    print("FILE_PATH: path to the file containing the Fourier parameters")
    print("The file must contain at least five columns, with the first feive being:")
    print("1: the name of the variable")
    print("2: the period of the variable")
    print("3: the amplitude of the first Fourier harmonic in the I-band")
    print("4: the amplitude of the second Fourier harmonic in the I-band")
    print("5: the epoch-independent phase difference phi31 in the I-band")
    exit()

try:
    names, periods, A1s, A2s, phi31s = np.loadtxt(FILE,
                                                  usecols=[0,1,2,3,4],
                                                  unpack=True,
                                                  dtype='|S30,<f8,<f8,<f8,<f8')
except:
    print("Error reading datafile")
    exit()

try:
    npzfile = np.load(path.dirname(__file__)+'/pyrime_const.npz')
    cut     = npzfile['cut']
    const_p = npzfile['const_p']
except:
    print("pyrime_const.npz file not found")
    exit()

if is_python3:
    corrections_path = path.dirname(__file__)+"/pyrime_correct_py3.pkl"
else:
    corrections_path = path.dirname(__file__)+"/pyrime_correct_py2.pkl"

try:
    clf = pickle.load( open( corrections_path, "rb" ))
except:
    print("pyrime_correct_py2(3).pkl not found!")
    exit()

feh_eq3 = -6.125 -4.795 * periods + 1.181 * phi31s + 7.876 * A2s
feh_final = np.zeros_like(feh_eq3)

periods_r = periods - (const_p[0] + const_p[1] *A1s + const_p[2] *A1s**2 + const_p[3] * A1s**3)

oo1 = (periods_r < cut[0] + feh_eq3*cut[1])
oo2 = np.logical_not(oo1)

feh_final[oo1] = feh_eq3[oo1] - clf.predict(A1s[oo1].reshape(-1,1)).reshape(1,-1)[0] - 1.05
feh_final[oo2] = feh_eq3[oo2]

for i in range(feh_final.size):
    if is_python3:
        name = names[i].decode('utf-8')
    else:
        name = names[i]

    if oo1[i] == True:
        print(name, '{:+5.3f}'.format(feh_final[i]), "OoI")
    else:
        print(name, '{:+5.3f}'.format(feh_final[i]), "OoII")


