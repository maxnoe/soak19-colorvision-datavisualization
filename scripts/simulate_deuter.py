from skimage.io import imread, imsave
from skimage import img_as_ubyte, img_as_float
from colorspacious import cspace_convert
import numpy as np

img = img_as_float(imread('images/feuerwerk.jpg'))

for severity in [50, 100]:
    cvd_space = {
        "name": "sRGB1+CVD",
        "cvd_type": "deuteranomaly",
        "severity": severity,
    }

    img_deuter = cspace_convert(img, cvd_space, 'sRGB1')
    img_deuter = img_as_ubyte(np.clip(img_deuter, 0, 1))
    imsave(f'build/plots/fireworks_deuter_{severity}.jpg', img_deuter)
