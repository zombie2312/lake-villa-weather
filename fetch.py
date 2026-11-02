"""Copies Open-Meteo's current weather for one place into site/weather.json, the file the world reads.

The world keeps reading the same address for as long as it is published, so the address and the fields
of the JSON must not change. Change the place freely: the next run moves the weather with no re-upload.
"""
import json
import os
import time
import urllib.parse
import urllib.request

LATITUDE = 39.09        # Lake Tahoe
LONGITUDE = -120.04
TRIES = 3


def read():
    query = urllib.parse.urlencode({
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        "current": "weather_code,precipitation",
        "timeformat": "unixtime",
    })
    with urllib.request.urlopen("https://api.open-meteo.com/v1/forecast?" + query, timeout=20) as reply:
        return json.load(reply)["current"]


def main():
    for attempt in range(TRIES):
        try:
            current = read()
            break
        except (OSError, KeyError, ValueError) as error:
            print("Try", attempt + 1, "failed:", error)
            if attempt + 1 == TRIES:
                raise
            time.sleep(20)
    # A bad reading stops the run here, so the last good file stays published.
    feed = {
        "current": {
            "time": int(current["time"]),
            "weather_code": int(current["weather_code"]),
            "precipitation": float(current["precipitation"]),
        },
        "attribution": "Weather data by Open-Meteo.com (CC BY 4.0)",
    }
    os.makedirs("site", exist_ok=True)
    with open("site/weather.json", "w", encoding="ascii") as out:
        json.dump(feed, out, separators=(",", ":"))
    print(feed)


main()
