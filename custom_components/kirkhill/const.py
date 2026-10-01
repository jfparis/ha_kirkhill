"""Constants for the Kirk Hill Wind Farm integration."""

from __future__ import annotations

from datetime import timedelta

DOMAIN = "kirkhill"

BASE_URL = "https://dashboard.kirkhillcoop.org"
API_PREFIX = "/api/v1"

# Cloudflare fronts the dashboard and 403s the default aiohttp/urllib
# User-Agent (error code 1010). Always send an explicit UA on API calls.
USER_AGENT = "ha-kirkhill"

ENDPOINT_SUMMARY = f"{API_PREFIX}/summary"
ENDPOINT_GENERATION = f"{API_PREFIX}/generation"
ENDPOINT_WIND_SPEED = f"{API_PREFIX}/wind-speed"
ENDPOINT_TURBINES = f"{API_PREFIX}/turbines"

SCOPE_OWNER = "owner"
SCOPE_SITE = "site"

CONF_API_KEY = "api_key"
CONF_RANGE = "range"
CONF_SCAN_MINUTES = "scan_minutes"
CONF_PRICE = "price_gbp_per_mwh"

CURRENCY_GBP = "GBP"

DEFAULT_RANGE = "7d"
DEFAULT_SCAN_MINUTES = 5
DEFAULT_SCAN_INTERVAL = timedelta(minutes=DEFAULT_SCAN_MINUTES)
MIN_SCAN_MINUTES = 1
MAX_SCAN_MINUTES = 60

# Ranges offered in the options flow for the live (summary/turbine/wind) window.
# Sub-day ranges are rejected by the API (302), so they are intentionally absent.
ALLOWED_RANGES = ["today", "7d", "30d"]

# Turbine ids are constrained server-side to ^T[1-8]$
TURBINE_IDS = [f"T{i}" for i in range(1, 9)]

NAME = "Kirk Hill Wind Farm"
MANUFACTURER = "Kirk Hill Community Wind Farm"
MODEL_SITE = "Community Wind Farm"
MODEL_TURBINE = "Wind Turbine"
ATTRIBUTION = "Data provided by Kirk Hill Community Wind Farm"

MONTHLY_FORECAST = {
    1: {
        "expected_wind_speed_mps": 11,
        "p50_kwh": 7354000,
        "p75_kwh": 6943000,
        "p90_kwh": 6575000,
    },
    2: {
        "expected_wind_speed_mps": 10,
        "p50_kwh": 5722000,
        "p75_kwh": 5402000,
        "p90_kwh": 5116000,
    },
    3: {
        "expected_wind_speed_mps": 9.3,
        "p50_kwh": 5863000,
        "p75_kwh": 5536000,
        "p90_kwh": 5242000,
    },
    4: {
        "expected_wind_speed_mps": 7,
        "p50_kwh": 4445000,
        "p75_kwh": 4197000,
        "p90_kwh": 3974000,
    },
    5: {
        "expected_wind_speed_mps": 6.9,
        "p50_kwh": 4250000,
        "p75_kwh": 4013000,
        "p90_kwh": 3800000,
    },
    6: {
        "expected_wind_speed_mps": 5.5,
        "p50_kwh": 3180000,
        "p75_kwh": 3002000,
        "p90_kwh": 2843000,
    },
    7: {
        "expected_wind_speed_mps": 5.2,
        "p50_kwh": 2901000,
        "p75_kwh": 2739000,
        "p90_kwh": 2594000,
    },
    8: {
        "expected_wind_speed_mps": 5.7,
        "p50_kwh": 3329000,
        "p75_kwh": 3143000,
        "p90_kwh": 2976000,
    },
    9: {
        "expected_wind_speed_mps": 7,
        "p50_kwh": 4321000,
        "p75_kwh": 4080000,
        "p90_kwh": 3863000,
    },
    10: {
        "expected_wind_speed_mps": 8,
        "p50_kwh": 5595000,
        "p75_kwh": 5283000,
        "p90_kwh": 5002000,
    },
    11: {
        "expected_wind_speed_mps": 8.6,
        "p50_kwh": 6402000,
        "p75_kwh": 6044000,
        "p90_kwh": 5724000,
    },
    12: {
        "expected_wind_speed_mps": 10,
        "p50_kwh": 6904000,
        "p75_kwh": 6518000,
        "p90_kwh": 6172000,
    },
}
