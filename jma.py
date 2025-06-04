# Simplified JMA weather helper using the Open-Meteo API
import aiohttp
import json
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent / "data"
OPEN_METEO_URL = f"file://{DATA_DIR / 'weather_sample.json'}"


async def fetch_jma_weather(latitude: float = 35.68, longitude: float = 139.76) -> dict | None:
    """Fetch a minimal weather forecast from the Open-Meteo JMA model."""
    url = OPEN_METEO_URL
    if url.startswith("file://"):
        try:
            data = json.loads(Path(url[7:]).read_text(encoding="utf-8"))
        except Exception:
            return None
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(url.format(lat=latitude, lon=longitude)) as resp:
                if resp.status != 200:
                    return None
                try:
                    data = await resp.json()
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
