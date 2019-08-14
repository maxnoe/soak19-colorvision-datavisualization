from soak19 import plot_xyz_gamut, cmf
import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=True)
w, h = fig.get_size_inches()
fig.set_size_inches(h, h)

ax = fig.add_subplot(1, 1, 1)
plot_xyz_gamut(ax=ax)
fig.savefig('build/plots/gamut.pdf')
