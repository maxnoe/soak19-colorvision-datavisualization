import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
from soak19 import wl_to_rgb
import pandas as pd


cone = pd.read_csv('data/cone_response_5nm.csv', index_col=0, comment='#')
fig, axs = plt.subplots(1, 3)
_, h = fig.get_size_inches()
fig.set_size_inches(h, h)

for ax, (name, c) in zip(axs[::-1], cone.items()):
    ax.set_axis_off()

    wl = c.index.values
    ax.barh(wl, width=10**c.values, height=5, color=wl_to_rgb(wl))
    ax.set_title(name)
    ax.set_ylim(700, 390)

fig.tight_layout()
fig.savefig(f'build/plots/cone_response_matrix.pdf')
