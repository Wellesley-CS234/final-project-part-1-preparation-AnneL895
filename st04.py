# This app was written by Geemini Flass2.5, on Nov 7, 2025.
# It was the response of this prompt:

"""
create a simple streamlit that does the following:
- uses the titanic dataset
- on the sidebar it has a menu of five different exploratory analysis that it can do with the dataset
- whenever one clicks a menu item, we see the analysis on the main page
- the main page should have some widget that allow for some control over the graphs, such as dropdown for choosing values, or something else
Do not write complex code, keep it simple.
"""

import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime
from datetime import time
import plotly.express as px
import json

st.header("Exploring Pageviews by Language")

st.write("Select a language to see the pagviews for wikipedia articles in that language")
st.write("Click multiple languages to compare data")

df = pd.read_csv('st04_data.csv')


#finding all the unique languages
langs = df["langCode"].unique()

#letting users interact with them and pick which ones to display
selected_lang = st.multiselect(
    "Pick a language to focus on",
    options = langs,
)

#filtering the data frame based on the selected languages
langdf = df[df["langCode"].isin(selected_lang)]

fig = px.line(
    langdf,
    x="Date",
    y="pageviews",
    color="langCode",
    markers=True,
    title="Pageviews by Language"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Pageviews",
    legend_title="Language"
)

st.plotly_chart(fig, use_container_width=True)

bottom25 = ["Lingua Franca Nova", "Gorontalo", "Low German", "Romansh", "Lojban", 
            "Central Tibetan", "Pontic Greek", "Kabiye", "Ripuarian", "Zeelandic", 
            "Moksha", "Doteli", "Alemannic German", "Norman", "Lezgian", "Inuktitut", 
            "Pali", "Jamaican Patois", "Tok Pisin", "Kalmyk Oirat", "Cherokee", "Navajo", "Xhosa"]


langdf2 = df[df["langCode"].isin(bottom25)]

fig = px.line(
    langdf2,
    x="Date",
    y="pageviews",
    color="langCode",
    markers=True,
    title="Pageviews for the Bottom 25 Languages"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Pageviews",
    legend_title="Language"
)

st.plotly_chart(fig, use_container_width=True)