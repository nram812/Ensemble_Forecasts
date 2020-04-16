def make_choropleth(ax, df, var=None, dict_colors=None):
    """
    makes a choropleth map from
    """

    from shapely.geometry import Point, LineString
    import cartopy.crs as ccrs
    from cartopy.feature import ShapelyFeature

    for i, row in df.iterrows():

        v = row.loc[var]

        if v == 'missing':

            color = dict_colors[v]

            geom = row.geometry

            sp = ShapelyFeature([geom], ccrs.PlateCarree(),
                                edgecolor='none',
                                facecolor=color, lw=0)
        else:

            color = dict_colors[v]

            geom = row.geometry

            sp = ShapelyFeature([geom], ccrs.PlateCarree(),
                                edgecolor='k',
                                facecolor=color, lw=0.5)

            ax.add_feature(sp)
