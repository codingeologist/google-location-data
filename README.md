# google-location-data
Access personal Google Location History and plot in a GIS software

## download personal Google Maps data

- Open Google Maps on an iOS/Android App.
  - [Web access has been disabled by Google for some reason](https://support.google.com/maps/thread/320977024/google-location-history-not-on-google-takeout-any-more?hl=en).
- Click on your profile icon then `your data in maps`.
- Scroll down to the card titled `Download you Maps data`.
- Follow the steps to export the Google Maps data.
- The data will be saved in a `Location History/Location History.json` file.
- Run the Python script to access the latitudelongitude pairs in the JSON file and create a GeoDataFrame, which can be saved in any spatial formats: ESRI Shapefile, GeoJSON, GeoPackage etc...
- NOTE: depending on the size of the json file, this can take awhile to complete processing!
- Once done, the data can be opened in any GIS software like QGIS, plotted and merged with different polygons such as national and local level boundaries.
