def make_legend_outlook(ax, facecolors=None, title = 'ICU Rainfall forecast', subtitle = None, fontsize=9):

    from matplotlib.patches import Rectangle

    #     xt = 0.75
    xt = 0.74


    ax.text(xt, 0.95, title, fontsize=13, transform=ax.transAxes)
    ax.text(xt, 0.915, subtitle, fontsize=11, transform=ax.transAxes)

    ax.add_patch(Rectangle([xt, 0.85], 0.04, 0.04, facecolor=facecolors[-5], edgecolor='0.8', transform=ax.transAxes))
    ax.add_patch(Rectangle([xt, 0.8], 0.04, 0.04, facecolor=facecolors[-3], edgecolor='0.8', transform=ax.transAxes))
    ax.add_patch(Rectangle([xt, 0.75], 0.04, 0.04, facecolor=facecolors[0], edgecolor='0.8', transform=ax.transAxes))
    ax.add_patch(Rectangle([xt, 0.7], 0.04, 0.04, facecolor=facecolors[2], edgecolor='0.8', transform=ax.transAxes))
    ax.add_patch(Rectangle([xt, 0.65], 0.04, 0.04, facecolor=facecolors[4], edgecolor='0.8', transform=ax.transAxes))
    ax.add_patch(Rectangle([xt, 0.58], 0.04, 0.04, facecolor=facecolors[-666], edgecolor='0.8', transform=ax.transAxes))

    toffset_x = 0.05
    toffset_y = 0.015

    ax.text(xt + toffset_x, 0.85 + toffset_y, 'Below', transform=ax.transAxes, fontsize=9)
    ax.text(xt + toffset_x, 0.8 + toffset_y, 'Normal or below', transform=ax.transAxes, fontsize=9)
    ax.text(xt + toffset_x, 0.75 + toffset_y, 'Near normal', transform=ax.transAxes, fontsize=9)
    ax.text(xt + toffset_x, 0.7 + toffset_y, 'Normal or above', transform=ax.transAxes, fontsize=9)
    ax.text(xt + toffset_x, 0.65 + toffset_y, 'Above', transform=ax.transAxes, fontsize=9)

    ax.text(xt + toffset_x, 0.58 + toffset_y, 'No clear guidance', transform=ax.transAxes, fontsize=9)
