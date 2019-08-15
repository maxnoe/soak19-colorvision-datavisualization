import xarray
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, DivergingNorm
import numpy as np

dataset = xarray.open_dataset('data/ETOPO1_Ice_g_gdal.grd')
shape = tuple(dataset.dimension.values[::-1])
z = dataset.z.values.reshape(shape)

lon1 = -22
lon2 = 45
lat1 = 30
lat2 = 75

idx2 = int(-lat1 / 180 * shape[0]) + shape[0] // 2
idx1 = int(-lat2 / 180 * shape[0]) + shape[0] // 2
idx3 = int(lon1 / 360 * shape[1]) + shape[1] // 2
idx4 = int(lon2 / 360 * shape[1]) + shape[1] // 2

print(idx1, idx2, idx3, idx4)


z = z[idx1:idx2, idx3:idx4]
print(z.min(), z.max())

fig = plt.figure(constrained_layout=True)
ax = fig.add_subplot(1, 1, 1)
ax.set_axis_off()

img = plt.imshow(
    z,
    cmap='jet',
    vmin=-5e3,
    vmax=5e3,
    # extent=[-180, 180, -90, 90]
)
img.set_rasterized(True)

fig.colorbar(img)
fig.savefig('build/plots/europe_jet.pdf')


colors_undersea = plt.cm.terrain(np.linspace(0, 0.17, 256))
colors_land = plt.cm.terrain(np.linspace(0.25, 1, 256))
all_colors = np.vstack((colors_undersea, colors_land))
terrain_map = LinearSegmentedColormap.from_list('terrain_map', all_colors)
divnorm = DivergingNorm(vmin=-5e3, vcenter=0, vmax=5e3)


fig = plt.figure(constrained_layout=True)
ax = fig.add_subplot(1, 1, 1)
ax.set_axis_off()

img = plt.imshow(
    z,
    cmap=terrain_map,
    norm=divnorm,
    # extent=[-180, 180, -90, 90]
)
img.set_rasterized(True)

fig.colorbar(img)
fig.savefig('build/plots/europe_divnorm.pdf')
