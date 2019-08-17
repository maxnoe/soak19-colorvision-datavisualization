import matplotlib.pyplot as plt
import numpy as np

gradient = np.linspace(0, 1, 256).reshape(1, 256)

w, h = plt.rcParams['figure.figsize']
fig, axs = plt.subplots(5, 2, figsize=(w, 0.3333 * w), constrained_layout=True)

uniform = ['viridis', 'plasma', 'magma', 'inferno', 'cividis']
other = ['gray', 'gist_heat', 'jet', 'Blues', 'Reds']


for i, cmaps in enumerate([uniform, other]):

    for ax, cmap in zip(axs[:, i], cmaps):

        img = ax.imshow(gradient, cmap=cmap)
        img.set_rasterized(True)

        ax.set_aspect('auto')
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_ylabel(cmap, rotation=0, ha='right')

axs[0, 0].set_title('Perceptually uniform')
axs[0, 1].set_title('Andere')

fig.savefig('build/plots/sequential.pdf', dpi=300)
