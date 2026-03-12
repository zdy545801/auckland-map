import folium

# Auckland coordinates
lat = -36.8485
lon = 174.7633

# Create map
m = folium.Map(
    location=[lat, lon],
    zoom_start=11
)

# Add marker
folium.Marker(
    [lat, lon],
    popup="Auckland, New Zealand",
    tooltip="Click me!"
).add_to(m)

# Save map
m.save("auckland_map.html")

print("Map created: auckland_map.html")