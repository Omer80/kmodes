#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
  kmodes.py
  
  Copyright 2015 Ohm <ohm@ohm-S400CA>
  
  This program is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 2 of the License, or
  (at your option) any later version.
  
  This program is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.
  
  You should have received a copy of the GNU General Public License
  along with this program; if not, write to the Free Software
  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
  MA 02110-1301, USA.
  
"""

__version__=1.0
__author__ = """Omer Tzuk (cliffon@gmail.com)"""

import numpy as np
import cv2
from astroML.correlation import two_point
import matplotlib.pyplot as plt
from scipy.fftpack import ifftn
import matplotlib.cm as cm

def using_cv(imagefile = "SH.png"):
	
	#im_gray = cv2.imread(imagefile, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	#(thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
	img = cv2.imread("./data/"+imagefile,0)
	dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
	dft_shift = np.fft.fftshift(dft)
	
	magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
	
	plt.subplot(121),plt.imshow(img, cmap = 'gray')
	plt.title('Input Image'), plt.xticks([]), plt.yticks([])
	plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
	plt.title('Magnitude Spectrum')#, plt.xticks([]), plt.yticks([])
	plt.show()


			
	return 0
	
def main():
	using_cv()

if __name__ == '__main__':
	main()

