import matplotlib.pyplot as plt
import numpy as np

gradient = np.linspace(0, 1, 256).reshape(1, 256)

w, h = plt.rcParams['figure.figsize']
fig, axs = plt.subplots(4, 1, figsize=(0.4 * w, 0.3 * w), constrained_layout=True)

cmaps = ['coolwarm', 'RdBu', 'seismic', 'bwr']

for ax, cmap in zip(axs, cmaps):
    img = ax.imshow(gradient, cmap=cmap)
    img.set_rasterized(True)

    ax.set_aspect('auto')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylabel(cmap, rotation=0, ha='right', va='center')


fig.savefig('build/plots/diverging.pdf', dpi=300)
