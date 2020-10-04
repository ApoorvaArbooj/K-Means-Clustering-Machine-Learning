# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 17:43:14 2020

@author: Apoorva Arbooj
"""


import pandas as pd
import numpy as np
import urllib.request

#!conda install -c conda-forge geopy --yes
from geopy.geocoders import Nominatim

#!conda install -c conda-forge folium=0.5.0 --yes
import folium

import requests # library to handle requests
from pandas.io.json import json_normalize # tranform JSON file into a pandas dataframe

# import k-means from clustering stage
from sklearn.cluster import KMeans

# Matplotlib and associated plotting modules
import matplotlib.cm as cm
import matplotlib.colors as colors

CLIENT_ID = '0FENVP43DTETNE4SXYJ43A4MOYXNPEA0FWJMCW35IJIUVLDO' # your Foursquare ID
CLIENT_SECRET = 'THNPS1TLJOITTFKT4IAU0YV3F2PBREOE1L3UUEJOYTPU2GXM' # your Foursquare Secret
VERSION = '20200710'
#LIMIT = 10000
#radius = 1000
print('Your credentails:')
print('CLIENT_ID: ' + CLIENT_ID)
print('CLIENT_SECRET:' + CLIENT_SECRET)

address = 'BOSTON'

geolocator = Nominatim(user_agent="foursquare_agent")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print(latitude, longitude)

#search_query = 'hotels'
radius = 500
url = f'https://api.foursquare.com/v2/venues/search?categoryId=4d4b7105d754a06374d81259&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&ll={latitude},{longitude}&v={VERSION}'

results = requests.get(url).json()
