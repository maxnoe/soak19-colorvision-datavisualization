import matplotlib.pyplot as plt
import colorspacious
import numpy as np


N = 1200
a, b = np.meshgrid(np.linspace(-100, 100, N), np.linspace(-100, 100, N))

for L in (20, 50, 80):
    lab = np.full((N, N, 3), L)
    lab[:, :, 1] = a
    lab[:, :, 2] = b

    rgb = colorspacious.cspace_convert(lab, 'CIELab', 'sRGB1')
    # rgb = np.clip(rgb, 0, 1)
    rgb[np.any((rgb < 0) | (rgb > 1), axis=-1)] = 0

    w, h = plt.rcParams['figure.figsize']
    fig = plt.figure(figsize=(h, h))

    ax = fig.add_subplot(1, 1, 1)
    img = plt.imshow(rgb[::-1], extent=[-100, 100, -100, 100])
    img.set_rasterized(True)

    ax.set_title(f'$L* = {L}$')
    ax.set_xlabel('a*')
    ax.set_ylabel('b*')

    fig.tight_layout()
    fig.savefig(f'build/plots/lab_{L}.pdf')
