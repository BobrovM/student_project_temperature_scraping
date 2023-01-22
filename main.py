import streamlit as st
import plotly.express as px
import pandas as pd


df = pd.read_csv("data.txt")

line = px.line(x=df["datetime"], y=df["temperature"],
               labels={"x": "Datetime", "y": "Temperature (C)"})

st.plotly_chart(line)
