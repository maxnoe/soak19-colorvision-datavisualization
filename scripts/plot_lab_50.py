import matplotlib.pyplot as plt
import colorspacious
import numpy as np


N = 400
a, b = np.meshgrid(np.linspace(-50, 50, N), np.linspace(-50, 50, N))

for L in (20, 50, 80):
    lab = np.full((N, N, 3), L)
    lab[:, :, 1] = a
    lab[:, :, 2] = b

    rgb = colorspacious.cspace_convert(lab, 'CIELab', 'sRGB1')
    rgb = np.clip(rgb, 0, 1)

    plt.title(f'$L = {L}$')
    plt.imshow(rgb, extent=[-1, 1, -1, 1])
    plt.xlabel('a')
    plt.ylabel('b')
    plt.tight_layout()
    plt.savefig(f'build/plots/lab_{L}.pdf')
