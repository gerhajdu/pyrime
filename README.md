# PyRIME: Rectified I-band Metallicity Estimae of rr lyrae variables

This routine calculates the I-band photometric iron abundance of RR Lyrae variables,
based on Equation 3 of [Smolec (2005)](http://adsabs.harvard.edu/abs/2005AcA....55...59S),
but correcting for the amplitude-dependent offset in the Oosterhoff I variables, as 
described by Hajdu et al. (2018).

This routine was developed for:
 - `Python` 2.7
 - `Numpy` 1.12

## Installation

Copy the files `pyrime`, `pyrime.py`, `pyrime-const.py` and `pyrime-correct.pkl` to the same
directory in the system PATH.

## Usage

The only argument the program expects is the location of a file, containing at least five columns,
where the first five columns should be:
- NAME: the name of the variable
- PERIOD: the period of the variable
- A1: the amplitude of the first Fourier harmonic in the I band
- A2: the amplitude of the second Fourier harmonic in the I band
- phi31: the epoch independent phase difference of the first and third Fourier harmonics in the I-band
