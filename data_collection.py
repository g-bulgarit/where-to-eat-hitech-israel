import logging
from pathlib import Path

from api import get_nearby_restaurant_data
from geo_structs import PlacesOfInterest as places_of_interest

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)


def collect_data(outputs_dir_path: Path) -> None:
    for place in places_of_interest:
        logging.info(f"Looking for restaurants around workplace: {place.name}")
        nearby_restaurants_json = get_nearby_restaurant_data(latitude=place.latitude, longitude=place.longitude)
        output_file_path = outputs_dir_path / place.to_filename
        output_file_path.write_text(nearby_restaurants_json)

if __name__ == "__main__":
    collect_data(outputs_dir_path=Path("outputs_500m"))
