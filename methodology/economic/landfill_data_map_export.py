import json
import multiprocessing
from shapely.geometry import Polygon
import pyproj
import warnings
import time
import folium
from folium.plugins import MarkerCluster

def convert_coordinates(ring):
    # Define the EPSG:27700 coordinate system
    crs_27700 = pyproj.CRS.from_epsg(27700)

    # Define the EPSG:4326 coordinate system
    crs_4326 = pyproj.CRS.from_epsg(4326)

    # Create a transformer to convert between coordinate systems
    transformer = pyproj.Transformer.from_crs(crs_27700, crs_4326, always_xy=True)

    # Convert the coordinates to latitude and longitude
    gps_locs = []
    for point in ring:
        lon, lat = transformer.transform(point[0], point[1])
        gps_locs.append((lat, lon))
    
    return gps_locs

def calculate_centroid(gps_points):
    # Create a Shapely polygon object from the coordinates
    poly = Polygon(gps_points)

    # Calculate the centroid of the polygon
    return poly.centroid

def lies_within(gps, lat_north, lat_south, lon_west):
    # Define the EPSG:27700 coordinate system
    crs_27700 = pyproj.CRS.from_epsg(27700)

    # Define the EPSG:4326 coordinate system
    crs_4326 = pyproj.CRS.from_epsg(4326)

    # Create a transformer to convert between coordinate systems
    transformer = pyproj.Transformer.from_crs(crs_27700, crs_4326, always_xy=True)
    lon, lat = transformer.transform(gps[0], gps[1])
    return lat > lat_south and lat < lat_north and lon > lon_west

if __name__ == '__main__':
    # very crude boundaries of the region
    BOUNDARIES_NORTH_LATITUDE =  55.811513
    BOUNDARIES_SOUTH_LATITUDE =  54.342958
    BOUNDARIES_WEST_LONGITUDE =  -2.880627

    start_ts = time.monotonic()
    FILE_PATH = "Historic_Landfill_Sites.json"
    
    # load data
    with open(FILE_PATH, 'r') as fIn:
        data = json.load(fIn)
    
    coords = []
    num_features = len(data['features'])
    for i, feature in enumerate(data['features']):
        print(f"{i}/{num_features} ({len(coords)})")
        for ring in feature['geometry']['rings']:
            # filter on region boundaries
            if lies_within(ring[0], BOUNDARIES_NORTH_LATITUDE, BOUNDARIES_SOUTH_LATITUDE, BOUNDARIES_WEST_LONGITUDE):
                coords.append(ring)

    # Number of processes to create
    num_processes = 8

    # Create a pool of processes
    pool = multiprocessing.Pool(processes=num_processes)

    # Map the worker function to the list of arguments
    results = pool.map(convert_coordinates, coords)

    # Close the pool
    pool.close()

    # Wait for the processes to finish
    pool.join()

    print(f"Took {time.monotonic() - start_ts:.2f} s")

    # map the result
    map = folium.Map(location=(54.973184, -1.624439), zoom_start=9)

    # create a marker cluster with custom parameters
    marker_cluster = MarkerCluster().add_to(map)

    # add all polygons and markers to the map
    for landfill in results:
        folium.Polygon(locations=landfill, 
                        color='None', 
                        fill=True, 
                        fill_color="red", 
                        fill_opacity=0.35
                        ).add_to(map)
        landfill_centroid = calculate_centroid(landfill)

        folium.CircleMarker(
            location=(landfill_centroid.x, landfill_centroid.y),
            color=None,
            fill=False,
        ).add_to(marker_cluster)

    # save the map to a file
    map.save('economic_landfill_map.html')
    print("Done.")