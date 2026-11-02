# Lake Villa weather

The current weather for one place, published once an hour as a small JSON file for a VRChat world.
VRChat lets every player load strings from `*.github.io`, so this copy reaches players who have Allow
Untrusted URLs off.

- File: `weather.json` on this repository's GitHub Pages site.
- To follow another place, change `LATITUDE` and `LONGITUDE` in `fetch.py`. The next run moves the
  weather, with no re-upload of the world.
- A published world keeps reading the same address, so do not rename this repository or the file, and
  keep the `current.time`, `current.weather_code` and `current.precipitation` fields.

Weather data by [Open-Meteo.com](https://open-meteo.com/), under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The file is an unchanged copy of three
fields of their reply.
