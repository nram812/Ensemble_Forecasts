def draw_NZ(ax, extent = [125, -120, -32, 25], facecolor='0.9', edgecolor='0.6'):
    """
    draws a blank map of the Pacific, 
    note that `ax` needs to be a cartopy subclass of matplotlib axes, i.e. define first 
    
    ```
    extent = [120, -120, -45., 30]
    crs = ccrs.Mercator(central_longitude=180., latitude_true_scale=0., min_latitude=extent[-2], max_latitude=extent[-1])
    f, ax = plt.subplots(figsize=(10, 8), subplot_kw=dict(projection=crs))
    ```
    """
    
    import cartopy.feature as cfeature
    land_10m = cfeature.NaturalEarthFeature('physical', 'land', '10m',
                                        edgecolor='0.1',
                                        facecolor='0.0', alpha=0.0, linewidth=0.2)
    ax.set_extent(extent)
    ax.add_feature(land_10m)
