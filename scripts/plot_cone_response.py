import pandas as pd
import matplotlib.pyplot as plt
from soak19 import plot_visible_spectrum

cone_response = pd.read_csv('data/cone_response.csv', comment='#', index_col=0)

fig = plt.figure(constrained_layout=True)
ax = fig.add_subplot(1, 1, 1)

plot_visible_spectrum(ax=ax, height=1.1)


for name, column in cone_response.items():
    ax.plot(column.index.values, column.values, color='w')
    wl = column.idxmax()
    ax.annotate(
        name, (wl, 1), xytext=(0, 5), textcoords='offset points', color='w',
        size=14, weight='bold'
    )


ax.set_xlim(390, 700)
ax.set_ylim(0, 1.1)
ax.set_xlabel('Wellenlänge / nm')
ax.set_ylabel('Normierte Zapfenabsorbtion')

fig.savefig('build/plots/cone_response.pdf')
