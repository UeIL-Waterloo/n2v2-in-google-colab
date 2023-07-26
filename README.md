# n2v2-in-google-colab
Noise2Void (N2V) is a deep-learning technique used to denoise images, developed by Krull et. al. in 2019. It is unique from other deep-learning techniques in that it is self-supervised, so sets of high- and low- noise images are not required for training. As such, it lends itself well to use for microscopy images, where multiple high signal-to-noise ratio images are not often feasible.

This particular notebook uses an improved version of N2V, N2V2, developed in 2022. This version eliminates the checkerboard artifacts that often result from N2V, as shown below:

![diagram](https://github.com/gracefacetseng/n2v2-in-google-colab/assets/132942058/c7e66975-e9d9-492c-bc3a-695f0b8cd5a6)

## Pretrained Models:

This notebook supports both training your own model and predicting denoised images. If you do not have the data to train a model, you can still use this notebook! I have included some preloaded models trained on specific subjects. You can peruse the selection in the "pretrained models" directory above, and they will be made available to you when you load the notebook. To use one, please follow the instructions in the notebook :) 

### Sample Images:


## Acknowledgements:
This notebook was heavily influenced by Noise2Void (2D) by the Zero-Cost Download for Microscopy Project, found here: [Noise2Void_2D_ZeroCostDL4Mic](https://colab.research.google.com/github/HenriquesLab/ZeroCostDL4Mic/blob/master/Colab_notebooks/Noise2Void_2D_ZeroCostDL4Mic.ipynb)

The paper about N2V by Krull et. al.: [Noise2Void - Learning Denoising from Single Noisy Images](https://arxiv.org/abs/1811.10980)

The paper for N2V2: [N2V2 -- Fixing Noise2Void Checkerboard Artifacts with Modified Sampling Strategies and a Tweaked Network Architecture](https://arxiv.org/abs/2211.08512)

Source code for N2V was found here: https://github.com/juglab/n2v

**If you use this notebook in your research, please cite the above papers.**

Pretrained models were trained using images from the following datasets:
 *  mitochondria_mitolab: [EMPIAR-11037](https://www.ebi.ac.uk/empiar/EMPIAR-11037/)
 *  

<img width="368" alt="NSERC_FIP_RGB" src="https://github.com/gracefacetseng/n2v2-in-google-colab/assets/132942058/748f0a73-55dd-4c28-9f5a-20fb03246775">

We acknowledge the support of the Natural Sciences and Engineering Research Council of Canada (NSERC).

Nous remercions le Conseil de recherches en sciences naturelles et en génie du Canada (CRSNG) de son soutien.
