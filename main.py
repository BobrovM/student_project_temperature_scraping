import streamlit as st
import plotly.express as px
import psycopg2 as pg


connection = pg.connect("dbname=temp_scrape user=postgres password=4531")
cursor = connection.cursor()
cursor.execute("SELECT * FROM temperatures")
data = cursor.fetchall()
cursor.close()
connection.close()


print(data)

timestamps = []
tempers = []

for value in data:
    timestamps.append(value[0])
    tempers.append(value[1])


line = px.line(x=timestamps, y=tempers,
               labels={"x": "Datetime", "y": "Temperature (C)"})

st.plotly_chart(line)
