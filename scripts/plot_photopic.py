import pandas as pd
import matplotlib.pyplot as plt
from soak19 import plot_visible_spectrum

cone_response = pd.read_csv('data/photopic.csv', comment='#', index_col=0)

fig = plt.figure(constrained_layout=True)
ax = fig.add_subplot(1, 1, 1)

plot_visible_spectrum(
    ax=ax,
    height=1.1,
)


ax.plot(cone_response.index.values, cone_response.response, color='w')


ax.set_xlim(390, 700)
ax.set_ylim(0, 1.1)
ax.set_xlabel('Wellenlänge / nm')
ax.set_ylabel('Lichtempfindlichkeit')

fig.savefig('build/plots/photopic.pdf')
