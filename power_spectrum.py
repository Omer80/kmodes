#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  power_spectrum.py
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

from scipy import fftpack
import cv2
import numpy as np
import pylab as py
import radialProfile

def main(imagefile = "SH.png"):
		
	
	image = cv2.imread("./data/"+imagefile)
	 
	# Take the fourier transform of the image.
	F1 = fftpack.fft2(image)
	 
	# Now shift the quadrants around so that low spatial frequencies are in
	# the center of the 2D fourier transformed image.
	F2 = fftpack.fftshift( F1 )
	 
	# Calculate a 2D power spectrum
	psd2D = np.abs( F2 )**2
	 
	# Calculate the azimuthally averaged 1D power spectrum
	psd1D = radialProfile.azimuthalAverage(psd2D)
	 
	# Now plot up both
	py.figure(1)
	py.clf()
	py.imshow( np.log10( image ), cmap=py.cm.Greys)
	 
	py.figure(2)
	py.clf()
	py.imshow( np.log10( psf2D ))
	 
	py.figure(3)
	py.clf()
	py.semilogy( psf1D )
	py.xlabel('Spatial Frequency')
	py.ylabel('Power Spectrum')
	 
	py.show()
	
	return 0

if __name__ == '__main__':
	main()

