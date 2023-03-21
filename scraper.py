from geopy.geocoders import Nominatim
from geopy import distance
import numpy as np
import math
import pandas as pd

geolocator = Nominatim(user_agent="GetDistance")
cities = ['Jakarta','Surabaya','Bogor','Tanjung Pinang']
distancesMatrix = np.zeros((len(cities),len(cities)))


for x in range(len(cities)):
  for y in range(len(cities)):
    place1 = geolocator.geocode(cities[x])
    place2 = geolocator.geocode(cities[y])

    lat1, lon1 = (place1.latitude), (place1.longitude)
    lat2, lon2 = (place2.latitude), (place2.longitude)

    loc1 = (lat1, lon1)
    loc2 = (lat2, lon2)
    
    distancesMatrix[x][y] = int(math.ceil(distance.distance(loc1, loc2).km))
    
df = pd.DataFrame(distancesMatrix, columns = cities, index = cities)

df.to_csv("distance_matrix.csv")
    
