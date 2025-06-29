import osmnx as ox
import geopandas as gpd

def get_poi_data(city, tags):
    """
    Fetch POI data from OpenStreetMap for the given city and tags.
    """
    print(f"Downloading POI data for {city}...")
    poi_data = ox.features_from_place(city, tags)
    return poi_data

if __name__ == "__main__":
    city = "Bangalore, India"
    
    # Define POI types of interest
    tags = {
        'amenity': ['cafe', 'restaurant', 'hospital', 'clinic'],
        'shop': True,
        'office': True
   }

    pois = get_poi_data(city, tags)
    pois.to_file("data/bangalore_pois.geojson", driver='GeoJSON')
    print("POI data saved to data/bangalore_pois.geojson")