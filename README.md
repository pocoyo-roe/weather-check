# North Landing Opening Planner

A one-page planner for deciding when to open a beach business at North Landing,
Flamborough. It scores every daylight hour for the coming week on:

- **Waves into the cove**: wave height × how directly the waves point into the
  north-facing mouth of the cove.
- **Onshore wind**: wind speed × the same exposure, plus strong gusts from any
  direction.
- **Tide plus waves**: modelled sea level above mean sea level, plus half the
  effective wave height as a run-up allowance.
- **Rain**.

Sunrise and sunset are calculated in the page. Wind, waves and tide come from
the free [Open-Meteo](https://open-meteo.com) weather and marine APIs.

## Files

- `index.html`: the planner page (published as a claude.ai artifact).
- `scripts/refresh_forecast.py`: fetches the forecast and writes
  `forecast.json`, which the page loads on open. Needs network access to
  `api.open-meteo.com` and `marine-api.open-meteo.com`.

If `forecast.json` is missing or stale, the page's **Load a forecast** panel
lets you paste the data in from the two Open-Meteo links by hand.

Exposure sector, thresholds and tide limits are adjustable in the page's
**Settings** panel and remembered per device.
