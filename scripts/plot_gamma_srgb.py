import matplotlib.pyplot as plt
import numpy as np


def gamma_srgb(value):
    return np.where(
        value < 0.04045,
        value / 12.92,
        ((value + 0.055) / 1.055)**2.4
    )


vals = np.linspace(0, 1, 100)

fig, ax = plt.subplots(figsize=(2, 2))
ax.plot(vals, gamma_srgb(vals))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
fig.tight_layout()
fig.savefig('build/plots/gamma_srgb.pdf')
