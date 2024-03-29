import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
from matplotlib import image

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

st.title("Dashboard - Titanic Data")

img = image.imread(IMAGE_PATH)
st.image(img)


df = pd.read_csv(DATA_PATH)
st.dataframe(df)

# Count Plot to Compare the Male vs Females on the Titanic
st.subheader("Value Counts based on Sex")
st.bar_chart(df['sex'].value_counts())

# Count Plot to Compare the Passenger Class on the Titanic
st.subheader("Value Counts based on Passenger Class")
st.bar_chart(df['pclass'].value_counts())