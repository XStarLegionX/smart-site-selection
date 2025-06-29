import geopandas as gpd
import numpy as np

def add_mock_demographics(input_path, output_path):
    wards = gpd.read_file(input_path)
    wards["population_density"] = np.random.randint(10000, 30000, size=len(wards))
    wards["income_level"] = np.random.randint(20000, 100000, size=len(wards))
    wards.to_file(output_path, driver="GeoJSON")
    print(f"Saved with mock demographics: {output_path}")

if __name__ == "__main__":
    add_mock_demographics("data/bangalore_wards.geojson", "data/bangalore_wards_demo.geojson")