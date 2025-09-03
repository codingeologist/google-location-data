import pandas as pd
import geopandas as gpd
from datetime import datetime as dt

df1 = pd.read_json('/Takeout/Location History/Location History.json')

#Map latitude, longitude and timestamps into dataframe
df1['latitude'] = df1['locations'].map(lambda x: x ['latitudeE7'])
df1['longitude'] = df1['locations'].map(lambda x: x ['longitudeE7'])
df1['timestamp_ms'] = df1['locations'].map(lambda x: x ['timestampMs'])

#Convert lat-long into decimal degrees and timestamps into datetime
df1['latitude'] = df1['latitude'] / 10.**7
df1['longitude'] = df1['longitude'] / 10.**7
df1['timestamp_ms'] = df1['timestamp_ms'].astype(float) / 1000
df1['datetime'] = df1['timestamp_ms'].map(lambda x: dt.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))

#Drop unused columns from dataframe to save on file size
df1 = df1.drop(labels=['locations', 'timestamp_ms'], axis=1, inplace=False)

#Convert to GeodataFrame and save to file (Co-ordinate system WGS84 EPSG: 4326)
df1 = gpd.GeoDataFrame(df1, geometry=gpd.points_from_xy(df1.longitude, df1.latitude))
df1 = df1.set_crs(epsg=4326, inplace=True)
df1.to_file('/gis-data/locationhistory.gpkg', driver='GPKG')

print('Number of location rows: {:,}'.format(len(df1)))
print(' ')
print(df1.head(5))
