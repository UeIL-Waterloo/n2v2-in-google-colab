# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 14:25:17 2023

@author: Grace Tseng
"""
# The barebones training code used for the pretrained models, which were trained using Compute Canada's servers. Either Cedar or Graham will work.

# run training by importing both n2v2_job_script.sh and n2v2_training.py to the project directory, then run the following:
# cd $project
# sbatch n2v2_job_script.sh

##Import key dependencies:
import tensorflow
from n2v.models import N2VConfig, N2V
from n2v.internals.N2V_DataGenerator import N2V_DataGenerator
import os
import sys

##Ignore warnings
if not sys.warnoptions:
  import warnings
  warnings.filterwarnings('ignore')

## create file directories
#replace fields with the names of your folders
training_data = os.path.abspath('placeholder_folder_name') #folder which contains your training data
model_results = os.path.abspath('results') #create a results folder in your project directory first
model_name = 'placeholder_model_name' #name of the folder containing the finished model

## Load data/training parameters:
datagen = N2V_DataGenerator()
imgs = datagen.load_imgs_from_directory(directory=training_data, filter='*.tiff') #adjust the filter for the type of file you have
#note that N2V2 only supports 2D, single-frame image files

#adjust as needed:
number_of_epochs = 50
patch_size = 64
batch_size = 128
initial_learning_rate = 0.0004
percent_validation = 10
data_augmentation = False

# Prepare data and model for training:
patch_dims = (patch_size, patch_size)
patches = datagen.generate_patches_from_list(imgs, shape=patch_dims, augment=data_augmentation)
patch_shape = patches.shape
threshold = int(patches.shape[0]*(percent_validation/100))
X = patches[threshold:]
X_Val = patches[:threshold]

number_of_steps = int(patch_shape[0]/batch_size)+1

config = N2VConfig(X, unet_kern_size=3,
                   train_steps_per_epoch=number_of_steps, train_epochs=number_of_epochs, train_loss='mse', batch_norm=True,
                   train_batch_size=batch_size, n2v_perc_pix=0.198, n2v_neighborhood_radius=5,
                   single_net_per_channel=False, train_learning_rate=initial_learning_rate, blurpool=True, skip_skipone=True,
                   n2V_manipulator='median', unet_residual=False)

model = N2V(config=config, name=model_name, basedir=model_results)

#Train model:
history = model.train(X, X_Val)

model.export_TF(name='N2V2',
                description='Pretrained N2V2 model for N2V2 image denoising',
                authors=['Grace_T'],
                test_img=X_Val[0,...,0], axes='YX',
                patch_shape=patch_dims)
