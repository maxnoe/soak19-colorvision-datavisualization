import xarray
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, DivergingNorm
import numpy as np

dataset = xarray.open_dataset('data/ETOPO1_Ice_g_gdal.grd')
shape = tuple(dataset.dimension.values[::-1])
z = dataset.z.values.reshape(shape)

fig = plt.figure(constrained_layout=True)
ax = fig.add_subplot(1, 1, 1)

img = plt.imshow(
    z,
    cmap='jet',
    extent=[-180, 180, -90, 90]
)
img.set_rasterized(True)

fig.colorbar(img)
fig.savefig('build/plots/worldmap_jet.pdf')


colors_undersea = plt.cm.terrain(np.linspace(0, 0.17, 256))
colors_land = plt.cm.terrain(np.linspace(0.25, 1, 256))
all_colors = np.vstack((colors_undersea, colors_land))
terrain_map = LinearSegmentedColormap.from_list('terrain_map', all_colors)
divnorm = DivergingNorm(vmin=-5e3, vcenter=0, vmax=6000)


fig = plt.figure(constrained_layout=True)
ax = fig.add_subplot(1, 1, 1)

img = plt.imshow(
    z,
    cmap=terrain_map,
    norm=divnorm,
    extent=[-180, 180, -90, 90]
)
img.set_rasterized(True)

fig.colorbar(img)
fig.savefig('build/plots/worldmap_divnorm.pdf')
