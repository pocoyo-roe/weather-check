#!/usr/bin/env python3
"""Fetch the 7-day Open-Meteo weather and marine forecast for North Landing
and write forecast.json next to index.html. The page loads that file on open.

Usage: python3 scripts/refresh_forecast.py
Then republish the planner with forecast.json as a supporting file.
"""
import datetime
import json
import pathlib
import urllib.request

LAT, LON = 54.1285, -0.1005
COMMON = f"latitude={LAT}&longitude={LON}&timezone=Europe%2FLondon&forecast_days=7"
WEATHER = (
    "https://api.open-meteo.com/v1/forecast?" + COMMON
    + "&hourly=temperature_2m,precipitation,weather_code,wind_speed_10m,"
    "wind_direction_10m,wind_gusts_10m&wind_speed_unit=mph"
)
MARINE = (
    "https://marine-api.open-meteo.com/v1/marine?" + COMMON
    + "&hourly=wave_height,wave_direction,wave_period,swell_wave_height,"
    "swell_wave_direction,sea_level_height_msl&cell_selection=sea"
)


def get(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


def main():
    out = {
        "fetchedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "weather": get(WEATHER),
        "marine": get(MARINE),
    }
    path = pathlib.Path(__file__).resolve().parent.parent / "forecast.json"
    path.write_text(json.dumps(out, separators=(",", ":")))
    print(f"Wrote {path} ({len(out['weather']['hourly']['time'])} hours)")


if __name__ == "__main__":
    main()
