# -*- coding: utf-8 -*-
"""

"""
import numpy as np
import pandas as pd
import pickle
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space

# Jai Shri Ram
# Jai Shri Ram
st.set_page_config(layout = "wide")

# Talk about nature of dataset (what the dataset is)

def main():
    st.title("Introduction Page")
    
    st.subheader("How is literacy rate measured?")
    st.write("A country's total literacy rate is the percentage of people 15 and above that can both read and write with understanding a short simple sentence about their life.")
    
    add_vertical_space(2)
    
    st.subheader("About the Web Application")
    st.markdown(
        """
        - On the left of the screen, you can locate the Machine Learning Model which was trained on "Youth & Adult Literacy Rates" from Kaggle, and consists of the literacy rates for youth and adults in various regions and countries from 2011-2018. 
        - Predictive Models can provide invaluable insights into making informed policy decisions related to education policies, resource allocation, and interventions.
        - Predictive Models can also be used as part of a monitoring system to track the effectiveness of educational iniatives over time.
        - We can try to predict future growth in literacy rate (ex. 2024). 
        
        
        """
        )
    
    add_vertical_space(2)
    
    st.markdown(
        """
        - On the left side of the screen, you can also locate an interactive map depicting the countries with the lowest literacy rates for individual ages 15+ from recent years.
        - The interactive map is critical for researchers and educators, helping them identify regions for making informed decisions on educational policies.
        """
        )
if __name__ == "__main__":
    main()
# Interactive Map (future implications)

# What the Machine Learning Model will tell you

# Future implications of social good
