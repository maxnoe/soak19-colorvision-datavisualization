import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from soak19 import wl_to_rgb
from scipy.constants import h, k, c


def planck(wl, T):
    f = 2 * h * c**2 / wl**5
    return f * 1 / (np.exp(h * c / (wl * k * T)) - 1)


wl = np.arange(380, 701, 5)

p1 = norm.pdf(wl, 620, 20)
p1 /= np.max(1)
p2 = np.zeros(len(wl))
p2[len(wl) * (540 - wl.min()) // (wl.max() - wl.min())] = 1

p3 = planck(wl * 1e-9, 3200)
p3 /= p3.max()


for i, power in enumerate([p1, p2, p3]):

    fig = plt.figure()
    w, _ = fig.get_size_inches()
    fig.set_size_inches(w, w / 4)

    ax = fig.add_subplot(1, 1, 1)
    ax.set_axis_off()
    ax.bar(wl, width=5, height=power, color=wl_to_rgb(wl), align='edge')
    fig.tight_layout()
    fig.savefig(f'build/plots/spectrum{i}.pdf')
