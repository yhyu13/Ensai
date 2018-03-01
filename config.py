
'''
   Defining global variables
'''

num_out = 5    #number ouf output parameters being predicted 
numpix_side = 192   #number of image pixels on the side

max_trainoise_rms = 0.1 # maximum rms of noise in training data
max_testnoise_rms = 0.1 # maximum rms of noise in test or validation data
max_noise_rms = max_testnoise_rms

max_psf_rms = 0.08/0.04  # maximum Gaussian PSF rms (in pixels)
max_cr_intensity = 0.5 # maximum scaling for cosmic ray and artefact maps

variable_noise_rms = True  #if True, the noise rms will be chosen randomly for each sample with a max of max_noise_rms (above)

cycle_batch_size = 50   # how many examples to read at a time (here it's equal to the batch size)
num_test_samples = 1000 # number of test samples

pix_res = 0.04 # pixel size in arcsec
L_side = pix_res * numpix_side

min_unmasked_flux = 0.75

num_data_dirs = 3 #number of folders containing training or test data. If all 3 point to the same folder that's OK (only that folder will be used).

num_training_samples = 100000
max_num_test_samples = 1000
arcs_data_path_1 = 'data/SAURON_TEST/'
arcs_data_path_2 = 'data/SAURON_TEST/'
arcs_data_path_3 = 'data/SAURON_TEST/'
test_data_path_1 = 'data/SAURON_TEST/'
test_data_path_2 = 'data/SAURON_TEST/'
test_data_path_3 = 'data/SAURON_TEST/'

lens_data_path_1 = 'data/SAURON_TEST/'
lens_data_path_2 = 'data/SAURON_TEST/'
lens_data_path_3 = 'data/SAURON_TEST/'
testlens_data_path_1 = 'data/SAURON_TEST/'
testlens_data_path_2 = 'data/SAURON_TEST/'
testlens_data_path_3 = 'data/SAURON_TEST/'

#folder containing cosmic rays
CRay_data_path  = 'data/CosmicRays/'

max_xy_range = 0.5 # xy range of center of the lens. The image is shifted in a central area with a side of max_xy_range (arcsec) during training or testing

