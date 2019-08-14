import matplotlib.pyplot as plt
import colorspacious
import numpy as np
import pandas as pd
from matplotlib.patches import PathPatch

cmf = pd.read_csv('data/ciexyz06.csv', comment='#', index_col=0)
XYZ = cmf.values
cmf['x'] = XYZ[:, 0] / XYZ.sum(axis=1)
cmf['y'] = XYZ[:, 1] / XYZ.sum(axis=1)


def plot_visible_spectrum(ax=None, wl_min=390, wl_max=700, height=1):
    if ax is None:
        ax = plt.gca()

    wl = cmf[wl_min:wl_max].index.values
    xyz = cmf.loc[wl_min:wl_max, ['X', 'Y', 'Z']].values

    rgb = colorspacious.cspace_convert(xyz / 2, 'XYZ1', 'sRGB1')
    rgb = np.clip(rgb, 0, 1)
    return ax.bar(wl, height=height, color=rgb, width=np.diff(wl)[0], lw=0)


def plot_xyz_gamut(ax=None, color='k', wavelengths=True):
    if ax is None:
        ax = plt.gca()

    x = cmf.loc[380:700, 'x'].values
    y = cmf.loc[380:700, 'y'].values
    x = np.append(x, x[0])
    y = np.append(y, y[0])

    line, = ax.plot(x, y, color=color)

    px = py = np.linspace(0, 1, 300)
    x, y = np.meshgrid(px, py)

    xyY = np.empty((len(px), len(px), 3))
    xyY[:, :, 0] = x
    xyY[:, :, 1] = y
    xyY[:, :, 2] = 0.4

    rgb = colorspacious.cspace_convert(xyY, 'xyY1', 'sRGB1')
    rgb = np.clip(rgb, 0, 1)

    im = ax.imshow(rgb[::-1], extent=[0, 1, 0, 1])
    patch = PathPatch(line.get_path(), transform=ax.transData)
    im.set_clip_path(patch)

    if wavelengths:
        wls = np.arange(460, 640, 20)
        for wl in wls:
            x = cmf.loc[wl, 'x']
            y = cmf.loc[wl, 'y']
            ax.plot(x, y, 'k.')

            ax.annotate(
                str(wl) + ' nm',
                xy=(x, y),
                xytext=(2, 2),
                textcoords='offset points',
                rotation=0 if wl != 460 else 30,
            )
