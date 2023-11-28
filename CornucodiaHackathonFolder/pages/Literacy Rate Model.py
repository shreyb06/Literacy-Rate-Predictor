# -*- coding: utf-8 -*-
"""
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
import os
import joblib
from streamlit_extras.no_default_selectbox import selectbox
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.colored_header import colored_header
from streamlit_extras.streaming_write import write
import time

# retrieves the path of the folder
current_directory = os.path.dirname(os.path.realpath(__file__))

# name of the model
model_filename = 'xgb_best_model.pkl'

# file path of the model
model_path = os.path.join(current_directory, model_filename)


trained_model = joblib.load(model_path)
    
def streaming_write():
    word_list = "Predicted Literacy rate is: "
    for word in word_list.split():
        yield word + " "
        time.sleep(0.25)

st.title("Literacy Rate Predictor")

colored_header(
    label = "Input the required values below!",
    description = "Please note that the model may not be 100 percent accurate. Also, the model does not take into different geographical regions within a country, which could potentially affect the literacy rate.",
    color_name = "violet-70"
    )



predict_region = selectbox("Select region", ('Central and Southern Asia', 'Eastern and South-Eastern Asia', 'Europe and Northern America', 'Latin America and the Caribbean', 'Northern Africa and Western Asia', 'Oceania', 'Sub-Saharan Africa'), key = 'region')
add_vertical_space(1)
# Retrieve index if the region is in the dictionary
dict_predict_region = {0 : 'Central and Southern Asia', 1 : 'Eastern and South-Eastern Asia', 2 : 'Europe and Northern America', 3 : 'Latin America and the Caribbean', 4 : 'Northern Africa and Western Asia', 5 : 'Oceania', 6 : 'Sub-Saharan Africa'}

key_list = list(dict_predict_region.keys())
values_list = list(dict_predict_region.values())


predict_region_1 = None

if (predict_region is not None):
    predict_region_1 = values_list.index(predict_region)



select_country = None
if (predict_region == 'Central and Southern Asia'):
    select_country = selectbox('Select country', ('Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Iran (Islamic Republic of)', 'Kazakhstan', 'Kyrgyzstan', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka', 'Tajikistan', 'Turkmenistan', 'Uzbekistan'), key = 'CentralSouthernAsia')
    add_vertical_space(1)
elif (predict_region == 'Eastern and South-Eastern Asia'):
    select_country = selectbox('Select country', ('Brunei Darussalam', 'Cambodia', 'China', 'China, Macao Special Administrative Region', 'Indonesia', "Lao People's Democratic Republic", 'Malaysia', 'Mongolia', 'Myanmar', 'Philippines', 'Singapore', 'Thailand', 'Timor-Leste', 'Vietnam'), key = 'EasternSouthEasternAsia')
    add_vertical_space(1)
elif (predict_region == 'Europe and Northern America'):
    select_country = selectbox('Select country', ('Albania', 'Belarus', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Estonia', 'Greece', 'Hungary', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Montenegro', 'Portugal', 'Republic of Moldova', 'Romania', 'Russian Federation', 'San Marino', 'Serbia', 'Slovenia', 'Spain', 'The former Yugoslav Republic of Macedonia', 'Ukraine'), key = 'EuropeNorthernAmerica')
    add_vertical_space(1)
elif (predict_region == 'Latin America and the Caribbean'):
    select_country = selectbox('Select country', ('Antigua and Barbuda', 'Argentina', 'Aruba', 'Barbados', 'Bolivia (Plurinational State of)', 'Brazil', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominican Republic', 'Ecuador', 'El Salvador', 'Grenada', 'Guadeloupe', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica', 'Martinique', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru', 'Puerto Rico', 'Suriname', 'Trinidad and Tobago', 'Uruguay', 'Venezuela (Bolivarian Republic of)'), key = 'LatinAmericaCarribean')
    add_vertical_space(1)
elif (predict_region == 'Northern Africa and Western Asia'):
    select_country = selectbox('Select country', ('Algeria', 'Armenia', 'Azerbaijan', 'Bahrain', 'Cyprus', 'Egypt', 'Georgia', 'Iraq', 'Jordan', 'Kuwait', 'Lebanon', 'Morocco', 'Oman', 'Palestine', 'Qatar', 'Saudi Arabia', 'Sudan', 'Tunisia', 'Turkey'), key= 'NorthernAfricaWesternAsia')
    add_vertical_space(1)
elif (predict_region == 'Oceania'):
    select_country = selectbox("Select country", ('Fiji', 'Marshall Islands', 'New Caledonia', 'Palau', 'Papua New Guinea', 'Samoa', 'Tonga', 'Vanuatu'), key = "Oceania")
    add_vertical_space(1)
elif(predict_region == 'Sub-Saharan Africa'):
    select_country = selectbox("Select country", ('Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Congo', "Côte d'Ivoire", 'Democratic Republic of the Congo', 'Equatorial Guinea', 'Eritrea', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'South Africa', 'South Sudan', 'Swaziland', 'Togo', 'Uganda', 'United Republic of Tanzania', 'Zambia', 'Zimbabwe'), key = 'Sub-SaharanAfrica')
    add_vertical_space(1)

# List of all countries in the dataset
select_country_list = [
    'Afghanistan', 'Bangladesh', 'Bhutan', 'India', 'Iran (Islamic Republic of)',
    'Kazakhstan', 'Kyrgyzstan', 'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka',
    'Tajikistan', 'Turkmenistan', 'Uzbekistan', 'Brunei Darussalam', 'Cambodia',
    'China', 'China, Macao Special Administrative Region', 'Indonesia',
    "Lao People's Democratic Republic", 'Malaysia', 'Mongolia', 'Myanmar',
    'Philippines', 'Singapore', 'Thailand', 'Timor-Leste', 'Vietnam', 'Albania',
    'Belarus', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Estonia',
    'Greece', 'Hungary', 'Italy', 'Latvia', 'Lithuania', 'Malta', 'Montenegro',
    'Portugal', 'Republic of Moldova', 'Romania', 'Russian Federation',
    'San Marino', 'Serbia', 'Slovenia', 'Spain',
    'The former Yugoslav Republic of Macedonia', 'Ukraine',
    'Antigua and Barbuda', 'Argentina', 'Aruba', 'Barbados',
    'Bolivia (Plurinational State of)', 'Brazil', 'Chile', 'Colombia',
    'Costa Rica', 'Cuba', 'Dominican Republic', 'Ecuador', 'El Salvador',
    'Grenada', 'Guadeloupe', 'Guatemala', 'Guyana', 'Haiti', 'Honduras', 'Jamaica',
    'Martinique', 'Mexico', 'Nicaragua', 'Panama', 'Paraguay', 'Peru',
    'Puerto Rico', 'Suriname', 'Trinidad and Tobago', 'Uruguay',
    'Venezuela (Bolivarian Republic of)', 'Algeria', 'Armenia', 'Azerbaijan',
    'Bahrain', 'Cyprus', 'Egypt', 'Georgia', 'Iraq', 'Jordan', 'Kuwait', 'Lebanon',
    'Morocco', 'Oman', 'Palestine', 'Qatar', 'Saudi Arabia', 'Sudan', 'Tunisia',
    'Turkey', 'Fiji', 'Marshall Islands', 'New Caledonia', 'Palau',
    'Papua New Guinea', 'Samoa', 'Tonga', 'Vanuatu', 'Angola', 'Benin', 'Botswana',
    'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon',
    'Central African Republic', 'Chad', 'Comoros', 'Congo', "Côte d'Ivoire",
    'Democratic Republic of the Congo', 'Equatorial Guinea', 'Eritrea',
    'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya',
    'Lesotho', 'Liberia', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius',
    'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Rwanda', 'Sao Tome and Principe',
    'Senegal', 'Seychelles', 'Sierra Leone', 'South Africa', 'South Sudan',
    'Swaziland', 'Togo', 'Uganda', 'United Republic of Tanzania', 'Zambia',
    'Zimbabwe'
]


select_country_index = None
# Input for the Country
if (select_country is not None):
    select_country_index = select_country_list.index(select_country)  # retrieve index of the country in the list
    



# Input for the Year
select_year = selectbox("Select a year", ("2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"), key = "year")
add_vertical_space(1)

select_year_index = None
select_year_list = ["2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
if select_year is not None:
    select_year_index = select_year_list.index(select_year)




# Input for the Age
select_age = st.number_input("Enter an age between 0 and 120 years", min_value = 0, max_value = 120, step = 1)
add_vertical_space(1)
select_age_index = None

if ((select_age > 15) and (select_age < 25)):
    select_age_index = 1
    
elif ((select_age >= 25) and (select_age <= 64)):
    select_age_index = 2

elif ((select_age >= 65)):
    select_age_index = 3
    



select_biological = selectbox("Select Biological Sex", ("Female", "Male"), key = 'biologicalidentity')
add_vertical_space(1)

if (select_biological == "Female"):
    select_biological_index = 0
else:
    select_biological_index = 1
    




# Literacy Rate Model Prediction

def predict_literacy_rate(user_input):
    user_input = list(user_input)
    user_input = [user_input]
    
    prediction_value = trained_model.predict(user_input)
    
    return prediction_value
    

final_predicted_value = predict_literacy_rate((predict_region_1, select_country_index, select_year_index, select_age_index, select_biological_index))


with stylable_container(
    key="red_button",
    css_styles="""
        button {
            background-color: red;
            color: white;
            border-radius: 20px;
        }
        """,
):
        prediction_button = st.button("Predict Literacy Rate")
# if the user presses the button in the Streamlit App

if (prediction_button):
    if (not predict_region or not select_country or not select_year or not select_age or not select_biological):
        st.warning("Please fill out all the information!")
    else:
        if (final_predicted_value >= 1): 
            st.success(str(99.00) + "%")
            
        else:
            final_predicted_percent = np.round(final_predicted_value * 100, 2)
            
            write(streaming_write())
            time.sleep(0.2)
            
            st.success(str(final_predicted_percent[0]) + "%")


