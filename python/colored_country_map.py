# example of reading a shapefile using geopandas from
# https://medium.com/analytics-vidhya/making-colored-country-maps-with-real-data-using-matplotlib-and-geopandas-2d10687ca7ac

import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

map_df = gpd.read_file("../data/nz-police-district-boundaries/nz-police-district-boundaries.shx")

# This is a shapefile of New Zealand Police District Boundaries https://en.wikipedia.org/wiki/Shapefile

# print(map_df)

licenses_df = pd.read_csv("../data/nz_firearm_licenses.csv")

merged_df = map_df.merge(licenses_df, left_on=["DISTRICT_N"], right_on=["Residence District"])
merged_df.plot(column="Licenses", cmap="Blues", legend=True)
plt.title("Firearm Licenses by Police District in New Zealand (July 2021)")
plt.tick_params(
    axis="both",        # affect both the X and Y axes
    which="both",       # get rid of both major and minor ticks
    top=False,          # get rid of ticks on top/bottom/left/right
    bottom=False,
    left=False,
    right=False,
    labeltop=False,     # get rid of labels on top/bottom/left/right
    labelbottom=False,
    labelleft=False,
    labelright=False)
plt.show()
