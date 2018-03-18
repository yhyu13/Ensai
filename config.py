from PIL import Image

import tensorflow as tf
import tensorflow.contrib.slim as silm

import scipy
import scipy.ndimage
import scipy.io
from scipy import misc
from scipy.interpolate import RectBivariateSpline

import numpy as np
import numpy.matlib as ml

import random
import time
import os
import gc


'''
   Defining global variables
'''

num_out = 5  # number ouf output parameters being predicted
numpix_side = 192  # number of image pixels on the side

max_trainoise_rms = 0.1  # maximum rms of noise in training data
max_testnoise_rms = 0.1  # maximum rms of noise in test or validation data
max_noise_rms = max_testnoise_rms

max_psf_rms = 0.08 / 0.04  # maximum Gaussian PSF rms (in pixels)
max_cr_intensity = 0.5  # maximum scaling for cosmic ray and artefact maps

# if True, the noise rms will be chosen randomly for each sample with a max of max_noise_rms (above)
variable_noise_rms = True

cycle_batch_size = 50   # how many examples to read at a time (here it's equal to the batch size)
num_test_samples = 1000  # number of test samples

pix_res = 0.04  # pixel size in arcsec
L_side = pix_res * numpix_side

min_unmasked_flux = 0.75

# number of folders containing training or test data. If all 3 point to the same folder that's OK (only that folder will be used).
num_data_dirs = 3

num_training_samples = 50000
max_num_test_samples = 10000
arcs_data_path_1 = 'data/ARCS_2/ARCS_2/'
arcs_data_path_2 = 'data/ARCS_2/ARCS_2/'
arcs_data_path_3 = 'data/ARCS_2/ARCS_2/'
test_data_path_1 = 'data/SAURON_TEST/'
test_data_path_2 = 'data/SAURON_TEST/'
test_data_path_3 = 'data/SAURON_TEST/'

lens_data_path_1 = 'data/ARCS_2/ARCS_2/'
lens_data_path_2 = 'data/ARCS_2/ARCS_2/'
lens_data_path_3 = 'data/ARCS_2/ARCS_2/'
testlens_data_path_1 = 'data/SAURON_TEST/'
testlens_data_path_2 = 'data/SAURON_TEST/'
testlens_data_path_3 = 'data/SAURON_TEST/'

# folder containing cosmic rays
CRay_data_path = 'data/CosmicRays/'

# xy range of center of the lens. The image is shifted in a central area with a side of max_xy_range (arcsec) during training or testing
max_xy_range = 0.5
