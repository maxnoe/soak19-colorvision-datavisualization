from soak19 import plot_xyz_gamut
import matplotlib.pyplot as plt

fig = plt.figure(constrained_layout=True)
w, h = fig.get_size_inches()
fig.set_size_inches(0.85 * h, h)

ax = fig.add_subplot(1, 1, 1)
ax.set_xlim(0, 0.85)
ax.set_xlabel('x')
ax.set_ylabel('y')
plot_xyz_gamut(ax=ax)
fig.savefig('build/plots/gamut.pdf')
