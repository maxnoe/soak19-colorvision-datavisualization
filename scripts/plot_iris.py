from sklearn.datasets import load_iris
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

iris = load_iris()

n_classes = len(iris.target_names)

cmap = ListedColormap([f'C{i}' for i in range(n_classes)])

w, h = plt.rcParams['figure.figsize']
plt.figure(figsize=(w, h / 2))

plt.scatter(
    iris.data[:, 0], iris.data[:, 1],
    c=iris.target,
    cmap=cmap,
    vmin=-0.5,
    vmax=n_classes - 0.5,
    s=10,
)

bar = plt.colorbar(label='Klasse')
bar.set_ticks(np.arange(n_classes))
bar.set_ticklabels(iris.target_names)

plt.xlabel(r'$\text{Kelchblattlänge} \mathbin{/} \si{\centi\meter}$')
plt.ylabel(r'$\text{Kelchblattbreite} \mathbin{/} \si{\centi\meter}$')

plt.title('Iris Blumen')
plt.tight_layout()
plt.savefig('build/plots/iris.pdf')
