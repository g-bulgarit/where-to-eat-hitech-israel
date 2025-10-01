import os
import requests
import json

from geo_structs import haversine_distance

API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
DEFAULT_SERACH_RADIUS_M = 500
DEFAULT_MAX_RESULTS = 20
DEFAULT_JSON_INDENT = 4

if not API_KEY:
    raise RuntimeError("Set the env var to continue")

def get_nearby_restaurant_data(
    latitude: float, longitude: float, radius_m=DEFAULT_SERACH_RADIUS_M
) -> str:
    url = "https://places.googleapis.com/v1/places:searchNearby"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": API_KEY,
        # specify which fields to return to reduce quota usage
        "X-Goog-FieldMask": "places.displayName,places.rating,places.userRatingCount,places.location",
    }

    body = {
        "includedTypes": ["restaurant"],
        "maxResultCount": DEFAULT_MAX_RESULTS,
        "rankPreference": "POPULARITY",
        "locationRestriction": {
            "circle": {
                "center": {"latitude": latitude, "longitude": longitude},
                "radius": radius_m,
            }
        },
    }

    resp = requests.post(url, headers=headers, json=body)
    resp.raise_for_status()

    response_places = resp.json().get("places")
    places_with_ratings = [p for p in response_places if p.get("rating") is not None]
    for place in places_with_ratings:
        place["distance_to_center"] = haversine_distance(longitude, 
                                                         latitude, 
                                                         place.get("location").get("longitude"), 
                                                         place.get("location").get("latitude"))
    return json.dumps(places_with_ratings, indent=DEFAULT_JSON_INDENT)
