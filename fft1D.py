#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fft1D.py
#  
#  Copyright 2015 Ohm <ohm@ohm-S400CA>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import scipy
import scipy.fftpack
import pylab
from scipy import pi

def main():
	
	
	t = scipy.linspace(0,120,4000)
	acc = lambda t: 10*scipy.sin(2*pi*2.0*t) + 5*scipy.sin(2*pi*8.0*t) + 2*scipy.random.random(len(t))
	
	signal = acc(t)
	
	FFT = abs(scipy.fft(signal))
	freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])
	
	pylab.subplot(211)
	pylab.plot(t, signal)
	pylab.subplot(212)
	pylab.plot(freqs,20*scipy.log10(FFT),'x')
	pylab.show()
	
	return 0

if __name__ == '__main__':
	main()

