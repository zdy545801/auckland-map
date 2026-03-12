import folium
from flask import Flask

app = Flask(__name__)


def build_map_html() -> str:
    lat = -36.8485
    lon = 174.7633

    m = folium.Map(location=[lat, lon], zoom_start=11)
    folium.Marker(
        [lat, lon],
        popup="Auckland",
        tooltip="Auckland",
    ).add_to(m)
    return m.get_root().render()


@app.route("/")
def index():
    return build_map_html()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
