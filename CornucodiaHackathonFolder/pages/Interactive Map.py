# -*- coding: utf-8 -*-
"""
"""


import numpy as np
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium
from streamlit_extras.colored_header import colored_header


map_center = [0,0]

colored_header(
    label = "Map of the 15 countries with the lowest literacy rates in the dataset from 2011-2018." ,
    description = "Click on the popups for details on each country's literacy rate!",
    color_name = "violet-70"
    )


# st.header("Map of the 15 countries with the lowest literacy rates in the dataset from 2011-2018.")


my_map = folium.Map(location = map_center, zoom_start = 3, scrollWheelZoom = False)


arr1 = ["Guinea", "Chad","Afghanistan","Mali","Benin","Niger","Central African Republic","Sierra Leone","Burkina Faso","South Sudan", "Cote d'Ivoire","Guinea-Bissau","Gambia","Senegal","Liberia"]
arr2 = [(9.9456, -9.6966),(15.4542, 18.7322),(33.9391, 67.7100), (17.5707, -3.9962), (9.3077, -2.3158),(17.6078, 8.0817), (6.6111, 20.9394), (8.4606, -11.7799),(12.2383, -1.5616), (6.8770, 31.3070), (7.5400, -5.5471),(11.8037, -15.1804), (13.4432, -15.3101), (14.4974, -14.4524),(6.4281, -9.4295) ]
arr3 = [
    {"rate": 45.22, "year": 2021},
    {"rate": 26.76, "year": 2021},
    {"rate": 37.3, "year": 2021},
    {"rate": 30.76, "year": 2020},
    {"rate": 45.84, "year": 2021},
    {"rate": 37.34, "year": 2021},
    {"rate": 37.24, "year": None},
    {"rate": 47.70, "year": 2021},
    {"rate": 46.04, "year": 2021},
    {"rate": 34.52, "year": 2018},
    {"rate": 47.16, "year": 2018},
    {"rate": 52.89, "year": 2021},
    {"rate": 58.1, "year": 2021},
    {"rate": 56.30, "year": 2021},
    {"rate": 48.3, "year": 2022}
    ]


for country, coordinates, literacy_rate in zip(arr1, arr2, arr3):
    folium.Marker(coordinates, popup = f" {country} total literacy rate in {literacy_rate['year']}: {literacy_rate['rate']}%").add_to(my_map)
                  

folium_static(my_map, width = 800)
