#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 15:22:32 2017

@author: jsaavedr
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage
from skimage import io, morphology, filters
import argparse

#Use: python3 tarea1.py <imagen de RUT>
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='OCR')
    parser.add_argument('image', help='input image')
    parser.add_argument('--save', dest='save', type=bool, default=False, nargs='?', const=True, help='input image')
    args=parser.parse_args()
    filename=args.image
    image=io.imread(filename)
    #thresholding
    th=filters.threshold_otsu(image*0.95)
    im_bin = image > th
    #extracting connected components
    mlabels, nlabels=morphology.label(1-im_bin, connectivity=1, return_num=True)
    for i in range(1, nlabels + 1):
        px, py=ndimage.find_objects(mlabels==i)[0]
        roi=im_bin[px, py]
        #padding the image wiht border=1, border width=2
        roi=np.pad(roi, 2, mode='constant', constant_values=1)
        #TODO
        #clase=classifyROI(roi)
        if (args.save):
            print('saving roi' + str(i))
            io.imsave('roi_' + str(i) + '.png', roi*255)
	

    print('RUT: ')
