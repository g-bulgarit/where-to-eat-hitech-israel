from dataclasses import dataclass
from pydantic import BaseModel
import numpy as np

@dataclass
class GeoWorkplace:
    name: str
    lat_lang: tuple[float, float]

    @property
    def latitude(self):
        return self.lat_lang[0]

    @property
    def longitude(self):
        return self.lat_lang[1]
    
    @property
    def to_filename(self):
        return f"{self.name.replace(" ", "_")}.json"


class RestaurantDisplayName(BaseModel):
    text: str
    languageCode: str

class RestaurantLocation(BaseModel):
    latitude: float
    longitude: float

class Restaurant(BaseModel):
    displayName: RestaurantDisplayName
    location: RestaurantLocation
    rating: float
    userRatingCount: int
    distance_to_center: float



def haversine_distance(lon1, lat1, lon2, lat2) -> float:
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = np.sin(dlat/2.0)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2.0)**2
    
    c = 2 * np.arcsin(np.sqrt(a))
    km = 6378.137 * c
    return km * 1_000


PlacesOfInterest: list[GeoWorkplace] = [
    GeoWorkplace(name="Bursa (Ramat Gan)", lat_lang=(32.08372862289339, 34.80081000517727)),
    GeoWorkplace(name="Midtown (Tel Aviv)", lat_lang=(32.07727347992267, 34.79361453085333)),
    GeoWorkplace(name="Sarona (Tel Aviv)", lat_lang=(32.07084391171884, 34.78717804432757)),
    GeoWorkplace(name="Azrieli (Tel Aviv)", lat_lang=(32.07415702910825, 34.79219114427281)),
    GeoWorkplace(name="High-Tech Park (Hod HaSharon)", lat_lang=(32.13349175482649, 34.89656687565937)),
    GeoWorkplace(name="Azrieli (Holon)", lat_lang=(32.00794310318063, 34.800661546998136)),
    GeoWorkplace(name="Kiryat Atidim (Tel Aviv)", lat_lang=(32.115192049289625, 34.84301101244939)),
    GeoWorkplace(name="High-Tech Park (Petah Tiqwa)", lat_lang=(32.09978904343739, 34.853179199877346)),
    GeoWorkplace(name="High-Tech Park (Yokne'am)", lat_lang=(32.66521172831295, 35.10517076186598)),
    GeoWorkplace(name="Herzelia Pituach (Herzelia)", lat_lang=(32.159355646198335, 34.80943450895464)),
    GeoWorkplace(name="High-Tech Park (Beer-Sheva)", lat_lang=(31.264113538064862, 34.81397096634936)),
    GeoWorkplace(name="ARM and stuff (Ra'anana)", lat_lang=(31.264113538064862, 34.81397096634936)),
    GeoWorkplace(name="Har Hotzvim (Jerusalem)", lat_lang=(31.80264981740041, 35.210053939767334)),
    GeoWorkplace(name="Technology Park (Jerusalem)", lat_lang=(31.749371820834085, 35.186377074401626)),
    GeoWorkplace(name="Matam (Haifa)", lat_lang=(32.788303906052754, 34.959496219726965)),
    GeoWorkplace(name="Vayyar (Yehud)", lat_lang=(32.027789515091854, 34.897400624082316)),
    GeoWorkplace(name="Airport City (Airpot)", lat_lang=(31.98821816748933, 34.91295163838598)),
]