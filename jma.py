# Simplified JMA weather helper using the Open-Meteo API
import aiohttp
import json
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent / "data"

# Primary Open-Meteo endpoint using the JMA model
OPEN_METEO_URL = (
    "https://api.open-meteo.com/v1/jma?latitude={lat}&longitude={lon}" "&hourly=temperature_2m,weather_code"
)

# Fallback local data file when the network request fails
FALLBACK_FILE = DATA_DIR / "weather_sample.json"


async def fetch_jma_weather(latitude: float = 35.68, longitude: float = 139.76) -> dict | None:
    """Fetch a minimal weather forecast from Open-Meteo.

    The function attempts to retrieve data from the Open-Meteo endpoint first.
    If the request fails or returns a non-200 status, it falls back to the local
    ``weather_sample.json`` file so the integration can operate offline or when
    network access is restricted.
    """

    url = OPEN_METEO_URL.format(lat=latitude, lon=longitude)
    data: dict | None = None
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
    except Exception:
        data = None

    if data is None:
        try:
            data = json.loads(FALLBACK_FILE.read_text(encoding="utf-8"))
        except Exception:
            return None

    temps = data.get("hourly", {}).get("temperature_2m", [])
    codes = data.get("hourly", {}).get("weather_code", [])
    if temps and codes:
        return {
            "temperature": float(temps[0]),
            "condition": codes[0],
        }

    return None

def get_mock_jma_data():
    # Simulate fetching data from JMA
    return {
        "temperature": 25.0,
        "condition": "Sunny"
    }
