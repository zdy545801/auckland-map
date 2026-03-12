import folium

# Auckland coordinates
lat = -36.8485
lon = 174.7633

m = folium.Map(location=[lat, lon], zoom_start=11)

folium.Marker(
    [lat, lon],
    popup="Auckland",
    tooltip="Auckland"
).add_to(m)

m.save("auckland_map.html")