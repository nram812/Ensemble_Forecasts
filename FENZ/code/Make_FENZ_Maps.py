import os
import sys
import pathlib

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

import geopandas as gpd

import cartopy.crs as ccrs
from cartopy.feature import ShapelyFeature
import cartopy.io.shapereader as shpreader


# ### loads the local functions

sys.path.append(str(pathlib.Path.cwd().parent))

from lib import *

# ### defines the path to the shapefiles 

shapes_path = pathlib.Path.cwd().parents[1] /'FENZ'/'data'/ 'shapes' / 'NZ_Regions' 

# ### build dictionnary with level: colors for mapping of rainfall forecasts 

outlook_rgb = [[255, 244, 65], [255, 159, 65], [255, 59, 65], [255,255,255]]

outlook_rgb = [rgb2hex(*x) for x in outlook_rgb]

outlook_rgb = dict(zip(['low', 'medium', 'high', 'missing'], outlook_rgb))


# ### set crs here 

# **NOTE**: potential problems with the Mercator projection might be due to the version of `proj4` that is used

# In[18]:


extent = [166, 179, -47.5, -34.1]

crs = ccrs.Mercator(latitude_true_scale=-40., min_latitude=extent[-2], max_latitude=extent[-1])

# ### read the shapefile with the ICU EEZ geometries

shape_gpd = gpd.read_file(shapes_path / 'svr.shp')

shape_gpd = shape_gpd.loc[:,['REGC2018_1','geometry']]

shape_gpd = shape_gpd.drop(16, axis=0)

# ### reads the table containing the rainfall forecasts 

# ### do not forget to set the climatological forecasts to -666 in the below CSV BEFORE loading it in this notebook

table = pd.read_csv(pathlib.Path.cwd().parents[1] /'FENZ'/ 'FENZ_Outlook.csv', index_col=0)

table = table.dropna()

shape_gpd_m = shape_gpd.merge(table, on='REGC2018_1')

shape_gpd_m = shape_gpd_m.replace({'none':'missing'})


f, axes = plt.subplots(ncols=7, figsize=(14, 5), subplot_kw=dict(projection=crs))
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0,)

f.subplots_adjust(wspace=0)


for i, day in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']): 
    
    ax = axes[i]
    
    make_choropleth(ax, shape_gpd_m, var=day, dict_colors=outlook_rgb)

    draw_Pacific(ax, extent = extent)
        
    transform = ccrs.PlateCarree()._as_mpl_transform(ax)
    
    ax.set_extent(extent, crs=ccrs.PlateCarree())
    
    ax.set_title(day)
    ax.outline_patch.set_visible(False)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

f.savefig('../figures/map.png', bbox_inches='tight', dpi=200)

plt.close(f)



