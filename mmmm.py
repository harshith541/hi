from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
map=Basemap(projection='merc', llcrnrlat=-60, urcrnrlat=80,
llcrnrlon=-180, urcrnrlon=180, resolution='c')
map.drawcoastlines()
map.drawcountries()
map.drawmapboundary(fill_color='lightblue')
map.fillcontinents(color='lightgreen', lake_color='lightblue')
plt.title("World Map using Basemap")
plt.show()
21
Python Programming — Unit IV
Important Note