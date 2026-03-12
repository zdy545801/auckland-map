import folium
from flask import Flask

app = Flask(__name__)


def build_map_html() -> str:
    lat = -36.8485
    lon = 174.7633

    # Use tiles that are typically more reachable in mainland China.
    m = folium.Map(location=[lat, lon], zoom_start=11, tiles=None)
    folium.TileLayer(
        tiles="https://webrd0{s}.is.autonavi.com/appmaptile"
        "?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}",
        attr="Amap",
        name="Amap",
        subdomains=["1", "2", "3", "4"],
        max_zoom=18,
    ).add_to(m)
    folium.TileLayer("CartoDB positron", name="CartoDB").add_to(m)

    folium.Marker(
        [lat, lon],
        popup="Auckland",
        tooltip="Auckland",
    ).add_to(m)
    folium.LayerControl().add_to(m)
    return m.get_root().render()


@app.route("/")
def index():
    return build_map_html()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
