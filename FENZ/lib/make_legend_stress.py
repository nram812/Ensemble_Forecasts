def make_legend_stress(ax, facecolors=None, title = 'Potential water stress', subtitle = None, fontsize=9):

    from matplotlib.patches import Rectangle

    xt = 0.75

    ax.text(xt, 0.95, title, fontsize=13, transform=ax.transAxes)
    ax.text(xt, 0.915, subtitle, fontsize=11, transform=ax.transAxes)

    ax.add_patch(Rectangle([xt, 0.85], 0.04, 0.04, facecolor=facecolors[-3], edgecolor='0.8', transform=ax.transAxes))
    ax.add_patch(Rectangle([xt, 0.8], 0.04, 0.04, facecolor=facecolors[-2], edgecolor='0.8', transform=ax.transAxes))
    ax.add_patch(Rectangle([xt, 0.75], 0.04, 0.04, facecolor=facecolors[-1], edgecolor='0.8', transform=ax.transAxes))
    ax.add_patch(Rectangle([xt, 0.7], 0.04, 0.04, facecolor=facecolors[0], edgecolor='0.8', transform=ax.transAxes))
    ax.add_patch(Rectangle([xt, 0.65], 0.04, 0.04, facecolor=facecolors[1], edgecolor='0.8', transform=ax.transAxes))
    ax.add_patch(Rectangle([xt, 0.6], 0.04, 0.04, facecolor=facecolors[2], edgecolor='0.8', transform=ax.transAxes))
    ax.add_patch(Rectangle([xt, 0.55], 0.04, 0.04, facecolor=facecolors[3], edgecolor='0.8', transform=ax.transAxes))
    # ax.add_patch(Rectangle([xt, 0.5], 0.04, 0.04, facecolor='w', edgecolor='0.8', transform=ax.transAxes, hatch='//'))

    toffset_x = 0.05
    toffset_y = 0.015

    ax.text(xt + toffset_x, 0.80 + toffset_y, 'Potential high water stress\n(below normal rainfall)', transform=ax.transAxes, fontsize=9)
    ax.text(xt + toffset_x, 0.55 + toffset_y, 'Potential low water stress\n(above normal rainfall)', transform=ax.transAxes, fontsize=9)
    ax.text(xt + toffset_x, 0.7 + toffset_y, 'Normal', transform=ax.transAxes, fontsize=9)
    # ax.text(xt + toffset_x, 0.5 + toffset_y, 'Non-ICU participant', transform=ax.transAxes, fontsize=9)