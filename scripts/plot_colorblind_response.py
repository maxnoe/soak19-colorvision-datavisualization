import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/cone_response.csv', comment='#', index_col=0)

fig, axs = plt.subplots(2, 2, constrained_layout=True, sharex=True)

width, height = fig.get_size_inches()
fig.set_size_inches(width, 0.8 * height)

ax = axs[0, 0]
ax.set_title('Deuteranomalie (5 %)')

shift = 0.7 * (df.L.idxmax() - df.M.idxmax())

ax.plot(df.index.values, df.S, color='xkcd:blue')
ax.plot(df.index.values, df.M, ls=':', color='xkcd:green', alpha=0.3)
ax.plot(df.index.values, df.L, color='xkcd:red')
ax.plot(df.index.values + shift, df.M, color='k')
ax.arrow(df.M.idxmax(), 1.05, dx=shift, dy=0, width=0.02, length_includes_head=True, head_length=10, lw=0)


ax = axs[0, 1]
ax.set_title('Deuteranopie (1 %)')

ax.plot(df.index.values, df.S, color='xkcd:blue')
ax.plot(df.index.values, df.M, ls=':', color='xkcd:green', alpha=0.3)
ax.plot(df.index.values, df.L, color='xkcd:red')


ax = axs[1, 1]
ax.set_title('Protanopie (1 %)')

ax.plot(df.index.values, df.S, color='xkcd:blue')
ax.plot(df.index.values, df.L, ls=':', color='xkcd:red', alpha=0.3)
ax.plot(df.index.values, df.M, color='xkcd:green')

ax = axs[1, 0]
ax.set_title('Protanomalie (1 %)')

shift = 0.8 * (df.M.idxmax() - df.L.idxmax())
ax.plot(df.index.values, df.S, color='xkcd:blue')
ax.plot(df.index.values, df.L, ls=':', color='xkcd:red', alpha=0.3)
ax.plot(df.index.values + shift, df.L, color='k')
ax.plot(df.index.values, df.M, color='xkcd:green')
ax.arrow(df.L.idxmax(), 1.05, dx=shift, dy=0, width=0.02, length_includes_head=True, head_length=10, lw=0)


for ax in axs[1]:
    ax.set_xlim(380, 700)
    ax.set_xlabel('Wellenlänge / nm')

for ax in axs.flatten():
    ax.set_ylim(0, 1.1)

for ax in axs.flatten():
    ax.set_yticks([])
    for spine in ('top', 'left', 'right'):
        ax.spines[spine].set_visible(False)

fig.savefig('build/plots/colorblind_response.pdf')
