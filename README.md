# n2v2-in-google-colab
Noise2Void (N2V) is a deep-learning technique used to denoise images, developed by Krull et. al. in 2019. It is unique from other deep-learning techniques in that it is self-supervised, so sets of high- and low- noise images are not required for training. As such, it lends itself well to use for microscopy images, where multiple high signal-to-noise ratio images are not often feasible.

This particular notebook uses an improved version of N2V, N2V2, developed in 2022. This version eliminates the checkerboard artifacts that often result from N2V, as shown below:

![diagram](https://github.com/gracefacetseng/n2v2-in-google-colab/assets/132942058/8f0d7623-b8ad-4565-b253-5919cc9e0e3c)


For a rundown on N2V2 and a tutorial on how to use this notebook, see [this slideshow.](https://drive.google.com/file/d/1zVN9yAHxPEt3SDd98zo1HEB0rJ1jbWHn/view?usp=drive_link)

## Pretrained Models:

This notebook supports both training your own model and predicting denoised images. If you do not have the data to train a model, you can still use this notebook! I have included some preloaded models trained on specific subjects. You can peruse the selection in the "pretrained models" directory above, and they will be made available to you when you load the notebook. To use one, please follow the instructions in the notebook :) 

I have included the source code used to train the pretrained models, which were trained using Compute Canada's Cedar and Graham clusters. Models were trained using dataset sizes and parameters larger than the notebook version can handle. If you want to train your own models externally, I found that both clusters named work well, with similar performance.  

**Tip:** Models work best on similar-looking data. It may work better to use a model that was trained on images that look like your images, even if the subjects are different. Likewise, you can expect your models to have better performance if your training images are similar to the images you want to denoise.

### Sample Images:
![10533 sample](https://github.com/gracefacetseng/n2v2-in-google-colab/assets/132942058/8d9c82a7-d9b8-413c-b5ce-c6e61f3e930f)
![10870 sample](https://github.com/gracefacetseng/n2v2-in-google-colab/assets/132942058/81712daf-35ed-4bdd-8c77-4c05e93ae54c)
![11449 sample](https://github.com/gracefacetseng/n2v2-in-google-colab/assets/132942058/adf36b62-4084-4557-834e-207c238fbe54)
![mitolab sample](https://github.com/gracefacetseng/n2v2-in-google-colab/assets/132942058/a145e76a-9e09-440e-8610-0d8f19d7aee2)
![11415 sample](https://github.com/gracefacetseng/n2v2-in-google-colab/assets/132942058/255ae64c-e769-4617-917c-fd424fad7fc5)
![11237 sample](https://github.com/gracefacetseng/n2v2-in-google-colab/assets/132942058/ce3ce087-9544-47f7-814f-6ef28e5a4cb3)
![t cell sample](https://github.com/gracefacetseng/n2v2-in-google-colab/assets/132942058/e798355f-2cd8-4869-a0c9-1284675242cb)
![10967 sample](https://github.com/gracefacetseng/n2v2-in-google-colab/assets/132942058/9504adb1-a022-46b7-a800-f5cbb36acb42)

## Acknowledgements:
This notebook was heavily influenced by Noise2Void (2D) by the Zero-Cost Download for Microscopy Project, found here: [Noise2Void_2D_ZeroCostDL4Mic](https://colab.research.google.com/github/HenriquesLab/ZeroCostDL4Mic/blob/master/Colab_notebooks/Noise2Void_2D_ZeroCostDL4Mic.ipynb)


The paper about N2V by Krull et. al.: [Noise2Void - Learning Denoising from Single Noisy Images](https://arxiv.org/abs/1811.10980)

The paper for N2V2: [N2V2 -- Fixing Noise2Void Checkerboard Artifacts with Modified Sampling Strategies and a Tweaked Network Architecture](https://arxiv.org/abs/2211.08512)

Source code for N2V was found here: https://github.com/juglab/n2v

**If you use this notebook in your research, please cite the above papers.**

Pretrained models were trained using images from the following datasets:
 *  alveolar_stem_cells_10533: [EMPIAR-10533](https://www.ebi.ac.uk/empiar/EMPIAR-10533/)
 *  C.reinhardtii_10870: [EMPIAR-10870](https://www.ebi.ac.uk/empiar/EMPIAR-10870/)
 *  mitochondria_11449: [EMPIAR-11449](https://www.ebi.ac.uk/empiar/EMPIAR-11449/)
 *  mitochondria_mitolab: [EMPIAR-11037](https://www.ebi.ac.uk/empiar/EMPIAR-11037/)
 *  mouse_brain_11415: [EMPIAR-11415](https://www.ebi.ac.uk/empiar/EMPIAR-11415/)
 *  mouse_optic_nerve_steyer-mobius: [EMPIAR-11214](https://www.ebi.ac.uk/empiar/EMPIAR-112124/), [EMPIAR-11215](https://www.ebi.ac.uk/empiar/EMPIAR-11215/), [EMPIAR-11216](https://www.ebi.ac.uk/empiar/EMPIAR-11216/), [EMPIAR-11219](https://www.ebi.ac.uk/empiar/EMPIAR-11219/), [EMPIAR-11220](https://www.ebi.ac.uk/empiar/EMPIAR-11220/), [EMPIAR-11237](https://www.ebi.ac.uk/empiar/EMPIAR-11237/), [EMPIAR-11238](https://www.ebi.ac.uk/empiar/EMPIAR-11238/), [EMPIAR-11239](https://www.ebi.ac.uk/empiar/EMPIAR-11239/), [EMPIAR-11240](https://www.ebi.ac.uk/empiar/EMPIAR-11240/)
 *  t-cells_10329: [EMPIAR-10329](https://www.ebi.ac.uk/empiar/EMPIAR-10329/)
 *  villi_10967: [EMPIAR-10967](https://www.ebi.ac.uk/empiar/EMPIAR-10967/)

<img width="368" alt="NSERC_FIP_RGB" src="https://github.com/gracefacetseng/n2v2-in-google-colab/assets/132942058/748f0a73-55dd-4c28-9f5a-20fb03246775">

We acknowledge the support of the Natural Sciences and Engineering Research Council of Canada (NSERC).

Nous remercions le Conseil de recherches en sciences naturelles et en génie du Canada (CRSNG) de son soutien.
