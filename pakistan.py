import streamlit as st
import folium
from streamlit.components.v1 import html

# Define the center of the map (coordinates of Pakistan)
pakistan_coords = [30.3753, 69.3451]

# Create a Folium map centered at Pakistan
m = folium.Map(location=pakistan_coords, zoom_start=6)

# Add a marker for demonstration (e.g., Islamabad)
folium.Marker([33.6844, 73.0479], tooltip="Islamabad").add_to(m)

# Convert the Folium map to HTML and display it in Streamlit
map_html = m._repr_html_()

# Streamlit App Title
st.title("Interactive Map of Pakistan")

# Display the map
st.markdown("This is a simple map of Pakistan with a marker on Islamabad.")

# Render the map in Streamlit
html(map_html, height=100000)
